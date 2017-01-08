序列包括：
	列表（list）、元组(tuple)、字符串（str）、unicode字符串
	字符串和元组是固定长度，不能修改，列表可以修改
	列表定义：
		list1 = [1,2,3,4]
	元组定义：
		tuple1 = (1,2,3,4)
	字符串定义：
		str1 = "1234"
	使用：
		都是name[下标]

序列基本操作：
	in		obj in seq		判断obj是否在seq中（返回True或False）
	not in	obj not in seq	判断obj是否不在seq中
	+		seq1 + seq2		连接序列seq1和seq2
	*		seq*N			序列重复相加N次
	cmp		cmp(s1,s2)		比较两个字符串大小
			python3可用(s1 > s2) - (s1 < s2)代替
	chr		chr(num)		接收一个整数返回ASCII码(0~255)
	unichar	unichar(num)	接收0~0xffff，返回ASCII码
	ord		ord('a')		根据字符返回ASCII码

序列切片操作：
	[index]				取索引值为index的元素
	[start:stop]		取索引start到stop的所有元素,不包含stop
	[start:stop:step]	在索引start到stop之间，每隔step个取一个元素
	例子：
		list1[2:]：取索引2及后面的所有元素

序列内建函数：
	len			返回列表长度
	max/min		返回列表最大或最小值
	sum			返回seq的整形的总和
	reversed	返回序列的逆序访问的迭代器
				a=reversed(list1)--->a.__next__()访问序列
	zip			接受任意多个（包括0和1个）序列作为参数，返回一个tuple列表


字符串：单引号'，双引号"或者三引号（'''/"""）定义字符串，字符串的内容是不可变的
	创建和赋值：
		str1 = "hello
		str1 = str(10)
		str1 = str([1,2,3,4,5])
		str1 = str((1,2,3,4,5))
	格式化操作%:格式化输出
		%c		将数值转换为字符			print("%c"% 65)
		%d		将数字转换为10进制数		print("%d"% 65)
		%s		用str()将参数转换为字符串	print("%s"% [1,2,3])
				打印元祖需要強转利用str((1,2,3,4))
		%o %O	将数字转为8进制数			print("%o"% 65)
		%x %X	将数字转换为16进制数		print("%x"% 65)
		%f %F	将数字转为浮点				print("%f"% 65.1)
		%%		输出%
	同时格式化输出多个：
		print("%d,%d"%(10,10))	
	原始字符串操作符（R/r）
		print(r"\n")---->\n
	python字符串结尾
		python字符串不是以'\0'结尾
		python解析器来管理字符串内存

字符串unicode
	unicode定义：
		u'abc'		U+0061 U+0062 U+0063
		u'\u0061'	a
	unicode编码格式：
		支持ASCII，ISO-8859-1,UTF-8,UTF-16
		UTF-8使用1～4个字节来表示其它语言的字符
		UTF-16使用2个字节来表示其它语言字符
	unicode和其他编码的互相转换
		str1 = u"一"					u'\u4e00'
		utf8 = s.encode('utf8')			'\xe4\xb8\x80'
		utf8.decode('utf8')				u'\u4e00'
		gbk=s.encode('gbk')				'\xd2\xbb'
		gbk.decoder('gbk')				u'\u4e00'


列表（列表元素可以改变，可以通过索引或者切片访问一个或多个列表元素）
	定义初始化：
		mylist = [1,2,3,4,5]
		mylist = list("123456")	将字符串转换为列表
		mylist = list((1,2,3)) 将元组转换为字符串
		mylist = range(10)
	列表访问
		mylist[1]
		mylist[1:4]
	列表跟新：
		mylist[1] = 10
		mylist = mylist*2
		mylist = mylist + [4,5,6]
	列表操作函数：
		in/not in			成员关系
		cmp(seq1,seq2)		比较两个列表
		len(seq)			返回列表元素个数
		sorted(seq)			列表正序(列表中只能有数字)
		sum(seq)			列表统计数字的和（列表中只能有数字）
		zip(seq,...)		根据seq和其它列表生成一个元组列表	
			例：zip([1,2,3],['a','b','c'])--->[(1,'a'),(2,'b'),(3,'c')]
			注意：以最少的列表作为最终列表的长度
	列表常用方法：
		l.append(x)			在列表末尾追加元素
		l.insert(i,x)		在列表索引i插入元素
		l.remove(x)			删除第一次出现值为x的元素
		l.pop(i)			弹出并删除位置为i的元素
		l.sort()			列表排序

元组：
	元组是不可变的序列，元组由不同的元素组成，每隔元素可以存储不同类型的数据，元组通常代表一行数据，而元组中的元素则代表不同的数据项，一旦创建后则不能修改长度
	元组的创建：
		tuple1 = ('what','is','python')
		tuple1 = tuple("abc")
		tuple1 = ()
		tuple1 = ("abc",)
		tuple1 = 'a','b','c'
		tuple1 = tuple(range(10))
	访问：
		print(tuple1[0])
		print(tuple1[0:2])
		print(tuple1[0:4:2])
	元组的操作函数：
		t1 + t2
		t1*N
		t1 > t2
		len(t1)
		sum(t1)
		max(t1)
		min(t1)









