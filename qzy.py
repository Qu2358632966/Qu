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
    for i in list1:
        if len(i)==1:
            continue
        counts[i]=counts.get(i,0)+1
    #    list2=list2+[i]
    list3=list(counts.items())
    list3.sort(key=lambda x:x[1],reverse=1)
    list6=list3[0:100]
    dict1=dict(list6)
    list4=list(dict1.keys())
    list5=list(dict1.values())





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

pagef={
        "成绩分析":p1,
        "词频统计":p2
        
        
        
        }
s=st.sidebar.selectbox('跳转网页',pagef.keys())
pagef[s]()
