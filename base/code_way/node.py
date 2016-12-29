计算机内部使用的是ASCII编码（127个字母）

中文编码：GB2312

统一编码：Unicode（最小单位通常2个字节）

UTF-8编码：包含了ASCII编码，数据在内存中一般是unicode编码，存储磁盘用UTF-8编码

浏览网页的时候，服务器会把动态生成的unicode内容转换为UTF-8再传输到浏览器
浏览器源码一般<meta charset="UTF-8" />

1、python3中，字符串使用unicode编码，所以python的字符串支持多语言
2、ord("A")(或ord('A')):返回字符A对应的unicode码
3、chr(48):把unicode码转换为对应的字符
4、'\u4e2d\u6587'===>'中文':可以用\u加unicode码表示字符
5、Python对bytes类型的数据用带b前缀的单引号或双引号表示：
	x = b'ABC'
6、以Unicode表示的str通过encode()方法可以编码为指定的bytes
	'ABC'.encode('ascii')------> b'ABC'
	'中文'.encode('utf-8')-----> b'\xe4\xb8\xad\xe6\x96\x87'
	'中文'.encode('ascii')-----> 会报错，含有中文的字符串不能无法使用ASCII编码
7、如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法
	b'ABC'.decode('ascii')-----> 'ABC'
	b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')----> '中文'

len(b'ABC'):计算字符串长度

由于Python源代码也是一个文本文件，所以，当你的源代码中包含中文的时候，在保存源代码时，就需要务必指定保存为UTF-8编码。当Python解释器读取源代码时，为了让它按UTF-8编码读取，我们通常在文件开头写上这两行：
	#!/usr/bin/python
	# -*- coding: utf-8 -*-
