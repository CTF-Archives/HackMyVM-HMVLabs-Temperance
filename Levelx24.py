from pwn import *
import requests

HOST = "temperance.hackmyvm.eu"
PORT = 9988
context.proxy = (socks.SOCKS5, "localhost", 7891)

s = remote(HOST, PORT)

log.success("Receiving Introduction")
data_introduction = s.recv(1024)
print(data_introduction)

# send level information
s.send(b"levelx24")

log.success("Receiving Challenge")
data_chall = s.recv(1024)
print(data_chall)

data_chall = data_chall.decode()
data_chall = requests.get(data_chall).text.strip()

log.success("Sending Challenge")
s.send(data_chall)

# Receive the flag / Recibe la flag.
log.success("Receiving Flag")
data_flag = s.recv(1024)
print(data_flag.decode())
