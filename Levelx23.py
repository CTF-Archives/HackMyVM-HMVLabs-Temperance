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
s.send(b"levelx23")

log.success("Receiving Challenge")
data_chall = s.recv(1024)
print(data_chall)

data_chall = base64.b64decode(data_chall.decode())
data_chall_res = []
data_chall_img = io.BytesIO(data_chall)
data_chall_img = Image.open(data_chall_img)
X, Y = data_chall_img.size
for y in range(Y):
    for x in range(X):
        data_chall_res.append(data_chall_img.getpixel((x, y))[3])
data_chall_res = "".join([chr(i) for i in data_chall_res])
data_chall = data_chall_res

log.success("Sending Challenge")
s.send(data_chall)

# Receive the flag / Recibe la flag.
log.success("Receiving Flag")
data_flag = s.recv(1024)
print(data_flag.decode())
