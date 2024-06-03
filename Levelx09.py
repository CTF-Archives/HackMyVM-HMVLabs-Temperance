from pwn import *
import string

HOST = "temperance.hackmyvm.eu"
PORT = 9988
context.proxy = (socks.SOCKS5, "localhost", 7891)

s = remote(HOST, PORT)

log.success("Receiving Introduction")
data_introduction = s.recv(1024)
print(data_introduction)

# send level information
s.send(b"levelx09")

log.success("Receiving Challenge")
data_chall = s.recv(1024)
print(data_chall)

data_chall = data_chall.decode()
data_chall_res = ""
dics = string.ascii_uppercase + string.ascii_lowercase
dics_len = len(dics)
for i in data_chall:
    if i in string.ascii_lowercase:
        offset = string.ascii_lowercase.find(i) - 13
        if offset in range(0, 26):
            data_chall_res += string.ascii_lowercase[offset]
        else:
            data_chall_res += string.ascii_lowercase[offset + 26]
    elif i in string.ascii_uppercase:
        offset = string.ascii_uppercase.find(i) - 13
        if offset in range(0, 26):
            data_chall_res += string.ascii_uppercase[offset]
        else:
            data_chall_res += string.ascii_uppercase[offset + 26]
    else:
        data_chall_res += i
print(data_chall)
print(data_chall_res)

data_chall = data_chall_res

log.success("Sending Challenge")
s.send(data_chall)

# Receive the flag / Recibe la flag.
log.success("Receiving Flag")
data_flag = s.recv(1024)
print(data_flag.decode())
