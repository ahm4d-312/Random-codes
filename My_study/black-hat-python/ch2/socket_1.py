import socket
import threading
import time

def tcp_connection():

    # create socket object
    client =socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    target_host="www.google.com"
    target_port=80
    
    client.connect((target_host,target_port))

    client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")
    response=client.recv(4096)

    client.close()
    print(response.decode())

def udp_connection():
    target_host="127.0.0.1"
    target_port=9997
    # create socket object
    client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    # send some data
    client.sendto(b"AAABBBCCC",(target_host,target_port))

    # receive some data
    respone,addrsess=client.recvfrom(4096)
    client.close()
    print(respone,addrsess)

def main():
    #print("connecting to a tcp clinet...")
    #tcp_connection()
    #print("connection closed.\n")
    #print("talking to a udp clinet...")
    #udp_connection()
    #print("conversation ended.\n")
    t=time.time()
    tcp_server()
    print(time.time()-t)


def tcp_server():
    IP = "0.0.0.0"
    port=1337
    server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind((IP,port))
    server.listen(500)
    print(f"[*] Listening on {IP}:{port}")
    i=0
    while True:
        i+=1
        if i==50000:
            break
        client,address=server.accept()
        print(f"[*] Accepted connection from {address[0]}:{address[1]}")
        client_handler=threading.Thread(target=handle_client,args=(client,))
        client_handler.start()
    
def handle_client(client_socket):
    with client_socket as sock:
        request=sock.recv(1024)
        print(f"[*] Received: {request.decode("utf-8")}")
        sock.send(b'ACK')

if __name__=='__main__':
    main()
