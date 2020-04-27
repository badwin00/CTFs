import os

os.system("file flag > state.txt")
f = open("state.txt","r")

os.system("7z -y x flag")
os.system("mv flag~ flag")
os.system("python rock.py")





