# PDF Merger 📄

A simple command-line tool to merge multiple PDF files into one, built with Python.

## Features
- Merge unlimited PDF files into a single file
- Enter file paths one by one
- Skips missing files automatically
- Name your output file whatever you want

## How to Use
Run the script:

python pdf_merger.py

Then follow the prompts:
1. Enter the full path of each PDF file one at a time
2. Type done when you have entered all your files
3. Enter a name for the merged output file

## Example

Please enter file path. If you're done type "done": C:\Users\Omaima\Documents\file1.pdf
Please enter file path. If you're done type "done": C:\Users\Omaima\Documents\file2.pdf
Please enter file path. If you're done type "done": done
What would you like to call the new merged file? final_document
final_document.pdf created successfully!

## Requirements
- Python 3.x
- pypdf

## Installation
pip install pypdf
