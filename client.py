import socket
import time
from config import server_address

#client 发送端
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
      start = time.time()  #获取当前时间
      print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(start)))  #以指定格式显示当前时间
      msg= input("本客户端，请输入要发送的内容：")  

      client_socket.sendto(msg.encode(), server_address) #将msg内容发送给指定接收方
      now = time.time() #获取当前时间
      run_time = now-start #计算时间差，即运行时间
      print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(now)))
      print("run_time: %d seconds\n" %run_time)