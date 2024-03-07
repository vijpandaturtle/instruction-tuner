import os

import pandas as pd
import streamlit as st


def flow_images_from_directory(folder_path):
    if 'counter' not in st.session_state: 
        st.session_state.counter = 0

    if st.session_state.content is not None:
        st.image(st.session_state.content)
        st.write(f"Index as a session_state attribute: {st.session_state.counter}")   
    
    def show_next_photo(photo):
        st.session_state.content = photo 
        ## Increments the counter to get next photo
        st.session_state.counter += 1
        if st.session_state.counter >= len(paths_images):
            st.session_state.counter = 0
    
    def show_prev_photo(photo):
        st.session_state.content = photo 
        ## Increments the counter to get next photo
        st.session_state.counter -= 1
        if st.session_state.counter <= 0:
            st.session_state.counter = 0
    
    if not os.path.exists(folder_path):
        st.write("Please enter a valid path.")
    else: 
        # Get list of images in folder
        col1, col2, _, col4 = st.columns(4)
        paths_images = [os.path.join(folder_path, f) for f in os.listdir(folder_path)]
        if paths_images == []:
            st.write("Enter valid path")
        else:
            st.sidebar.subheader("List of images in folder")
            st.sidebar.write(paths_images)

            # Select photo and send it to button
            photo = paths_images[st.session_state.counter]
        
            # Select text and show it on button click
            prev_btn = col1.button("Show prev image ⏮️", on_click=show_prev_photo, args=([photo]))
            show_btn = col2.button("Show next image ⏭️", on_click=show_next_photo, args=([photo]))
   
def flow_videos_from_directory(folder_path):
    if 'counter' not in st.session_state: 
        st.session_state.counter = 0

    if st.session_state.content is not None:
        video_file = open(st.session_state.content, 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes)
        st.write(f"Index as a session_state attribute: {st.session_state.counter}")   
    
    def show_next_video(video):
        st.session_state.content = video 
        ## Increments the counter to get next photo
        st.session_state.counter += 1
        if st.session_state.counter >= len(paths_videos):
            st.session_state.counter = 0
    
    def show_prev_video(video):
        st.session_state.content = video
        ## Increments the counter to get next photo
        st.session_state.counter -= 1
        if st.session_state.counter <= 0:
            st.session_state.counter = 0
    
    if not os.path.exists(folder_path):
        st.write("Please enter a valid path.")
    else: 
        # Get list of images in folder
        col1, col2, _, col4 = st.columns(4)
        paths_videos = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.mp4')]
        if paths_videos == []:
            st.write("Enter valid path")
        else:
            st.sidebar.subheader("List of videos in folder")
            st.sidebar.write(paths_videos)

            # Select photo and send it to button
            video = paths_videos[st.session_state.counter]
        
            # Select text and show it on button click
            prev_btn = col1.button("Show prev video ⏮️", on_click=show_prev_video, args=([video]))
            show_btn = col2.button("Show next video ⏭️", on_click=show_next_video, args=([video]))

def flow_audio_from_directory(folder_path):
    if 'counter' not in st.session_state: 
        st.session_state.counter = 0

    if st.session_state.content is not None:
        st.audio(st.session_state.content, format="audio/*")
        st.write(f"Index as a session_state attribute: {st.session_state.counter}")   
    
    def show_next_audio(audio):
        st.session_state.content = audio
        ## Increments the counter to get next photo
        st.session_state.counter += 1
        if st.session_state.counter >= len(paths_audio):
            st.session_state.counter = 0
    
    def show_prev_audio(audio):
        st.session_state.content = audio
        ## Increments the counter to get next photo
        st.session_state.counter -= 1
        if st.session_state.counter <= 0:
            st.session_state.counter = 0
    
    if not os.path.exists(folder_path):
        st.write("Please enter a valid path.")
    else: 
        # Get list of images in folder
        col1, col2, _, col4 = st.columns(4)
        paths_audio = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.wav')]
        if paths_audio == []:
            st.write("Enter valid path")
        else:
            st.sidebar.subheader("List of videos in folder")
            st.sidebar.write(paths_audio)

            # Select photo and send it to button
            audio = paths_audio[st.session_state.counter]
        
            # Select text and show it on button click
            prev_btn = col1.button("Show prev audio ⏮️", on_click=show_prev_audio, args=([audio]))
            show_btn = col2.button("Show next audio ⏭️", on_click=show_next_audio, args=([audio]))

