from health_DB_connection import *
import os

conn = db_connection()

#폴더 읽어와서 band = 1, body_weight = 2, Dumbbell = 3, Kettlebell = 4, Roll = 5로 변환 후 하위 폴더 읽어오기
#C:/Users/kevin/git/healpro/healpro/src/main/webapp/resources/img/Band
#part_id, name, img_link
#1~14 (Band), 15~31 (Body weight) 32~46 (Dumbbell) 47~63 (Kettlebell) 64~75 (Roll)
path = "C:/Users/kevin/git/healpro/healpro/src/main/webapp/resources/img/"
target = "Roll/"
folder_name = os.listdir(path + target)

clear_target = target.split("/")[0] #"/" 삭제

category_id = select_exercise_category_id(conn, clear_target)
clear_category_id = int(category_id[0])#필요없는 문자 삭제

for part in folder_name :
    print(f'[[ {part} ]]')
    img_name = os.listdir(path + target + part)
    part_id = select_exercise_part_id(conn, part, clear_category_id)
    clear_part_id = part_id[0]
    for img in img_name :
        img_name = img.split(".")[0]
        insert_exercise(conn, clear_part_id, img_name)
    print(f'{part}에서 {len(img_name)}개의 이미지를 조회했습니다.')

'''
count_data = select_exercise(conn, 1)
print(count_data[0])
'''


'''
for folders in folder:
    insert_exercise_part(conn, '5', folders)6
'''

#폴더명 찾고 band/chest