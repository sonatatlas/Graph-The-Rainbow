import requests as r; # 引入 requests;
from lxml import etree; # 引入 etree;

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

