from PIL import Image, ImageDraw, ImageFont

# 打开 png格式的图片，
# 注意源图片最好不要是jpg，容易有问题
im = Image.open('source.png')

# 添加文字
draw = ImageDraw.Draw(im)

# 指定字体文件为 微软雅黑，
# Windows中的字体文件在 windows/fonts目录下
font = ImageFont.truetype("msyh.ttc", 15) 

# 添加文字到指定坐标
draw.text((76,43), ('测试架'), fill='#0000ff', font=font)
draw.text((246,43), ('A0'), fill='#0000ff', font=font)
draw.text((76,70), ('TWS1'), fill='#0000ff', font=font)
draw.text((76,104), ('EDF-ZJ-PZ-3306'), fill='#0000ff', font=font)
draw.text((76,134), ('RF'), fill='#0000ff', font=font)
draw.text((93,165), ('2019-12-31'), fill='#0000ff', font=font)
draw.text((240,165), ('工程部'), fill='#0000ff', font=font)

# 可以添加其他图片内容上去，比如二维码
qrcode =  Image.open('qr.png')
im.paste(qrcode, (313,46))

# 注意这里一定要 指定 dpi保存，否则会有图片dpi改变的问题
im.save('new.png',dpi = im.info['dpi'])