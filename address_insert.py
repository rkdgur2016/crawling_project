from DB_connection import db_connection, insert_addr_data
import pandas as pd

conn = db_connection()

df = pd.read_csv('C:/web_study/vscode_workspace/crowling_study/국토교통부_법정동코드_20240805.csv', encoding="ANSI").to_numpy()
print(df)

filtered_arr = [row for row in df if row[2] == '존재']
print(filtered_arr)

processed_data = []
for row in filtered_arr:
    try:
        address_code = row[0]
        full_address = row[1]
        address_parts = full_address.split(' ')

        # 주소 구성 요소 분리 및 기본값 처리
        city = address_parts[0] if len(address_parts) > 0 else None
        district = address_parts[1] if len(address_parts) > 1 else None
        dong = address_parts[2] if len(address_parts) > 2 else None

        # 가공된 데이터를 리스트에 추가
        processed_data.append((address_code, city, district, dong))

    except Exception as e:
        print(f"오류 발생: {e}, 데이터: {row}")

print(processed_data)
insert_addr_data(conn, processed_data)

conn.close()
