from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os.path
import re

chrome_options = Options()
chrome_options.add_argument("--headless")
d = webdriver.Chrome(chrome_options=chrome_options)

lacras = 'https://www1.lacras-io.jp/'
kyuyo_page = 'secret'
bonus_page = 'secret'
company_id = 'secret'
user_id = 'secret'
password = 'secret'

kyuyo_data_dir = 'kyuyo_data'
bonus_data_dir = 'bonus_data'

if not os.path.isdir(kyuyo_data_dir):
    os.mkdir(kyuyo_data_dir)

if not os.path.isdir(bonus_data_dir):
    os.mkdir(bonus_data_dir)

d.get(lacras)
time.sleep(2)
d.find_element_by_name("loginCompany").send_keys(company_id)
d.find_element_by_name("LoginName").send_keys(user_id)
d.find_element_by_name("Passwd").send_keys(password)
d.find_element_by_id("Login").click()
iframe = d.find_element_by_id("header")
time.sleep(2)
d.switch_to_frame(iframe)
time.sleep(1)
d.get(kyuyo_page)
time.sleep(2)
os.chdir(kyuyo_data_dir)
for i in d.find_elements_by_tag_name('a'):
    m = re.match(r'[0-9]{4}/[0-9]{2}/[0-9]{1,2}', i.text)
    if m:
        fname = re.sub(r'/', '-', i.text) + '.html'
        i.click()
        print('Creating ' + fname + '...')
        time.sleep(2)
        d.switch_to_window(d.window_handles[-1])
        time.sleep(1)
        with open(fname, 'w') as f:
            f.write(str(d.page_source))
        d.close()
        time.sleep(1)
        d.switch_to_window(d.window_handles[0])
        time.sleep(1)

os.chdir('../' + bonus_data_dir)
d.get(bonus_page)
time.sleep(2)
for i in d.find_elements_by_tag_name('a'):
    m = re.match(r'[0-9]{4}/[0-9]{2}/[0-9]{1,2}', i.text)
    if m:
        fname = re.sub(r'/', '-', i.text) + '.html'
        i.click()
        print('Creating ' + fname + '...')
        time.sleep(2)
        d.switch_to_window(d.window_handles[-1])
        time.sleep(1)
        with open(fname, 'w') as f:
            f.write(str(d.page_source))
        d.close()
        time.sleep(1)
        d.switch_to_window(d.window_handles[0])
        time.sleep(1)
