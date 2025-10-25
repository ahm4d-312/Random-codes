import argparse
import textwrap
import sys
import socket


def main():
    parser = argparse.ArgumentParser(
        description="My simple net tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent(
            """Example:
        nc.py -t 192.168.1.108 -p 5555 -l -c\t#command shell               

        nc.py -t 192.168.1.108 -p 5555 -l -u=mytest.txt\t#upload to file

        nc.py -t 192.168.1.108 -p 5555 -l -e="cat /etc/passwd"\t# execute command 
        
        echo 'ABC' | ./nc.py -t 192.168.1.108 -p 135\t# echo text to server port 135
        
        nc.py -t 192.168.1.108 -p 5555\t# connect to server
        """
        ),
    )
    parser.add_argument("-c", "--command", action="store_true", help="command shell")
    parser.add_argument("-e", "--execute", help="execute specified command")
    parser.add_argument("-p", "--port", type=int, default=5555, help="specified port")
    parser.add_argument("-u", "--uplaod", help="uplaod file")
    parser.add_argument("-l", "--listen", action="store_true", help="listen")
    parser.add_argument("-t", "--target", default="192.168.1.11")

    args = parser.parse_args()

    if args.listen:
        buffer = ""
    else:
        buffer = sys.stdin.read()
    nc = Netcat(args, buffer.encode())
    nc.run()
    args = parser.parse_args()


class Netcat:
    def __init__(self, args, buffer=None):
        self.args = args
        self.buffer = buffer
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def run(self):
        if self.args.listen:
            self.listen()
            return
        self.send()

    def send(self):
        self.socket.connect((self.args.target, self.args.port))
        if self.buffer:
            self.socket.send(self.buffer)
        try:
            while True:
                recv_len = 1
                response = ""
                while recv_len:
                    data = self.socekt.recv(4096)
                    recv_len = len(data)
                    response = data.decode()
                    if recv_len < 4096:
                        break
                if response:
                    print(response)
                    buffer = input("> ")
                    buffer += "\n"
                    self.socket.send(buffer.encode())
        except KeyboardInterrupt:
            print("user terminated.")
            self.socket.close()
            sys.exit()


if __name__ == "__main__":
    main()
