from tkinter import *
import os


def restart() -> None:
    os.system("shutdown /r /t 1")


def restart_time() -> None:
    os.system("shutdown /r /t 20")


def logout() -> None:
    os.system("shutdown -1")


def shutdown() -> None:
    os.system("shutdown /s /t 1")


st = Tk()
st.title("ShutDown App")
st.geometry("500x500")
st.config(bg="Gray")
r_button = Button(st, text="Restart", font=("Times New Roman", 20, "bold"), relief=RAISED,cursor="plus",
                  command=restart)
r_button.place(x=150, y=60, height=50, width=200)
rt_button = Button(st, text="Restart Time", font=("Times New Roman", 20, "bold"),relief=RAISED,  cursor="plus",
                   command=restart_time)
rt_button.place(x=150, y=170, height=50, width=200)
logout_button = Button(st, text="Log-Out", font=("Times New Roman", 20, "bold"), relief=RAISED, cursor="plus",
                       command=logout)
logout_button.place(x=150, y=270, height=50, width=200)
st_button = Button(st, text="ShutDown", font=("Times New Roman", 20, "bold"), relief=RAISED,cursor="plus",
                   command=shutdown)
st_button.place(x=150, y=370, height=50, width=200)
st.mainloop()
