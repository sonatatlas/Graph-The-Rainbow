# 引入 matplotlib 库
import matplotlib.pyplot as plt;

# 输入一个数组
plt.plot([1, 2, 3, 4]);

# 设置 y 轴标签
plt.ylabel('some numbers');

# 设置 x 轴标签
plt.xlabel('this is x label');

# save the plt...
plt.savefig('figure');

# show the plt...
plt.show()

# 注意: 如果先展示图片后存储图片，图片会空的。
