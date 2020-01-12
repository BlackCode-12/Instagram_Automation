from selenium import webdriver
import time

driver = webdriver.Chrome("E:/chromedriver.exe")
driver.implicitly_wait(30)
driver.maximize_window()
driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
driver.refresh()

username = driver.find_element_by_xpath("//input[@name='username']")
password = driver.find_element_by_xpath("//input[@name='password']")
username.send_keys("your username")
password.send_keys("your password")


login_btn = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button')
login_btn.click()

time.sleep(5)
driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]').click()


def liking_a_post(link):
    driver.get(link)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[2]/section[1]/span[1]/button').click()


def search_a_user(user_name):
    home_page()
    search = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
    search.send_keys(user_name)
    de = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]/div/div[2]/div/span')
    de.click()


def home_page():
    hf = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[1]/a/div/div[2]/img')
    hf.click()


def log_out(user_name):
    driver.get("https://www.instagram.com/" + user_name)
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div/button/span').click()
    driver.find_element_by_xpath("/html/body/div[4]/div/div/div/button[9]").click()


#examples of the above functions
liking_a_post("https://www.instagram.com/p/B7DR_-XBoVi/?igshid=1aco8unst8hjl")
time.sleep(10)
search_a_user("a user")
time.sleep(10)
home_page()
time.sleep(10)
log_out("your username")

