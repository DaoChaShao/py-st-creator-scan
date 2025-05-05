#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/5/3 12:31
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   helper.py
# @Desc     :   

from pandas import DataFrame
from plotly.express import scatter
from re import findall
from time import perf_counter
from wordcloud import WordCloud


def filter_chinese(text: str) -> list[str]:
    """ Filter the Chinese characters from the text

    :param text: the text to filter
    :type text: str
    :return: the filtered text
    :rtype: str
    """
    return findall(r"[0-9\u4e00-\u9fff]+", text)


def filter_english(text: str) -> list[str]:
    """ Filter the English characters from the text

    :param text: the text to filter
    :type text: str
    :return: the filtered text
    :rtype: str
    """
    return findall(r"[a-zA-Z0-9]+", text)


def filter_chinese_and_english(words: list[str]) -> list[str]:
    """ Filter the Chinese and English characters from the text

    :param words: the text to filter
    :type words: list[str]
    :return: the filtered text
    :rtype: str
    """
    CHARACTERS: list[str] = []
    for word in words:
        matches: list[str] = findall(r"[a-zA-Z\u4e00-\u9fff]+", word)
        CHARACTERS.extend(matches)
    return CHARACTERS


def filter_stopwords(stopwords_file: str) -> list[str]:
    """ Filter the stopwords from the stopwords file

    :param stopwords_file: the stopwords file
    :type stopwords_file: str
    :return: the filtered stopwords
    :rtype: list[str]
    """
    with open(stopwords_file, "r", encoding="utf-8") as file:
        return file.read().splitlines()


def wordcloud_generator(font: str, top_n: int, sorted_df: DataFrame, colour: str = "white") -> WordCloud:
    """ Generate a wordcloud image

    :param font: the font to use
    :type font: str
    :param top_n: the number of words to return
    :type top_n: int
    :param sorted_df: the sorted dataframe
    :type sorted_df: DataFrame
    :param colour: the colour to use
    :type colour: str
    :return: the wordcloud image
    :rtype: WordCloud
    """
    # Filter top n words
    top: DataFrame = sorted_df.head(top_n)
    # Zip the new dataframe with the column word and frequency of the top dataframe
    frequencies: dict[str, int] = dict(zip(top["word"], top["frequency"]))
    return WordCloud(
        font_path=font,
        background_color=colour,
        width=800,
        height=600
    ).generate_from_frequencies(frequencies)


def chart_scatter(dataframe: DataFrame, X: str, Y: str):
    """ Display chart scatter plot

    :param dataframe: the dataframe
    :type dataframe: DataFrame
    :param X: the X axis
    :type X: str
    :param Y: the Y axis
    :type Y: str
    """
    return scatter(
        dataframe,
        x=X,
        y=Y,
        title=f"The trend and situation of {X} vs {Y}",
        labels={"X": f"{X}", "Y": f"{Y}"},
        hover_data=[f"{X}", f"{Y}"],
        trendline="ols"  # Regression: Ordinary Least Squares
    )


def emotion_rater(score: float) -> str:
    if score >= 0.8:
        return "Happy"
    elif score >= 0.6:
        return "Smile"
    elif score >= 0.4:
        return "Neutral"
    elif score >= 0.2:
        return "Sad"
    else:
        return "Cry"


class Timer(object):
    """ A simple timer class to measure the elapsed time.

    :param precision: the number of decimal places to round the elapsed time
    :type precision: integer
    :param description: the description of the timer
    :type description: str
    """

    def __init__(self, description: str = None, precision: int = 5):
        self._description: str = description
        self._precision: int = precision
        self._start: float = 0.0
        self._end: float = 0.0
        self._elapsed: float = 0.0

    def __enter__(self):
        self._start = perf_counter()
        print()
        print("-" * 50)
        print(f"{self._description} has been started.")
        return self

    def __exit__(self, *args):
        self._end = perf_counter()
        self._elapsed = self._end - self._start

    def __repr__(self):
        if self._elapsed != 0.0:
            print("-" * 50)
            return f"{self._description}, which took {self._elapsed:.{self._precision}f} seconds."
        return f"{self._description} has NOT been started."
