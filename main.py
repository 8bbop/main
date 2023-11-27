import tkinter as tk

def login_booking():
    # Implement login logic here
    print("Logging")
    create_new_window("User Login")#In this line we def the new window name.

def sign_up_booking():
    # Implement sign-up logic here
    print("Sign-Up")
    create_new_window("New User")

def forget_password():
    # Implement forget password logic here
    print("Forget Password")
    create_new_window("Reset Password")

def exit_program():
    window.destroy()

def create_new_window(title):# In this def we state what the new windows will look like.
    new_window = tk.Toplevel(window)
    new_window.title(title)
    new_window.geometry("300x300")
    new_label = tk.Label(new_window, text=title)
    new_label.pack()

#In the welcome screen we state it's size, window title & what button is seen on landing page.
window = tk.Tk()
window.title("MaxiTaxi Booking")
window.geometry("300x300")

# label for title
hello = tk.Label(window, text="Welcome to MaxtiTaxi Booking")
hello.pack(expand=True)

# Button for Sign-Up.
btn_sign_up = tk.Button(window, text="Sign-Up", bg="blue", fg="white", activebackground="blue", command=sign_up_booking)
btn_sign_up.pack(expand=True)

# Button for Login.
btn_login = tk.Button(window, text="Login", bg="green", fg="white", activebackground="blue", command=login_booking)
btn_login.pack(expand=True)

# Button for Forget Password
btn_forget_password = tk.Button(window, text="Forget Password", command=forget_password, bg="red", fg="white", activebackground="blue")
btn_forget_password.pack(expand=True)

# Button for canceling booking
#btn_cancel = tk.Button(window, text="Cancel", command=exit_program, bg="red", fg="white", activebackground="blue")
#btn_cancel.pack(expand=True)

# Button for exiting program
btn_exit = tk.Button(window, text="Exit", command=exit_program)
btn_exit.pack(expand=True)

window.mainloop()
