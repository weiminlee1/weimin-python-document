import re
pattern1 = 'cat'
pattern2 = 'bird'

print(re.search(pattern1,string))
print(re.search(pattern2,string))

#匹配多种
#ran,run
ptn = r'r[au]n'
print(re.search(ptn,'dog runs to cat')

ptn = r'r[A-Z]n'
ptn = r'r[a-z]n'
ptn = r'r[0-9]n'

##特殊匹配方式
\d匹配数字
\D匹配数字以外的字符
\s匹配空格
\n,\r换行符
.任意字符，除了\n
^string句首匹配string
string$句尾匹配
string? 匹配0次或1次

##多行匹配

string = '''dog runs to cat.
i run to dog.'''
print(re.search(r'^i',string))
print(re.search(r'^i',string,flag=re.M)) ##flag=re.M匹配多行multiple line

string* 匹配0次以上
string+ 匹配一次以上

string{x,y} 匹配x到y次

#group组
match = re.search(r'(\d+),Date:(.+)', 'ID:021523', Date:Feb/12/2017')
print(match.group()) ##返回所有
print(match.group(1)) ##返回第一个括号的内容
print(match.group(2)) ##返回第二个括号的内容

match = re.search(r'(?P<id>\d+), Date:(?P<date>.+)','ID:021523, Date:Feb/12/2017') ##添加标签
print(match.group('id'))
print(match.group('date'))



