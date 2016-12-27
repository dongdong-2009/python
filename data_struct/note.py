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
