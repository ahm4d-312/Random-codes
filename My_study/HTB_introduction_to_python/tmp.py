import socket

clinet = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clinet.sendto(b"b", ("localhost", 4444))
