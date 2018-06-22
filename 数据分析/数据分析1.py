#author:WeiminLee
#-*-coding:utf-8-*-
#date:''
#function=''

"""
读取本地文件
"""
import numpy as np
import pandas as pd
from pandas import *
#import matplotlib.pyplot as plt
#打印pandas 的版本
print pd.__version__


input_file = pd.read_csv('tissue_gene_expression.fpkm_tracking',sep='\t')
#input_file.head()
print input_file['gene_id'].head() ##预览'gene_id'列的前五行
#print input_file

##预览输入文件的前几行
input_file_row5 = pd.read_csv('tissue_gene_expression.fpkm_tracking', sep='\t', nrows=5)
##获取gene_id列的第一个值
print input_file_row5.gene_id[0]
print input_file_row5.index

##指定输入文件中的某列作为行索引
input_file_row = pd.read_csv('tissue_gene_expression.fpkm_tracking', sep='\t', index_col=0) ##指定第0列为索引
print input_file_row.head()

##指定输入文件中某列的数据类型
input_file_dtype = pd.read_csv('tissue_gene_expression.fpkm_tracking', sep='\t', index_col=0, dtype={'Ro':np.float64,
                                                                                                     'Le':np.float64})
print input_file_dtype.head()

##更改列索引
input_file_colume = pd.read_csv('tissue_gene_expression.fpkm_tracking', sep='\t',header=0, names=['sepal1','sepal2', 'sepal3','sepal4','gynocium1','gynocium2','gynocium3','gynocium4','gynocium5','gynocium6','gynocium7','ovule1','ovule2','ovule3','ovule4','ovule5','ovule6','ovule7','petal1','petal2','petal3','stamen1','stamen2','stamen3','stamen4','stamen5','stamen6','fruit1', 'fruit2', 'fruit3','fruit4','fruit5','fruit7','root','leaf', 'flower'] )
print input_file_colume.head()
print input_file_colume.index ##默认第0列为index

##加载输入文件特定的列
input_file_special_columns = pd.read_csv('tissue_gene_expression.fpkm_tracking', sep='\t',
                                         usecols=['gene_id','Ro','Le','Fl'],index_col=['gene_id'])
print input_file_special_columns.head()

##保存文件
input_file_special_columns.to_csv('new_output.txt',sep='\t', index_label='gene_id')
#input_file_special_columns.to_excel('new_output.xlsx', index_label='gene_id') ##excel 格式
##跳过不需要的行
input_file_out1 = pd.read_csv('new_output.txt', sep='\t', skiprows=[1,2], index_col=0)
print input_file_out1

##跳过倒数行skip only two lines at the end
input_file_out2= pd.read_csv('new_output.txt', sep='\t', skipfooter=100, engine='python', index_col=0) #省略最后100行
print input_file_out2


##加载Excel表格中的某个表
input_file_excel = pd.read_excel('new_output.xlsx', sheet_name='gene2',index_col=0,sep='\t')
print input_file_excel
input_file_excel.to_excel('new_output1.xlsx', index_label='gene_id', sheet_name='geneid2')


##把Excel文件转换为json文件
input_file_excel.to_json('new_output2.json') ##以json格式储存

##加载json文件
input_file_json = pd.read_json('new_output2.json')
print input_file_json.head(5)


##读取网页的HTML文件
url = 'http://www.boc.cn/investor/ir4/201501/t20150114_4461543.html'
table = pd.read_html(url) ##返回的是很多表格
table2 = table[1]##挑选自己感兴趣的表格
table2[0:5].to_excel('new_out5.xlsx')
#table.to_excle('new_out3.xlsx')


##从SQL数据库中读取和写入文件

#1 写入文件
import sqlite3

msft = pd.read_csv('tissue_gene_expression.fpkm_tracking',sep='\t', index_col=0)
print msft.head()
msft['Symbol'] = 'TGEF'
#创建连接
#.to_sql()将创建SQL，储存数据框
connection = sqlite3.connect('stocks.sqlite')
msft.to_sql('stock_data', connection, if_exists='replace')
msft.to_sql('stock_data', connection, if_exists='append')

##commit the SQL and close the connection
connection.commit()
connection.close()

#2 读取文件

#2.1连接数据库文件
connection = sqlite3.connect('stocks.sqlite')

#2.2 询问stock_data 里的所有记录
#2.3 返回数据框
#2.4 inde_col specifies which column to make the DataFrame index
stocks = pd.io.sql.read_sql("SELECT * FROM STOCK_DATA;",connection, index_col='gene_id')
##有条件的提取数据框
#######################################################################
query = "SELECT * FROM STOCK_DATA WHERE Fr_S1>100 AND Symbol='TGEF';"  # 筛选Fr_S1时期fpkm值大于100的基因
stocks_q = pd.io.sql.read_sql(query, connection, index_col='gene_id') #
#######################################################################
connection.close()
print '#############################################################################'
print stocks.head(4)
print '#############################################################################'
print stocks_q.head()

