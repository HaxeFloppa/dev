import os
import sys
import time
from time import sleep

user_check = os.listdir('src/data/users')

'''
PUNIX - A lightweight Python OS, based off of the beautiful Unix project.
'''

os.system("clear")
while True:
    print("PYNIX OS - REG PAGE\n(1) Sign Up\n(2) Log In\n")
    pick = input(">  ")
    if pick == "1":
        os.system("clear")
        new_user = input("Your new, unique username:  ")
        os.system("cd src/data/users")
        os.system(f'mkdir {new_user}')
        os.system(f'cd {new_user}')
        os.system('mkdir home')
        os.system('touch .userconfig')
        save_user = open('.userconfig', 'w')
        save_user.write({new_user})
        new_pass = input("Your strong password:  ")
        os.system('touch .passconfig')
        save_pass = open('.passconfig', 'w')
        save_pass.write(new_pass)
        os.system("clear")
        print("Setup complete! Pynix should be loading in no time...")
        time.sleep(2.5)
        os.system("clear")
        os.system("cd home")
        break
    elif pick == "2":
        os.system("clear")
        os.system("cd src/data/users")
        enter_user = input("Name a user to login as:  ")
        if enter_user in user_check:
            os.system(f'cd {enter_user}')
            check_pass = open('.passconfig', 'r').read()
            while True:
                enter_pass = input(f'Type in the password of user {enter_user}:  ')
                if enter_pass == check_pass:
                    os.system("clear")
                    print("Setup complete! Pynix should be loading in no time...")
                    time.sleep(2.5)
                    os.system("clear")
                    os.system("cd home")
                    break
                else:
                    os.system("clear")
                    print("Incorrect. Try again.")
    else:
        os.system("clear")
        print("No such command has been listed. Try again.")

# plays after the register shit
while True:
    print("▉▉▉▉▉▉▉[🗕 ❏ ✖ ]")
    print("▊                    ▊")
    print("▊                    ▊")
    print("▊                    ▊")
    print("▊                    ▊")
    print("▊                    ▊")
    print("▊                    ▊")
    print("▉▉▉▉▉▉▉▉▉▉▉▉▉")