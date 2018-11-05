### 网页图片抓取并保存

#### 模块
+ os ~> os 包含普遍的操作系统功能
+ lxml ~> lxml 将 html 文本转成 xml 对象且对象执行 xpath 的功能
+ requests ~> 网络请求库

#### 思路
+ 获取相关网页内容
+ 筛选包含图片的标签并获取图片链接
+ 请求图片链接，并将返回的数据写入文件

#### 示例

![image](/assets/images/albums.png)

#### [代码][2]

```python
# 引入 os 库，用于操作 “操作系统”(windows, mac, linux)
import os;

# 引入 requests; {% requests: 进行网络请求 %}
import requests as r; 

# 引入 etree; {% etree: 于格式化抓取到的网页内容 %} 
from lxml import etree;

# 获取网页; {% 使用 requests 发起 'get' 请求 %} 
res = r.get('https://pitchfork.com/reviews/albums/');

# 设置数据的编码模式 {% 如果不进行设置，由于网络传输的问题，会出现乱码 %}
res.encoding = 'utf-8';

# 将网页格式化 {% 使用 etree 格式化网页，便于过滤特定的数据 %}
html = etree.HTML(res.text);

# 抓取 titles {% |xpath 语法| %} 
# "//img" ~> (获取所有 img)
# "//img//@src" ~> (获取所有 img 的 src)
imgs = html.xpath('//img//@src');

# 如果不存在 ALBUMS 文件夹
if os.path.exists('ALBUMS') == False:
    # 创建名为 ALBUMS 的文件夹
    os.mkdir('ALBUMS')

# 请求所有的图片链接，将图片写入 ALBUMS 文件夹
# enumerate 是一个特殊函数，能够打印出列表的 `index` - 索引
for idx, img in enumerate(imgs):

    # 构造存储的地址
    # os.path.join 将文件加入 ALBUMS 文件夹
    # str(idx) ~> 将数字转换为字符串 => 拼接字符串
    path = os.path.join('ALBUMS', str(idx) + '.png');
    
    # 在 `path` 创建新文件
    f = open(path, 'wb');

    # 请求图片链接并写入文件
    f.write(r.get(img).content);

    # 关闭文件
    f.close();
```

[2]: https://github.com/sonatatlas/Graph-The-Rainbow/blob/master/spider/image.py
