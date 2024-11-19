import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 크롬 드라이버 설정
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.safekorea.go.kr/idsiSFK/neo/sfk/cs/sfc/dis/disasterMsgList.jsp?menuSeq=679")

# 데이터 배열
data_array = []

# tbody 안의 모든 tr 요소 가져오기
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'tbody')))
tbody = driver.find_element(By.TAG_NAME, 'tbody')
rows = tbody.find_elements(By.TAG_NAME, 'tr')

# 각 tr 요소에 대해 반복
for index, row in enumerate(rows):
    # 각 행의 td 요소들 가져오기
    columns = row.find_elements(By.TAG_NAME, 'td')
    row_data = {
        'data': [col.text for col in columns]  # td의 텍스트를 배열로 저장
    }

    # 세부 정보를 클릭하기 위한 td 요소 찾기
    clickable_element = row.find_element(By.XPATH, f'.//*[@id="disasterSms_tr_{index}_MSG_CN"]')
    clickable_element.click()

    # 세부 정보 가져오기
    detail_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'bbsDetail_0_cdate'))
    )
    row_data['detail_info'] = detail_element.text  # 세부 정보 추가

    # 이전 페이지로 돌아가기
    driver.back()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'tbody')))

    data_array.append(row_data)

# 결과 출력
for item in data_array:
    print(f"{item['data']} - 송출지역: {item.get('detail_info', 'N/A')}")

# 드라이버 종료
driver.quit()
