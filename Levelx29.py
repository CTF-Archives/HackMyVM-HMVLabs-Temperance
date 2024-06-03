from pwn import *
from geopy import distance

HOST = "temperance.hackmyvm.eu"
PORT = 9988
context.proxy = (socks.SOCKS5, "localhost", 7891)

s = remote(HOST, PORT)

log.success("Receiving Introduction")
data_introduction = s.recv(1024)
print(data_introduction)

# send level information
s.send(b"levelx29")

log.success("Receiving Challenge")
data_chall = s.recv(1024)
print(data_chall)

data_chall = data_chall.decode()
data_chall = [i.strip().split(" ") for i in data_chall.split("-")]
data_chall = [[int(i[1]), int(i[3])] for i in data_chall]
print(data_chall)
R = 6373.0
lat1 = data_chall[0][0]
lat2 = data_chall[1][0]
lon1 = data_chall[0][1]
lon2 = data_chall[1][1]
dlon = lon2 - lon1
dlat = lat2 - lat1
pt1 = (lat1, lon1)
pt2 = (lat2, lon2)
print(pt1, pt2)
data_chall = distance.distance(pt1, pt2)
data_chall = format(float(str(data_chall).split(" ")[0]), ".3f")

log.success("Sending Challenge")
s.send(data_chall)

# Receive the flag / Recibe la flag.
log.success("Receiving Flag")
data_flag = s.recv(1024)
print(data_flag.decode())
