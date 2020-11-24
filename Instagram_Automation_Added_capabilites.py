#Backend Starts here

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from datetime import datetime
import os.path
import csv
from datetime import date
from pylab import *


""" open('insta.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Date", "Followers","Followers change","Likes Change","Comments Change"])
    writer.writerow(["1 Feb 2019","120","0","10","4"])
    writer.writerow(["2 Feb 2019","125","5", "20", "6"])
    writer.writerow(["3 Feb 2019","130","5", "20", "2"])
    writer.writerow(["4 Feb 2019","110","-20", "30", "8"])
    writer.writerow(["5 Feb 2019","90", "-20", "10", "21"])
"""

# "Followers change","Likes Change","Comments Change"

driver = webdriver.Chrome("D:/chromedriver.exe")


def starting():
    driver.implicitly_wait(30)
    driver.maximize_window()
    driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
    driver.refresh()
    username = driver.find_element_by_xpath("//input[@name='username']")
    password = driver.find_element_by_xpath("//input[@name='password']")
    username.send_keys("your_username")
    password.send_keys("your_password")
    login_btn = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button')
    login_btn.click()
    time.sleep(5)
    driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]').click()


followers = []


def liking_a_post(link):
    driver.get(link)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[2]/section[1]/span[1]/button').click()


def home_page():
    hf = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[1]/a/div/div[2]/img')
    hf.click()


def search_a_user(insta_id):
    home_page()
    search = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
    search.send_keys(insta_id)
    de = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]/div')
    de.click()


def log_out(user_name):
    driver.get("https://www.instagram.com/" + user_name)
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div/button/span').click()
    driver.find_element_by_xpath("/html/body/div[4]/div/div/div/button[9]").click()


def follower_count(user_name):
    driver.get("https://www.instagram.com/" + user_name)
    time.sleep(5)
    fw = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').text
    return fw
    #followers.append(fw)
    #file_save(user_name, fw)


def file_save(user_name, fw):
    if os.path.isfile(user_name + '.csv'):
        with open(user_name + '.csv', 'w') as csvfile:
            fr = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
            d1 = date.today()
            d1 = d1.strftime("%B %d, %Y")
            fr.writerow([user_name, d1, fw])
    else:
        with open(user_name + '.csv', 'w') as csvfile:
            fr = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
            fr.writerow(['UserName', 'Date', 'Follower\'s count'])


def line_graph(user_name):
    t = arange(0.0, 20.0, 1)
    s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    plot(t, s)
    xlabel('Date (s)')
    ylabel('Follower\'s count')
    title('Follower Data :' + user_name)
    grid(True)
    show()


def follow(insta_id):
    search_a_user(insta_id)
    fl = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/span/span[1]/button')
    if fl.text == 'Follow':
        fl.click()
    time.sleep(2)
    if fl.text == 'Following':
        print("Done,followed.")
    elif fl.text == 'Requested':
        print(fl.text)


def unfollow(insta_id):
    search_a_user(insta_id)
    fl = driver.find_element_by_xpath(
        '//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/span/span[1]/button')
    fl.click()
    time.sleep(2)
    if fl.text == 'Following':
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[1]').click()
    time.sleep(2)
    print(driver.find_element_by_xpath(
        '//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/span/span[1]/button').text)


def collect_pictures(tag, nur):
    search_a_user(tag)
    row = 1
    col = 1
    while nur > 0:
        with open(tag + str(nur) + '.png', 'wb') as file:
            try:
                pat = '//*[@id="react-root"]/section/main/article/div[2]/div/div['+str(row)+']/div['+str(col)+']/a/div'
                file.write(driver.find_element_by_xpath(pat).screenshot_as_png)
                print(pat)
            except:
                nur = nur + 1
        if col < 3:
            col = col + 1
        elif col >= 3:
            col = 1
            row = row + 1
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        nur = nur - 1
        print(nur)


follower_list_who_you_follow = []
follower_list_you_dont_follow = []
you_follow = []


"""def dat():
    month_list = ['blank','Jan','Feb','March','April','May','June','July','August','Oct'
                  'Nov','Dec']
    nw = datetime.now()
    mn = month_list[nw.month]
    yr = nw.year
    dt = nw.day
    print(str(dt) + ' ' + str(mn) + ' ' + str(yr) )
"""



