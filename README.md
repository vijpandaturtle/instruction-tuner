# LLM Instruction Tuner

<p align="center">
  <img src="assets/blackboard.png" alt="Instruction Tuner" width="200">
</p>

This is a simple utility designed using the Streamlit library to facilitate the creation and annotation of instruction tuning datasets using multiple modalities. The tool allows you to import a folder containing the content you want to annotate and provides an easy-to-use interface for labeling.

## Features

- **Multi-Modality Support:** Annotate datasets with multiple modalities, such as text, image, audio & video. 

- **Folder & CSV File Import:** Import your data/prompts from a CSV file or a folder. CSV file import is only supported for text data. 

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/vijpandaturtle/instruction-tuner.git
    cd instruction-tuner
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the application (for text only):

    ```bash
    streamlit run app.py
    ```
   For multimodal support 
   ```bash
   streamlit run app_mm.py
   ```

2. Open the provided URL in your web browser.

3. Select your data source from the dropdown on the sidebar. 

4. Specify the folder path/choose manual mode, and start annotating!
5. After annotation is complete, the dataset will be available in the "database.csv" file.

# 𝑰𝒏𝒔𝒕𝒓𝒖𝒄𝒕ion 𝑻𝒖𝒏𝒆𝒓

<p align="center">
  <img src="assets/blackboard.png" alt="Instruction Tuner" width="200">
</p>

This is a simple utility designed using the Streamlit library to facilitate the creation and annotation of instruction tuning datasets using multiple modalities. The tool allows you to import a folder containing the content you want to annotate and provides an easy-to-use interface for labeling.

## Features

- **Multi-Modality Support:** Annotate datasets with multiple modalities, such as text, image, audio & video. 

- **Folder & CSV File Import:** Import your data/prompts from a CSV file or a folder. CSV file import is only supported for text data. 

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/vijpandaturtle/instruction-tuner.git
    cd instruction-tuner
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the application (for text only):

    ```bash
    streamlit run app.py
    ```
   For multimodal support 
   ```bash
   streamlit run app_mm.py
   ```

2. Open the provided URL in your web browser.

3. Select your data source from the dropdown on the sidebar. 

4. Specify the folder path, and start annotating!

## Demo

<video width="640" height="360" controls>
  <source src="assets/demo.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

## Contributing

Contributions are welcome! Simply make a pull request with the feature you are planning to add!

## Contact

For questions or feedback, please contact thisisvij98@gmail.com. 

## Contributing

Contributions are welcome! Simply make a pull request with the feature you are planning to add!

## Contact

For questions or feedback, please contact thisisvij98@gmail.com. 
