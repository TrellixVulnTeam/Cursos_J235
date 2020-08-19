import argparse
import logging
logging.basicConfig(level=logging.INFO)
from urllib.parse import urlparse

import pandas as pd


logger = logging.getLogger(__name__)


#_______________________________________________________________________________
def main(filename):
    logger.info('Starting cleaning process')

    df = _read_data(filename)
    uid = _extract_uid(filename)
    df = _add_newspaper_uid_column(df, uid)
    #df = _fill_missing_titles(df)

    return df

#_______________________________________________________________________________
def _read_data(filename):
    """
    _read_data() read and return a .csv

    input: filename
    output: DataFrame of filename
    """
    logger.info(f'Reading file {filename}')

    return pd.read_csv(filename)

#_______________________________________________________________________________
def _extract_uid(filename):
    logger.info('Extracting uid of the newspaper')

    newspaper_uid = filename.split('_')[0].upper()
    return newspaper_uid

#_______________________________________________________________________________
def _add_newspaper_uid_column(df, uid):
    logger.info('Filling DataFrame with the uid')
    df['uid'] = uid
    return df

#_______________________________________________________________________________
def _fill_missing_titles(df):
    logger.info('Filling missing titles ')
    missing_title_mask = df['title'].isna()

    missing_title = (df[missing_title_mask]['url'])
                        .str.extract(r'(?P<missing_titles>[^/]+)$')
                        .applymap(lambda title: title.split('-'))
                        .applymap(lambda title_word_list: ' '.join(
                        title_word_list))
                    )
                    
    df.loc[missing_title_mask, 'title'] = missing_titles.loc[:, 'missing_titles']
    return df
#_______________________________________________________________________________
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename',
                       help = 'The path to the filename',
                       type = str)

    args = parser.parse_args()

    df = main(args.filename)
    print(df)
