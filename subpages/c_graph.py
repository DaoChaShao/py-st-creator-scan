#!/usr/bin/env python3.12
# -*- Coding: UTF-8 -*-
# @Time     :   2025/5/3 13:13
# @Author   :   Shawn
# @Version  :   Version 0.1.0
# @File     :   c_graph.py
# @Desc     :   

from pandas import DataFrame
from streamlit import (session_state, empty, sidebar, selectbox, multiselect,
                       subheader, write)

from utils.helper import chart_scatter

if "data" not in session_state:
    session_state.data = None

empty_message: empty = empty()
empty_fluctuation_subheader: empty = empty()
empty_fluctuation_chart: empty = empty()
empty_relationship_subheader: empty = empty()
empty_mean_subheader: empty = empty()
empty_table: empty = empty()
empty_number: empty = empty()
empty_scatter: empty = empty()

if session_state.data is None:
    empty_message.warning("Please select a CSV file to upload initially.")
else:
    # Set the parameters of the LINE chart
    with sidebar:
        subheader("Fluctuation")
        option_box: list[str] = ["date", "time"]
        X: str | None = selectbox("X Axis", options=option_box, index=None, placeholder="Select X axis you want")
        if X is not None:
            option_mul: list[str] = ["like", "comment", "collection", "forward", "face", "duration"]
            Y: list[str] | None = multiselect("Y Axis", options=option_mul, placeholder="Select Y axis you want")
            if Y:
                empty_fluctuation_subheader.subheader("Fluctuation")
                empty_fluctuation_chart.line_chart(session_state.data, x=X, y=Y, use_container_width=True)

                subheader("Specific Details")
                # Check the details of X
                detail: str = selectbox(
                    "Date or Time",
                    options=session_state.data[X],
                    index=None, placeholder="Pick up a date or a time",
                    help="Select a date or time to check the mean values of all interactions",
                )
                if detail:
                    # Select the proper data style to calculate the mean value
                    categories: list[str] = ["int64", "float64"]
                    mean: dict[str, int | float] = round(
                        session_state.data.select_dtypes(include=categories).mean(), 2).to_dict()
                    empty_mean_subheader.subheader("Mean Values")
                    empty_table.data_editor(DataFrame([mean]), hide_index=True, disabled=True, use_container_width=True)

                    # Set all interactions of the date or time
                    like, comment, collection, forward, face, duration = empty_number.columns(len(option_mul))

                    like_cur: int = session_state.data[session_state.data[X] == detail]["like"].sum()
                    like_sub: int = round(like_cur - mean["like"], 2)
                    like.metric("Like", f"{like_cur}", f"{like_sub}")

                    comment_cur: int = session_state.data[session_state.data[X] == detail]["comment"].sum()
                    comment_sub: int = round(comment_cur - mean["comment"], 2)
                    comment.metric("Comment", f"{comment_cur}", f"{comment_sub}")

                    collection_cur: int = session_state.data[session_state.data[X] == detail]["collection"].sum()
                    collection_sub: int = round(collection_cur - mean["collection"], 2)
                    collection.metric("Collection", f"{collection_cur}", f"{collection_sub}")

                    forward_cur: int = session_state.data[session_state.data[X] == detail]["forward"].sum()
                    forward_sub: int = round(forward_cur - mean["forward"], 2)
                    forward.metric("Forward", f"{forward_cur}", f"{forward_sub}")

                    face_cur: int = session_state.data[session_state.data[X] == detail]["face"].sum()
                    face_sub: int = round(face_cur - mean["face"], 2)
                    face.metric("Face", f"{face_cur}", f"{face_sub}")

                    duration_cur: int = session_state.data[session_state.data[X] == detail]["duration"].sum()
                    duration_sub: int = round(duration_cur - mean["duration"], 2)
                    duration.metric("Duration", f"{duration_cur}", f"{duration_sub}")
                else:
                    empty_message.warning("Please select a date or time to check the comparison of mean values.")

                subheader("Relationships & Trend")
                # Display the relationship and trend between two interactions
                option_relationship: list[str] = ["like", "comment", "collection", "forward", "face", "duration"]
                relationshipX: str | None = selectbox(
                    "Relationship X", options=option_relationship, index=None, placeholder="Select X axis you want"
                )
                if relationshipX:
                    option_relationship.remove(relationshipX)
                    relationshipY: str | None = selectbox(
                        "Relationship Y", options=option_relationship, index=None, placeholder="Select Y axis you want"
                    )
                    if relationshipY:
                        fig = chart_scatter(session_state.data, relationshipX, relationshipY)
                        # empty_relationship_subheader.subheader("Relationships")
                        empty_scatter.plotly_chart(fig, use_container_width=True)
            else:
                empty_message.warning("Please select Y axis you want.")
        else:
            empty_message.warning("Please select X axis you want initially.")
