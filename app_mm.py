import os

import pandas as pd
import streamlit as st

from src.data_handlers import (flow_audio_from_directory,
                               flow_images_from_directory,
                               flow_video_from_directory)
from src.utils import submit_to_db


def main():
    st.title("Instruction Tuner")

    if 'content' not in st.session_state:
        st.session_state.content = None
    
    if 'file_path' not in st.session_state:
        st.session_state.file_path = None

    # Add sidebar with options
    selected_option = st.sidebar.selectbox("Select Option", ["Image", "Audio", "Video"])
    folder_path = st.sidebar.text_input("Enter Folder Path:")

    if selected_option == "Image":
        if os.path.exists(folder_path):
            flow_images_from_directory(folder_path)
        else:
            st.write("Please enter a valid path.")
    elif selected_option == "Audio":
        st.session_state.content = None
        if os.path.exists(folder_path):
            flow_audio_from_directory(folder_path)
        else:
            st.write("Please enter a valid path.")
       
    elif selected_option == "Video":
        st.session_state.content = None
        if os.path.exists(folder_path):
            flow_video_from_directory(folder_path)
        else:
            st.write("Please enter a valid path.")
      
    st.session_state.output_text = st.text_area("Output", "")

    if st.button("Submit to DB"):
        # Push to a local/cloud database
        submit_to_db(selected_option, st.session_state.content, st.session_state.output_text)


if __name__ == "__main__":
    main()