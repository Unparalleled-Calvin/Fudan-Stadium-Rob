from selenium import webdriver
import re
import numpy as np
import easyocr
import io
from PIL import Image
from PIL import ImageEnhance
import time

class 场地秒杀():
    def __init__(self, username, password, day, timespan, service, chromedrive):
        self.username = username
        self.password = password
        self.day = day
        self.timespan = timespan
        self.service = service
        self.chromedrive = chromedrive
        
        self.browser = webdriver.Chrome(self.chromedrive)

    def visit_elife_page(self):
        self.browser.get('http://elife.fudan.edu.cn')
        input_button = self.browser.find_element_by_id('login_table_div')\
                    .find_element_by_css_selector("div:nth-child(2)")\
                    .find_element_by_tag_name("input")
        input_button.click()

    def login(self):
        username_input = self.browser.find_element_by_id("username")
        password_input = self.browser.find_element_by_id("password")
        login_button = self.browser.find_element_by_id("idcheckloginbtn")

        username_input.send_keys(self.username)
        password_input.send_keys(self.password)
        login_button.click()

    # reference from: https://github.com/ZiYang-xie/Hello_Fudan/blob/main/main.py
    def read_captcha(self, img_byte):
        img = Image.open(io.BytesIO(img_byte)).convert('L')
        enh_bri = ImageEnhance.Brightness(img)
        new_img = enh_bri.enhance(factor=1.5)
        
        image = np.array(new_img)
        reader = easyocr.Reader(['en'])
        horizontal_list, free_list = reader.detect(image, optimal_num_chars=4)
        character = '0123456789'
        allow_list = list(character)
    
        result = reader.recognize(image, 
                                allowlist=allow_list,
                                horizontal_list=horizontal_list[0],
                                free_list=free_list[0],
                                detail = 0)
        return result

    def rob_one_field(self, order_button):
        order_button.click()
        time.sleep(1)
        captcha_line = self.browser.find_elements_by_class_name("txxd_td2-2")[4]
        captcha = captcha_line.find_element_by_tag_name("img")
        captcha_input = captcha_line.find_element_by_tag_name("input")
        captcha = captcha.screenshot_as_png
        captcha = self.read_captcha(captcha)
        if len(captcha) == 0:
            captcha = self.read_captcha(captcha)
        captcha_input.send_keys(captcha)
        submit_button = self.browser.find_element_by_id("btn_sub")
        submit_button.click()

    def rob_one_day(self, day):
        self.browser.get(self.service)
        day = self.browser.find_element_by_id("one" + str(day))
        day.click()
        lines = self.browser.find_elements_by_class_name("site_tr")
        for i in range(len(lines)):
            try:
                line = self.browser.find_elements_by_class_name("site_tr")[i]
                timespan = line.find_element_by_class_name("site_td1").text
                match = re.match("([0-9]+?):00\\n([0-9]+?):00", timespan, flags=0)
                if not match:
                    continue
                start = int(match.groups()[0])
                if start in self.timespan:
                    number_table = line.find_element_by_class_name("site_td4")
                    current_number = int(number_table.find_element_by_tag_name("font").text)
                    max_number = int(number_table.find_element_by_tag_name("span").text)
                    order_button = line.find_element_by_tag_name("img")
                    if current_number < max_number:
                        current_url = self.browser.current_url
                        self.rob_one_field(order_button)
                        self.browser.get(current_url)
            except Exception:
                pass
                
    def 抢(self):
        self.visit_elife_page()
        self.login()
        for day in self.day:
            self.rob_one_day(day)



# 标场的url
standard_badminton_service = "https://elife.fudan.edu.cn/public/front/toResourceFrame.htm?contentId=2c9c486e4f821a19014f82418a900004"
# 非标场的url
nonstandard_badminton_service = "https://elife.fudan.edu.cn/public/front/toResourceFrame.htm?contentId=2c9c486e4f821a19014f86df4f662ba9"

# 国权路网球场
test_service = "https://elife.fudan.edu.cn/public/front/toResourceFrame.htm?contentId=8aecc6ce7d2dffbd017de9ea4e7e4ece"

uid = ""
password = ""
days = [] # 1-7代表周一至周日
timespan = list(range(12,22)) # 12代表12:00-13:00的时间段
service = standard_badminton_service # 实际url
drive_path = "" # chromedrive的地址
秒杀 = 场地秒杀(uid, password, days, timespan, service, drive_path)
秒杀.抢()
