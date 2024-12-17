import pymysql as db

def db_connection():
    conn = db.connect(
        host='health-adviser-project.cbmgm2mw0i0s.us-east-1.rds.amazonaws.com',
        port=3306,
        user='limrkdgur2016',
        password='dla010216!',
        db='health_advisor_project',
        charset='utf8mb4'
    )
    return conn

def main():
    try: 
        conn = db_connection()
        print('연결 성공!')
    except Exception as e:
        print(f'연결 오류 : {e}')
    conn.close()
    print('연결 종료!')


def insert_exercise_category (conn, target):
    try:
        with conn.cursor() as cur:
            # SQL 쿼리 작성
            sql = '''
                    INSERT INTO EXERCISE_CATEGORY (name)
                        VALUES (
                        %s
                        )
                    '''
            # 여러 데이터를 한 번에 삽입
            cur.execute(sql, target)
            # 변경 사항 저장
            conn.commit()
            print(f"{target}이이 성공적으로 삽입되었습니다.")
    except Exception as e:
        print("데이터 삽입 중 오류 발생:", e)

#운동 부위 데이터 insert
def insert_exercise_part(conn, id, target):
    try:
        with conn.cursor() as cur:
            # SQL 쿼리 작성
            sql = '''
                    INSERT INTO EXERCISE_PART(
                        category_id,
                        name)
                        VALUES (
                        %s, 
                        %s
                        )
                    '''
            # 여러 데이터를 한 번에 삽입
            cur.execute(sql, (id, target))
            # 변경 사항 저장
            conn.commit()
            print(f"{target}이이 성공적으로 삽입되었습니다.")
    except Exception as e:
        print("데이터 삽입 중 오류 발생:", e)

if __name__ == "__main__" :
    main()

    '''
    리스트로 받지 않아도 반복문으로 넣는 방법도 있다.

        cursor.execute(CREATE TABLE IF NOT EXISTS folders
                  (id INTEGER PRIMARY KEY, name TEXT))

        for folder in folder_list:
        cursor.execute("INSERT INTO folders (name) VALUES (?)", (folder,))

    '''