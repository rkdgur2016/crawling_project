from DB_connection import db_connection, insert_messege_data
import pandas as pd
import numpy as np

conn = db_connection()

# CSV 파일 읽기
df = pd.read_csv('C:/web_study/vscode_workspace/crowling_study/indexing_file.csv', encoding="ANSI")
print(df)

# NaN 값을 None으로 변환
df = df.replace({np.nan: None})

# DataFrame을 리스트로 변환
data_list = df.values.tolist()

for data in data_list:
    print(data)

# 데이터 삽입
insert_messege_data(conn, data_list)
conn.close()
