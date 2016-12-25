#!/usr/bin/python
#环境变量配置，利用python解析器执行

#模块引入,会自动生成pyc文件（字节码文件），会加快加载速度
import test

def hello():
	print ("\ncall hello fun\n")

#this is entry
#如果该模块被单独执行，__name__ = "__main__"
#如果该模块被引用，__name__ = "__模块名字__"
#一条语句结尾有没有;都可以
print("__name__ = "+__name__)
if __name__ == "__main__":
	print ("\nhello world\n");
	hello();
	test.test_func()
