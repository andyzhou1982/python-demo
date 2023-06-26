import cv2
import os

def video2frame(video_path,output_folder):
    # 读取视频文件
    # video_path = 'path/to/video.mp4'
    cap = cv2.VideoCapture(video_path)
 
    # 检查视频是否成功打开
    if not cap.isOpened():
        print("Error opening video file")
 
    # 创建输出文件夹
    # output_folder = 'path/to/output'
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
 
    # 逐帧读取视频并保存到输出文件夹
    frame_count = 1
    while cap.isOpened():
        # 读取一帧
        ret, frame = cap.read()
 
        # 检查是否成功读取帧
        if not ret:
            break
 
        # 指定输出文件名
        output_file = os.path.join(output_folder, f'{frame_count:04d}.png')
        print('\r geneframe:',output_file,end='')
 
        # 保存帧到输出文件
        cv2.imwrite(output_file, frame)
 
        # 更新帧计数器
        frame_count += 1
 
    # 释放视频对象
    cap.release()
    print('\n :) done!')
 
def frame2video(image_folder,ouput_dir,fps):
    # 读取图像文件列表
    image_files = [f for f in os.listdir(image_folder) if f.endswith('.png') or f.endswith('.jpg')]
    image_files.sort()
 
    # 获取图像的宽度和高度
    img = cv2.imread(os.path.join(image_folder, image_files[0]))
    height, width, _ = img.shape
 
    # 创建输出视频对象
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(ouput_dir+'\output.mp4', fourcc, fps, (width, height))
    num_images = len(image_files)
    frame_num = 0
    # 逐帧写入视频帧
    for image_file in image_files:
        image_path = os.path.join(image_folder, image_file)
        frame = cv2.imread(image_path)
        out.write(frame)
        frame_num +=1
        print('\r generating video:',f'{100*frame_num/num_images:5.2f}%',end='')
 
    # 释放视频对象
    out.release()
    print('\n :) done!')

frame2video('D:\\aigc\\bak\\video\\1_3','D:\\aigc\\bak\\video\\output',5)
#video2frame('D:\\aigc\\bak\\video\\2.mp4','D:\\aigc\\bak\\video\\2')
     