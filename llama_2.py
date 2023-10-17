import pytesseract
from PIL import Image
import json
import pandas as pd
import openai


# Setup OpenAI API
openai.api_base = 'http://10.0.0.167:1234/v1'
openai.api_key = 'testing'

def summarize_dataframe(df):
    # Convert the dataframe to a string representation
    df_string = df.to_string()
    messages = [
        {"role": "user", "content": f"Please summarize the following data:\n{df_string}"}
    ]

    # Request a summary from OpenAI Chat Completion
    response = openai.ChatCompletion.create(
        messages=messages,
        temperature=0.7,
        stream=False,
        max_tokens=1500  # Adjust based on the desired length of the summary
    )

    # Extract the response and return it
    summary = response.choices[0].message.get('content')
    return summary


def image_to_dataframe(img_path):
    # Open the image
    img = Image.open(img_path)
    
    # Extract text using Tesseract
    text = pytesseract.image_to_string(img)
    
    # Split the text by lines
    lines = text.split("\n")
    
    # Remove empty lines and lines with only spaces
    lines = [line for line in lines if line.strip() != ""]
    
    # Extract column headers and rows
    headers = lines[0].split()
    rows = lines[1:]
    
    # Convert rows to list of dictionaries format
    data = []
    for row in rows:
        split_row = row.split()
        
        # To ensure we only process valid rows
        if len(split_row) >= 6:
            date = split_row[0]
            winning_numbers = " ".join(split_row[1:5])
            megaball = split_row[5]
            megaplier = split_row[6] if len(split_row) > 6 else None
            
            row_data = {
                "Date": date,
                "Winning Numbers": winning_numbers,
                "Megaball": megaball,
            }
            if megaplier:
                row_data["Megaplier"] = megaplier
            
            data.append(row_data)

    # Convert list of dictionaries to DataFrame
    df = pd.DataFrame(data)
    
    return df


# Path to the image
img_path = 'data_img.png'


# Print the JSON data.
df = image_to_dataframe(img_path)

print(df)

print(summarize_dataframe(df))
