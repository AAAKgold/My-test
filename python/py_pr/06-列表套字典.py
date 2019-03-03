name_list = []

while True:
    choice = int(input("请输入 1/2/3/4/5/6/7:"))
    if choice ==1:

        name = input("请输入名字：")
        wechat = input("请输入微信：")
        phone = input("请输入电话：")
        addr = input("请输入地址：")

        #创建字典
        card_infor = {}
        card_infor['name'] = name 
        card_infor['wechat'] = wechat 
        card_infor['phone'] = phone 
        card_infor['addr'] = addr 

        #print(card_infor) for test

        #把字典添加到列表中
        name_list.append(card_infor)
        #print(name_list) for test
    elif choice ==2:
        print("姓名\t微信\t电话\t地址")
        #从名片字典中循环出列表
        for temp in name_list:
            print("%s\t%s\t%s\t%s"%(temp["name"],temp["wechat"],temp["phone"],temp["addr"]))
    
    elif choice ==3:
        del_name = input("请输入您要删除的名字：")
        
        x = -1
        for temp in name_list:
            #每迭代一个字典x+1 ，第一个字典位置加1刚好为0
            x += 1
            if del_name == temp["name"]:
                del name_list[x]
                print("名片已删除")
                break
        else:#此处有两种做法：else配break 或者 flag=1/0 标记删除和不存在
            print("您要删除的名片不存在")
    elif choice ==4:
        edit_name = input("请输入您要修改的名字：")
        
        x = -1
        for temp in name_list:
            x += 1
            if edit_name in temp["name"]:
                name = input("请输入名字：")
                wechat = input("请输入微信：")
                phone = input("请输入电话：")
                addr = input("请输入地址：")
                card_infor = {}
                card_infor['name'] = name 
                card_infor['wechat'] = wechat 
                card_infor['phone'] = phone 
                card_infor['addr'] = addr 
                name_list[x] = card_infor
                break
        else:
            print("您要修改的名字不存在")
    elif choice ==5:
        find_name = input("请输入您要查询的名字：")
        for temp in name_list:
            if find_name in temp["name"]:
                print("%s\t%s\t%s\t%s"%(temp["name"],temp["wechat"],temp["phone"],temp["addr"]))
                break#没有break的话 ，找到了还会执行else
        else:
            print("查无此人……")

    elif choice == 6:
        print("感谢使用本系统，再见！")
        break

    elif choice == 7:
        choice = int(input("请再次输入数字7确认删库："))
        if choice == 7:
            name_list.clear()
            print("已删除数据库！")
            break
    else:
        print("您的输入有误，请重新输入！")

    print("")

