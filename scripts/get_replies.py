usage = "Usage:\n\n\
\
python3 replies.py [-o OUTPUT_CSV_PATH] CSV_PATH\n\n\
\
* OUTPUT_CSV_PATH: default is 'output.csv'\n\
path to save output csv in\n\n\
\
* CSV_PATH: \n\
path to a csv file to be processed"

from datetime import datetime, timedelta
import twint
import pandas as pd
import os
from tqdm import tqdm
from optparse import OptionParser
import os

def getreplies(csv_path: list, output_path: str):
    df = pd.read_csv(csv_path[0], sep='\t', dtype={'place':str}, error_bad_lines=True, warn_bad_lines=True)
    # for the place column it is important to explicitly mention the data type.
    output_loc = output_path
    output = pd.DataFrame(columns=df.columns)
    output.set_index('id')
    output.to_csv(output_loc, sep='\t')

    for twt in tqdm(range(len(df.index))):
        username = "to:@" + df.loc[twt, 'username'] # All tweets sent to this user
        dt = datetime.strptime(df.loc[twt, 'date'], "%Y-%m-%d") # Date of sending
        dtb = str(dt + timedelta(days = -1))
        dtf = str(dt + timedelta(days = 2))
        conv_id = df.loc[twt, 'conversation_id']

        # Configure
        c = twint.Config()
        c.Search = username
        c.Since = dtb
        c.Until = dtf
        c.Store_csv = True
        c.Output = 'temp.csv'
        c.Hide_output = True

        # Run
        twint.run.Search(c)

        if(os.path.exists('temp.csv')):
            df_temp = pd.read_csv('temp.csv', sep=',', dtype={'place':str}, error_bad_lines=True, warn_bad_lines=True, index_col=0)
            output = output.append(df_temp[df_temp['conversation_id'] == conv_id])
            os.remove('temp.csv')

        if (twt + 1) % 50 == 0:
            output.to_csv(output_loc, sep='\t', mode='a', header=False)
            output = pd.DataFrame(columns=df.columns)
            output.set_index('id')


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
    
    getreplies(args, out_path)
