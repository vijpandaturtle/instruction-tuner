import csv
import os
import openai

# OPENAI Config
openai.api_key = "YOUR_OPENAI_API_KEY"
model_name = "gpt-4-1106-preview"

def generate_output(prompt_text):
    try:
        # Make a call to the OpenAI API
        response = openai.Completion.create(
            engine=model_name,
            prompt=prompt_text,
            max_tokens=150,  # Adjust max_tokens as needed
            n=1,  # Number of completions to generate
            stop=None  # You can provide a list of strings to stop the generation
        )

        # Extract and return the generated text from the response
        generated_text = response['choices'][0]['text'].strip()
        return generated_text
    except Exception as e:
        return None

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
        data = [f"{prompt}", "<noinput>", output_text]
    else:
        st.warning("Invalid input_type")

    # Append the data to the CSV file
    with open(csv_file_path, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

