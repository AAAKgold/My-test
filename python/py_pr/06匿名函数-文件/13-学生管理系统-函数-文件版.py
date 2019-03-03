import os
admin_infors = []
def print_menu():
    '''完成打印功能菜单'''
    #1.打印菜单功能
    print("="*30)
    print("  学生管理系统V0.01 ")
    print("  1.添加一个新的信息")
    print("  2.删除一个学生信息")
    print("  3.修改一个学生信息")
    print("  4.查询一个学生信息")
    print("  5.显示所有学生信息")
    print("  6.保存数据到文件中")
    print("  7.退出系统")
    print("  8.删除数据库")
    print("="*30)

def add_new_infor(): 
    '''添加一个新的信息'''
    new_name = input("请输入您要添加的姓名：")
    new_age = int(input("请输入该学生的年龄："))
    new_SID = int(input("请输入该学生的学号："))
    new_sex = input("请输入该学生的性别：")
    new_infor = {}
    new_infor['name'] = new_name
    new_infor['age'] = new_age
    new_infor['SID'] = new_SID
    new_infor['sex'] = new_sex 
    #print(new_infor) #for test
    admin_infors.append(new_infor)
    #print(admin_infors) #for test

def del_infor():
    '''删除信息'''
    del_name = input("请输入您要删除的姓名：")
    i = 0#计数 记录要删除的名字的位置 
    for temp in admin_infors:
        i += 1
        if del_name == temp['name']:
            print("要删除的信息已找到！")
            del admin_infors[i-1]
            print("信息已删除！")
            #print(i)#for test
            break #找到了裂开终止
    else:
        print("您要删除的信息不在此……")

def modi_infor():
    '''修改信息'''
    modi_name = input("请输入您要修改的学生姓名：") 
    j = 0
    for temp in admin_infors:
        j += 1
        if modi_name == temp['name']:
            print("要修改的姓名已找到")
            new_name = input("请输入您要添加的姓名：")
            new_age = int(input("请输入该学生的年龄："))
            new_SID = int(input("请输入该学生的学号："))
            new_sex = input("请输入该学生的性别：")
            new_infor = {}
            new_infor['name'] = new_name
            new_infor['age'] = new_age
            new_infor['SID'] = new_SID
            new_infor['sex'] = new_sex
            
            admin_infors[j-1] = new_infor
            print("信息已修改")
            break
    else:
        print("您要修改的学生信息不在此")

def find_infor():
    '''查询信息'''
    find_name = input("请输入您要查询的名字：")
    for temp in admin_infors:
        if find_name == temp['name']:
            print("姓名\t年龄\t学号\t性别")
            print("%s\t%s\t%s\t%s"%(temp['name'],temp['age'],temp['SID'],temp['sex']))
            break
    else:
        print("您要查找的信息不在此")

def show_infor():
    '''显示所有信息'''
    print("姓名\t年龄\t学号\t性别")
    for temp in admin_infors:
        print("%s\t%s\t%s\t%s"%(temp['name'],temp['age'],temp['SID'],temp['sex']))

def exit_infor():
    '''退出系统'''
    print("感谢使用本系统，再见！")

def clear_infor():
    '''删除数据库'''
    num = int(input("请输入数字1再次确认删除数据库："))
    if num == 1:
        admin_infors.clear()
        print("数据库已删除！系统已自动报警，谁也跑不了！！！")
    else:
        print("操作失败")

def sava_data():
    """加载之前存储的数据"""
    folder_name = open("info_data.data","w")
    folder_name.write(str(admin_infors))
    folder_name.close()

def load_data():
    """加载之前存储的数据"""
    folder_name = open("info_data.data")
    content = folder_name.read()
    admin_infors = eval(content)
    folder_name.close()

def tip_infor():
    '''输入提示'''
    print("您的输入有误，请重新输入(1~7)")

def main():
    '''主函数'''

    #加载数据 1次即可
    load_data()

    while True:
        #打印菜单功能
        print_menu()
        #2.用户输入
        num = int(input("请输入操作序号："))
        #3.添加姓名
        if num == 1:
            add_new_infor()
        #4.删除姓名
        elif num ==2:
            del_infor()
        #5.修改姓名
        elif num ==3:
            modi_infor()
        #6.查询姓名
        elif num ==4:
            find_infor()
        #7.显示所有学生信息
        elif num ==5:
            show_infor()
        #8.保存数据到文件中
        elif num ==6:
            sava_data()
        #9.退出系统
        elif num ==7:
            exit_infor()
            break
        #10.数据库删除
        elif num ==8:
            clear_infor()
        else:
            tip_infor()
#调用主函数
main()

