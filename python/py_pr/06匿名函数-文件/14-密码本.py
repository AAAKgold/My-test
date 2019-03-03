import os
import os.path
infors = {}  #传建一个存储内容的字典


url_file = open("password.txt", "r+")  #打开文件 
content = url_file.readlines()  # 缓冲文件内容到content
url_file.close()

def menu():
    """创建一个菜单函数"""
    print("=" * 30)
    name = "密码本 V1.0"
    print(name.center(30))
    print("增加【1】")
    print("删除【2】")
    print("修改【3】")
    print("查找【4】")
    print("退出【5】")
    print("=" * 30)


def add():
    """创建一个添加信息函数"""
    url_file = open("password.txt", "r+")
    input_add_name = input("请输入要添加的名称：")
    add_call_find = find(input_add_name)
    if add_call_find[0] == 0:

        input_add_url= input("请输入你要添加的URL：")
        input_add_explian = input("请输入URL的说明：")
        infors["URL名称"] = input_add_name
        infors["URL："] = input_add_url
        infors["URL说明："] = input_add_explian

        data = str(infors) + "\n"
        url_file.seek(0,2)
        url_file.write(data)
        url_file.flush()

        url_file.close()
    else:
        print("URL名称已存在！")

def pop():
    """创建一个删除函数"""
    input_pop_name = input("请输入你要删除的URL的名称：")
    pop_call_find = find(input_pop_name)

    if pop_call_find[0] == 1:
        pop_file = open("password.txt", "r")
        old_file = pop_file.readlines()

        write_file = open("password.txt", "w")
        for temp in old_file:
            pop_content = eval(temp)
            if pop_content["URL名称："] == input_pop_name:
                continue
            write_file.writelines(temp)

        pop_file.flush()
        write_file.flush()

        pop_file.close()
        write_file.close()
        print("文件已删除！")


    else:
        print("你要删除的文件不存在！")


def amend():
    """创建一个修改函数"""
    input_amend_name = input("请输入你要修改的URL名称：")
    amend_call_find = find(input_amend_name)

    if amend_call_find[0] == 1:
        input_amend_newname = input("请输入新的URL名称：")
        input_amend_newurl = input("请输入新的URL:")
        input_amend_newexplain = input("请输入新的URL说明：")
        new_amend_file = open("[备份]password.txt", "a+")

        for old_file in content:
            old_file = eval(old_file)
            if old_file["URL名称："] == input_amend_name:
                infors["URL名称："] = input_amend_newname
                infors["URL："] = input_amend_newurl
                infors["URL说明："] = input_amend_newexplain
                new_content = str(infors) + "\n"
                new_amend_file.write(new_content)

                continue
            new_content = str(old_file) + "\n"
            new_amend_file.writelines(new_content)

        new_amend_file.close()
        url_file.close()
        file_name = os.path.basename("password.txt")
        #os.chdir("D:\python")
        os.remove("password.txt")
        os.rename("[备份]password.txt",file_name)

    else:
        print("你要修改的文件不存在！")


def find(x):
    """创建一个查找函数工具，找到函数名称返回1 没找到返回0"""
    #input_find_name = input("请输入你要查找的URL名称：")
    input_find_name = x
    i = 0
    for eachline in content:
        str_content = eval(eachline)

        if str_content["URL名称："] == input_find_name:
            i = 1
            return i , str_content
            #else:
            #return i , "没有数据"
    return i , "没有数据"



def find_true():
    """创建一个查找函数"""
    input_find_true_name = input("请输入你要查找的URL名称：")

    find_true_call = find(input_find_true_name)

    if find_true_call[0] == 1:
        print("URL名称：%s URL: %s URL说明：%s" %(find_true_call[1]["URL名称"] , find_true_call[1]["URL："] ,
                                            find_true_call[1]["URL说明："]))
    else:
        print("您要查找的函数不存在！")

def quit():
    print("感谢您的使用！ -*- ")


def main():

    while True:
        print("")
        menu()
        print("")
        input_num = int(input("请输入功能序号："))

        if input_num == 1:
            add()
        elif input_num == 2:
            pop()
        elif input_num == 3:
            amend()
        elif input_num == 4:
            find_true()
        elif input_num == 5:
            quit()
            break
        else:
            print("请输入正确的功能序号：")

main()
