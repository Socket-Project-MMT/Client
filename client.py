# fileclient.py

#------------- global variables

# HOST = input("Enter server IP: ")
HOST="127.0.0.1"
FORMAT="utf-8"

#______ function_____________

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
import tkinter
import threading

import socket 
from socket import IPPROTO_TCP, SO_KEEPALIVE, TCP_KEEPIDLE, TCP_KEEPINTVL, TCP_KEEPCNT
user="ta"
passw="ta"
searchinfor=[]
def disconnectWindow():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            client.close()
            messagebox.showinfo('Announce', 'Disconnected from Server.')
            window.destroy()

def sendList(list):
    for item in list:
        client.sendall(item.encode(FORMAT))
        msg=client.recv(1024).decode(FORMAT)
    msg="end"
    client.sendall(msg.encode(FORMAT))

def recvList():
  mylist=[]
  item=client.recv(1024).decode(FORMAT)
  while(item!="end"):
    mylist.append(item)
    client.sendall(item.encode(FORMAT))
    item=client.recv(1024).decode(FORMAT)
  return mylist
def formatDate(list):
    newlist=[]
    for date in list: 
        year =date[0:4]
        month =date[4:6]
        day =date[6:8]
        new= day+'/'+month+'/'+ year
        newlist.append(new)
    return newlist
def reformatDate(date):
    year = date[6:10]
    month =date[3:5]
    day =date[0:2]
    new= year+month+day
    return new



def Log_in():
    window.destroy()
    searchInfor=["", ""]
    Log_in_win = Tk()
    Log_in_win.title('TRA TỶ GIÁ VÀNG')
    Log_in_win.geometry('1000x562')
    Log_in_win.resizable(0, 0)

    bg_tracuu = PhotoImage(file = 'tracuu.png')
    Label(Log_in_win, image = bg_tracuu).place(x = 0, y = 0, relwidth = 1, relheight = 1)
    
    #log_out_pic = PhotoImage(file = 'logout.png') 
    code_arr = recvList()
    date_arr = formatDate(recvList())
    date_dis = ttk.Combobox(Log_in_win, state = 'readonly', value = date_arr, width = 8, font = ('VNI-Avo', 13))
    date_dis.place(x = 380, y = 192)
    def disconnect1():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            # Thủ tục
            messagebox.showinfo('Announce', 'Disconnected from Server.')
            Log_in_win.destroy()

    log_out_pic = PhotoImage(file = 'logout.png')
    quit = Button(Log_in_win, image = log_out_pic, width = 45, height =50,  command = disconnect1).place(x = 40, y = 240)
    code_dis = ttk.Combobox(Log_in_win, state = 'readonly', value = code_arr, width = 8, font = ('VNI-Avo', 13))
    code_dis.place(x = 730, y =192)
    def Search(code_dis, date_dis):
        stri=date_dis.get()
        searchInfor[0]=reformatDate(stri)
        # searchInfor[0]=date_dis.get()
        searchInfor[1]=code_dis.get()

        sendList(searchInfor)
        response= recvList()
        Label(Log_in_win, text = response[0], font = ('VNI-Avo', 14),  bg ='white').place(x = 200, y = 300)
        Label(Log_in_win, text = response[1], font = ('VNI-Avo', 14),  bg ='white').place(x = 500, y = 300)
        response.clear()
        rabb1= recvList()
        rabb2=recvList()
        rabb1.clear()
        rabb2.clear()
    def disconnectLogin(log_in_win):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            # ngat kết nối server
            client.close()
            messagebox.showinfo('Announce', 'Disconnected from Server.')
            Log_in_win.destroy()
    TraCuu_But = Button(Log_in_win, width = 8, height = 2, bd = 1, fg = 'white', bg = 'coral', text = 'SEARCH', font = ('arial', 10, 'italic', 'bold'), command = lambda:  Search(code_dis, date_dis)).place(x = 850, y = 185)
    Label(Log_in_win, text = "Sell", font = ('VNI-Avo', 14, 'bold'), fg = 'orange', bg ='white').place(x = 200, y = 250)
    Label(Log_in_win, text = "Buy", font = ('VNI-Avo', 14, 'bold'), fg = 'orange', bg ='white').place(x = 500, y = 250)
    Log_in_win.mainloop()  
   

# server hien thi duow danh sach client
# server thong bao cho tat ca client la ngat ket noi

# thiet ke lai du lieu ben server

# cap nhat dươc danh sach client hoạt động + conn của client
# 


def checkIp(IpServer):
    return 1

def check(username, password):
    return 1

def Connect():
    host = Ip.get()
    try: 
        client.connect((HOST, 6767)) #lắng nghe ở cổng 6767
        print("Client address: ", client.getsockname())
        return 1

    except:
        print("Error")
        messagebox.showinfo("Announce", "Ip invalid.")

def enterIp():
    if Connect() == 1:
        messagebox.showinfo("Announce", "Connected to Server.")
        Ip_win.destroy()
    else:
        messagebox.showinfo("Announce", "Ip invalid.")
   
def Sign_in():
    infor=["", "", ""]
    infor[0]="signin"
    # infor[1]=username.get()
    # infor[2] =password.get()
    infor[1]=user
    infor[2] =passw
    sendList(infor)
    msg = client.recv(1024).decode(FORMAT)
    if msg=="signinsuccess":
        messagebox.showinfo("Announce", "Sign in successfully.")
        Log_in()
    else:
        messagebox.showinfo("Announce", "Invalid username or password.")


