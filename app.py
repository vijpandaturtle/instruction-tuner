import streamlit as st
import os
import pandas as pd
from src.utils import submit_to_db
from src.text_data_handlers import (flow_text_from_csv,
                                    flow_text_from_directory)


def main():
    st.title("Instruction Tuner")
 
    if 'content' not in st.session_state:
        st.session_state.content = "Instruction Tuner"

    if 'selected_option' not in st.session_state:
        st.session_state.selected_option = None

    text_option = st.sidebar.selectbox("Select Text Option", ["Text from CSV", "Text from Folder", "Manual"])
 
    # Check if the selected option is different from the previous one
    if st.session_state.selected_option != selected_option:
        st.session_state.selected_option = selected_option
        st.session_state.counter = 0  # Reset the session state index
    
    if text_option == "Text from CSV":
        csv_path = st.text_input("Enter CSV File Path:")
        if os.path.exists(csv_path):
            flow_text_from_csv(csv_path)
        else:
            st.write("Please enter a valid path.")
    elif text_option == "Text from Folder":
        folder_path = st.text_input("Enter Folder Path:")
        if os.path.exists(folder_path):
            flow_text_from_directory(folder_path)
        else:
            st.write("Please enter a valid path.")
    elif text_option == "Manual":
        st.session_state.prompt_text = st.text_area("Enter Prompt")

    st.session_state.output_text = st.text_area("Output", "")

    col1, col2, _, _ = st.columns(4)

    if col1.button("Generate Output"):
        # Generate output with an LLM model
        if generated_output is None:
            st.session_state.output_text = generate_output(st.session_state.prompt_text)

    if col2.button("Submit to DB"):
        # Push to a local/cloud database
        submit_to_db(selected_option, st.session_state.content, st.session_state.output_text)


if __name__ == "__main__":
    main()