class Home:
    def __init__(self,new_area,new_info,new_addr):
        self.area = new_area
        self.left_area = new_area
        self.info = new_info
        self.addr = new_addr
        self.contain_items = []

    def __str__(self):
        msg = "房子的总面积是%d,可用面积是%d,房型是%s,房子的地址是%s"%(self.area,self.left_area,self.info,self.addr)
        msg = msg + "当前房子有物品%s"%(self.contain_items)
        return msg

    def add_item(self,item):
        self.left_area = self.left_area - item.get_area()
        self.contain_items.append(item.get_name())

class Bed:
    def __init__(self,new_area,new_name):
        self.area = new_area
        self.name = new_name

    def __str__(self):
        return "%s占用的面积是%d"%(self.name,self.area)

    def get_area(self):
        return self.area

    def get_name(self):
        return self.name

fangzi = Home(129,"三室一厅","北京市朝阳区666号")
print(fangzi)

bed1 = Bed(6,"三人床")
print(bed1)

fangzi.add_item(bed1)
print(fangzi)

bed2 = Bed(4,"双人床")
fangzi.add_item(bed2)
print(fangzi)

