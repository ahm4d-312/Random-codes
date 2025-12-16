def infinite_numbers():
    n = 0
    while True:
        yield n
        n += 1

def gen():
    gen = infinite_numbers()
    for i in range(20):
        print(next(gen), end=" ")

def main():
    lis=[1,2,3,4]
    with open('list.txt','r') as f:
        lis=f.read()
    for i in lis:
        print(i)
if __name__=='__main__':
    main()