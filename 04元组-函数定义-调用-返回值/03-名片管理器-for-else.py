card_infors = [{"name":"laowang","age":18},{"name":"laoli","age":19},{"name":"laozhao","age":20}]

find_name = input("请输入要查询的名字:")

for temp in card_infors:
    if temp["name"] == find_name:
        print('zhaodao')
        break#用了break else 不会执行； 没有break else一定执行
else:
    print("没有找到")





