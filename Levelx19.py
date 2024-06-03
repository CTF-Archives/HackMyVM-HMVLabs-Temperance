from pwn import *
from io import BytesIO
import base64
from zipfile import ZipFile

HOST = "temperance.hackmyvm.eu"
PORT = 9988
context.proxy = (socks.SOCKS5, "localhost", 7891)

s = remote(HOST, PORT)

log.success("Receiving Introduction")
data_introduction = s.recv(1024)
print(data_introduction)

# send level information
s.send(b"levelx19")

log.success("Receiving Challenge")
data_chall = s.recv(1024)
print(data_chall)

data_chall = base64.b64decode(data_chall.decode())
data_chall_zip = ZipFile(BytesIO(data_chall))
data_chall_filename = data_chall_zip.namelist()[0]
for line in data_chall_zip.open(data_chall_filename).readlines():
    data_chall = line.decode("utf-8")

log.success("Sending Challenge")
s.send(data_chall)

# Receive the flag / Recibe la flag.
log.success("Receiving Flag")
data_flag = s.recv(1024)
print(data_flag.decode())
