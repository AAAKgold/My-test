#名片管理系统
card_infor = []

#0.人机交互，接收键盘输入的信息
def input_infor():
    num = int(input("请输入功能序号:"))
    pass


#1.函数：打印信息提示
def print_menu():
    print("="*40)
    print(" 名片管理系统V0.01")
    print("1.添加一个名片")
    print("2.删除一个名片")
    print("3.修改一个名片")
    print("4.查询一个名片")
    print("5.显示所有名片")
    print("6.退出系统")
    print("="*40)


#2.函数：添加一个新名字
def add_new_name():
    new_name = input("请输入要添加的姓名:")
    new_QQ = input("请输入QQ:")
    new_wechat = input("请输入微信:")
    new_addr = input("请输入地址:")

    #建立字典,把信息保存到字典的相对应位置
    new_infor = {}
    new_infor["name"] = new_name
    new_infor["QQ"] = new_QQ
    new_infor["wechat"] = new_wechat
    new_infor["addr"] = new_addr

    #将字典添加到列表中
    card_infor.append(new_infor)

    #打印名片
    print(card_infor)


#3.函数：删除一个名字
def del_name():
    del_names = input("请输入要删除的姓名：")
    i = 0

    for temp in card_infor:
        i += 1
        print(i)
        if del_names in temp["name"]:
            print("删除的名片已找到")
            break
    #删除名片
    del card_infor[(i-1)]
    print("名片已删除")



#4.修改一个名字
def modification_name():
    pass

#5.查询一个名字
def find_name():
    find_name = input("请输入要查找的姓名：")
    find_flag = 0

    for temp in card_infor:
        if find_name in temp["name"]:
            print("姓名：%s\nQQ:%s\n微信：%s\n地址：%s"%(temp["name"],temp["QQ"],temp["wechat"],temp["addr"]))
            find_flag = 1
            break
    if find_flag == 0:
        print("查无此人")



#6.显示所有名片
def display_all_name():
    for temp in card_infor:
        print("姓名：%s\tQQ:%s\t微信：%s\t地址：%s"%(temp["name"],temp["QQ"],temp["wechat"],temp["addr"]))



#主函数
def main():

    print_menu()

    while True:
        num = int(input("请输入功能序号："))
        #input_infor()

        if num == 1:
            add_new_name()
        elif num == 2:
            del_name()
        elif num == 3:
            modification_name()
        elif num == 4:
            find_name()
        elif num == 5:
           display_all_name()
        elif num == 6:
            break
        else:
            print("您的输入有误，请重新输入！")


main()


