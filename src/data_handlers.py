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
            prev_btn = col1.button("Show prev text ⏭️", on_click=show_prev_photo, args=([photo]))
            show_btn = col2.button("Show next text ⏭️", on_click=show_next_photo, args=([photo]))
   
def flow_audio_from_directory(folder_path):
    if 'counter' not in st.session_state: 
        st.session_state.counter = 0

    if st.session_state.content is not None:
        st.audio(st.session_state.content, format="audio/*")
        st.write(f"Index as a session_state attribute: {st.session_state.counter}")

    def play_audio(audio_file):
        st.session_state.content = audio_file
        ## Increments the counter to get the next audio file
        st.session_state.counter += 1
        if st.session_state.counter >= len(paths_audio):
            st.session_state.counter = 0

    if not os.path.exists(folder_path):
        st.write("Please enter a valid path.")
    else: 
        # Get list of audio files in folder
        paths_audio = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith(('.mp3', '.wav'))]
        if paths_audio == []:
            st.write("Enter valid path")     
        else:
            st.sidebar.subheader("List of audio files in folder")
            st.sidebar.write(paths_audio)
    
            # Select audio file and send it to button
            audio_file = paths_audio[st.session_state.counter]
            play_btn = st.button("Play next audio ⏭️", on_click=play_audio, args=([audio_file]))

def flow_video_from_directory(folder_path):
    if 'counter' not in st.session_state: 
        st.session_state.counter = 0

    if st.session_state.content is not None:
        st.video(st.session_state.content)
        st.write(f"Index as a session_state attribute: {st.session_state.counter}")

    def play_video(video_file):
        st.session_state.content = video_file
        ## Increments the counter to get the next video file
        st.session_state.counter += 1
        if st.session_state.counter >= len(paths_video):
            st.session_state.counter = 0

    if not os.path.exists(folder_path):
        st.write("Please enter a valid path.")
    else:
        # Get list of video files in folder
        paths_video = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.mp4')]
        if paths_video == []:
            st.write("Enter valid path")  
        else:
            st.sidebar.subheader("List of videos in folder")
            st.sidebar.write(paths_video)
        
            # Select video file and send it to button
            video_file = paths_video[st.session_state.counter]
            play_btn = st.button("Play next video ⏭️", on_click=play_video, args=([video_file]))



