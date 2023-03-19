from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from chatgpt import generate_text
import time


def login_douyin():
    driver = webdriver.Chrome() # 定义一个驱动 <路径地址>
    driver.get("https://www.douyin.com")
    wait = WebDriverWait(driver, 10) 
    time.sleep(3)

    #  切换到手机号+密码登陆
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="web-login-container"]/article/article/article/div[1]/ul[1]/li[3]'))).click()
    # 输入账号和密码
    phone_num_pos = driver.find_element(By.XPATH, '//*[@id="web-login-container"]/article/article/article/form/div[1]/div/input')
    phone_num_pos.send_keys('18915732397')
    time.sleep(1)
    pass_word_pos = driver.find_element(By.XPATH, '//*[@id="web-login-container"]/article/article/article/form/div[2]/div/div/input')
    pass_word_pos.send_keys('qwertyuiop123')
    
    # 登录
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="web-login-container"]/article/article/article/form/div[5]/button'))).click()
    time.sleep(20)  # 请在20秒内完整验证码输入工作
    return driver

# 爬取一条评论
def get_one_element(i, driver):
    try:
        comment = driver.find_element(By.XPATH, '//*[@id="douyin-right-container"]/div[2]/div/div[1]/div[5]/div/div/div[3]/div[' + str(i) + ']/div/div[2]/div/p/span/span/span/span/span/span/span')
    except:
        return None
        
    driver.execute_script('window.scrollBy(0, 100)') # 下滑100个像素
    return comment

# 回复
def click_one_resp(i, comment, driver):
    wait = WebDriverWait(driver, 10) 
    # 点击回复按钮
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="douyin-right-container"]/div[2]/div/div[1]/div[5]/div/div/div[3]/div[' + str(i) + ']/div/div[2]/div/div[3]/div/div[3]/div/span'))).click()
    time.sleep(3)
    # 输入框    
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="douyin-right-container"]/div[2]/div/div[1]/div[5]/div/div/div[3]/div[' + str(i) + ']/div/div[2]/div/div[3]/div/div[3]/div/span')))
    time.sleep(3)
    # 根据留言，去搞到回复
    print("评论:" + comment)
    try:
        resp = generate_text(str(comment) + "，用中文回答")
        if len(resp) > 90: # 限制回复长度
            resp = resp[:90]
        print("回答:" + resp)
    except:
        print('<-- 生成回复失败 -->')
        return
    time.sleep(2)

    if (len(resp) > 3):
        driver.switch_to.active_element.send_keys(resp)
        time.sleep(2)
        # 点击发送按钮
        try:
            try:
                wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="douyin-right-container"]/div[2]/div/div[1]/div[5]/div/div/div[3]/div[' + str(i) + ']/div/div[2]/div[1]/div[3]/div[2]/div/div/div[2]/div/span[3]'))).click()
            except:
                driver.execute_script('window.scrollBy(0, 150)') # 下滑150个像素
                try:
                    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="douyin-right-container"]/div[2]/div/div[1]/div[5]/div/div/div[3]/div[' + str(i) + ']/div/div[2]/div[1]/div[3]/div[2]/div/div/div[2]/div/span[3]'))).click()
                except:
                    driver.execute_script('window.scrollBy(0, 150)') # 下滑150个像素
                    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="douyin-right-container"]/div[2]/div/div[1]/div[5]/div/div/div[3]/div[' + str(i) + ']/div/div[2]/div[1]/div[3]/div[2]/div/div/div[2]/div/span[3]'))).click()
            time.sleep(2)
            print("<-- 评论成功！ -->")
        except:
            print("<-- 评论失败！ -->")

def check_string(comment):
    with open('123.txt', encoding="utf-8") as temp_f:
        datafile = temp_f.readlines()
    for line in datafile:
        if comment in line:
            return True # The string is found
    return False  # The string does not exist in the file


