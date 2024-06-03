from pwn import *

HOST = "temperance.hackmyvm.eu"
PORT = 9988

s = remote(HOST, PORT)

# recive introduction
log.success("Receiving Introduction")
data_introduction = s.recv(1024)
print(data_introduction)

# send level information
s.send(b"levelx03")

# revice challenge data
log.success("Receiving Challenge")
data_chall = s.recv(1024)
print(data_chall)

# challenge processing
import base64

data_result = base64.b64decode(data_chall.decode()).decode()

# send result
log.success("Sending Result")
s.send(data_result)

# Receive the flag
log.success("Receiving Flag")
data_flag = s.recv(1024)
print(data_flag.decode())
