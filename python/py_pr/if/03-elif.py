score_s = input("请输入你的成绩")

score =int(score_s)

if score>=90 and score<=100:
    print("本次考试等级为A")
elif score>=80 and score<90:
    print("本次考试等级为B")
elif score>=70 and score<80:
    print("本次考试等级为C")
elif score>=60 and score<70:
    print("本次考试等级为D")
elif score>=0 and score<60:
    print("本次考试等级为E")
