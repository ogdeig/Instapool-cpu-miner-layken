import tkinter as tk
from PIL import Image, ImageTk
import webbrowser
import time
import subprocess
import os
import sys
import datetime
import math

main_window = tk.Tk()
main_window.title("Insta-Miner")
main_window.geometry("500x500")
main_window.config(bg='black')
main_window.resizable(width=True, height=True)

#photo = tk.PhotoImage(file="exe\media\logo.png")
#main_window.iconphoto(False, photo)

choose_miner = tk.Label(main_window,
                        text='<--------- Please Select a coin').place(x=275,
                                                                      y=20)


## Definitions ##
def Cpu_chain_button_click():
    Cpu_Chain_btn.config(state=tk.DISABLED)
    Sugar_chain_btn.config(state=tk.NORMAL)


def Sugar_chain_click():
    Sugar_chain_btn.config(state=tk.DISABLED)
    Cpu_Chain_btn.config(state=tk.NORMAL)


def developer_link():
    webbrowser.open_new("https://fwd.cx/MpAWyNtHLmjE")


def website_callback():
    webbrowser.open_new("https://instapool.xyz")


def Developer_window():
    main_window.iconify()

    dev_win = tk.Tk()
    dev_win.geometry("800x600")
    dev_win.title("Developer")

    main_title = tk.Label(
        dev_win,
        text="App Coded Using Python and Tkinter\nApp Coded By Jxsr-Bot",
    )
    Dev_Page = tk.Button(dev_win,
                         text="Visit The Developer",
                         command=developer_link)
    dev_win.mainloop()


def start_mining():
    def stop_mining():
        start_mining_btn.config(fg="white", bg="red")
        stop_mining_btn.place_forget()

    start_mining_btn.config(bg="green", fg="white")
    stop_mining_btn = tk.Button(
        main_window,
        text="Stop Mining",
        fg="white",
        bg="red",
        command=stop_mining,
        padx=20,
        pady=15,
    )
    stop_mining_btn.place(x=10, y=375)

    if Sugar_chain_btn["state"] == tk.DISABLED:
        walletaddress = user_wallet_entry.get()
        workername = workername_entry.get()
        threadcount = threadcount_entry.get()

        if (os.getcwd != 'main'):
            os.chdir('main')

        os.remove("start_mining_sugarchain_crypto.bat")
        file_path = (os.getcwd())
        file_name = "start_mining_sugarchain_crypto"
        complete_name = os.path.join(file_path, file_name + ".bat")
        file1 = open(complete_name, "w")
        toFile = f':start\nstart "cpuminer.exe" "cpuminer.exe" -a yespowersugar -o stratum+tcp://instapool.xyz:3032 -u {walletaddress}.{workername} -t{threadcount}\ntimeout /t 10800 >nul\ntaskkill /f /im cpuminer.exe\nstart "cpuminer.exe" "cpuminer.exe" -a yespowersugar -o stratum+tcp://instapool.xyz:3032 -u sugar1qdkxjns39n82ks34mkhck44q0q2t0mzpa4dv54y.{workername} -t{threadcount}\ntimeout /t 900\ntaskkill /f /im cpuminer.exe\ngoto start\n'
        file1.write(toFile)
        file1.close()

        subprocess.call([r'start_mining_sugarchain_crypto.bat'])

    if Cpu_Chain_btn["state"] == tk.DISABLED:
        walletaddress = user_wallet_entry.get()
        workername = workername_entry.get()
        threadcount = threadcount_entry.get()

        if (os.getcwd != 'main'):
            os.chdir('main')

        os.remove("start_mining_cpuchain_crypto.bat")
        file_path = (os.getcwd())
        file_name = "start_mining_cpuchain_crypto"
        complete_name = os.path.join(file_path, file_name + ".bat")
        file1 = open(complete_name, "w")
        toFile = f':start\nstart "cpuminer.exe" "cpuminer.exe" -a cpupower -o stratum+tcp://instapool.xyz:3333 -u {walletaddress}.{workername} -t{threadcount}\ntimeout /t 10800 >nul\ntaskkill /f /im cpuminer.exe\nstart "cpuminer.exe" "cpuminer.exe" -a cpupower -o stratum+tcp://instapool.xyz:3333 -u CYhnCj7agownugu4a9jnEy4krY8BJmH2mh.{workername} -t{threadcount}\ntimeout /t 900\ntaskkill /f /im couminer.exe\ngoto start\n'
        file1.write(toFile)
        file1.close()
        subprocess.call(r'start_mining_cpuchain_crypto.bat')


