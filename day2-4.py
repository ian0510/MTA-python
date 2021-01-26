import random
ans = random.randint(1,10)
time = 1
while True:
    guess = int(input("guess number?"))
    if ans == guess:
        print("right")
        print(time)
        break
    elif guess < ans:
        print("guess a bigger number")
        print("wrong")
    elif guess > ans:
        print("guess a smaller number")
        print("wrong")
    time += 1 