数字：
	数字用来存储值。它是不可改变的数据类型，每次改变数据类型的值。需要一个新分配的内存空间或者现有的值做绑定
	int		整数		int a = 10
	long	长整形		long a = 10L	#测试不通过
	float	浮点数		float a = 3.14
	complex 复数		complex a = 3 + 4j
	bool	布尔值		bool a = True

	优先级：
		complex > float > long > int
		低优先级和高优先级的数字进行计算会自动升阶
	
	強转：
		complex(x)：将x转换为实部x和虚部0的复数
		complex(x,y):将x和y转换为实部x,虚部y的复数

在计算机系统中，数值一律用补码来表示和存储
	正数：源码=反码=补码
	负数：反码等于源码取反，补码等于反码符号位不变加1

运算符：
	/：普通除，会有精度
	//：地板除，只保留整数部分

移位操作：
	正数移位，缺的位补0
	负数移位，缺的位补1

位运算优先级：
	取反运算符 > 左移运算符 > 右移运算符 > 按位与运算 > 按位异或运算 > 按位或运算

标准函数
	abs(x)		求x的绝对值
	cmp(x,y)
				x < y :return -1
				x == y : return 0
				x > y : return 1
	max(x,y,z...):返回最大值
	min(x,y,z...):返回最小值

随机数：
import random
	random.random()：用于生成0到1的随机浮点数
	random.uniform():用于生成一个指定范围内的随机浮点数
	random.randint(a,b):用于生成一个指定范围内的整数
	random.randrange(0,101,2)：从指定范围内，在指定基数递增的集合中获取一个随机数
	random.choice(sequence)：从序列中获取一个随元素
	random.shuffle([]),用于将一个列表中的元素打乱
		list(items)：打印列表
	random.sample(sequence,k):从指定序列中随机获取指定长度的片断

