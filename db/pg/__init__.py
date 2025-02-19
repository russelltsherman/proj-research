import os
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker

def get_url():
    return "postgresql://%s:%s@%s/%s" % (
        os.getenv("PGUSER"),
        os.getenv("PGPASSWORD"),
        os.getenv("PGHOST"),
        os.getenv("PGDATABASE"),
    )

# Create an engine
engine = sa.create_engine(get_url(), echo=False)

# Create a sessionmaker
Session = sessionmaker(bind=engine)
