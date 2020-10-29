from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time,sys,random



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
        return delelement.size["height"]
    except:
        return 0
def search(driver, url,text_for_wolfram_alpha,image_name):
    driver.get(url)

    inputElement = driver.find_element_by_xpath('//*[@id="__next"]/div/div/div/div/div[1]/section/form/div/div/input')
    inputElement.send_keys(text_for_wolfram_alpha)
    inputElement.send_keys(Keys.ENTER)

    while (isLoadedByXpath(driver,'//*[@id="__next"]/div/div/main/div[2]/div/div/section/header')) != \
            True and isLoadedByXpath(driver,'//*[@id="__next"]/div/div/main/div[2]/div/div/section') != True:
        pass
    time.sleep(15) # the time you give the search engine to load
    size=0
    size+=deleteByXpath(driver, '//*[@id="__next"]/div/div/main/a')
    size+=deleteByXpath(driver, '//*[@id="__next"]/div/header')
    size+=deleteByXpath(driver,'//*[@id="__next"]/div/div/main/div[2]/div/div/div[1]/section/div/div')
    size+=deleteByXpath(driver,'//*[@id="__next"]/div/div/main/div[2]/div/div/section')
    size+=deleteByXpath(driver,'//*[@id="__next"]/div/div/main/div[2]/div/div/div[2]')
    size+=deleteByXpath(driver, '//*[@id="__next"]/div/footer')
    size+=deleteByXpath(driver, '//*[@id="__next"]/div/section')
    time.sleep(1)
    # the element with longest height on page
    ele = driver.find_element("xpath", '//*[@id="__next"]/div/div/main')
    total_height = min(ele.size["height"]-size,2160) # You can change the default max height which is 2160
    #If you want to get the whole page use total_height=ele.size["height"]-size instead
    driver.set_window_size(1280,total_height)  # the trick
    
    #Site Error handling
    if driver.find_elements_by_xpath('//*[@id="__next"]/div/div/div/div/img')!=[] or driver.find_elements_by_xpath("//*[contains(text(), 'Try another server')]")!=[]:
        driver.back()
        time.sleep(5)
    if driver.find_elements_by_xpath('//*[@id="__next"]/div/div/div/div/img')!=[] or driver.find_elements_by_xpath("//*[contains(text(), 'Try another server')]")!=[]:
        raise
        
    driver.save_screenshot(image_name)
    driver.close()



def create_wolf_screen_shot(text_for_wolfram_alpha,image_name):
    tries=0
    while(tries<3):
        options = webdriver.ChromeOptions() #you can add the path here if its not in the same folder as the script
        options.add_argument('--ignore-certificate-errors')
        options.add_argument("--test-type")
        options.add_argument("--headless")
        options.add_experimental_option('excludeSwitches', ['enable-logging']) # disable printing
        options.add_argument("--hide-scrollbars")
        options.add_argument("--disable-web-security")
        driver = webdriver.Chrome(options=options)
        try:
            search(driver, 'https://www.wolframalpha.com',text_for_wolfram_alpha,image_name)
            break
        except:
            tries+=1
            driver.close()
            return False
            pass
    return True

def gen_image_name():
    return "wolf_sc_"+str(random.randint(10,1000))+".png"


if __name__ == '__main__':
    imag_name=gen_image_name()
    wolf_text=" ".join(sys.argv[1:])
    print("strat scraping you image will be save as "+imag_name)
    create_wolf_screen_shot(wolf_text,imag_name)
    exit()

