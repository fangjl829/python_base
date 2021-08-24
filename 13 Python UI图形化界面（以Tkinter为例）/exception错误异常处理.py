
# 脚本用途：自动化运维
# 编写者：方胜山（ciossfang）
# 编写时间：2021/8/11 09:20
# !/usr/bin/python3
# -*- coding:utf-8 -*-

# 多分支 except
# while True:
#   try:
#     x = int(input("请输入一个数字："))
#     print("您输入的数字是：",x)
#     if x == 88:
#       print("退出程序")
#       break
#   except BaseException as e:
#     print(e)
#     print("异常，请输入一个正确的格式：数字")
#
# print("程序结束")

# 输入多分支 except
# try:
#     a = input("请输入被除数：")
#     b = input("请输入除数：")
#     c = float(a)/float(b)
#     print(c)
# except ZeroDivisionError:
#     print("异常：除数不能为 0")
# except TypeError:
#     print("异常：除数和被除数都应该为数值类型")
# except NameError:
#     print("异常：变量不存在")
# except ValueError:
#     print("输入的值有问题，应该输入浮点型数值")
# except BaseException as e:
#     print(e)
#     print(type(e))

# try..except..else 结构
# try:
#     a = input("请输入被除数：")
#     b = input("请输入除数：")
#     c = float(a)/float(b)
#     print(c)
# except ZeroDivisionError:
#     print("异常：除数不能为 0")
# except TypeError:
#     print("异常：除数和被除数都应该为数值类型")
# except NameError:
#     print("异常：变量不存在")
# except ValueError:
#     print("输入的值有问题，应该输入浮点型数值")
# except BaseException as e:
#     print(e)
#     print(type(e))
# else:
#     print("您输入的数值计算结果是:",c)
# finally:
#     print("不管你们上面炒成啥样，现在都得给我老老实实的！")

# try..except..finally 结构
# try:
#     a = input("请输入被除数：")
#     b = input("请输入除数：")
#     c = float(a)/float(b)
#     print(c)
# except ZeroDivisionError:
#     print("异常：除数不能为 0")
# except TypeError:
#     print("异常：除数和被除数都应该为数值类型")
# except NameError:
#     print("异常：变量不存在")
# except ValueError:
#     print("输入的值有问题，应该输入浮点型数值")
# except BaseException as e:
#     print(e)
#     print(type(e))
# else:
#     print("您输入的数值计算结果是:",c)
# finally:
#     print("不管你们上面炒成啥样，现在都得给我老老实实的！")


# return 语句放在 try语句外面。
# def calculate():
#     try:
#         a = input("请输入被除数：")
#         b = input("请输入除数：")
#         c = float(a)/float(b)
#         print(c)
#     except ZeroDivisionError:
#         print("异常：除数不能为 0")
#     except TypeError:
#         print("异常：除数和被除数都应该为数值类型")
#     except NameError:
#         print("异常：变量不存在")
#     except ValueError:
#         print("输入的值有问题，应该输入浮点型数值")
#     except BaseException as e:
#         print(e)
#         print(type(e))
#     else:
#         print("您输入的数值计算结果是:",c)
#     finally:
#         print("不管你们上面炒成啥样，现在都得给我老老实实的！")
#     return "503"
#
# print(calculate())

# with对上下文的管理
# with open("d:/bb.txt") as f:
#     for line in f:
#         print(line)

# traceback对错误信息的打印
# import traceback
#
# try:
#     a = input("请输入被除数：")
#     b = input("请输入除数：")
#     c = float(a)/float(b)
#     print(c)
# except ZeroDivisionError:
#     print("异常：除数不能为 0")
# except TypeError:
#     print("异常：除数和被除数都应该为数值类型")
# except NameError:
#     print("异常：变量不存在")
# except ValueError:
#     traceback.print_exc()
#     # 打印valueerror的错误信息
#     # print("输入的值有问题，应该输入浮点型数值")
# except BaseException as e:
#     print(e)
#     print(type(e))
# else:
#     print("您输入的数值计算结果是:",c)
# finally:
#     print("不管你们上面炒成啥样，现在都得给我老老实实的！")
#
# except:
# with open("d:/a.log","a") as f:
#      traceback.print_exc(file=f)

# 自定义异常类
#coding=utf-8
#测试自定义异常类
# class AgeError(Exception):
#     def __init__(self, errorInfo):
#         Exception.__init__(self)
#         self.errorInfo = errorInfo
#     def __str__(self):
#         return str(self.errorInfo) + ",年龄错误！应该在 1-150 之间"
#
# ############测试代码################
# if __name__ == "__main__":
#     age = int(input("输入一个年龄:"))
# # 如果为 True，则模块是作为独立文件运行， 可以执行测试代码
#     if age < 1 or age > 150:
#         raise AgeError(age)
#     else:
#         print("正常的年龄：", age)


