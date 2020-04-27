from pwn import *
import base64
sh = remote("chal.pctf.competitivecyber.club",7070)
sh.recvuntil("====================================================================================================\n")
base = sh.recvuntil("==")
out = open("shorts","ab")
try:
    while(1==1):
        #decode the recieved string and write it to a file
        print("loop!")
        base = base64.b64decode(base)
        f = open("img.png","wb")
        f.write(base)
        f.close()
        print("code written")

        #run the decoded image through a QR reader, and get another b64 code
        io = process(argv=["zbarimg","img.png"])
        io.recvuntil(":")
        base = io.recvline()
        io.close()
        print("QR decoded")
        print(base)
        out.write(base[:-2])
        #catch gg==
        if(len(base) < 10):
            print("send ==gg")
            sh.send(base)
            sh.interactive()
        sh.send(base)
        print("data sent")

        #read every byte of the new code from the server
        base = ""
        byte = " "
        while(1==1):
            byte = sh.recv(1,timeout=1)
            if(byte == ''):
                break
            base+=byte
        print(base)
except:
    print("i really don't know what to do from here")
    sh.interactive()
