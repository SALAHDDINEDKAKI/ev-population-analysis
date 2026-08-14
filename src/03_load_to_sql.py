from config import CLEANED_DATA
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Load variables from .env file
load_dotenv()
db_password = os.getenv("DB_PASSWORD")

# Load the cleaned data
df = pd.read_csv(CLEANED_DATA)

# Connect to PostgreSQL
# Connect to PostgreSQL using the password from .env (never hardcoded)
engine = create_engine(f"postgresql://postgres:{db_password}@localhost:5432/ev_population")

# Push the dataframe into a new SQL table
df.to_sql('ev_population', engine, if_exists='replace', index=False)

print("Data loaded successfully!")