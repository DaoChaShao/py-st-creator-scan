#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/5/3 12:32
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   a_home.py
# @Desc     :   

from streamlit import title, divider, expander, caption, empty

title("Tiktok Short Video Analysis")
divider()
with expander("Introduction", expanded=True):
    caption("1. 抖音账号：@章职电商·青春纪")
    caption("2. 数据范围：2025年4月2日至2025年5月1日")

empty_message = empty()
empty_message.info("Please check the details at the different pages of manipulation.")
