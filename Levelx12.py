from pwn import *

HOST = "temperance.hackmyvm.eu"
PORT = 9988
context.proxy = (socks.SOCKS5, "localhost", 7891)

s = remote(HOST, PORT)

log.success("Receiving Introduction")
data_introduction = s.recv(1024)
print(data_introduction)

# send level information
s.send(b"levelx12")

log.success("Receiving Challenge")
data_chall = s.recv(1024)
print(data_chall)

data_chall = data_chall.decode().split(" ")
data_chall = str(data_chall[0] * int(data_chall[1])).encode()

log.success("Sending Challenge")
s.send(data_chall)

# Receive the flag / Recibe la flag.
log.success("Receiving Flag")
data_flag = s.recv(1024)
print(data_flag.decode())
