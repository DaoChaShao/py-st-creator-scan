#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/5/3 12:33
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   b_description.py
# @Desc     :

from pandas import read_csv, to_datetime
from streamlit import (empty, session_state, sidebar, dataframe, subheader,
                       caption, spinner, write)

from utils.helper import Timer


def main() -> None:
    """ streamlit run main.py """
    empty_message: empty = empty()

    # Initialise the data in the session state
    if "data" not in session_state:
        session_state["data"] = None

    # Keep the widget of file_uploader visible in always
    with sidebar:
        subheader("Data File Uploader")
        with spinner("The file is being uploaded..."):
            with Timer("The file is being uploaded") as timer:
                file = sidebar.file_uploader(
                    "Choose a CSV file to upload",
                    type=".csv",
                    accept_multiple_files=False,
                    help="Choose a CSV file to upload to your disks",
                )
            empty_message.success(f"{timer}")

    # Read the content of the uploaded file
    if file is not None:
        session_state["data"] = read_csv(file)
        if "date" in session_state["data"].columns:
            session_state["data"]["date"] = to_datetime(session_state["data"]["date"]).dt.date
        if "time" in session_state["data"].columns:
            session_state["data"]["time"] = session_state["data"]["time"].astype(str).str.slice(0, 5)

    # If there is data, display the content
    if session_state["data"] is not None:
        df = session_state.data.copy()

        # If content exists, delete the column
        if "content" in df.columns:
            df = df.drop(columns=["content"])

        # If like, comment and forward exist, add the column of total interaction
        if {"like", "comment", "forward"}.issubset(df.columns):
            df["total interaction"] = df["like"] + df["comment"] + df["collection"] + df["forward"]

        # Display the new dataframe
        styled_df = df.style.highlight_max(axis=0, color="yellow", subset=df.columns.difference(["date", "time"]))
        subheader("Basic Data Details")
        dataframe(styled_df, use_container_width=True, hide_index=True)

        # Calculate the ratio between the different interactions
        sidebar.subheader("Comparison Ratio")
        options: list[str] = ["like", "comment", "collection", "forward"]
        ratioX: str = sidebar.selectbox(
            "Select an interaction", options=options, index=0, disabled=True, placeholder="Select an interaction"
        )
        if ratioX:
            options.remove(ratioX)
            ratioY: str = sidebar.selectbox(
                "Select the other interaction", options=options, index=None, placeholder="Select the other interaction"
            )
            if ratioY:
                df_ratio = df[["date", "time", ratioX, ratioY]].copy()
                # Delete the zero column
                df_ratio = df_ratio[df_ratio[ratioY] != 0].copy()
                df_ratio["ratio"] = (df_ratio[ratioX] / df_ratio[ratioY]).round(2)

                styled_df_ratio = df_ratio.style.format({"ratio": "{:.2f}"}).highlight_max(
                    axis=0, color="yellow", subset=df_ratio.columns.difference(["date", "time"])
                )
                subheader("Comparison Ratio")
                dataframe(styled_df_ratio, use_container_width=True, hide_index=True)

                mean = df_ratio["ratio"].mean()
                caption(f"The average ratio of {ratioX.upper()} and {ratioY.upper()} is {mean:.2f}: 1")
                caption(f"Should we calculate the ratio between followers and likes")
                caption(f"Should we calculate the ratio between followers and comments")
    else:
        empty_message.info("Please select a CSV file to upload.")


if __name__ == "__main__":
    main()
