"""
Chris Francis (chris.francis@iitgn.ac.in)

Script to combine CSVs and also remove duplicate tweets
"""
usage = "Usage:\n\n\
\
python3 combine_csvs.py [-o OUTPUT_CSV_PATH] CSV_PATH [CSV_PATH ...]\n\n\
\
* OUTPUT_CSV_PATH: default is 'output.csv'\n\
path to save output csv in\n\n\
\
* CSV_PATH: \n\
path to a csv file to be processed"

from optparse import OptionParser
import os
import pandas as pd


def combine_csvs(csv_paths:list, output_path:str):
    """
    Function to combine csvs (also remove duplicates) and save as a csv

    Args:
        csv_paths: list of str
            the list of paths to csvs to be combined

        output_path: str
            Path to save combined csv in
    
    Returns:
        None
    """
    list_dfs = []
    for path in csv_paths:
        df = pd.read_csv(path, sep='\t', dtype={'place':str}, error_bad_lines=False)
        list_dfs.append(df)

    combined_df = pd.concat(list_dfs, ignore_index=True)
    combined_df.drop_duplicates(subset='id', inplace=True, ignore_index=True)

    combined_df.to_csv(output_path, sep='\t', index=False)

if __name__ == "__main__":
    """
    Main function
    """
    parser = OptionParser()

    parser.add_option("-o", "--out", dest="out", type='str', 
	help="Path to save output csv in. Default: %default", default='output.csv')

    (options, args) = parser.parse_args()

    out_path = options.out
    try:
        for a in args:
            assert(os.path.isfile(a))
    except:
        print(usage)
        exit()
    
    combine_csvs(args, out_path)
