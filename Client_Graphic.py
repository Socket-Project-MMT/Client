from tkinter import *
from tkinter import messagebox
import tkinter

def Log_in():
    window.destroy()

    Log_in_win = Tk()
    Log_in_win.title('TRA TỶ GIÁ VÀNG')
    Log_in_win.geometry('400x500')



    #Log_in_win.attributes('-fullscreen', 1)

    Log_in_win.mainloop()

def check(username, password):
    return 1

def Sign_in():
    if check(username.get(), password.get()) == 1:
        messagebox.showinfo("Thông báo", "Đăng nhập thành công")
        Log_in()
    else:
        messagebox.showinfo("Thông báo", "Tên đăng nhâp hoặc mật khẩu không đúng.")

def Sign_up():
    if check(username.get(), password.get()) == 1:
        messagebox.showinfo("Thông báo", "Đăng ký thành công.")
        Log_in()
    else:
        messagebox.showinfo("Thông báo", "Tên đăng nhập tồn tại.")

window = Tk()
window.title("W E L C O M E")
window.geometry('700x350')
window.resizable(0, 0)

bg = PhotoImage(file = "bg.jpg")
  
# Show image using label
label1 = Label( root, image = bg)
label1.place(x = 0, y = 0)

Frame(window, width = 2, height = 300, bg = 'gold').place(x = 350, y = 25)

# --- Đăng nhập ---

Label(window, text = "Tên đăng nhập").place(x = 0, y = 10)
Label(window, text = "Mật khẩu", bg = 'red').place(x = 10, y = 50)

username = Entry(window, width = 15, font = ('arial', 14), bd = 5, insertwidth = 2, bg = 'violet')
username.grid(row = 0, column = 1)
password = Entry(window, width = 15, font = ('arial', 14), bd = 5, insertwidth = 2, bg = 'violet', show = '*')
password.grid(row = 1, column = 1)

signin_but = Button(window, padx = 10, bd = 5, fg = 'black', font = ('arial', 16, 'bold'), text = 'Đăng nhập', bg = '#ffffff', command = Sign_in).grid(row = 2)

# --- Đăng ký ---

Label(window, text = "Tên đăng nhập", bg = 'red').grid(row = 4, column = 0)
Label(window, text = "Mật khẩu", bg = 'red').grid(row = 5, column = 0)
Label(window, text = "Nhập lại mật khẩu", bg = 'red').grid(row = 6, column = 0)

username1 = Entry(window, width = 15, font = ('arial', 14), bd = 5, insertwidth = 2, bg = 'violet')
username1.grid(row = 4, column = 1)
password1 = Entry(window, width = 15, font = ('arial', 14), bd = 5, insertwidth = 2, bg = 'violet', show = '*')
password1.grid(row = 5, column = 1)
password1_s = Entry(window, width = 15, font = ('arial', 14), bd = 5, insertwidth = 2, bg = 'violet', show = '*')
password1_s.grid(row = 6, column = 1)

signup_but =  Button(window, padx = 24, bd = 5, fg = 'black', font = ('arial', 16, 'bold'), text = 'Đăng ký', bg = 'violet', command = Sign_up).grid(row = 7)

window.mainloop()