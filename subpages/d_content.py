#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/5/3 18:00
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   d_content.py
# @Desc     :   

from collections import Counter
from jieba import load_userdict, lcut
from pandas import DataFrame
from streamlit import (session_state, empty, image, data_editor, bar_chart,
                       subheader, sidebar, selectbox, slider, write)

from utils.helper import (filter_chinese_and_english,
                          filter_stopwords,
                          wordcloud_generator)

if "data" not in session_state:
    session_state.data = None

empty_message: empty = empty()
empty_table: empty = empty()
empty_cloud: empty = empty()

if session_state.data is None:
    empty_message.warning("Please select a CSV file to upload initially.")
else:
    # Get the content from session
    contents = session_state.data["content"]

    # Join the contents together
    contents = " ".join(contents)

    # Add the user dictionary
    DICTIONARY: str = "assets/wordsDict.txt"
    load_userdict(DICTIONARY)

    phrases: dict[str, str] = {
        "what is love": "whatIsLove",
        "come on": "comeOn",
        "be like": "beLike",
    }
    for original, substitute in phrases.items():
        contents = contents.replace(original, substitute)

    # Segment the contents
    words: list[str] = lcut(contents, cut_all=False)

    # Get the Chinese and English contents
    words = filter_chinese_and_english(words)

    # Filter out stopwords
    STOPWORDS: str = "assets/wordsStop.txt"
    stopwords = filter_stopwords(STOPWORDS)
    words = [word for word in words if word not in stopwords and len(word) > 1]
    # write(words)
    # write(len(words))

    # Count the frequency of each word, and remove the duplicates
    frequencies = Counter(words)
    # write(frequencies)
    # write(len(frequencies))

    # Filter the lower frequency words, the word frequency should be higher than 1
    frequencies = {word: freq for word, freq in frequencies.items() if freq > 1}
    # write(frequencies)
    # write(len(frequencies))

    # Transform frequencies dict into a dataframe
    freq: DataFrame = DataFrame(list(frequencies.items()), columns=["word", "frequency"])
    # write(freq)
    # write(len(freq))
    # Sort the frequencies dataframe
    sorted_freq: DataFrame = freq.sort_values("frequency", ascending=False)
    # write(freq)
    # write(len(sorted_freq))

    # Display the chart of the sorted dataframe
    subheader("Table for words Frequencies")
    data_editor(sorted_freq, hide_index=True, disabled=True, use_container_width=True)
    subheader("Chart for words Frequencies")
    bar_chart(sorted_freq.set_index("word"), use_container_width=True)

    # Generate the word cloud
    with sidebar:
        subheader("Wordcloud Settings")
        FONTS: list[str] = ["qingKeHuangYou", ]
        font: str = selectbox(
            "Font",
            options=FONTS, index=0,
            help="Font for the word cloud",
        )
        if font:
            font = f"assets/{font}.ttf"
        MAX: int = slider(
            "Number of Top Words Frequencies",
            min_value=1, max_value=len(sorted_freq), value=12, step=1,
            help="Max words for the word cloud",
        )
        if MAX:
            cloud = wordcloud_generator(font, top_n=MAX, sorted_df=sorted_freq)

    # Display the word cloud
    img = cloud.to_image()
    subheader("Wordcloud for words Frequencies")
    image(img, use_container_width=True)
