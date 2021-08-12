from datetime import datetime, timedelta
import twint
import pandas as pd
import os
from tqdm import tqdm

df = pd.read_csv('../scraped_tweets_no_replies/amey/psgate.csv', sep='\t', dtype={'place':str}, error_bad_lines=True, warn_bad_lines=True)
# for the place column it is important to explicitly mention the data type.
output_loc = '../scraped_replies/amey/psgate_replies.csv'
output = pd.DataFrame(columns=df.columns)
output.set_index('id')

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

output.to_csv(output_loc, sep='\t')
