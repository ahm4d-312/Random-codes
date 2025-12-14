import threading as th
import socket as s

server = s.socket(s.AF_INET, s.SOCK_STREAM)


def tcp_server():
    i = 0
    while i != 4:
        client, addr = server.accept()
        handle_clients = th.Thread(target=clients_handler, args=(client, addr))
        handle_clients.start()
        i += 1


def clients_handler(clinet_socket, addr):
    with clinet_socket as c:
        resp = c.recv(1024).decode()
        print(f"Received: {resp}, from {addr[0]}:{addr[1]}")
        c.send(f"Response Length:{len(resp)}\nFirst_char= {resp[0]}".encode())


def main():
    server.bind(("localhost", 9003))
    server.listen(4)
    tcp_server()


if __name__ == "__main__":
    main()
