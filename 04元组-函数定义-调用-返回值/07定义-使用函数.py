def print_menu():
    print("="*50)
    print(" 名片管理系统v0.1")
    print("1")
    print("2")
    print("="*50)

def print_triangle():
    print("*")
    print("*"*2)
    print("*"*3)
    print("*"*4)

def print_oneline():
    print("-"*30)


def print_numLine(num):
    i = 0
    while i < num:
        print_oneline()
        i += 1

#调用函数
print_menu()
print_triangle()

print_oneline()

print_numLine(3)


