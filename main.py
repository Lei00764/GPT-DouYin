from douyin import login_douyin, get_one_element, check_string, click_one_resp
import time

if __name__ == '__main__':
    video_id = "7211018111678549304"
    debug = False
    driver = login_douyin()
    script = "window.open('https://www.douyin.com/video/" + video_id + "')"
    driver.execute_script(script)
    wins = driver.window_handles
    driver.switch_to.window(wins[-1])

    print("<-- 开始评论 -->")
    print('\n')
    fp = open("123.txt", 'a+', encoding="utf-8") # a+ 读写（追加）
    for i in range(1, 31):
        comment = get_one_element(i, driver)
        if comment != None:
            if not check_string(comment.text): # 不存在
                fp.write(comment.text + '\n')
                click_one_resp(i, comment.text, driver)
            else:
                print("<-- 已经回复过该评论 -->")
            time.sleep(3)
        else:
            print("comment: None")
        print('\n')
    fp.close()