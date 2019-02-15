from selenium import webdriver
import time
from selenium.webdriver import ActionChains
import requests

driver = webdriver.Chrome()

# 请求目标网站的网址
driver.get('https://sycm.taobao.com/custom/login.htm?_target=http://sycm.taobao.com/')
time.sleep(0.1)

# 页面有iframe 需要切换至iframe  但是iframe没有id和name属性  需要先通过标签名找到iframe  然后再切换
iframe = driver.find_elements_by_tag_name("iframe")[0]

# 切换至iframe
driver.switch_to.frame(iframe)

# 输入用户名和密码
driver.find_element_by_id('TPL_username_1').send_keys('xxxx')
driver.find_element_by_id('TPL_password_1').send_keys('xxxx')

# 滑动验证码
action = ActionChains(driver)
source = driver.find_element_by_xpath("//span[@id='nc_1_n1z']")  # 找到滑动的按钮
print("找到滑动的按钮")

action.click_and_hold(source).perform()  # 鼠标左键按下不放
print("鼠标左键按下不放")

action.move_by_offset(206, 0)  # 需要滑动的坐标
print("需要滑动的坐标")

action.release().perform()  # 释放鼠标
print("释放鼠标")
time.sleep(0.1)

driver.find_element_by_id('J_SubmitStatic').submit()
print("点击登陆")

time.sleep(10)
driver.quit()