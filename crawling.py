import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import pandas as pd


# 크롬 드라이버 생성
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://www.safekorea.go.kr/idsiSFK/neo/sfk/cs/sfc/dis/disasterMsgList.jsp?menuSeq=679")
print("페이지 로딩")

# 기존의 fn_search 함수를 빈 함수로 대체
if driver.execute_script("return typeof fn_search !== 'undefined';"):
    print("기존 fn_search 함수를 빈 함수로 대체합니다.")

# fn_search 함수에 새로운 로직 추가
driver.execute_script("""
fn_search = function() {
    // 비교할 날짜 (예: 사용자가 입력한 날짜)
    var valid_st_date = moment(datepicker1.getValue(), "YYYY-MM-DD", true).isValid();
    var valid_ed_date = moment(datepicker2.getValue(), "YYYY-MM-DD", true).isValid();

    if (!valid_st_date) {
        alert('시작일이 날짜형식(년-월-일)에 맞지 않습니다.');
        $('#datepicker1').focus();
        return false;
    }

    if (!valid_ed_date) {
        alert('종료일이 날짜형식(년-월-일)에 맞지 않습니다.');
        $('#datepicker2').focus();
        return false;
    }

    var startDate = moment(datepicker1.getValue());
    var endDate = moment(datepicker2.getValue());

    if (endDate.isBefore(startDate)) {
        alert("종료일이 시작일보다 먼저입니다.");
        $('#datepicker2').focus();
        return false;
    }

    // 재해구분
    disasterSms_searchinfo.set("c_ocrc_type", search_c_ocrc.getValue());
    disasterSms_searchinfo.set("dstr_se_Id", search_dsstr.getValue());

    // 시도, 시군구
    disasterSms_searchinfo.set("sbLawArea1", sbLawArea1.getValue());
    disasterSms_searchinfo.set("sbLawArea2", sbLawArea2.getValue());
    disasterSms_searchinfo.set("sbLawArea3", sbLawArea3.getValue());

    // 검색 날짜
    disasterSms_searchinfo.set("searchBgnDe", datepicker1.getValue());
    disasterSms_searchinfo.set("searchEndDe", datepicker2.getValue());
                      
    // 페이지 세팅 초기화
    disasterSms_searchinfo.set("pageIndex", "1");
    getDisasterSmsList_submission.exec();
}
""")

# fn_search 함수 호출
driver.execute_script("fn_search();")

# 페이지에 존재하는 함수 가져오기 (예: fn_search 함수)
function_name = "fn_search"
js_code = f"return {function_name}.toString();"

try:
    function_code = driver.execute_script(js_code)
    print(f"{function_name} 함수의 코드:")
    print(function_code)
except Exception as e:
    print(f"함수를 가져오는 중 오류 발생: {e}")

# 2. 자바스크립트로 datepicker에 날짜 입력
# 'datepicker1'과 'datepicker2'는 실제 페이지에서 사용하는 날짜 필드의 ID입니다.
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'datepicker1')))
driver.execute_script("document.getElementById('datepicker1').value = '2023-10-01';")
driver.execute_script("document.getElementById('datepicker2').value = '2023-10-07';")

search_btn = driver.find_element(By.CLASS_NAME, 'search_btn')
search_btn.click()

# 데이터 배열
data_array = []

current_page = int(driver.find_element(By.CLASS_NAME, 'nowNum').text) #현재 페이지 번호
print(current_page)

max_page = int(driver.find_element(By.ID, 'tbpagetotal').text.replace("/", ""))
#최대 페이지 번호 : 문자열 "/" 치환 후 => 정수형변환 
print(max_page)

next_button = driver.find_element(By.ID, "apagenext")

while current_page <= max_page:
    time.sleep(3)
    # tbody 안의 모든 tr 요소 가져오기
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.TAG_NAME, 'tbody')))
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
        detail_element = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.ID, 'bbsDetail_0_cdate'))
        )
        row_data['send_place'] = detail_element.text 

        # 이전 페이지로 돌아가기
        driver.back()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'tbody')))

        data_array.append(row_data)

    next_button.click()
    
    current_page += 1

# 결과 출력
for item in data_array:
    print(f"{item['data']} - 송출지역: {item.get('send_place', 'N/A')}")

df = pd.json_normalize(data_array)
df_data_split = pd.DataFrame(df['data'].tolist(), columns=['ID', '유형', '분류', '발신처', '발송시간', '내용'])
# 'send_place'와 병합
df_split = df["send_place"].str.split(",", expand=True)
df_combined = pd.concat([df_data_split, df_split], axis=1)

df_combined.to_csv('indexing_file.csv', index=True, encoding="ANSI")

