#1.打印菜单功能
print("="*30)
print("  学生管理系统V0.01 ")
print("  1.添加一个新的信息")
print("  2.删除一个学生信息")
print("  3.修改一个学生信息")
print("  4.查询一个学生信息")
print("  5.显示所有学生信息")
print("  6.退出系统")
print("  7.删除数据库")
print("="*30)
admin_infors = []
while True:
    #2.用户输入
    num = int(input("请输入操作序号："))

    #3.添加姓名
    if num == 1:
        new_name = input("请输入您要添加的姓名：")
        new_age = int(input("请输入该学生的年龄："))
        new_SID = int(input("请输入该学生的学号："))
        new_sex = input("请输入该学生的性别：")

        new_infor = {}
        new_infor['name'] = new_name
        new_infor['age'] = new_age
        new_infor['SID'] = new_SID
        new_infor['sex'] = new_sex
        
        print(new_infor)
        admin_infors.append(new_infor)
        print(admin_infors)
    #4.删除姓名
    elif num ==2:
        i = 0
        del_name = input("请输入您要删除的姓名：")
        for temp in admin_infors:
            i += 1
            if del_name == temp['name']:
                print("要删除的信息已找到！")
                del admin_infors[i-1]
                print("信息已删除！")
                #print(i)#for test
                break
        else:
            print("您要删除的信息不在此……")



    #5.修改姓名
    elif num ==3:
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



    #6.查询姓名
    elif num ==4:
        find_name = input("请输入您要查询的名字：")
        for temp in admin_infors:
            if find_name == temp['name']:
                print("姓名\t年龄\t学号\t性别")
                print("%s\t%s\t%s\t%s"%(temp['name'],temp['age'],temp['SID'],temp['sex']))
                break
        else:
            print("您要查找的信息不在此")



    #7.显示所有学生信息
    elif num ==5:
        print("姓名\t年龄\t学号\t性别")
        for temp in admin_infors:
            print("%s\t%s\t%s\t%s"%(temp['name'],temp['age'],temp['SID'],temp['sex']))


    #8.退出系统
    elif num ==6:
        print("感谢使用本系统，再见！")
        break
    #9.数据库删除
    elif num ==7:
        num = int(input("请输入数字1再次确认删除数据库："))
        if num == 1:
            admin_infors.clear()
            print("数据库已删除！系统已自动报警，谁也跑不了！！！")
        else:
            print("操作失败")
    else:
        print("您的输入有误，请重新输入")



    



