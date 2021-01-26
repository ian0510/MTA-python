score_list = []
num = int(input("number?"))
for i in range(num):
    score = int(input("score"))
    if score < 60:
        score = 60
    score_list.append(score)
score_list.sort()
a = score_list[-1]
b = score_list[0]
print("最高分",a)
print("最低分",b)