stus = [{"name":"zhangsan","age":18},{"name":"lisi","age":19},{"name":"wangwu","age":17}]

stus.sort(key = lambda x:x['name'])#按name排序

print(stus)

stus.sort(key = lambda x:x['age'])#按age排序

print(stus)


