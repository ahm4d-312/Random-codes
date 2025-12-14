import socket as s
import threading as th


def tcp_connect():
    clinet = s.socket(s.AF_INET, s.SOCK_STREAM)
    ip, port = "localhost", 9003
    clinet.connect((ip, port))
    clinet.send(input("> ").encode())
    resp = clinet.recv(1024).decode()
    print(resp)
    clinet.close()


def main():
    for i in range(4):
        handler = th.Thread(target=tcp_connect, args=())
        handler.start()


if __name__ == "__main__":
    main()
