score_list = []
num = int(input("number?"))
for i in range(num):
    score = int(input("score"))
    if score < 60:
        score = 60
    score_list.append(score)