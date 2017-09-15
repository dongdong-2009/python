#!/usr/bin/python
import akon.module_1 as m1

m1.test()
print("m1.__doc__ = %s" % (m1.__doc__))	#调用文档注释
print("m1.num = %d[public]" % (m1.num))
print("m1._num = %d[private]" % (m1._num))		#不应该访问模块的私有变量，但是可以访问
print("m1.__num = %d[private]" % (m1.__num))











