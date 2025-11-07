print("I'm suffering")

i = -10
try:
    while i:
        print(i)
        i -= 1
except KeyboardInterrupt:
    print("KeyboardInterrupt")
