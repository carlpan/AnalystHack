import pandas as pd
from sqlalchemy import create_engine
from secrets import *

# Create engine with PostgreSQL url
engine = create_engine(DATABASE_URL)

df = pd.read_csv('NYC_Jobs.csv')
df.columns = [c.lower() for c in df.columns]

# Use pandas to_sql function to create table 
# CSV file is imported to PostgreSQL manually
df.to_sql('jobs', engine, index=False, index_label="job_id")

