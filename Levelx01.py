from pwn import *

HOST = "temperance.hackmyvm.eu"
PORT = 9988

s = remote(HOST, PORT)

# recive introduction
log.success("Receiving Introduction")
data_introduction = s.recv(1024)
print(data_introduction)

# send level information
s.send(b"levelx01")

log.success("Receiving Challenge #1")
data_chall_1 = s.recv(1024)
print(data_chall_1)

log.success("Sending Challenge #1")
s.send(data_chall_1)

log.success("Receiving Challenge #2")
data_chall_2 = s.recv(1024)
print(data_chall_2)

log.success("Sending Challenge #2")
s.send(data_chall_2)

# Receive the flag
log.success("Receiving Flag")
data_flag = s.recv(1024)
print(data_flag.decode())
