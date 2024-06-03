from pwn import *
from hashlib import md5

HOST = "temperance.hackmyvm.eu"
PORT = 9988
context.proxy = (socks.SOCKS5, "localhost", 7891)

s = remote(HOST, PORT)

log.success("Receiving Introduction")
data_introduction = s.recv(1024)
print(data_introduction)

# send level information
s.send(b"levelx32")

log.success("Receiving Challenge")
data_chall = s.recv(1024)
print(data_chall)


def get_permutations(string):
    from itertools import permutations

    perms = permutations(string)
    perms_list = ["".join(perm) for perm in perms]
    return perms_list


data_chall = data_chall.decode().split(" ")
data_chall_list = get_permutations(data_chall[1])
for i in data_chall_list:
    if md5(i.encode()).hexdigest() == data_chall[0]:
        data_chall = i
        break

log.success("Sending Challenge")
s.send(data_chall)

# Receive the flag / Recibe la flag.
log.success("Receiving Flag")
data_flag = s.recv(1024)
print(data_flag.decode())
