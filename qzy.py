# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 15:26:35 2024

@author: qu
"""
import streamlit as st
from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.faker import Faker
from streamlit_echarts import st_pyecharts
from io import StringIO
import pandas as pd
import jieba
from pyecharts.charts import Bar
def p1():
    st.title("智酷机器人")
    a=['语文','数学','英语']
    b=[0,0,0]
    b[0]=st.number_input('输入语文成绩',step=1)
    b[1]=st.number_input('输入数学成绩',step=1)
    b[2]=st.number_input('输入英语成绩',step=1)
    if st.button("开始画图"):
        c = (
            Pie()
            .add(
                "",
                [list(z) for z in zip(a,b)],
                radius=["30%", "75%"],
                center=["50%", "50%"],
                rosetype="area",
            )
            .set_global_opts(title_opts=opts.TitleOpts(title="成绩"))
        
        )
        st_pyecharts(c)
def p2():
    up_file = st.file_uploader('上传一个txt文件')
    if up_file is not None:
        # To convert to a string based IO:
        stringio = StringIO(up_file.getvalue().decode("utf-8"))
    txt = st.text_area(
        "",
        ""
        ""
        ,
        )
    st.write(f'输入了{len(txt)}个字')
    list1=jieba.lcut(txt)
    #list2=[]
    counts={}
    list4=[]
    excludes=['将军', '却说','丞相',
              '二人', '不可', '荆州', '不能', '如此',
              '商议', '如何', '主公', '军士', '左右', '军马', 
              '引兵', '次日', '大喜', '云长', 
              '天下', '东吴', '于是', '今日', '不敢', '魏兵', '陛下', 
              '一人', '都督', '人马', '不知', '汉中',
              '只见', '众将', '后主','蜀兵', '上马', '大叫',
              '太守', '此人', '夫人', '先主', '后人', 
              '背后', '城中', '天子', '一面', '何不',  '大军',
              '忽报', '先生', '百姓', '何故', '然后', '先锋', '不如',
              '赶来', '原来', '令人', '江东', '下马', '喊声',
              '正是', '徐州', '忽然', '因此', '成都', '不见', '未知',
              '大败', '大事', '之后', '一军', '引军', '起兵', '军中',
              '接应', '进兵', '大惊', '可以', 
              '以为', '大怒']
    for i in list1:
        if len(i)==1 or i in excludes:
            continue
        elif i=='孔明' or i=='孔明曰':
            i='诸葛亮'
        
        counts[i]=counts.get(i,0)+1
    #    list2=list2+[i]
    list3=list(counts.items())
    list3.sort(key=lambda x:x[1],reverse=1)
    list6=list3[0:100]
    dict1=dict(list6)
    list4=list(dict1.keys())
    list5=list(dict1.values())
  #  st.write(f'{list4}')





    c = (
        Bar()
        .add_xaxis(list4)
        .add_yaxis("三国演义词频统计", list5, color=Faker.rand_color())
        .set_global_opts(
            title_opts=opts.TitleOpts(title="三国演义词频统计"),
            datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_="inside")],
        )

    )
    st_pyecharts(c)
def p3():
    a = st.number_input('宪法学 ',step=1)
    b = st.number_input('大学生心理健康 ',step=1)
    c = st.number_input('大学英语',step=1)
    d = st.number_input('大学计算机基础 ',step=1)
    e = st.number_input('公安学基础理论 ',step=1)
    f = st.number_input('水上警务救护 ',step=1)
    g = st.number_input('思想道德 ',step=1)
    h = st.number_input('国家安全教育 ',step=1)
    i = st.number_input('大数据导论 ',step=1)
    j = st.number_input('形势与政策 ',step=1)
    k = st.number_input('高等数学 ',step=1)
    l = st.number_input('慕课 1',step=1)
    m = st.number_input('慕课 2',step=1)
    n = st.number_input('慕课 3',step=1)
    o = st.number_input('慕课 4',step=1)
    p = st.number_input('慕课 5',step=1)
    if l==0:
        l1=0
    else:
        l1=1
    if m==0:
        m1=0
    else:
        m1=1
    if n==0:
        n1=0
    else:
        n1=1
    if o==0:
        o1=0
    else:
        o1=1
    if p==0:
        p1=0
    else:
        p1=1

    x=(a*2+b*2+c*2+d*2+e*2+f*2+g*2+h*1+i*1+j*0.25+k*5+l+m+n+o+p)/(21.25+l1+m1+n1+o1+p1)
    x=(x-50)/10
    y=(a*2+b*2+c*2+d*2+e*2+f*2+g*2+h*1+i*1+j*0.25+k*6+l+m+n+o+p)/(22.25+l1+m1+n1+o1+p1)
    y=(y-50)/10







    st.write('基础班绩点', x)
    st.write('提高班绩点', y)


pagef={
        "成绩分析":p1,
        "词频统计":p2,
        '绩点':p3
        
        
        
        }
s=st.sidebar.selectbox('跳转网页',pagef.keys())
pagef[s]()
