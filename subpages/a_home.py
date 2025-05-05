#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/5/3 12:32
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   a_home.py
# @Desc     :   

from streamlit import title, divider, expander, caption, empty

title("Short Video Analysis")
divider()
with expander("APPLICATION INTRODUCTION", expanded=True):
    caption("1. Arrangement of Data：from2nd April 2025 to 1st May 2025")
    caption("2. Categories of Data：date, time, like, comment, collection, forward, face, duration, content")
    caption("3. Data Source：CSV file, UTF-8 encoding")
    caption("4. Data Cleaning：Remove duplicate data, handle missing values, convert data types")
    caption("5. Data Visualization：Use Streamlit to visualize data")
    caption("6. Data Analysis：Use Python to analyze data")

empty_message = empty()
empty_message.info("Please check the details at the different pages of manipulation.")
