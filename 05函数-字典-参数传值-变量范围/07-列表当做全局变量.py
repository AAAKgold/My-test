#列表或者字典 当做全局变量 可以不用global 直接用

nums = [11,22,33]


infor = {"name":"laowang"}

def test():
    #for num in nums:
     #   print(num)
    nums.append(44)
    infor["age"]=18
    #infor["name"] = "laoli"
def test2():
    print(nums)
    print(infor)
test()
test2()