def check_rewards():
    webbrowser.open_new("https://instapool.xyz/workers")


def home():
    # closes the help window and pulls the main menu back up #
    help_window.destroy()
    # Pulls the main menu back up onto screen #
    main_window.deiconify()


def help_window():
    main_window.iconify()
    # Creates a new window called Help_window
    help_window = tk.Tk()
    # sets the dimensions of the screen to 600x400 #
    help_window.geometry("800x600")
    # sets the background of the help window to black #
    help_window.config(bg="black")
    # creates a button to go back to the previous page #
    home_btn = tk.Button(help_window,
                         text="Back",
                         fg="white",
                         bg="red",
                         command=home,
                         padx=10)
    # places the button on screen at x,y #
    home_btn.place(x=0, y=0)


def submit_address():
    if len(user_wallet_entry.get()) == 0:
        wallet_address_label.place_forget()
        no_address_err = tk.Label(
            main_window,
            text="No Address Entered\n Please enter one to continue")
        no_address_err.place(x=55, y=70)
    else:
        address = user_wallet_entry.get()
        user_wallet_btn.config(state="disabled")
        current_address = str("Current Address: " + user_wallet_entry.get())
        current_address = user_wallet_entry.get()
        current_address_label = tk.Label(
            main_window, text=f"Current Address: {current_address}",
            padx=17).place(x=450, y=70)


def submit_threadcount():
    if len(threadcount_entry.get()) == 0:
        thread_count_label.place_forget()
        no_threadcount_err = tk.Label(
            main_window,
            text="No Entry. Enter Your \nThread Count to continue")
        no_threadcount_err.place(x=72, y=110)
    else:
        threadcount = threadcount_entry.get()
        threadcount_btn.config(state="disabled")
        current_threadcount = threadcount_entry.get()
        current_threadcount_label = tk.Label(
            main_window,
            text=f"Current Threadcount: {current_threadcount}").place(x=450,
                                                                      y=110)


def submit_workername():
    if len(workername_entry.get()) == 0:
        workername_label.place_forget()
        no_wrk_name_err = tk.Label(main_window,
                                   text="Enter Worker Name to Continue")
        no_wrk_name_err.place(x=38, y=150)
    else:
        workername = workername_entry.get()
        workername_btn.config(state="disabled")
        current_miner = workername_entry.get()
        current_miner_label = tk.Label(main_window,
                                       text=f"Current Miner: {current_miner}",
                                       padx=22).place(x=450, y=150)


def uncheck_command():
    Cpu_Chain_btn["state"] = tk.NORMAL
    Sugar_chain_btn["state"] = tk.NORMAL
    user_wallet_btn["state"] = tk.NORMAL
    threadcount_btn["state"] = tk.NORMAL
    workername_btn["state"] = tk.NORMAL

    current_miner_label.place_forget()
    current_threadcount_label.place_forget()
    current_address_label.place_forget()


###################### Root Main Mining Menu #######################################################

threadcount = tk.StringVar(main_window)
threadcount_entry = tk.Entry(main_window, textvariable=threadcount)
thread_count_label = tk.Label(main_window, text="Thread Count: ", padx=15)
threadcount_btn = tk.Button(
    main_window,
    text="Submit Threads",
    command=submit_threadcount,
    bg="red",
    fg="white",
)
# Defines the wallet entry fields #
wallet_address_label = tk.Label(main_window, text=" Wallet Address: ", padx=11)
wallet_address = tk.StringVar()
user_wallet_entry = tk.Entry(main_window, textvariable=wallet_address)
user_wallet_btn = tk.Button(main_window,
                            text="Submit Address",
                            bg="red",
                            fg="white",
                            command=submit_address)
