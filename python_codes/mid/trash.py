import socket as s
import dns.resolver as dns

c = s.socket(s.AF_INET, s.SOCK_STREAM)
c.settimeout(1)
lis = [22, 11, 443, 80, 8080]
for i in lis:
    r = c.connect_ex(("127.0.0.1", i))
    if r == 0:
        print(s.getservbyport(i), i)
c.close()
