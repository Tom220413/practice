from selenium import webdriver

def check():
    try:
        print('checkstart')
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        # Selenium Gridのハブに接続
        with webdriver.Remote(
            # command_executor="http://localhost:4444/",
            command_executor="http://selenium-hub:4444/wd/hub",
            options=chrome_options
        ) as driver:
            # ウェブサイトを開く
            driver.get("https://www.google.co.jp/")
            print(driver.current_url)

        print('checkend')
    except Exception as e:
        print(e)

print('--------')
check()
print('--------')

