
#------------------------------------#
#            --- ---- ---            #
#       Instagram Scraping Bot       #
#            --- ---- ---            #
#------------------------------------#

import argparse
import random
import sys
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# User information
CHROMEDRIVER_PATH = r"C:\path\to\chromedriver.exe"
USERNAME = "hello.world"
PASSWORD = "YOUR_INSTAGRAM_PASSWORD"
HASHTAG = "#yourhashtaghere"            # Example: "#likeforlike"
TARGET_ACCOUNT_NAME = "ccreyes"         # Example: "cristiano"
NUMBER_OF_FOLLOWS = 50
NUMBER_OF_LIKES = 250

# Bot mode constants
LIKE_AND_COMMENT = 0
LIKE = 1
FOLLOW = 2

# Create a list to be filled with random comments
comment_list = []
comment_list.append("Fantastic photo. Keep it up! :)")
comment_list.append("Great shot")
comment_list.append("Nice!!! :)")
comment_list.append("I like your page!")
comment_list.append("great stuff")

#------------------------------------------------------------------------------#

def parseArgs():
    action = None
    if follow is not None and comment is not None:
        print("Invalid argument list <cannot have 'comment' mode with 'follow' mode on>")
        sys.exit(return_code)
    elif follow is not None and like is not None:
        print("Invalid argument list <cannot have 'follow' mode with 'like' mode on>")
        sys.exit(return_code)
    elif like and comment:
        action = LIKE_AND_COMMENT
    elif like:
        action = LIKE
    elif follow:
        action = FOLLOW
    else:
        print("Invalid argument selection")
        sys.exit(return_code)
    return action

#------------------------------------------------------------------------------#

def login(driver):
    print("Beginning login with credentials: [{}] [{}]".format(USERNAME, PASSWORD))
    driver.find_element_by_xpath("//input[@name='username']").send_keys(USERNAME)
    driver.find_element_by_xpath("//input[@name='password']").send_keys(PASSWORD)
    driver.find_element_by_xpath("//button[contains(.,'Log in')]").click()
    print("Login was successful")
    sleep(10)

#------------------------------------------------------------------------------#

def buildDriver():
    driver = webdriver.Chrome(CHROMEDRIVER_PATH)
    driver.implicitly_wait(15)
    driver.get("https://www.instagram.com")
    sleep(5)
    return driver

#------------------------------------------------------------------------------#

def performLikeAndComment(driver):
    driver.find_element_by_xpath("//input[@type='text' and @placeholder='Search']").send_keys(HASHTAG)

    # Generates a random comment from list in beginning of file
    random_number = random.randint(0, len(comment_list))
    comment_section = driver.find_element_by_css_selector('textarea')
    comment_section.click()
    print(random_number)
    comment_section.send_keys(comment_list[random_number])
    return None

#------------------------------------------------------------------------------#

def performLike(driver):

    # Accesses first post that comes up on the feed
    browser.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div').click()

    # Proceeds to second post to begin liking pics to avoid complications
    x = 0
    while x < 2:
        try:
            browser.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/div/a').click()
        except:
            continue
        x += 1

    number_of_likes = 0
    while like_number > 0:

        # Attempts to comment under a picture
        if commenting == "on":
            sleep(1)
            Comment(browser, comment_list)

        # Attempts to like a picture
        try:
            browser.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/article/div[2]/section[1]/a[1]').click()
        except:
            print("Possible problem encountered while trying to reach like button...")

        # Attempts to scroll to the next account
        try:
            browser.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/div/a[2]').click()
            sleep(1)
        except:
            print("Issue encountered while scrolling to next image...")
        number_of_likes += 1
        like_number -= 1

    print(number_of_likes, 'picture(s) were liked.')
    return None


#------------------------------------------------------------------------------#

def performFollow(driver):
    # Sequence of code reaches account and goes to following list
    search = browser.find_element_by_xpath("//input[@placeholder='Search']")
    search.send_keys(famous_account_name)
    browser.find_element_by_xpath('//*[@id="react-root"]/section/main/article/header/section/ul/li[2]/a').click()

    # Follow every account and add the account url's to a list for unfollowing
    following_list_urls = []
    num_followed = 0

    while (num_followed < number_of_follows):
        username = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/article/header/section/div[1]/h1')
        url = 'https://www.instagram.com/{0}/'.format(username)
        following_list.append(url)
        num_followed += 1
    return None

#------------------------------------------------------------------------------#

def perform(driver, action):
    login(driver)
    search_value = HASHTAG if action == LIKE or action == LIKE_AND_COMMENT else TARGET_ACCOUNT_NAME
    search = driver.find_element_by_xpath("//input[@placeholder='Search']")
    search.send_keys(search_value, Keys.DOWN, Keys.ENTER)
    print("Finished search for {}".format(search_value))
    if action == LIKE_AND_COMMENT:
        print("Beginning LIKE AND COMMENT mode")
        performLikeAndComment()
    elif action == LIKE:
        print("Beginning LIKE mode")
        performLike()
    else:
        print("Beginning FOLLOW mode")
        performFollow()
    return 0

#------------------------------------------------------------------------------#

if __name__ == "__main__":
    return_code = -1

    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--follow",   help="have bot follow users following {}".format(TARGET_ACCOUNT_NAME),  default=None)
    parser.add_argument("-l", "--like",     help="have bot like posts under #{}".format(HASHTAG),                   default=None)
    parser.add_argument("-c", "--comment",  help="optional argument used with like mode",                           default=None)
    parser.add_argument("--debug", help="print webdriver.page_source after selenium failure",                       default=None)
    args = parser.parse_args()
    follow = getattr(args, "follow")
    like = getattr(args, "like")
    comment = getattr(args, "comment")
    print("Follow\t\t[{}]\nLike\t\t[{}]\nComment\t\t[{}]".format(follow, like, comment))

    try:
        action = parseArgs()
        driver = buildDriver()
        return_code = perform(driver, action)
    except Exception as e:
        print("An exception occurred: {}".format(e))
        if args.debug:
            print(driver.page_source)
    finally:
        if driver:
            driver.quit()
            print("Safely closed chromedriver")
    print("Completed")
    sys.exit(return_code)
