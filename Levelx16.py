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
s.send(b"levelx16")

log.success("Receiving Challenge")
data_chall = s.recv(1024)
print(data_chall)

data_chall = base64.b64decode(data_chall.decode())
data_chall = io.BytesIO(data_chall)
data_chall = Image.open(data_chall)
data_chall = str(str(data_chall.size[0]) + "x" + str(data_chall.size[1])).encode()

log.success("Sending Challenge")
s.send(data_chall)

# Receive the flag / Recibe la flag.
log.success("Receiving Flag")
data_flag = s.recv(1024)
print(data_flag.decode())
