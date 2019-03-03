#1.定义字符串
questions = 'hello world'

#2.统计个数
for letter in questions:
    answer = questions.count('%s'%letter)
    print('%s'%letter, '%d'%answer)
    
'''    
questions = sorted(set(questions))
'''






