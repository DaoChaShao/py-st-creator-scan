#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/5/3 12:11
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   main.py
# @Desc     :   

from utils.layout import page_config, pages_setter


def main() -> None:
    """ streamlit run main.py """
    # Set the layout of the whole window
    page_config()

    # Set the layout of the subpages
    pages_setter()


if __name__ == "__main__":
    main()
