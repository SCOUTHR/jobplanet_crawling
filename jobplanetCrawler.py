import csv
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def crawlApage():
    driver.implicitly_wait(1)
    aside = driver.find_elements_by_css_selector('#job_search_app > div > div.job_search_content > div.job_search_detail > div.job_wrap_new.company_job_details > div > div.wrap > div.job_aside > div')
    company = driver.find_element_by_css_selector('#job_search_app > div > div.job_search_content > div.job_search_detail > div.job_wrap_new.company_job_details > div > div.job_apply_section > div > div > div.lft > div > div > div > span.company_name')
    info = [company.text,'','','','']

    for i in aside:
        elems = i.text.split('\n')

    for idx, el in enumerate(elems):
        # print(el)
        if el == '담당자':
            info[1] = elems[idx+1]
        elif el == '연락처':
            info[2] = elems[idx+1]
        elif el == '이메일':
            info[3] = elems[idx+1]
        elif el == '회사위치' :
            info[4] = elems[idx+1]
    # print(info)
    w.writerow(info)


driver = webdriver.Chrome(executable_path = r"C:/Users/SCOUT/Downloads/chromedriver_win32/chromedriver.exe")

URL = 'https://www.jobplanet.co.kr/job/search?q=2021+%EC%9A%94%EA%B8%B0%EC%9A%94+%EC%8B%A0%EC%9E%85+%EA%B0%9C%EB%B0%9C%EC%9E%90+%EC%B1%84%EC%9A%A9+%28Rookie+Hero+4%EA%B8%B0%29&posting_ids%5B%5D=1194719&_rs_con=job&_rs_act=popularity_job_postings&_rs_element=job_home_index'
filename = 'test'
collist = ["회사명","담당자","연락처","이메일","회사위치"]
size = 100 # 열 개 단위로 설정


with open(filename+'.csv','w',-1,newline='',encoding='utf-8-sig') as f:
    w = csv.writer(f)
    w.writerow(collist)
    driver.get(URL)

    for p in range((size//10)+1):
        for c in range(1,10):
            crawlApage()
            nextCompany = WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#job_search_app > div > div.job_search_content > div.job_search_list > div.list > ul > li:nth-child(%d)" %(c+1))))
            try:
                nextCompany.click()
            except:
                time.sleep(2)
                nextCompany.click()
        if p in (0,1,2):
            nextPage = WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#job_search_app > div > div.job_search_content > div.job_search_list > div.jply_pagination_ty1 > button:nth-child(%d)' %(p+2))))
        else :
            nextPage = WebDriverWait(driver, 100).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#job_search_app > div > div.job_search_content > div.job_search_list > div.jply_pagination_ty1 > button:nth-child(6)')))
        try:
            nextPage.click()
        except:
            time.sleep(2)
            nextPage.click()
        # nextPage.send_keys(Keys.ENTER)
