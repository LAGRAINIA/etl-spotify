import os 
from plugins.utils.etl.database.connection import close_conn, create_conn
import pandas as pd 
import logging

# Logger intitialization 
logging.basicConfig(format='[%(levelname)s]: %(message)s', level=logging.DEBUG)



# Database Location

engine = create_conn()

print(engine)

# df = pd.read_sql_query(
#             'SELECT * FROM INFORMATION_SCHEMA.COLUMNS', engine
#         )
