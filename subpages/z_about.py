#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/5/5 23:42
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   z_about.py
# @Desc     :   

from streamlit import title, divider, expander, caption, empty

title("Aspects for improvement")
divider()
with expander("ABOUT", expanded=True):
    caption("There are still many aspects that need improvement:")
    caption("1. **Supplementing basic data**, such as completion rate and comments.")
    caption("2. **Content diversity analysis**.")
    caption("3. **Annotation of special holidays or events**.")
    caption("4. **Analysis of video (subtitle) features**.")
    caption("5. **Analysis of background audio characteristics**.")
    caption("6. **Platform trend analysis**.")
    caption("7. **Multi-dimensional competitor analysis**.")

empty_message = empty()
empty_message.info("Please check the details at the different pages of manipulation.")
