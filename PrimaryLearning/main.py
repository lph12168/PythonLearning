#终端显示
#显示颜色的格式：\033[显示方式;前景色;背景色m显示内容\033[0m
#显示参数
#显示方式: 0（默认）、1（高亮）、22（非粗体）、4（下划线）、24（非下划线）、 5（闪烁）、25（非闪烁）、7（反显）、27（非反显）
#前景色: 30（黑色）、31（红色）、32（绿色）、 33（黄色）、34（蓝色）、35（洋 红）、36（青色）、37（白色）
#背景色: 40（黑色）、41（红色）、42（绿色）、 43（黄色）、44（蓝色）、45（洋 红）、46（青色）、47（白色）
print('\033[34m前景蓝色,背景默认\033[0m') 
print('\033[1;31;2;42m前景红色,背景绿色\033[0m')

#命令行和终端执行命令
#类似用户直接输入命令，终端有交互
import os
result = os.system('ls')
print(result)

#将目录和文件名合成一个路径
print(os.path.join('E:\GitHub\PythonLearning', 'PrimaryLearning', 'main.py'))
print(os.path.dirname('~/GitHub/PythonLearning/PrimaryLearning/main.py'))
print(os.path.basename('~/GitHub/PythonLearning/PrimaryLearning/main.py'))

#在程序中静默执行，终端没有交互
import subprocess
result = subprocess.getstatusoutput('ls')
print(result)

#命令行参数解析
##--表示可选参数，-和--后面参数用作参数名，有dest字段则以dest名字为准，prog指定程序名，epilog添加额外描述信息, metavar改变显示的名称 
import argparse
parser = argparse.ArgumentParser(description='Hi Python', prog='PrimaryLearning', epilog='')
parser.add_argument('--input', dest='abc', metavar = '\033[31mdata\033[0m', type=str, default='Hi Python', help='input params')
args = parser.parse_args()
print(args.abc)
#print(parser.print_help())

#时间
import datetime
print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

#打印当前执行的命令
import sys
print(''.join(sys.argv))

#XML解析
import xml.etree.ElementTree as ET
tree = ET.parse('LA.UM.9.14.r1-12800-LAHAINA.0.xml')
root = tree.getroot()
for elem in root.iterfind('project'):
    if elem.get('name') == 'kernel/msm-5.4':
        print(elem.attrib)
        print(elem.attrib['name'])

#config文件解析
import configparser
config = configparser.ConfigParser()
config.read("config.ini", encoding="utf-8")
print(config.sections())
#获取指定section
print(config.options('remote "origin"'))
#获取指定section和name的值
print(config.get('remote "origin"', 'url'))
