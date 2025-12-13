import threading as th
import socket as s


def tcp_server():
    server = s.socket(s.AF_INET, s.SOCK_STREAM)
    server.bind(("localhost", 9002))
    while True:
        client, addr = server.accept()
        handle_clients = th.Thread(target=clients_handler, args=((client, addr)))


def clients_handler(clinet_socket, addr):
    with clinet_socket as c:
        while True:
            resp = c.recv(1024).decode()
            print(f"Received: {resp}, from {addr[0]}:{addr[1]}")
            if resp == "exit":
                c.close()
                print("Connection closed")
                break
            c.send(f"Response Length:{len(resp)}\n First_char= {resp[0]}".encode())