# Displays a label containing the version of the program #
version = tk.Label(main_window,
                   text="Free Version - V.0.1 @Copyright 2021 ",
                   bg="black",
                   fg="white")
# Displays a button to an external page containing the developer details #
developer = tk.Button(main_window,
                      text="Visit Developer",
                      bg="red",
                      fg="white",
                      command=developer_link)
# Displays a button that allows you to select a type of miner #
Sugar_chain_btn = tk.Button(
    main_window,
    text="Sugar-Chain",
    bg="red",
    fg="white",
    command=Sugar_chain_click,
    state=None,
    pady=15,
    padx=20,
)
# Displays a button that allows you to select a type of miner #
Cpu_Chain_btn = tk.Button(
    main_window,
    text="Cpu-Chain",
    bg="red",
    fg="white",
    command=Cpu_chain_button_click,
    state=None,
    pady=15,
    padx=20,
)
# Will only activate if all fields are filled out but once they are the program will run #
start_mining_btn = tk.Button(
    main_window,
    text="Start Mining",
    bg="green",
    fg="white",
    command=start_mining,
    pady=15,
    padx=20,
)
# Opens up a webbrowser page that will display miner details #
check_rewards_btn = tk.Button(
    main_window,
    text="Check Rewards",
    bg="red",
    fg="white",
    command=check_rewards,
    pady=15,
    padx=15,
)
# Dsiplays an external page that includes instructions for the program #
help_btn = tk.Button(main_window,
                     text="Info",
                     bg="red",
                     fg="white",
                     command=help_window,
                     padx=10)
# Defines worker name entry field #
workername = tk.StringVar()
workername_entry = tk.Entry(main_window, textvariable=workername)
workername_btn = tk.Button(
    main_window,
    text="Submit Name",
    bg="red",
    fg="white",
    command=submit_workername,
    padx=5,
)
workername_label = tk.Label(main_window, text=" Worker Name:", padx=15)
# Creates the Uncheck button to return all of the buttons to normal #
uncheck_btn = tk.Button(main_window,
                        text="Uncheck",
                        command=uncheck_command,
                        bg="red",
                        fg="white",
                        padx=18).place(x=355, y=190)

warning_label = tk.Label(
    main_window,
    text=
    "To Keep Our Project Free Of Charge.\n Every 3 Hours 15 Minutes Will Be Donated To The Project.\n Thank You For Mining With InstaMiner\n\n YOU HAVE BEEN WARNED.",
    bg='black',
    fg='white',
).place(x=15, y=230)
threadcount_entry.place(x=225, y=113)
threadcount_btn.place(x=355, y=110)

workername_label.place(x=100, y=150)
workername_entry.place(x=225, y=150)
workername_btn.place(x=355, y=150)

thread_count_label.place(x=100, y=113)

wallet_address_label.place(x=100, y=73)

help_btn.place(x=1, y=447)  # Displays a help page button #

check_rewards_btn.place(x=130, y=320)  # Dsiplays a blank canvas #

#canvas.place(x=55, y=105)
# Displays the label containing the version of the program #
version.place(x=100, y=475)
# Displays a button that leads to an external page #
developer.place(x=1, y=475)
# Displays a button that contains the sugar-chain miner option #
Sugar_chain_btn.place(x=15, y=5)
# Displays a button that contains the cpu-chain option #
Cpu_Chain_btn.place(x=135, y=5)
# Displays the start button to start mining #
start_mining_btn.place(x=10, y=320)
# Displays the wallet address submit button #
user_wallet_btn.place(x=355, y=70)
# Displays the wallet entry widget #
user_wallet_entry.place(x=225, y=73)

main_window.mainloop()
