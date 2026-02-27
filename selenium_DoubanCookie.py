from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json

def save_cookies():
    driver = webdriver.Edge()
    wait = WebDriverWait(driver, 10)
    #webdriver_manager自动打开Edge浏览器，并且自动管理驱动
    driver.get("https://accounts.douban.com/passport/login")
    # 等待页面加载，切换到密码登录
    password_tab = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "account-tab-account")))
    password_tab.click()
    # 输入账号密码
    account_input = wait.until(EC.presence_of_element_located((By.ID, "username")))
    account_input.send_keys("账号替换")
    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys('密码替换')
    # 点击登录按钮
    Login_btn = driver.find_element(By.LINK_TEXT,'登录豆瓣')
    Login_btn.click()
    #处理验证码
    try :
        slider = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "tcaptcha-transform")))
        print("滑块出现了，请在10秒内手动拖动...")
        time.sleep(10)
    except:
        print("没有滑块验证，直接登录成功")
    # 等待登录成功，跳转到豆瓣首页
    wait.until(EC.presence_of_element_located((By.LINK_TEXT,'我的豆瓣')))
    print(f"✅ 登录成功！当前URL: {driver.current_url}")
    # 获取Cookie
    cookies_list = driver.get_cookies()
    print(f"获取到 {len(cookies_list)} 个Cookie")
    # 将Cookie写入JSON文件
    with open('douban_edge_cookies.json', 'w', encoding='utf-8') as f:
        json.dump(cookies_list, f, ensure_ascii=False, indent=2)
    print("✅ Cookie已保存到 douban_edge_cookies.json")

if __name__ == "__main__":
    save_cookies()





