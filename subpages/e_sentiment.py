#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/5/4 17:26
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   e_sentiment.py
# @Desc     :
from pandas.core.interchange.dataframe_protocol import DataFrame
from snownlp import SnowNLP
from streamlit import (subheader, session_state, empty, data_editor, sidebar,
                       selectbox, bar_chart, write)

from utils.helper import emotion_rater

if "data" not in session_state:
    session_state["data"] = None

empty_message: empty = empty()

if session_state.data is None:
    empty_message.warning("Please select a CSV file to upload initially.")
else:
    contents = session_state.data[["date", "like", "comment", "collection", "forward", "content"]].copy()
    subheader("Sentiment Analysis")
    # data_editor(contents, hide_index=True, disabled=True, use_container_width=True)

    # Sentiment per content in the contents
    contents["score"] = contents["content"].apply(lambda sentence: SnowNLP(sentence).sentiments)
    contents["rate"] = contents["score"].apply(emotion_rater)
    data_editor(contents, hide_index=True, disabled=True, use_container_width=True)

    # Divide the different rates of emotions and get their mean values
    interactions: list[str] = ["like", "comment", "collection", "forward"]
    mean = contents.groupby("rate")[interactions].mean().reset_index()
    # write(mean)

    # Display the bar chart
    with sidebar:
        subheader("Emotion Rating Division Selector")
        option: str = selectbox(
            "Select an interaction",
            options=interactions,
            index=0,
            placeholder="Select an interaction you want",
        )

    subheader("Mean for Emotion Rating Division")
    bar_chart(mean, x="rate", y=option)
