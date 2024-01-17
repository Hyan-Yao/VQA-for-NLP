# -*- coding: utf-8 -*-
import paramiko
import time
import os

class Sever():
    def __init__(self, local_path, hostname = 'r845686u08.zicp.fun', port = '12001',
                     username = 'root', password = '24601'):
        # 设置SSH连接参数
        self.local_path = local_path
        self.target_folder = '/yuanqisu/meter/cache/'
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(hostname = hostname, port = port, username = username, password = password)
        self.sftp = self.ssh.open_sftp()
        self.channel = self.ssh.invoke_shell()
        print("[Log] Sever Object Created!")
        print("[Log] Created Connection: ssh, sftp, command channel")
        
    def upload(self):
        # 上传图片和文本
        self.sftp.put(self.local_path + r"\input.jpg", self.target_folder + "input.jpg")
        self.sftp.put(self.local_path + r"\input.txt", self.target_folder + "input.txt")
        print("[Log] Uploaded image and question")
    
    def predict(self):
        # 执行预测
        print("[Log] Start predicting......")
        self.channel.send("cd meter\n")
        self.channel.send("python predict.py\n")
        # time.sleep(1)
        # print(channel.recv(1024))
    
    def download_answer(self):
        # 下载答案
        while True:
            try:
                self.sftp.get(self.target_folder + "output.txt", self.local_path + r"\output.txt")
                print("[Log] Finish to obtain the answer")
                break
            except FileNotFoundError:
                time.sleep(1)
                print("[Log] Try again to obtain the answer.")
                continue
            
    def show_answer(self):
        af = open(self.local_path + r"\output.txt")
        answer = af.read()
        print("[Log] Answer:" + answer)
        af.close()        
    
    def __del__(self):
        self.sftp.close()
        self.ssh.close()


if __name__ == "__main__":
    local_path = r'C:\Users\yaohy\Documents\src\nlp\cache'
    server = Sever(local_path)
    server.upload()
    server.predict()
    server.download_answer()
    server.show_answer()

