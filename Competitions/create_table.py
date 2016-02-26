import pandas as pd
from sqlalchemy import create_engine
from secrets import *

engine = create_engine(DATABASE_URL)

df = pd.read_csv('NYC_Jobs.csv')
df.columns = [c.lower() for c in df.columns]

df.to_sql('jobs', engine, index=False, index_label="job_id")

