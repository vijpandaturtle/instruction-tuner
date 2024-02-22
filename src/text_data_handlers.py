import os

import pandas as pd
import streamlit as st


def flow_text_from_csv(csv_file_path):
    if 'counter' not in st.session_state:
        st.session_state.counter = 0

    if not os.path.exists(csv_file_path):
        st.write("Please enter a valid path.")

    # Read text data from CSV file
    df = pd.read_csv(csv_file_path)
    text_data = df['prompt'].tolist()

    st.write(st.session_state.content)
    st.write(f"Index: {st.session_state.counter}")

    def show_next_text(text):
        st.session_state.content = text
        # Increments the counter to get the next text
        st.session_state.counter += 1
        if st.session_state.counter >= len(text_data):
            st.session_state.counter = 0
    
    def show_prev_text(text):
        st.session_state.content = text
        # Increments the counter to get the next text
        st.session_state.counter -= 1
        if st.session_state.counter <= 0:
            st.session_state.counter = 0

    col1, col2, _, _ = st.columns(4)
    # Select text and show it on button click
    text = text_data[st.session_state.counter]
    prev_btn = col1.button("Show prev text ⏭️", on_click=show_prev_text, args=([text]))
    show_btn = col2.button("Show next text ⏭️", on_click=show_next_text, args=([text]))
    
def flow_text_from_directory(folder_path):
    if 'counter' not in st.session_state:
        st.session_state.counter = 0

    def show_next_text(text):
        st.session_state.content = text
        # Increments the counter to get the next text
        st.session_state.counter += 1
        if st.session_state.counter >= len(text_data):
            st.session_state.counter = 0
    
    def show_prev_text(text):
        st.session_state.content = text
        # Increments the counter to get the next text
        st.session_state.counter -= 1
        if st.session_state.counter <= 0:
            st.session_state.counter = 0

    if not os.path.exists(folder_path):
        st.write("Please enter a valid path.")
    else: 
        # Get a list of text documents in the folder
        text_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.txt')]
        
        if text_files == []:
            st.write("Enter valid path")
        else:
            st.sidebar.subheader("List of documents in folder")
            st.sidebar.write(text_files)

            st.write(st.session_state.content)
            st.write(f"Index: {st.session_state.counter}")

            # Select text and show it on button click
            text_path = text_files[st.session_state.counter]

            with open(text_path, 'r') as file:
                text = file.read()

            col1, col2, _, _ = st.columns(4)
            prev_btn = col1.button("Show prev text ⏭️", on_click=show_prev_text, args=([text]))
            show_btn = col2.button("Show next text ⏭️", on_click=show_next_text, args=([text]))
    
