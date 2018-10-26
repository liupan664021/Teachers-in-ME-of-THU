import re
from urllib.request import urlopen

# url = r'http://python.org/jobs'
s = '<a style="FONT-SIZE: 14px; TEXT-DECORATION: underline; FONT-FAMILY: 宋体" href=".*"><span style="FONT-SIZE: 14px; FONT-FAMILY: 宋体">(.*)</span></a>'
pattern = re.compile(s)
url = r'http://me.tsinghua.edu.cn/publish/jxx/6138/index.html'

# urlopen(url).read()得到的是bytes类型，需要decode()转换为字符串才可以
text = urlopen(url).read().decode()
text = text.replace('</a>','</a>\n')
m = pattern.findall(text) 

for i in range(len(m)):
    if m[i] != '':
        m[i] = m[i].replace('&nbsp;','')
        # print(m[i])

remove_repeat = set(m)

res = [name for name in remove_repeat]
res.remove('')

print('Teachers in ME of THU:')
print(res)
print('Amount of teachers in ME of THU:',len(res))


    