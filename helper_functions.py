import datetime
import pandas as pd

def load_data(url, dtype=None):
    import os
    from six.moves import urllib
    _, filename = url.rsplit('/', 1)
    filename = str(datetime.date.today()) + '_' + filename
    filepath = 'datasets/' + filename
    if not os.path.isdir('datasets'):
        os.makedirs('datasets')
    try:
        if not os.path.exists(filepath):
            urllib.request.urlretrieve(url, filepath)
    except:
        print('Could not retrieve ' + url)
        raise
    return pd.read_csv(filepath, dtype=dtype)    

def load_main_dataframe(date=None):
    if date is None:
        date = datetime.datetime.today().date()
    return (pd.read_csv(f'datasets/{date}_covid19_stats.csv', float_precision='round_trip',
                        index_col=['country_region', 'province_state', 'county', 'date'], 
                        dtype={'country_region':str, 'province_state':str, 'county':str},
                        parse_dates=True)
            .sort_index(level=[0,1,2,3]))

def load_yx_dataframe(date=None):
    if date is None:
        date = datetime.datetime.today().date()
    return pd.read_csv(f'datasets/{date}_covid19_ml.csv', float_precision='round_trip')