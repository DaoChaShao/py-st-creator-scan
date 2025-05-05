#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/5/3 12:32
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   layout.py
# @Desc     :   

from streamlit import set_page_config, Page, navigation


def page_config() -> None:
    """ Set the window

    :return: None
    """
    set_page_config(
        page_title="Video Analysis",
        page_icon=":material/videocam:",
        layout="wide",
        initial_sidebar_state="expanded",
    )


def pages_setter() -> None:
    """ Set the subpages on the sidebar

    :return: None
    """
    pages: dict = {
        "page": [
            "subpages/a_home.py",
            "subpages/b_description.py",
            "subpages/c_graph.py",
            "subpages/d_content.py",
            "subpages/e_sentiment.py",
            "subpages/f_novelty.py",
            "subpages/z_about.py",
        ],
        "title": [
            "Home",
            "Data Description",
            "Graph",
            "Content",
            "Sentiment Analysis",
            "Content Novelty",
            "About",
        ],
        "icon": [
            ":material/home:",
            ":material/table:",
            ":material/line_axis:",
            ":material/description:",
            ":material/category:",
            ":material/stream:",
            ":material/info:",
        ],
    }

    structure: dict = {
        "Introduction": [
            Page(page=pages["page"][0], title=pages["title"][0], icon=pages["icon"][0]),
        ],
        "Manipulation": [
            Page(page=pages["page"][1], title=pages["title"][1], icon=pages["icon"][1]),
            Page(page=pages["page"][2], title=pages["title"][2], icon=pages["icon"][2]),
            Page(page=pages["page"][3], title=pages["title"][3], icon=pages["icon"][3]),
            Page(page=pages["page"][4], title=pages["title"][4], icon=pages["icon"][4]),
            Page(page=pages["page"][5], title=pages["title"][5], icon=pages["icon"][5]),
        ],
        "Information": [
            Page(page=pages["page"][6], title=pages["title"][6], icon=pages["icon"][6]),
        ],
    }
    pg = navigation(structure, position="sidebar", expanded=True)
    pg.run()