def scroll():
    SCROLL_PAUSE_TIME = 0.5
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height


def followers1():

    """This function is used to count the number of followers of a user
    Here specifically used to calculate followers and following of the main user"""

    fw = follower_count('robin_duhan1')
    fw = fw.split(" ")
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()

    number_of_followers = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span').text
    actions = ActionChains(driver)
    print("Number of Followers are: " + str(number_of_followers))

    number_of_following = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a/span').text
    number_of_following = int(number_of_following)
    print("Number of people you follow: " + str(number_of_following))

    with open('insta.csv', 'w', newline='') as fi:
        wr = csv.writer(fi)
#        wr.writerow([,number_of_followers])

    clickable = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]')
    actions.move_to_element_with_offset(clickable, 10, 5)
    actions.click()
    actions.perform()
    # clicking so that we can scroll down

    for i in range(1,int(number_of_followers)+1):
        ad = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/ul/div/li['+str(i)+']')
        ad = ad.text
        ad = ad.split("\n")
        follower_list_who_you_follow.append(ad[0])
        actions.send_keys(Keys.ARROW_DOWN).perform()

    dck = driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div/div[2]/button')
    dck.click()
    # cross the followers window


    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a').click()
    # open the following window

    time.sleep(2)

    act = ActionChains(driver)

    clik = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]')
    act.move_to_element_with_offset(clik, 10, 5)
    act.click()
    act.perform()
    # CLicking on the following window to scroll down

    for j in range(1,number_of_following+1):
        ad = driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/ul/div/li[' + str(j) + ']')
        ad = ad.text
        ad = ad.split("\n")
        you_follow.append(ad[0])
        act.send_keys(Keys.ARROW_DOWN).perform()

    driver.find_element_by_xpath('/html/body/div[4]/div/div[1]/div/div[2]/button').click()


likes = []


def user_posts(user_name):

    """This finds the number of likes on every photo of a user
    use actions to scroll"""

    driver.get("https://www.instagram.com/" + user_name)
    number_of_posts = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[1]/span').text
    number_of_posts = number_of_posts.split(" ")
    number_of_posts = int(number_of_posts[0])
    rows = 1
    cols = 1
    while number_of_posts > 0:
        with open(user_name + str(number_of_posts) + '.png', 'wb') as file:
            try:
                pat = '//*[@id="react-root"]/section/main/div/div[2]/article/div/div/div['+ str(rows) +']/div['+ str(
                    cols) + ']/a/div'
                driver.find_element_by_xpath(pat).click()
                number_of_likes = driver.find_element_by_xpath(
                    '/html/body/div[4]/div[2]/div/article/div[2]/section[2]/div/div[2]/'
                    'button/span').text
                print(number_of_likes)
                driver.find_element_by_xpath('/html/body/div[4]/button[1]').click()
                file.write(driver.find_element_by_xpath(pat).screenshot_as_png)
                print(pat)
            except:
                pass
        if cols < 3:
            cols = cols + 1
        elif cols >= 3:
            cols = 1
            rows = rows + 1
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        number_of_posts = number_of_posts - 1

comments = []


def comment_scrap():
    driver.get("https://www.instagram.com/chutiyapa_begins_from_here/")
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[3]/article/div[1]/div/div[2]/div[2]/a/div').click()

    sct = ActionChains(driver)
    clickable = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/div[1]/ul')
    sct.move_to_element_with_offset(clickable, 10, 5)
    sct.click()
    sct.perform()
    # CLicking on the following window to scroll down

    sct.send_keys(Keys.ARROW_DOWN).perform()

    t = time.clock()
    print(t)
    driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/div[1]/ul/li/div/button/span').click()
    driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/div[1]/ul/li/div/button/span').click()
    driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/div[1]/ul/li/div/button/span').click()
    driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/div[1]/ul/li/div/button/span').click()

    for i in range(1,30):
        te = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/div[1]/ul/ul['+str(i)+']'
                                          '/div/li/div/div[1]/div[2]/span')
        print(te.text)

    s = time.clock()
    print(s)

def open_insta():
    starting()
    home_page()
