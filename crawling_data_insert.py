from DB_connection import db_connection, insert_messege_data
import pandas as pd

conn = db_connection()

df = pd.read_csv('C:/web_study/vscode_workspace/crowling_study/크롤링 데이터 인덱싱 O.csv', encoding="ANSI").to_numpy()
print(df)

