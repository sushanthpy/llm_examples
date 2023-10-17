How to Use llm studio server to Chat to Summarize Data in Python
Description: This repository contains example code demonstrating how to use the OpenAI API to summarize data using the llm studio server. This example also includes the use of pytesseract to extract data from images.

Author: sushanth

Dependencies:
openai
pytesseract
pandas
PIL (from Pillow)

Setup:
Install the necessary Python libraries:

pip install openai pytesseract pandas Pillow

Make sure you have Tesseract installed on your system as it's required for pytesseract. Follow the installation guide for your OS from the official Tesseract GitHub repository.

Usage:
Set up the OpenAI API:

Modify the openai.api_base and openai.api_key as required. In this example, a local server endpoint is being used.
The function image_to_dataframe(img_path):

Converts the content of an image into a pandas DataFrame.
img_path: Path to the image containing tabular data.
The function summarize_dataframe(df):

Summarizes the given pandas DataFrame using the OpenAI Chat Completion model.
df: Input DataFrame to summarize.
Use the image path data_img.png to test the script. You can replace this with the path to your own image.

Execute the script to view the DataFrame extracted from the image and its summary.

Notes:
The image_to_dataframe function expects specific formatting in the image. Ensure the image has content structured similarly to the example for accurate extraction.
Adjust the max_tokens parameter in the summarize_dataframe function based on the desired length of the summary.


Contributing:
Feel free to raise issues or pull requests if you think there's room for improvement.

