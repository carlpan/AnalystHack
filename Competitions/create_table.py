from sqlalchemy import create_engine
import pandas as pd

DATABASE_URL = 'postgres://carlpan66:WAMozart66@localhost/nycdata'
engine = create_engine(DATABASE_URL)

df = pd.read_csv('NYC_Jobs.csv')
df.columns = [c.lower() for c in df.columns]

df.to_sql('jobs', engine, index=False, index_label="job_id")

