from pwn import *
import base64
from PIL import Image
import io

HOST = "temperance.hackmyvm.eu"
PORT = 9988
context.proxy = (socks.SOCKS5, "localhost", 7891)

s = remote(HOST, PORT)

log.success("Receiving Introduction")
data_introduction = s.recv(1024)
print(data_introduction)

# send level information
s.send(b"levelx18")

log.success("Receiving Challenge")
data_chall = s.recv(1024)
print(data_chall)

data_chall = data_chall.decode()
data_chall_res = ""
data_chall = [ord(str(i)) for i in data_chall]
for i in data_chall:
    # print(chr(i), str(i), str(bin(int(i))))
    data_chall_res += str(bin(int(i)))[2:].rjust(8, "0")
# print(data_chall_res)
data_chall = data_chall_res.encode()

log.success("Sending Challenge")
s.send(data_chall)

# Receive the flag / Recibe la flag.
log.success("Receiving Flag")
data_flag = s.recv(1024)
print(data_flag.decode())
