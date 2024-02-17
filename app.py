import streamlit as st

def main():
    st.title("Instruction Tuner")

    # Add sidebar with options
    selected_option = st.sidebar.selectbox("Select Option", ["Text", "Image", "Audio", "Video"])

    if selected_option == "Text":
        prompt_text = st.text_area("Enter Prompt")
        output_text = st.text_area("Output", "", key="output_text") #disabled=True)

        col1,col2,_,_ = st.columns(4)

        if col1.button("Generate Output"):
            # Generate output with an LLM model
            generated_output = generate_output(prompt_text)
            st.session_state.output_text = generated_output

        if col2.button("Submit to DB"):
            # Push to a local/cloud database
            submit_to_db(prompt_text, generated_output)

    elif selected_option == "Image":
        uploaded_image = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])
        output_text = st.text_area("Output", "", key="output_text")

        if uploaded_image is not None:
            st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)

        col1,col2,_,_ = st.columns(4)

        if col1.button("Generate Output"):
            # Generate output with an LLM model
            generated_output = generate_output(prompt_text)
            st.session_state.output_text = generated_output

        if col2.button("Submit to DB"):
            # Push to a local/cloud database
            submit_to_db(prompt_text, generated_output)

    elif selected_option == "Audio":
        audio_file = st.file_uploader("Choose an audio file", type=["mp3", "wav"])
        output_text = st.text_area("Output", "", key="output_text")

        if audio_file is not None:
            st.audio(audio_file, format="audio/*")

        if st.button("Submit to DB"):
            # Push to a local/cloud database
            submit_to_db("Audio", audio_file)

    elif selected_option == "Video":
        video_file = st.file_uploader("Choose a video file", type=["mp4"])
        output_text = st.text_area("Output", "", key="output_text")

        if video_file is not None:
            st.video(video_file)

        if st.button("Submit to DB"):
            # Push to a local/cloud database
            submit_to_db("Video", video_file)

if __name__ == "__main__":
    main()
