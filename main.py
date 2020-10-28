
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import timeit,time
from datetime import datetime

def isLoadedByXpath(driver,xpath):
    try:
        driver.find_element_by_xpath(xpath)
        return True
    except:
        return False
def deleteByXpath(driver,xpath):
    try:
        delelement = driver.find_element_by_xpath(xpath)
        driver.execute_script("""var element = arguments[0]; element.parentNode.removeChild(element); """, delelement)
    except:
        pass
def get_screen_shot(driver,url):
    driver.get(url)

    inputElement = driver.find_element_by_xpath('//*[@id="__next"]/div/div/div/div/div[1]/section/form/div/div/input')
    inputElement.send_keys(text_for_wolfram_alpha)
    inputElement.send_keys(Keys.ENTER)

    # while (isLoadedByXpath('//*[@id="__next"]/div/div/main/div[2]/div/div/section/header/h2'))==False:
    #   pass
    # driver.save_screenshot("sc_"+str(count)+".png")
    while (
    isLoadedByXpath(driver,'//*[@id="__next"]/div/div/main/div[2]/div/div/div[1]/section/div')) != True and isLoadedByXpath(
            driver,'//*[@id="__next"]/div/div/main/div[2]/div/div/section') != True:
        pass
    time.sleep(12)
    deleteByXpath(driver,'//*[@id="__next"]/div/div/main/div[2]/div/div/div[1]/section/div/div')
    deleteByXpath(driver,'//*[@id="__next"]/div/div/main/div[2]/div/div/section')
    deleteByXpath(driver,'//*[@id="__next"]/div/div/main/div[2]/div/div/div[2]')
    deleteByXpath(driver, '//*[@id="__next"]/div/footer')
    deleteByXpath(driver, '//*[@id="__next"]/div/section')
    # the element with longest height on page
    ele = driver.find_element("xpath", '//*[@id="__next"]/div/div/main')
    total_height = ele.size["height"]+300
    driver.set_window_size(800, total_height)  # the trick
    if driver.find_elements_by_xpath('//*[@id="__next"]/div/div/div/div/img')!=[] or driver.find_elements_by_xpath("//*[contains(text(), 'Try another server')]")!=[]:
        driver.back()
        time.sleep(5)
    if driver.find_elements_by_xpath('//*[@id="__next"]/div/div/div/div/img')!=[] or driver.find_elements_by_xpath("//*[contains(text(), 'Try another server')]")!=[]:
        raise
    driver.save_screenshot("sc_"+str(count)+".png")
    driver.close()

count=1
text_for_wolfram_alpha="integral of tanx/(tanx^2 +1)"


while(True):
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--test-type")
    options.add_argument("--headless")
    options.add_argument("--hide-scrollbars")
    options.add_argument("--disable-web-security")
    driver = webdriver.Chrome(chrome_options=options)
    try:
        s=datetime.now().second
        m = datetime.now().minute
        h=datetime.now().hour
        count=m*60+s
        get_screen_shot(driver,'https://www.wolframalpha.com')
        break
    except:
        driver.close()
        pass

