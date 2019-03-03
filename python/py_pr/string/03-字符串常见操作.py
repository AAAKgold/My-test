mystr = 'hello\nworld\titcast and itcastcpp'

#mystr.find('itcast')#查找 itcast 在列表中的位置 

#mystr.find('itcast',0,10)# 0,10 是查找范围 -1表示没有

#mystr.index('itcast',0,10)#跟find一样，如果str不在mystr会报一个异常

#mystr.count('itcast')# itcast 出现的次数

#mystr = mystr.replace("itcast","haha",1)#itcast 替换成 haha 1表示替换的次数

#mystr = mystr.split(' ',2)#mystr.split("i",2)  注意引号中间默认为空格 如果是i 则以i分隔



#mystr = mystr.capitalize()#把字符串的第一个字符大写
#mystr = mystr.title()#把字符串的每个单词首字母大写

#mystr = mystr.startswith('hello')#检查字符串是否是以hello开头，是返回True 否返回False
#mystr = mystr.endswith('cpp')#检查字符串是否以cpp结束

#mystr = mystr.lower()#转换mystr中所有大写字符为小写
#mystr = mystr.upper()#转换mystr中所有小写字符为大写

#mystr = mystr.ljust(100)#返回一个原字符串左对齐，并使用空格填充至长度100的新字符串
#mystr = mystr.rjust(100)#返回一个原字符串右对齐，并使用空格填充至长度100的新字符串
#mystr = mystr.center(100)#返回一个原字符串居中，并使用空格填充至长度100的新字符串

#mystr = mystr.lstrip()#删除mystr左边的空白字符
#mystr = mystr.rstrip()#删除mystr末尾的空白字符
#mystr = mystr.strip()#删除mystr两端的空白字符

#mystr = mystr.rfind('itcast') #从右边开始查找
#mystr = mystr.rindex('itcast') #从右边开始查找

#mystr = mystr.partition('itcast')#把mystr分割成三部分，itcast前 itcast 和 itcast后
#mystr = mystr.rpartition('itcast')#把mystr分割成三部分，从右边开始

#mystr = mystr.splitlines()#按照行分隔，返回一个包含各行作为元素的列表

#mystr = mystr.isalpha()#如果mystr所有字符都是字母，则返回True 否则返回False
#mystr = mystr.isdigit()#如果mystr只包含数字则返回True 否则返回False

#mystr = mystr.isalnum()#如果mystr都是字母或数字则返回True 否则返回False
#mystr = mystr.isspace()#如果mystr只包含空格 则返回True 否则返回False

#mystr = mystr.join(str)#mystr中每个字符后面插入str 构造一个新的字符串


print(mystr)


