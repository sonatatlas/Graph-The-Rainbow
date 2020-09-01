### 网页图片抓取并保存

#### 模块
+ matplotlib ~> 著名的绘图库

#### 思路
+ 输入图表数据
+ 保存并显示图标

#### 示例

![line][1]

#### 代码

```python
# 引入 matplotlib 绘制图表
import matplotlib.pyplot as plt;

# 设置 y 轴标签
plt.ylabel('some numbers');

# 设置 x 轴标签
plt.xlabel('this is x label');

# 绘制图表
plt.plot([1, 2, 3, 4]);

# 保存图表
plt.savefig(line);

# 显示图表
plt.show()

# 注意: 如果先展示图片后存储图片，图片会是空的。
```
[代码链接][2]

[1]: https://github.com/udtrokia/Graph-The-Rainbow/blob/master/assets/images/line.png?raw=true
[2]: https://github.com/udtrokia/Graph-The-Rainbow/blob/master/chart/descartes.py
