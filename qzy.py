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
