import datetime
import pandas as pd

def load_main_dataframe(date=None):
    if date is None:
        date = datetime.datetime.today().date()
    return (pd.read_csv(f'datasets/{date}_covid19_stats.csv', keep_default_na=False, float_precision='round_trip',
                        index_col=['country_region', 'province_state', 'county', 'date'], 
                        dtype={'country_region':str, 'province_state':str, 'county':str},
                        parse_dates=True)
            .sort_index(level=[0,1,2,3]))

def load_yx_dataframe(date=None):
    if date is None:
        date = datetime.datetime.today().date()
    return pd.read_csv(f'datasets/{date}_covid19_ml.csv', float_precision='round_trip')