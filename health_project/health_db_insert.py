from health_DB_connection import *
import os

conn = db_connection()

#폴더 읽어와서 band = 1, body_weight = 2, Dumbbell = 3, Kettlebell = 4, Roll = 5로 변환 후 하위 폴더 읽어오기
path = "C:/Users/kevin/git/crawling_project/crawling_project/image/Roll"
folder = os.listdir(path)
print(folder)

for folders in folder:
    insert_exercise_part(conn, '5', folders)

#폴더명 찾고 band/chest