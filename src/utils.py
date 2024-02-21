import csv
import os

# TODO : LLM API output for GPT-4 
def generate_output(prompt_text):
    return "Generated output for prompt: " + prompt_text

# TODO : LLM API output for GPT-4V 
def generate_output(prompt_text):
    return "Generated output for prompt: " + prompt_text


def submit_to_db(input_type, prompt, output_text):
    # Placeholder logic for submitting data to a CSV file
    csv_file_path = "database.csv"
    header = ["prompt", "input", "output"]

    # If the CSV file doesn't exist, create it with the header
    if not os.path.isfile(csv_file_path):
        with open(csv_file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(header)

    # Prepare the data based on the modality
    if input_type == "Text":
        data = [prompt, "<noinput>", output_text]
    elif input_type in ["Audio", "Image", "Video"]:
        data = [f"File Path: {prompt}", "<noinput>", output_text]
    else:
        st.warning("Invalid input_type")

    # Append the data to the CSV file
    with open(csv_file_path, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

    #st.write(f"Submitted {input_type} data to the database:", data)

