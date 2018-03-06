import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from requests_html import HTMLSession
from selenium import webdriver
#from  pyvirtualdisplay import Display
import os

chromedriver = "/home/xu/Desktop/flask2/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
#display = Display(visible=0, size=(1600,600))
#display.start()
driver1 = webdriver.Chrome(chromedriver,port = 9515)

driver1.maximize_window()
URL = "https://www.lagou.com/jobs/list_%E6%95%B0%E6%8D%AE%E6%8C%96%E6%8E%98?px=default&city=%E5%85%A8%E5%9B%BD#filterBox"
driver1.get(URL)
# f = open('search_data.log','a')
# last_flag_id = ""
# while True:
#     #content_list = driver1.find_elements_by_class_name('c-container')
#     #WebDriverWait(driver1, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'c-container')))
#     while True:
#         content_list = driver1.find_elements_by_class_name('c-container')
#         curr_flag_id = content_list[0].id
#         if curr_flag_id != last_flag_id:
#             last_flag_id = curr_flag_id
#             break
#         else:
#             time.sleep(1)
    
#     for x in content_list:
#         x1 = x.find_element_by_class_name('t')
#         x2 = x1.find_element_by_tag_name('a')
#         link = x2.get_attribute('href')
#         text = x2.text
#         print(text)
#         Q.put(link)
    

#     driver1.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     #pages = driver1.find_element_by_id("page").find_elements_by_tag_name('a')
#     page = WebDriverWait(driver1, 10).until(EC.presence_of_element_located((By.ID, 'page')))
#     page_num = page.find_element_by_tag_name('strong').text
#     print("-------------------------",page_num,"-------------------------",file=f)
#     pages = page.find_elements_by_tag_name('a')
#     nextpage = [p for p in pages if p.text == '下一页>']
    
#     if nextpage:
#         print(page_num,nextpage[0].id)
#         nextpage[0].click()
#     else:
#         break
# f.close()

# from queue import Queue

# import threading

# class BaseThread(threading.Thread):  # 继承父类threading.Thread
#     def __init__(self,Q,name):
#         threading.Thread.__init__(self)
#         self.Q = Q
#         self.name = name
#         self.session = HTMLSession()
#     def run(self):
#         while True:
#             url = Q.get()
#             if url is not None:
#                 self.get_content(url)
#             else:
                
#                 print('done!!!')
#                 break
#     def get_content(self,url):
#         r = self.session.get(url)
#         print(r.html.find('title')[0].text,self.name)
        


# Q = Queue(30)
# threads_list = []
# for i in range(10):
#     th = BaseThread(Q,'thread_'+str(i))
#     threads_list.append(th)

# for t in threads_list:
#     t.start()