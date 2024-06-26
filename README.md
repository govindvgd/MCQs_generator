# MCQ Generator

This repository contains code for generating Multiple Choice Questions (MCQs) from a given text using Natural Language Processing (NLP) techniques. The project uses a combination of text summarization, keyword extraction, and distractor generation to create MCQs.

## Features

- Summarizes input text to extract important information.
- Extracts keywords from the summarized text.
- Tokenizes sentences and maps them to the extracted keywords.
- Generates distractors for the keywords.
- Displays MCQs with options using Streamlit.

## Project Structure

- `requirements.txt` - Lists the required Python libraries.
- `mcq_generator.py` - Contains the core logic for generating MCQs.
- `streamlit_app.py` - Contains the Streamlit interface for interacting with the MCQ Generator.
- `README.md` - Provides an overview and instructions for the project.

## Usage

1. Enter the text you want to generate MCQs from in the text area.
2. Click the "Generate MCQs" button.
3. The generated MCQs will be displayed below the button with options to choose from.

## Acknowledgments

This project uses the following libraries:
- [transformers](https://github.com/huggingface/transformers)
- [torch](https://pytorch.org/)
- [rake-nltk](https://github.com/csurfer/rake-nltk)
- [nltk](https://www.nltk.org/)
- [streamlit](https://www.streamlit.io/)
