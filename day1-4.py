score = int(input("輸入成績"))
if (score <= 100 and score >= 0):
    if score >= 90:
        print("甲")
    elif score >= 80:
        print("乙")
    elif score >= 70:
        print("丙")
    elif score >= 60:
        print("丁")
    else:
        print("戊")
else:
    print("輸入錯誤")