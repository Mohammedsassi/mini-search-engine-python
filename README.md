# mini-search-engine-python
A command-line search engine built in Python with word indexing, frequency ranking, highlighted results, and colored terminal output.


# Mini Search Engine (Python)

A command-line search engine built from scratch using Python.

## Features

- Indexes multiple text files
- Case-insensitive search
- Automatic punctuation removal
- Multi-word search (AND logic)
- Ranks results by word frequency
- Displays only matching lines
- Highlights searched keywords
- Colored terminal output

## How It Works

The program scans all text files inside the `documents` folder,
builds an inverted index with word frequencies,
and allows users to search interactively from the terminal.

## Technologies Used

- Python
- os
- string
- colorama

## Run the Program

Install dependencies:

python -m pip install colorama

Then run:

python main.py

## Example

Search: python ai

Output:
- Matching files
- Ranked by score
- Relevant lines only
- Highlighted keywords
- Colored interface
