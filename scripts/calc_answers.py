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
import plotly.graph_objects as go
from tqdm import tqdm
from ast import literal_eval
import numpy as np
import sys
import os

if __name__ == "__main__":
    try:
        assert(len(sys.argv) == 2)
        assert(os.path.isdir(sys.argv[1]))
    except:
        print(usage)
        exit()

    dir_path = sys.argv[1]
    file_paths = [os.path.join(dir_path, path) for path in os.listdir(dir_path)]

    month_fig = go.Figure()

    stats = open('stats.txt', 'a')

    for f_path in tqdm(file_paths):
        print('\n' + f_path + ':\n', file=stats)
        # read subtopic file
        subtopic_df = pd.read_csv(f_path, sep='\t', dtype={'place':str}, error_bad_lines=False)

        subtopic_df['hashtags'].fillna(value='[]', inplace=True)
        subtopic_df['urls'].fillna(value='[]', inplace=True)
        subtopic_df['photos'].fillna(value='[]', inplace=True)
        subtopic_df['mentions'].fillna(value='[]', inplace=True)

        # top 10 hashtags
        hashtags = pd.Series(subtopic_df['hashtags'].apply(literal_eval).sum())
        top10hashtags = hashtags.value_counts()[:10]
        print('top 10 hashtags\n', top10hashtags, file=stats)
        fig = go.Figure()
        fig.add_trace(go.Bar(x=['#' + i for i in top10hashtags.index], y=top10hashtags))
        fig.update_layout(font_size=13, title_text='Top 10 hashtags for ' + os.path.basename(f_path).replace('.csv', ''),
                            xaxis_title='Hashtag', yaxis_title='Frequency')
        fig.show()

        # top 10 mentions
        mentions = pd.Series([x['screen_name'] for x in subtopic_df['mentions'].apply(literal_eval).sum()])
        top10mentions = mentions.value_counts()[:10]
        print('top 10 mentions\n', top10mentions, file=stats)
        fig = go.Figure()
        fig.add_trace(go.Bar(x=['@' + i for i in top10mentions.index], y=top10mentions))
        fig.update_layout(font_size=13, title_text='Top 10 mentions for ' + os.path.basename(f_path).replace('.csv', ''),
                            xaxis_title='Mention', yaxis_title='Frequency')
        fig.show()

        # top 5 languages
        top5langs = subtopic_df['language'].value_counts()[:5]
        print('language tags', subtopic_df['language'].value_counts(), file=stats)
        fig = go.Figure()
        fig.add_trace(go.Bar(x=top5langs.index, y=top5langs))
        fig.update_layout(font_size=13, title_text='Top 5 language tags for ' + os.path.basename(f_path).replace('.csv', ''),
                            xaxis_title='Language Tag', yaxis_title='Frequency')
        fig.show()

        # month-wise plot
        months = subtopic_df['date'].value_counts().sort_index()
        month_fig.add_trace(go.Scatter(x=months.index, y = months, name=os.path.basename(f_path).replace('.csv', '')))

        # words 
        words = (' '.join([str(i) for i in list(subtopic_df['tweet'])])).split()
        words_df = pd.DataFrame()
        words_df['words'] = words
        words_df.to_csv(f_path.replace('.csv', '_words.csv'), index=False, header=False)


        # stats
        print('No of tweets', subtopic_df.index.size, file=stats)
        print('No of mentions', len(mentions), file=stats)
        print('No of hashtags', len(hashtags), file=stats)
        print('No of unique mentions', mentions.nunique(), file=stats)
        print('No of unique hashtags', hashtags.nunique(), file=stats)
        print('No of unique languages', subtopic_df['language'].nunique(), file=stats)

        days = subtopic_df['date'].value_counts().sort_index()
        print('Max number of tweets in a day', days.max(), file=stats)

        print('Time zones', subtopic_df['timezone'].nunique(), file=stats)
        print('No of conversations/threads', subtopic_df['conversation_id'].nunique(), file=stats)
        print('No of users', subtopic_df['user_id'].nunique(), file=stats)
        print('No of places', subtopic_df['place'].nunique(), file=stats)

        # urls = pd.Series(subtopic_df['urls'].apply(literal_eval).sum())
        # print('No of urls', urls.nunique(), file=stats)

        # photos = pd.Series(subtopic_df['photos'].apply(literal_eval).sum())
        # print('No of photos', photos.nunique(), file=stats)

        print('Total number of likes', subtopic_df['likes_count'].sum(), file=stats)
        print('No of videos', subtopic_df['video'].sum(), file=stats)
        print('geo tags count', subtopic_df['geo'].nunique(), file=stats)
        print('percentage of tweets that are retweets', 100 - (subtopic_df['retweet']=='False').sum()*100/subtopic_df.index.size, file=stats)
        print('Total no of retweets received', subtopic_df['retweets_count'].sum(), file=stats)
        print('Total no of replies received', subtopic_df['replies_count'].sum(), file=stats)

    month_fig.update_layout(font_size=13, title_text='Monthly distribution of tweets',
                    xaxis_title='Month', yaxis_title='No. of tweets', legend_title_text='Subtopic')
    month_fig.show()

    stats.close()