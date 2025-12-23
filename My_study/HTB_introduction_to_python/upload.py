import socket
from os import path 
def recv_exact(clinet_socket,length):
        data=b''
        while len(data)<length:
            chunk=clinet_socket.recv(length-len(data))
            if not chunk:
                print("Connection currpted!")
                break
            data+=chunk
        return data


def upload(clinet_socket):

    try:
        fname_len=int.from_bytes(recv_exact(clinet_socket,4),'big')
        fname=recv_exact(clinet_socket,fname_len).decode()
        f_len=int.from_bytes(recv_exact(clinet_socket,8),'big')
        with open(fname,'wb') as f:
            received=0
            while received<f_len:
                chunk=clinet_socket.recv(min(4096,f_len-received))
                if not chunk:
                    raise ConnectionError("Connection corrupted: The sender closed early")
                received+=len(chunk)
                f.write(chunk)
            del(received)
    except ConnectionError as e:
        print("Upload failed: {e}")

def receive(clinet_socket):
    fpath=input("path:")
    fname=fpath.strip().split('/')[-1]
    fname_len=len(fname.encode())
    fsize=path.getsize(fpath)
    clinet_socket.sendall(fname_len.to_bytes(4,'big'))
    clinet_socket.sendall(fname.encode())
    clinet_socket.sendall(fsize.to_bytes(8,'big'))
    try:
        with open(fpath,'rb') as f:
            while True:
                chunk=f.read(4096)
                if not chunk:
                    break
                clinet_socket.send
    except Exception as e:
        print(f"Error: {e}")


def main():
    client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)