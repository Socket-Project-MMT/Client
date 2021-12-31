from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
import tkinter
import threading

def disconnect():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):

            messagebox.showinfo('Announce', 'Disconnected from Server.')
            window.destroy()

class TraCuu:
    def __init__(self, Log_in_win, code_arr, date_arr, log_out_pic):
        #self.date_dis = Entry(Log_in_win,  font = ('VNI-Avo', 13), width = 12, bd = 1)
        self.date_dis = ttk.Combobox(Log_in_win, state = 'readonly', value = date_arr, width = 8, font = ('VNI-Avo', 13))
        self.date_dis.place(x = 380, y = 192)

        self.code_dis = ttk.Combobox(Log_in_win, state = 'readonly', value = code_arr, width = 8, font = ('VNI-Avo', 13))
        self.code_dis.place(x = 730, y =192)

        self.TraCuu_But = Button(Log_in_win, width = 8, height = 2, bd = 1, fg = 'white', bg = 'coral', text = 'SEARCH', command =  self.Search).place(x = 850, y = 185)
        #self.quit = Button(Log_in_win, image = log_out_pic, width = 45, height =50,  command = self.disconnect1).place(x = 40, y = 240)

    def Search(self):
        self.code = self.code_dis.get()
        self.date = self.date_dis.get()
        print(self.code + self.date)

    #def disconnect1(self, Log_in_win):
    #    if messagebox.askokcancel("Quit", "Do you want to quit?"):

    #        messagebox.showinfo('Announce', 'Disconnected from Server.')
    #        Log_in_win.destroy()

def Log_in():
    window.destroy()

    Log_in_win = Tk()
    Log_in_win.title('TRA TỶ GIÁ VÀNG')
    Log_in_win.geometry('1000x562')
    Log_in_win.resizable(0, 0)

    bg_tracuu = PhotoImage(file = 'tracuu.png')
    Label(Log_in_win, image = bg_tracuu).place(x = 0, y = 0, relwidth = 1, relheight = 1)

    log_out_pic = PhotoImage(file = 'logout.png')

    date_arr = ['ddd', 'ddfff']
    code_arr = ['ddd', 'ddfff']
    Log_in_var = TraCuu(Log_in_win, code_arr, date_arr, log_out_pic)

    #col = ('Type', 'Sell', 'Buy')
    #table = Treeview(Log_in_win, columns = col, show = 'headings')
    #table.heading('Type', text = 'Type')
    #table.heading('Sell', text = 'Sell')
    #table.heading('Buy', text = 'Buy')

    Log_in_win.mainloop()

def checkIp(IpServer):
    print(IpServer)
    return 1

def check(username, password):
    return 1

def enterIp():
    if checkIp(Ip.get()) == 1:
        messagebox.showinfo("Announce", "Connected to Server.")
        Ip_win.destroy()
    else:
        messagebox.showinfo("Announce", "Ip invalid.")

def Sign_in():
    if check(username.get(), password.get()) == 1:
        messagebox.showinfo("Announce", "Sign in successfully.")
        Log_in()
    else:
        messagebox.showinfo("Announce", "Invalid username or password.")

class DangKi:
    def __init__(self, signup_win):
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
            if self.check_Signup() == 1:
                messagebox.showinfo("Announce", "Sign up successfully.")
                Log_in()
            else:
                messagebox.showinfo("Announce", "Existed username.")

    def check_Signup(self):
        #if self.username1.get() == 
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

window.protocol("WM_DELETE_WINDOW", disconnect)

window.mainloop()