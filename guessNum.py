import random
x = random.randint(1,50)
print(x)

for i in range(5):
    bingo = False
    while True:
        try:
            y = int(input("Pls key num(1~50)"))
            if x == y:
                print("good")
                bingo = True
                break
            if x > y:
                print("guess bigger")
            else:
                print("guess smaller")
            break
        except Exception as e:
            print("Pls key in number")

    if bingo:
        break
if bingo:
    print("congratulation")
else:
    print("Anser is x")

  