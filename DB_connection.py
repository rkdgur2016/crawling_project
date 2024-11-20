import pymysql as db

def db_connection():
    conn = db.connect(
        host='localhost',
        port=13306,
        user='root',
        password='0000',
        db='crawling_project',
        charset='utf8mb4'
    )
    return conn

def main():
    conn = db_connection()
    print('연결 완료!')
    conn.close()
    print('연결 종료!')

#주소 데이터 insert
def insert_addr_data(conn, list):
    try:
        with conn.cursor() as cur:
            # SQL 쿼리 작성
            sql = "INSERT INTO address (address_code, city, district, dong) VALUES (%s, %s, %s, %s)"
            # 여러 데이터를 한 번에 삽입
            cur.executemany(sql, list)
            # 변경 사항 저장
            conn.commit()
            print(f"{len(list)}개의 데이터가 성공적으로 삽입되었습니다.")
    except Exception as e:
        print("데이터 삽입 중 오류 발생:", e)

#크롤링 데이터 insert
def insert_messege_data(conn, list):
    try:
        with conn.cursor() as cur:
            # SQL 쿼리 작성
            sql = '''
            INSERT INTO crawling_data (
                id, 
                data_type, 
                seperate, 
                send_from, 
                send_time, 
                content, 
                send_place_1,
                send_place_2, 
                send_place_3,
                send_place_4,
                send_place_5
                ) VALUES (
                        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            
            '''
            # 여러 데이터를 한 번에 삽입
            cur.executemany(sql, list)
            # 변경 사항 저장
            conn.commit()
            print(f"{len(list)}개의 데이터가 성공적으로 삽입되었습니다.")
    except Exception as e:
        print("데이터 삽입 중 오류 발생:", e) 

if __name__ == "__main__" :
    main()