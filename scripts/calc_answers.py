"""
Chris Francis (chris.francis@iitgn.ac.in)

Script to find the answers for the Assignment 1 question from the scraped CSVs
"""
usage = "Usage:\n\n\
\
python3 calc_answers.py DIR_PATH\n\n\
\
* DIR_PATH: \n\
path to the directory which contains the scraped CSV files for the subtopics \
should not contain any other CSV file except the 'n' CSV files corresponding to \
'n' subtopics (all processing, like removing duplicates, concatenation etc should \
be done before)\n"

import pandas as pd
import plotly.express as px
import sys
import os

def make_plots():
    """
    Function to make the necessary plots from the data
    Plots will open in a browser window and you can export 
    to PNG using the button available

    Args:

    Returns:
        None
    """
    pass

def compute_stats():
    """
    Function to compute all necessary statistics

    Args:

    Returns:
        None
    """
    pass


if __name__ == "__main__":
    try:
        assert(len(sys.argv) == 2)
        assert(os.path.isdir(sys.argv[1]))
    except:
        print(usage)
        exit()

    