# 测试文件的写入
# f = open(r"/Users/ucloud/a.txt","a")
# s = "itbaizhan\nsxt\n"
# f.write(s)
# f.close()

# try:
#     f = open(r"/Users/ucloud/my01.txt", "a")
#     str = "gaoqi"
#     f.write(str)
# except BaseException as e:
#     print(e)
# finally:
#     f.close()

# read() 读取文件
# with open(r"/Users/ucloud/secure.log","r",encoding="utf-8") as f:
#     print(f.read(10))
#
# with open(r"/Users/ucloud/secure.log","r",encoding="utf-8") as f:
#     print(f.readline(20))

# 对二进制文件做拷贝处理
# with open(r"/Users/ucloud/Downloads/aa.png","rb") as f:
#     with open(r"/Users/ucloud/Downloads/aa_copy.png","wb") as e:
#         for line in f.readlines():
#             e.write(line)
#
# print("拷贝完成！")

# 对数据进行序列化到文件操作
# import pickle
# with open(r"/Users/ucloud/Downloads/a.txt","wb") as f:
#     a ="方胜山"
#     b = "董利杰"
#     c = "张三丰"
#     pickle.dump(a,f)
#     pickle.dump(b,f)
#     pickle.dump(c,f)

# 反序列化
# import pickle
# with open(r"/Users/ucloud/Downloads/a.txt","rb") as f:
#     a = pickle.load(f)
#     b = pickle.load(f)
#     c = pickle.load(f)
#
#     print(a)
#     print(b)
#     print(c)

# csv 文件的读取
# import csv
# with open(r"/Users/ucloud/Downloads/dd.csv","r") as f:
#     csv_read = csv.reader(f)
#     for i in csv_read:
#         print(i)

# csv 文件的写入
# import csv
# with open(r"/Users/ucloud/Downloads/ee.csv","w") as f:
#     csv_write = csv.writer(f)
#     csv_write.writerow(["ciofang","23","程序员","50000"])
#     csv_write.writerow(["donglijie", "33", "sale", "30000"])

# os模块
# import os
# # os.system("ping www.baidu.com")
# # os.mkdir(ciossfang)
# print(os.getcwd())
# # print(os.mkdir("ciossfang"))
# print(os.listdir)

# path = os.getcwd()
# file_list = os.listdir(path) #列出子目录和子文件
# for filename in file_list:
#     pos = filename.rfind(".")
#     if filename[pos + 1:] == "py":
#         print(filename, end="\t")
#
#
# print("##################")
# file_list2 = [filename for filename in os.listdir(path) if
# filename.endswith(".py") ]
# for filename in file_list2:
#     print(filename, end="\t")
#
#
# #coding=utf-8
# import os
# all_files = []
#
# path = os.getcwd()
# list_files = os.walk(path)
# for dirpath,dirnames,filenames in list_files:
#     for dir in dirnames:
#         all_files.append(os.path.join(dirpath, dir))
#     for name in filenames:
#         all_files.append(os.path.join(dirpath, name))
#
#
#     for file in all_files:
#         print(file)
#
# import shutil
# #copy 文件内容
# shutil.copyfile("1.txt","1_copy.txt")
#
# import shutil
# #"音乐"文件夹不存在才能用。
# shutil.copytree("电影/学习","音乐",ignore=shutil.ignore_patterns("*.html","*.htm"))
#
# import shutil
# import zipfile
# # 将"电影/学习"文件夹下所有内容压缩到"音乐 2"文件夹下生成 movie.zip
# shutil.make_archive("音乐 2/movie","zip","电影/学习")
#
# #压缩:将指定的多个文件压缩到一个 zip 文件
# z = zipfile.ZipFile("a.zip","w")
# z.write("1.txt")
# z.write("2.txt")
# z.close()
#
# import shutil
# import zipfile
#
# #解压缩：
# z2 = zipfile.ZipFile("a.zip","r")
# z2.extractall("d:/")
# #设置解压的地址
# z2.close()

# 递归操作
# 递归之中，一定要有触发递归的条件，也要有终止递归的条件。否则无限制的调用最终会耗尽资源，系统崩溃
#
# num = 0
# def number():
#     global num
#     num += 1
#     print(num)
#
#     # 增加终止条件
#     if num < 5:
#         number()
#
# print(number())

# 计算阶乘n！
#
# def facturial(n):
#     if n == 1:
#         return n
#     else:
#         return n + facturial(n-1)
#
# print(facturial(9))


#  遍历目录获取底下所有的文件内容（注意是全路径的）
# import os
#
# def getAllFiles(path):
#     childfile = os.listdir(path)
#     for file in childfile:
#         filepath=os.path.join(childfile,file)
#         if os.path.isdir(filepath):
#             getAllFiles(filepath)
#             # 如果是目录，就执行递归，进一步的查询目录下的文件
#         print(filepath)
#
#
# getAllFiles("/Users/ucloud/Downloads/gitbook")
