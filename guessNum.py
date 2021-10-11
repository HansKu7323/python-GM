import random
x = random.randint(1,50)
print(x)

for i in range(5):
    try:
        y = int(input("Pls key num(1~50)"))
        if x == y:
            print("good")
            break
        if x > y:
            print("guess bigger")
        else:
            print("guess smaller")
    except Exception as e:
        print(e)


  