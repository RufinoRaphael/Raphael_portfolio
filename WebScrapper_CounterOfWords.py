# Import necessary libraries
import requests  # for making HTTP requests to the website
from bs4 import BeautifulSoup  # for parsing HTML content
import re  # for regular expressions, used in text cleaning
import pandas as pd  # for creating and saving a DataFrame of word counts

# Specify the URL of the web page
url = 'http://www.analytictech.com/mb021/mlk.htm'

# Fetch the content of the web page
page = requests.get(url)

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(page.text, 'html.parser')

# Extract all <p> tags containing the text of the speech
mlkj_speech = soup.find_all('p')  # gets entire text

# Combine all paragraphs into a list of text
speech_combined = [p.text for p in mlkj_speech]

# Join all paragraphs into a single string
string_speech = ' '.join(speech_combined)

# Replace line breaks with spaces for readability
string_speech_cleaned = string_speech.replace('\r\n', ' ')

# Remove backslashes from the text
string_speech_cleaned = string_speech_cleaned.replace('\\', '')

# Remove punctuation using regex, keeping only words and spaces
speech_no_punt = re.sub(r'[^\w\s]', '', string_speech_cleaned)

# Convert all text to lowercase to avoid case sensitivity
speech_lower = speech_no_punt.lower()

# Split the text into a list of words based on whitespace
speech_broken_out = re.split(r'\s+', speech_lower)

# Create a DataFrame of words and their frequency counts
df = pd.DataFrame(speech_broken_out).value_counts()  # counts occurrences of each word

# Save the word counts to a CSV file
df.to_csv(r'C:\Users\CDV\Desktop\Nova pasta\MLKJ_SPEECH_COUNTS.csv', header=['Counts'], index_label='Word')