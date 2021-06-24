#python3

#字符串
message = "Hello world"
message1 = "Hello"
message2 = "Python"
message3 = "Hello "
message4 = " Python"
print("首字母大写")
print(message.title())
print("全部字母大写")
print(message.upper())
print("全部字母小写")
print(message.lower())
print("字符串合并")
print(f"{message1}  {message2}")
print("字符串添加换行")
print(f"Hello\n{message2}")
print("移除左右空格")
print(f"{message3.rstrip()}{message4.lstrip()}")

#数
print("用下划线分割大数字")
print(100_000_00_0000)
print("同时赋值多个变量")
x, y, z = 0, 1, 2
print(x, y, z)
print("Python之禅")
import this

#列表
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(f"bicycles[0]: {bicycles[0]}")
print(f"bicycles[3] strip: {bicycles[3].strip()}")
print(f"bicycles[-1]: {bicycles[-1]}")
print(f"bicycles[-2]: {bicycles[-2]}")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(f"单独修改motorcycles[0]: {motorcycles}")
motorcycles = []
print("初始化一个空列表")
print(motorcycles)
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print("添加三个元素后")
print(motorcycles)
motorcycles.insert(0, 'ducati')
print("首位插入元素ducati")
print(motorcycles)
del motorcycles[0]
print("删除首位元素ducati")
#python变量赋值默认是引用，拷贝需要显示调用
pop_motor = motorcycles.copy()
print(pop_motor)
#pop和del相比是可以拿到被删除元素的值
print(f"弹出方式删除末尾元素: 弹出值{pop_motor.pop()}，剩余值{pop_motor}")
print(pop_motor)
print(f"弹出方式删除首位元素: 弹出值{pop_motor.pop(0)}，剩余值{pop_motor}")
remove_motor = motorcycles.copy()
print(remove_motor)
remove_motor.remove('honda')
print(f"通过元素值删除元素: 删除值honda，剩余值{remove_motor}")

#列表排序
#看起来是按照首字母ASCII码排序的
print("原始顺序")
cars = ['BMW', 'audi', 'toyota', 'subaru']
cars1 = cars.copy() 
print(cars)
print("首字母排序")
cars.sort()
print(cars)
print("首字母反向排序")
cars.sort(reverse=True)
print(cars)
print("原始顺序")
print(cars1)
print("sorted临时排序")
print(sorted(cars1, reverse= True))
print("sorted排序后不影响原始顺序")
print(cars1)
print("反转列表顺序")
cars1.reverse()
print(cars1)
print(f"列表长度: {len(cars1)}")

#列表操作
magicians = ['alice', 'david', 'carolina']
print("原始列表")
print(magicians)
print("循环打印每个元素")
for magician in magicians:
    print(magician)
print("使用循环访问数字列表")
for value in range(1, 5):
    print(value)
print("使用list方法生成数字列表")
numbers = list(range(1, 6))
print(numbers)
print("使用range方法指定步长生成奇数列表")
numbers = list(range(1, 10, 2))
print(numbers)
print("使用range和列表解析生成平方数列表")
#列表解析，**表示平方
squares = [value ** 2 for value in range(1, 11)]
print(squares)
print("初始列表")
digits = list(range(0, 10))
print(digits)
print("最大值")
print(max(digits))
print("最小值")
print(min(digits))
print("求和")
print(sum(digits))
print("使用切片间隔2打印")
print(digits[0:-1:2])
#切片
print("初始列表")
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players)
print("使用切片打印中间3名队员的切片")
print(players[1:4])
print("打印player[:2]，无指定时，默认最大或者最小")
print(players[:2])
print("打印player[-3:]，无指定时，默认最大或者最小")
print(players[-3:])
print("使用for循环遍历打印切片")
for player in players[1:4]:
    print(player.title())
print("使用切片实现列表拷贝，python直接赋值是引用")
players1 = players[:]
del players1[0]
print(players)
print("删除新列表第一个元素")
print(players1)
#元组，不可变的列表
print("初始元组")
dimensions = (200, 50)
print(dimensions[:])
print("只能通过重新赋值改变元组")
dimensions = (200, 50, 80)
print(dimensions)
print("只有一个元素的元组")
#元组是由逗号标识，这里不加逗号会报错
dimensions = (200,)
print(dimensions[0])

#if语句
print("初始列表，判断不为空则打印")
cars = ['bmw', 'audi', 'toyota', 'subaru']
if cars:
    print(cars)
print("if条件使用, not in使用, elif使用")
for car in cars:
    if car == 'bmw' or car <= 'audi':
        print(car.upper())
    elif 'audi' not in cars:
        print('benz')
    else:
        print(car.title())
print(cars)
