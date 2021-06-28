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

#字典
alien_0 = {'color': 'green', 'points': 5}
print("初始字典")
print(alien_0)
print("单独访问")
print(alien_0["color"])
alien_0['x_position'] = 0
alien_0['y_position'] = 0
print("添加元素")
print(alien_0)
alien_0['x_position'] = alien_0['x_position'] + 10
print("修改元素")
print(alien_0)
del alien_0["points"]
print("删除元素")
print(alien_0)
print("获取元素，防止元素不存在时程序报错")
print(alien_0.get('points', 'No point value assigned.'))
#遍历字典
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
print("初始字典")
print(favorite_languages)
print("遍历字典")
for key, value in favorite_languages.items():
    print(f'{key}: {value}')
print("只遍历键,不加keys()方法默认也是keys()")
for key in favorite_languages.keys():
    print(key)
print("只遍历键值")
for value in favorite_languages.values():
    print(value)
print("用set()方法去除重复元素, set的意思是集合，即去除重复")
print(set(favorite_languages.values()))
#集合
languages = {
    'python', 'c', 'ruby', 'python'
}
print("定义集合")
print(languages)
#字典中存储列表
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}
print("字典中嵌入列表")
for name, languages in favorite_languages.items():
    print(f"{name}'s favorite languages:")
    for language in languages:
        print(f"\t{language.title()}")
#字典中存储字典
print("字典中嵌入字典")
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    }
}
for username, userinfo in users.items():
    print(f"Username: {username}")
    fullname = f"{userinfo['first']} {userinfo['last']}"
    location = userinfo['location']
    print(f"\tFull name: {fullname.title()}")
    print(f"\tLocation: {location.title()}")
'''
print("input获取输入，默认输入数据类型是字符串，将字符串转换为数字")
age = input("How old are you ? ")
age = int(age) + 1
print(age)
'''
print("求模运算")
print(f"10 % 7 = {10 % 7}")
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
print("使用while循环删除所有cat，不使用循环只能删除第一个cat")
while 'cat' in pets:
    pets.remove('cat')
print(pets)

#函数
def get_formatted_name(first_name, last_name, middle_name = ''):
    '''设置默认参数为空，达到可选参数目的'''
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()
print('''设置默认参数为空，达到可选参数目的''')
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)
def get_formatted_name(first_name, *name):
    '''用*表示参数列表'''
    if len(name) > 1:
        full_name = f"{first_name} {name[0]} {name[1]}"
    else:
        full_name = f"{first_name} {name[0]}"
    return full_name.title()
print('用*表示任意数量参数,实现传入多个参数')
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)
print('用**表示参数字典')
def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
user_profile = build_profile('albert', 'einstein', location = 'princeton', field = 'physics')
print(user_profile)
print("导入模块，模块以.py后缀名存储")
import pizza
pizza.make_pizza(16, 'pepperoni')
print("导入模块内特定函数，省去了模块名前缀")
from pizza import make_pizza
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
print("用as可以给函数或者模块起别名")
from pizza import make_pizza as mp
mp(12, 'mushrooms', 'green peppers', 'extra cheese')
print("用*运算符导入所有函数")
from pizza import *
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#类
print("定义Dog类，使用类的方法和属性")
class Dog:
    '''创建小狗类'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sit(self):
        print(f"{self.name} is now sitting.")
    def roll_over(self):
        print(f"{self.name} rolled over!")
my_dog = Dog("Willie", 6)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.age = 3
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()
my_dog.roll_over()
print("定义Teddy类继承自Dog类，并定义Teddy类的方法和属性")
class Teddy(Dog):
    def __init__(self, name, age, gender):
        self.gender = gender
        super().__init__(name, age)
    def describe_character(self):
        print(f"My teddy {self.name} is outgoing.")
my_teddy = Teddy('dude', 5, 'female')
my_teddy.describe_character()
print(f"{my_teddy.name.title()} gender is {my_teddy.gender}.")
print("从一个模块导入多个类: car, ElectricCar")
#import类似代码拷贝，模块中的程序流程会直接运行
from car import Car, ElectricCar
my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()

#Python标准库
from random import randint
print("Python标准库：生成10以内随机数")
print(randint(1, 10))
from random import choice
print("Python标准库：从列表里随机选择一个元素")
pets = ['dog', 'cat', 'goldfish', 'rabbit']
print(choice(pets))

#文件
print("Python文件操作")
print("文件路径中的反斜杠会进行转义，所以文件路径中可使用双反斜杠或者斜杠")
filename = 'pi_digits.txt'
print(filename)
print('读取整个文件')
with open(filename) as file_object:
    lines = file_object.read()
print(lines.strip())
print('逐行读取文件')
#文件中每行有换行符，print也会打印换行符
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
print('将文件内容存入列表再读取各行内容')
with open(filename) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.rstrip())
print('使用读取行的内容, 使用strip删除前后空格')
with open(filename) as file_object:
    lines = file_object.readlines()
pi = ''
for line in lines:
    pi = pi + line.strip()
print(pi)
print("写文件，只能写入字符串，如果是数值则需要用str()转换")
#读取模式'r'，写入模式'w'(会清空已存在文件内容)，附加模式'a'，读写模式'r+'，省略参数则默认只读模式
filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write('I love python\n')
    file_object.write('I love programming\n')
print("异常处理，求取文件单词数目")
def count_words(filename):
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        #静默失败，什么都不做
        pass
    else:
        #split方法以空格或者其他自定义符合将字符串分拆成列表
        words = contents.split()
        #通过求取列表长度间接得到单词数目
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")
filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt', 'programming.txt']
for filename in filenames:
    count_words(filename)
#使用json文件存储数据
print('使用json模块的dump和load方法保存和读取json文件数据')
import json

def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")

greet_user()
'''
#测试代码，单元测试，测试用例
print('unittest测试工具，一个点号表示一项测试通过，E表示错误，F表示断言失败')
import unittest

def get_formatted_name(first, last, middle=''):
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()

#测试代码放在继承自unittest.TestCase的这个类里
class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        formatted_name = get_formatted_name(
            'wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

if __name__ == '__main__':
    unittest.main()
'''
#测试类
print('测试AnonymousSurvey类')
class AnonymousSurvey:
    def __init__(self, question):
        self.question = question
        self.responses = []
        
    def show_question(self):
        print(self.question)
        
    def store_response(self, new_response):
        self.responses.append(new_response)
        
    def show_results(self):
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}")

import unittest

class TestAnonymousSurvey(unittest.TestCase):
    #setup用来创建一个调查对象和一组答案，供测试方法使用
    def setUp(self):
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_store_single_response(self):
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

if __name__ == '__main__':
    unittest.main()
