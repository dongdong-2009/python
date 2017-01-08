1、print 是调用str()函数显示字符串，交互式解析器是调用repr()函数来显示对象
2、_代表最后一个在python中执行的python表达式
3、python -c "print 'world'" >> out.txt可以实现python的重定向
   在python2重定向：print >>sys.stderr, "fatal error" 
   在python3重定向：print("fatal error", file=sys.stderr)
		file可以为之前打开的任意文件
			1、fd = open("文件名",'c'):文件不存在则创建文件
			2、print("helo",file = fd)
			3、fd.close()
			
4、print(x, end=" ")：打印输出，自定义结尾符
