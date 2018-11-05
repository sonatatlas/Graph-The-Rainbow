### 抓取特定文本

#### 模块
+ lxml ~> lxml 将 html 文本转成 xml 对象且对象执行 xpath 的功能
+ requests ~> 网络请求库

#### 思路
+ 获取相关网页内容
+ 筛选包含特定信息的标签
+ 打印标签

#### 示例
![text](/assets/images/text.png)

#### 代码

```python
# 引入 requests 库用于网络请求
import requests as r; 

# 引入 lxml 中的 etree 用于转换 html 格式
from lxml import etree;

# 获取网页
res = r.get('https://bitcoin.org/zh_CN/faq#how-are-bitcoins-created');

# 修改网页的编码模式
res.encoding = 'utf-8';

# 将网页格式化
html = etree.HTML(res.text);

# 抓取 titles
titles = html.xpath('//div[@class="sidebar-inner"]//a');

# 打印 titles;
for i in titles: print(i.text);
```
