import os

import pandas as pd
import streamlit as st

from src.text_data_handlers import (flow_text_from_csv, 
                                    flow_text_from_directory)
from src.utils import submit_to_db


def main():
    st.title("Instruction Tuner")
 
    if 'content' not in st.session_state:
        st.session_state.content = "Instruction Tuner"
    
    if 'disabled' not in st.session_state:
        st.session_state.disabled = False
    
    text_option = st.sidebar.selectbox("Select Text Option", ["Text from CSV", "Text from Folder", "Manual"], disabled=st.session_state.disabled)
    openai_api_key = st.sidebar.text_area("Enter OpenAI API Key")
 
    if text_option == "Text from CSV":
        st.session_state.disabled = True
        csv_path = st.sidebar.text_input("Enter CSV File Path:")
        if os.path.exists(csv_path):
            flow_text_from_csv(csv_path)
        else:
            st.write("Please enter a valid path.")
    elif text_option == "Text from Folder":
        st.session_state.disabled = True
        folder_path = st.sidebar.text_input("Enter Folder Path:")
        if os.path.exists(folder_path):
            flow_text_from_directory(folder_path)
        else:
            st.write("Please enter a valid path.")
    elif text_option == "Manual":
        st.session_state.disabled = True
        st.session_state.prompt_text = st.text_area("Enter Prompt")
        st.session_state.content = st.session_state.prompt_text

    st.session_state.output_text = st.text_area("Output", "")

    col1, col2, _, _ = st.columns(4)

    if col1.button("Generate Output"):
        # Generate output with an LLM model
        if generated_output is None:
            st.session_state.output_text = generate_output(openai_api_key, st.session_state.prompt_text)

    if col2.button("Submit to DB"):
        # Push to a local/cloud database
        submit_to_db(text_option, st.session_state.content, st.session_state.output_text)


if __name__ == "__main__":
    main()