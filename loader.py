import pandas as pd
import os
from sqlalchemy import create_engine
import configparser

def get_engine():
    config = configparser.ConfigParser()
    config.read('config.ini')
    creds = config['mysql']
    url = f"mysql+pymysql://{creds['username']}:{creds['password']}@{creds['host']}:{creds['port']}/{creds['database']}"
    engine = create_engine(url)
    return engine


def load_file_to_db(data_dir):
    engine = get_engine()
    for file in os.listdir(data_dir):
        if file.endswith('.csv'):
            table_name = os.path.splitext(file)[0]
            print(f'loading {file} into table {table_name}')
            df = pd.read_csv(os.path.join(data_dir, file))
            df.to_sql(table_name,con = engine , if_exists = 'replace', index = False)


     