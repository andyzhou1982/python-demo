import asyncio
import random

'''
异步打印
'''
async def printContext(context):
    #获得0到1之间的随机数
    waitTime = random.random()
    #等待
    await asyncio.sleep(waitTime)
    print("打印内容: ", context)

async def println():
    print("打印内容: ")    

async def main():
    print("开始执行")
    outstr=["文本1","文本2","文本3","文本4","文本5"]
    tasks = [asyncio.create_task(printContext(context)) for context in outstr]
    await asyncio.wait(tasks)
    print("结束执行") 

if __name__ == "__main__":
    asyncio.run(main())       