class DangKi:
    def __init__(self, signup_win):
        self.infor = []
        self.username1 = Entry(signup_win, font = ('VNI-Avo', 13), width = 15, bd = 0)
        self.username1.place(x = 90, y = 275)

        self.password1 = Entry(signup_win, font = ('VNI-Avo', 13), width = 15, bd = 0, show = '*')
        self.password1.place(x = 90, y = 340)

        self.password1_s = Entry(signup_win, font = ('VNI-Avo', 13), width = 15, bd = 0, show = '*')
        self.password1_s.place(x = 90, y = 405)

        self.DangKi_But = Button(signup_win, width = 8, height = 2, bd = 0, fg = 'white', bg = 'coral', text = 'S I G N U P', command =  self.Sign_up_1).place(x = 170, y = 450)

    def Sign_up_1(self):
        if self.password1.get() != self.password1_s.get():
            messagebox.showinfo("Announce", "Passwords does not match.")
        else:
            if self.check_Signup(client) == 1:
                messagebox.showinfo("Announce", "Sign up successfully.")
                Log_in()
            else:
                messagebox.showinfo("Announce", "Existed username.")

    def check_Signup(self, client):


        self.infor.append("signup")
        self.username=self.username1.get() 
        self.infor.append(self.username)
        self.password=self.password1.get()
        self.infor.append(self.password)
    
        sendList(self.infor)

        msg = client.recv(1024).decode(FORMAT) #"
        print(msg)
        if msg=="signupsuccess":
            messagebox.showinfo("Thông báo", "Đăng ký thành công.")
            Log_in()
        else:
            messagebox.showinfo("Thông báo", "Tên đăng nhập tồn tại.")
        return 1

def Sign_up():
    signup_win = Toplevel()
    signup_win.title('SIGN UP PAGE')
    signup_win.geometry('413x517')
    signup_win.resizable(0, 0)

    bg_signup = PhotoImage(file = 'bg_signup.png')
    Label(signup_win, image = bg_signup).place(x = 0, y = 0, relwidth = 1, relheight = 1)

    Sign_up_var = DangKi(signup_win)

    Label(signup_win, text = "Username", font = ('VNI-Avo', 14, 'italic'), fg = 'orange', bg ='white').place(x = 80, y = 240)
    Frame(signup_win, width = 250, height = 2, bg = 'orange').place(x = 80, y = 305)

    Label(signup_win, text = "Password", font = ('VNI-Avo', 14, 'italic'), fg = 'orange', bg ='white').place(x = 80, y = 310)
    Frame(signup_win, width = 250, height = 2, bg = 'orange').place(x = 80, y = 370)

    Label(signup_win, text = "Verify password", font = ('VNI-Avo', 14, 'italic'), fg = 'orange', bg ='white').place(x = 80, y = 375)
    Frame(signup_win, width = 250, height = 2, bg = 'orange').place(x = 80, y = 435)

    signup_win.mainloop()


# ----- Main -----

option=""
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

window = Tk()
window.title("W E L C O M E")
window.geometry('413x517')
window.resizable(0, 0)

bg_main = PhotoImage(file = 'bg_main.png')
Label(window, image = bg_main).place(x = 0, y = 0, relwidth = 1, relheight = 1)

# --- Đăng nhập ---

Label(window, text = "Username", font = ('VNI-Avo', 14, 'italic'), fg = 'orange', bg ='white').place(x = 80, y = 280)

username = Entry(window, font = ('VNI-Avo', 13), width = 15, bd = 0)
username.place(x = 90, y = 315)
Frame(window, width = 250, height = 2, bg = 'orange').place(x = 80, y = 345)

Label(window, text = "Password", font = ('VNI-Avo', 14, 'italic'), fg = 'orange', bg ='white').place(x = 80, y = 350)

password = Entry(window, font = ('VNI-Avo', 13), width = 15, bd = 0, show = '*')
password.place(x = 90, y = 385)
Frame(window, width = 250, height = 2, bg = 'orange').place(x = 80, y = 415)

Button(window, width = 8, height = 2, bd = 0, fg = 'white', bg = 'coral', text = 'S I G N I N', command =  Sign_in).place(x = 170, y = 430)
Button(window, width = 8, height = 2, bd = 0, fg = 'coral', bg ='white', text = 'OR SIGN UP', command = Sign_up).place(x = 250, y = 430)

# --- Nhập Server Ip ---

bg_Ip = PhotoImage(file = 'bg_Ip.png')
Ip_win = Frame(window)
Ip_win.pack(fill='both', expand=True)
Label(Ip_win, image = bg_Ip).place(x = 0, y = 0, relwidth = 1, relheight = 1)

Label(Ip_win, text = 'Server Ip', font = ('VNI-Avo', 15, 'italic'), fg = 'orange', bg ='white').place(x =80, y = 340)
Ip = Entry(Ip_win, font = ('VNI-Avo', 13), width = 15, bd = 0)
Ip.place(x = 90, y = 375)
Frame(Ip_win, width = 250, height = 2, bg = 'orange').place(x = 80, y = 405)

Button(Ip_win, width = 8, height = 2, bd = 0, fg = 'white', bg = 'coral', text = 'O K', command = enterIp).place(x = 170, y = 420)

window.protocol("WM_DELETE_WINDOW", disconnectWindow)

window.mainloop()