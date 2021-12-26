# fileclient.py

import socket 
from socket import IPPROTO_TCP, SO_KEEPALIVE, TCP_KEEPIDLE, TCP_KEEPINTVL, TCP_KEEPCNT
s = socket.socket()
# HOST = input("Enter server IP: ")
HOST="127.0.0.1"
FORMAT="utf8"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("I'm client")


try: 
    client.connect((HOST, 6767)) #lắng nghe ở cổng 6767
    print("Client address: ", client.getsockname())
    
    msg=None
    while(msg!="End"):
        msg=client.recv(1024).decode(FORMAT)
        print("Server: ", msg)

        msg=input("You: ")
        client.sendall(msg.encode(FORMAT))

except: 
    print("Error")
client.close()