from driver_connection import *
from file_create import *
from selenium.webdriver.support.select import Select
import requests

driver = driver()
path = "https://www.lyfta.app/ko"
driver_connection(driver, path)

login_btn = driver.find_element(By.CLASS_NAME, 'btn-primary-big')
login_btn.click()

apple_login_btn = driver.find_element(By.ID, 'apple-sign-in-button')
apple_login_btn.click()

id = 'limrkdgur2016@naver.com'
pw = 'Lim010216!'

id_field = driver.find_element(By.ID, 'account_name_text_field')
wd(driver, 3).until(EC.presence_of_element_located((By.ID, 'account_name_text_field')))
id_field.send_keys(id)

id_send_btn = driver.find_element(By.CLASS_NAME, 'shared-icon.icon_sign_in')
id_send_btn .click()

wd(driver, 10).until(EC.presence_of_element_located((By.ID, 'continue-password')))
id_to_pw_btn = driver.find_element(By.ID, 'continue-password')
id_to_pw_btn.click()

wd(driver, 20).until(EC.presence_of_element_located((By.ID, 'password_text_field')))
pw_filed = driver.find_element(By.ID, 'password_text_field')
pw_filed.send_keys(pw)

time.sleep(20)
#시간 내 로그인

select_box = driver.find_element(By.XPATH, "//*[@aria-label='Filter by equipment']")
select = Select(select_box)
select.select_by_value("Roll")

time.sleep(40)

exercise_data = []

image_elements = driver.find_elements(By.CLASS_NAME, 'ExerciseCard_exercise-landing-card-image__n_cOb')
exercise_elements = driver.find_elements(By.CLASS_NAME, 'body-large')
part_elements = driver.find_elements(By.CLASS_NAME, 'body-medium')

for i in range(len(image_elements)):
    try:
        image_url = image_elements[i].get_attribute('src')
        exercise = exercise_elements[i].text
        exercise_part = part_elements[i].text.split(',')[0]
        
        # 폴더 생성 및 이미지 저장
        folder_create(exercise_part)
        response = requests.get(image_url)
        if response.status_code == 200:
            file_extension = os.path.splitext(image_url.split('&')[0])[1]
            save_image(exercise_part, exercise, response.content, file_extension)
        
        exercise_data.append((image_url, exercise, exercise_part))
    
    except Exception as e:
        print(f"오류 발생: {e}")
        break  # 반복 중단

print(f'{len(exercise_data)} 개의 데이터 크롤링 성공!')