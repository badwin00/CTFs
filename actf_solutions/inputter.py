from pwn import *
s = ssh("team5967","shell.actf.co",password="b9dced405ff29421d20d")
args = ''' \n'"\a'''
s.set_working_directory("/problems/2020/inputter")
io = s.process(["/problems/2020/inputter/./inputter",args])
io.sendline("\0")
io.interactive()
