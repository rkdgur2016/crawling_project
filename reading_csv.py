import pandas as pd

address_code_csv = pd.read_csv('C:/web_study/vscode_workspace/crowling_study/국토교통부_법정동코드_20240805.csv', encoding="ANSI")
crawling_data_csv = pd.read_csv('C:/web_study/vscode_workspace/crowling_study/크롤링 데이터 인덱싱 O.csv', encoding="ANSI" )

print(address_code_csv)
print(crawling_data_csv)

address_code_arr = []
for address_code in address_code_csv['법정동코드']:
    address_code_arr.append(address_code)
    print(address_code_arr)
    
crawling_data_arr = []
for crawling_data in crawling_data_csv['send_place']:
    crawling_data_arr.append(crawling_data)
    print(crawling_data_arr)

