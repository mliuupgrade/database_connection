# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sqlalchemy as sa
from sqlalchemy.engine.url import URL
import db_config
import pandas as pd

# define URL params and connection params
url_p=db_config.url_params
conn_p=db_config.conn_params 

# construct sqlalchemy engine
engine = sa.create_engine(
    url=URL.create(**url_p),
    connect_args=conn_p
)

conn = engine.connect()

select_from_test_table = """select id, fico9 from decisioning.transunion_attributes limit 10"""
# execute statements

df = pd.read_sql_query(
    sql=select_from_test_table,
    con=conn.connection,
    index_col=None
)


