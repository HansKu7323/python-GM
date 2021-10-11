import random

low = 1
high = 50

x = random.randint(1,50)
print(x)

for i in range(5):
    bingo = False
    while True:
        try:
            print(f"{low}~{high}")
            y = int(input("Pls key num(1~50)"))
            if x == y:
                print("good")
                bingo = True
                break
            if x > y:
                print("guess bigger")
                if y > low:
                    low = y+1
            else:
                print("guess smaller")
                if y < high:
                    high = y-1
            break
        except:
            print("Pls key in number")

    if bingo:
        break
if bingo:
    print("congratulation")
else:
    print("Anser is ",x)

  
