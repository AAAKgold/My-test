'''
1.包类
2.包的属性
3.书包里放东西
4.定义所放物品的类
'''

class Ssbag(object):
    def __init__(self,new_capatity,new_name):
        self.capatity=new_capatity
        self.name = new_name
        self.left_capatity=new_capatity
        self.contain_items=[]
    def __str__(self):
        return "%s的容量是:%d,剩下的容量:%d,里面的有%s"%(self.name,self.capatity,self.left_capatity,str(self.contain_items))
        #return shch
    def add_item(self,item):
        self.left_capatity -= item.capatity
        self.contain_items.append(item.infor)
class Wp(object):
    def __init__(self,new_name,new_colour,new_brand,new_capatity):
        self.name=new_name
        self.colour=new_colour
        self.brand=new_brand
        self.capatity=new_capatity
        self.infor={}
        self.infor["capatity"]=self.capatity
        self.infor["name"]=self.name
        self.infor["colour"]=self.colour
        self.infor["brand"]=self.brand
    def __str__(self):
        return "%s占用的容量是%d,颜色是:%s,品牌是:%s,"%(self.name,self.capatity,self.colour,self.brand)
        #return a

danjianbao=Ssbag(10,"lv")
print(danjianbao)

lipstick=Wp("口红","999","迪奥",1)
print(lipstick)

#shouji=Wp("手机","黑","华为",1)
#print(shouji)

danjianbao.add_item(lipstick)
#danjianbao.add_item(shouji)
print(danjianbao)


