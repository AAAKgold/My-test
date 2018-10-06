
# 全局变量 用来存储名片 当全局变量是字典或者列表 可不用global 进行申明
card_infors = []


def print_menu():
    '''完成打打印功能菜单'''
    print("=" * 50)
    print("   名片管理系统  V0.01")
    print(" 1.添加一个新的名片")
    print(" 2.删除一个新的名片")
    print(" 3.修改一个新的名片")
    print(" 4.查询一个新的名片")
    print(" 5.显示所有的名片")
    print(" 6.退出系统")
    print(" 7.删除数据库")
    print("=" * 50)


def add_new_card_infor():
    '''完成添加一个名片'''
    # global card_infors#申明全局变量 此函数后面用到了 此处也可以不用global 列表或字典做
    #                   全局变量可以不用global
    new_name = input("请输入新的名字:")
    new_qq = input("请输入新的QQ:")
    new_wec = input("请输入新的微信:")
    new_addr = input("请输入新的地址:")

    # 定义一个新的字典，用来存储一个新的名片
    new_infor = {}
    new_infor['name'] = new_name
    new_infor['qq'] = new_qq
    new_infor['wec'] = new_wec
    new_infor['addr'] = new_addr

    # 将一个字典添加到列表中
    card_infors.append(new_infor)
    # print(card_infors) #for test


def del_card_infor():
    '''用来删除一个名片'''
    # global card_infors#可加global可不加
    del_name = input("请输入你要删除的姓名:")
    i = 0
    del_flag = 0  # 默认表示没有找到被删除的名片

    # 寻找要删除的名片位置
    for temp in card_infors:
        i += 1  # 记录找到名片的位置
        # print(i) #for test
        if del_name in temp["name"]:
            del_flag = 1  # 名片找到了
            print("删除的名片已找到")
            break  # 找到了就不在循环

    # 删除列表中的字典
    if del_flag == 1:
        del card_infors[(i - 1)]  # 列表计数从0开始
        print("名片已删除")
    else:
        print("您要删除的名片不存在")


def modi_card_infor():
    '''用来修改一个名片'''
    global card_infors
    modification_name = input("请输入您要修改的名字:")
    x = -1
    for temp in card_infors:
        x += 1  # 寻找要修改名片的位置
        modi_flag = 0  # 默认表示修改的名片没找到
        if modification_name == temp["name"]:
            modi_flag = 1
            # 添加修改的名片信息
            new_name = input("请输入新的名字：")
            new_qq = input("请输入新的QQ:")
            new_wec = input("请输入新的微信:")
            new_addr = input("请输入新的地址:")
            # 定义一个新的字典，用来存储一个新的名片
            new_infor = {}
            new_infor['name'] = new_name
            new_infor['qq'] = new_qq
            new_infor['wec'] = new_wec
            new_infor['addr'] = new_addr
            # 将一个字典添加到列表中
            card_infors[x] = new_infor
            print("修改成功")
            break
    if modi_flag == 0:
        print("您要修改的名片不存在")


def find_card_infor():
    '''用来查找一个名片'''
    global card_infors
    find_name = input("请输入要查找的姓名:")
    find_flag = 0  # 默认表示没有找到
    for temp in card_infors:
        if find_name == temp['name']:
            print("%s\t%s\t%s\t%s" %
                  (temp['name'], temp['qq'], temp['wec'], temp['addr']))
            find_flag = 1  # 表示找到了
            break

    # 判断是否找到 两种方法：用flag或者用for else
    # if find_flag ==0:
    else:
        print("查无此人……")


def show_card_infor():
    '''用来显示所有名片'''
    global card_infors
    print("姓名\tQQ\t微信\t地址")
    for temp in card_infors:
        print("%s\t%s\t%s\t%s" %
              (temp['name'], temp['qq'], temp['wec'], temp['addr']))


def sign_out():
    '''退出系统'''
    print("感谢使用本系统，再见！")


def del_card():
    '''删除数据库'''
    num = int(input("请再次输入数字1确认删除数据库："))
    if num == 1:
        card_infors.clear()
        print("数据库已删除，系统已自动报警，谁也跑不了！")
    else:
        print("删除失败")


def tip_card():
    '''输入错误提示'''
    print("输入有误，请重新输入")


def main():
    '''主函数'''
    # 1.打印功能提示
    print_menu()

    while True:
        # 2.获取用户的输入
        num = int(input("请输入操作序号："))
        # 3.根据用户的数据执行相应的功能
        if num == 1:
            add_new_card_infor()
        elif num == 2:
            del_card_infor()
        elif num == 3:
            modi_card_infor()
        elif num == 4:
            find_card_infor()
        elif num == 5:
            show_card_infor()
        elif num == 6:
            sign_out()
            break
        elif num == 7:
            del_card()
            break
        else:
            tip_card()

        print("")


# 调用主函数
main()
