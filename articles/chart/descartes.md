### René Descartes

#### 模块
+ numpy ~> 一大堆数学公式
+ matplotlib ~> 著名的绘图库

#### 思路
+ 输入图表数据
+ 保存并显示图标

#### 示例

![descartes][1]

#### 代码

```python
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

# 注意: 如果先展示图片后存储图片，图片会是空的。
```
[代码链接][2]

[1]: /assets/images/descartes.png
[2]: https://github.com/sonatatlas/Graph-The-Rainbow/blob/master/chart/descartes.py
