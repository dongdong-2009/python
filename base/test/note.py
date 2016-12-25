一、pyhton源码编辑编译执行
	1、python文件分类
		1.1：py(源码文件)
			环境变量
			import
			入口函数
			代码
			注释
		1.2：pyc
			字节码文件，提高加载速度，被其它文件引用
			python -m py_compile first.py
			字节码文件可以通过python xxx.pyc执行（python可以识别）
			不能./执行（bash shell解析器无法识别）
		1.3：pyo
			优化编译字节码文件 -O选项生成
			python -O -m py_compile first.py
			也可以使用python解析器执行
			不能通过shell命令行./xxx.pyo执行

	2、python源码文件到可执行文件过程
		1、python源码文件通过python解析器--->python字节码文件
		2、python字节码文件通过python虚拟机--->python可执行文件(二进制文件)
