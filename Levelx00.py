from pwn import *

HOST = "temperance.hackmyvm.eu"
PORT = 9988

s = remote(HOST, PORT)

# recive introduction
log.success("Receiving Introduction")
data_introduction = s.recv(1024)
print(data_introduction)

# send level information
s.send(b"levelx00")

# revice challenge data
log.success("Receiving Challenge")
data_chall = s.recv(1024)
print(data_chall)

# send result
log.success("Sending Challenge")
s.send(data_chall)

# Receive the flag
log.success("Receiving Flag")
data_flag = s.recv(1024)
print(data_flag.decode())
