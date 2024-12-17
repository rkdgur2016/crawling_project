from DB_connection import db_connection, select_addr_code, select_all_addr_code
import pandas as pd

conn = db_connection()

select_all_addr_code(conn)
conn.close()