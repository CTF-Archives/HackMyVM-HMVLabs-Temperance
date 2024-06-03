from pwn import *
import base64
from PIL import Image
import io
from pyzbar.pyzbar import decode

HOST = "temperance.hackmyvm.eu"
PORT = 9988
context.proxy = (socks.SOCKS5, "localhost", 7891)

s = remote(HOST, PORT)

log.success("Receiving Introduction")
data_introduction = s.recv(1024)
print(data_introduction)

# send level information
s.send(b"levelx31")

log.success("Receiving Challenge")
data_chall = s.recv(1024)
print(data_chall)

data_chall = base64.b64decode(data_chall.decode())
data_chall_img = io.BytesIO(data_chall)
data_chall_img = Image.open(data_chall_img)
data_chall=decode(data_chall_img)[0].data.decode()

log.success("Sending Challenge")
s.send(data_chall)

# Receive the flag / Recibe la flag.
log.success("Receiving Flag")
data_flag = s.recv(1024)
print(data_flag.decode())
