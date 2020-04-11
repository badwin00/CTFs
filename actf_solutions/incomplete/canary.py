from pwn import *
#s = ssh("team5967","shell.actf.co",password="b9dced405ff29421d20d")
#s.set_working_directory("/problems/2020/no_canary")
io = process("./canary")
gdb.attach(io)
io.sendline(cyclic(100))
io.sendline(cyclic(100))
io.interactive()

