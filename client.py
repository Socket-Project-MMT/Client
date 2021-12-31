# fileclient.py

import socket 
from socket import IPPROTO_TCP, SO_KEEPALIVE, TCP_KEEPIDLE, TCP_KEEPINTVL, TCP_KEEPCNT
from tkinter import *
from tkinter import messagebox
import tkinter
import threading


#------------- global variables

s = socket.socket()
# HOST = input("Enter server IP: ")
HOST="127.0.0.1"
FORMAT="utf8"

window = Tk()
window.title("W E L C O M E")
window.geometry('700x350')
window.resizable(0, 0)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#______ function_____________
def sendList(client, list):
    for item in list:
        client.sendall(item.encode(FORMAT))
        msg=client.recv(1024).decode(FORMAT)
        print("msg", msg)
    msg="end"
    client.sendall(msg.encode(FORMAT))
def recvList(conn):
  mylist=[]
  item=conn.recv(1024).decode(FORMAT)
  while(item!="end"):
    mylist.append(item)
    conn.sendall(item.encode(FORMAT))
    item=conn.recv(1024).decode(FORMAT)

  return mylist
def Log_in(client):
    # window.destroy()

    # Log_in_win = Tk()
    window.title('TRA TỶ GIÁ VÀNG')
    window.geometry('400x500')
  
    sjclist= recvList(client)
    print("sjclist:", sjclist)

    # variable = StringVar(window)
    # variable.set(sjclist[0]) # default value

    # w = OptionMenu(window, variable, *sjclist)
    # w.pack()
    # def ok():
    #     value=variable.get()
    #     Label(window, text = value, bg = 'red').grid(row = 4, column = 0)


    # button = Button(window, text="OK", command=ok)
    # button.pack()



    #Log_in_win.attributes('-fullscreen', 1)

    # Log_in_win.mainloop()

def check(username, password):
    return 1
def Option_Signin():
    global option
    option="signin"
def Option_Signup():
    global option
    option="signup"
def Sign_in(client):
    global username
    global password
    global infor 
    infor[0]="signin"
    username=username.get()
    infor[1]=username
    password=password.get()
    infor[2] =password
    sendList(client, infor)
    msg = client.recv(1024).decode(FORMAT)
    if msg=="signinsuccess":
        messagebox.showinfo("Thông báo", "Đăng nhập thành công")
        Log_in(client)
    else:
        messagebox.showinfo("Thông báo", "Tên đăng nhâp hoặc mật khẩu không đúng.")

def Sign_up(client):
    global username
    global password
    global infor 

    infor[0]="signup"
    username=username.get()
    infor[1]=username
    password=password.get()
    infor[2] =password
    print(infor)
    sendList(client, infor)

    msg = client.recv(1024).decode(FORMAT)
    print("msg result", msg)
    if msg=="signupsuccess":
        messagebox.showinfo("Thông báo", "Đăng ký thành công.")
        Log_in(client)
    else:
        messagebox.showinfo("Thông báo", "Tên đăng nhập tồn tại.")
        # Sign_up(client)

def Connect():
    global host
    global client
    host = host.get()
    print(host)
    try: 
        client.connect((HOST, 6767)) #lắng nghe ở cổng 6767
        print("Client address: ", client.getsockname())
        # if(option=="signin"):
        #     Sign_in(client)
        # if(option=="signup"):
        #     Sign_up(client)

    except:
        print("Error")

#------main
str="login"
option=""
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Label(window, text = "Tên đăng nhập").place(x = 0, y = 10)
Label(window, text = "Tên đăng nhập").place(x = 0, y = 15)
Label(window, text = "Mật khẩu", bg = 'red').place(x = 0, y = 20)
host = Entry(window, width = 15, font = ('arial', 14), bd = 5, insertwidth = 2, bg = 'violet')
host.grid(row = 0, column = 1)
username=""
password=""
option=""
infor=["","gg","gg"]
address="d:/MyWork/HK1_nam2/Socket_MMT/Client/client.py"


username = Entry(window, width = 15, font = ('arial', 14), bd = 5, insertwidth = 2, bg = 'violet')
username.grid(row = 1, column = 1)
password = Entry(window, width = 15, font = ('arial', 14), bd = 5, insertwidth = 2, bg = 'violet', show = '*')
password.grid(row = 2, column = 1)

connect = Button(window, padx = 10, bd = 5, fg = 'black', font = ('arial', 16, 'bold'), text = 'Ket noi', bg = '#ffffff', command = Connect).grid(row = 5)
login_but = Button(window, padx = 10, bd = 5, fg = 'black', font = ('arial', 16, 'bold'), text = 'Đăng nhập', bg = '#ffffff', command = lambda: Sign_in(client)).grid(row = 10)
signin_but = Button(window, padx = 10, bd = 5, fg = 'black', font = ('arial', 16, 'bold'), text = 'Dang ki', bg = '#ffffff', command = lambda: Sign_up(client)).grid(row = 20)

msg=None
# while(msg!="End"):
#     msg=client.recv(1024).decode(FORMAT)
#     print("Server: ", msg)

#     msg=input("You: ")
#     client.sendall(msg.encode(FORMAT))

input()
client.close()

window.mainloop()