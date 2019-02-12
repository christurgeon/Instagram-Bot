#------------------------------------#
#            --- ---- ---            #
#       Instagram Scraping Bot       #
#            --- ---- ---            #
#------------------------------------#

# User information
username = "YOUR_INSTAGRAM_USERNAME"
password = "YOUR_INSTAGRAM_PASSWORD"
popular_hashtag = "#SOME_HASHTAG"       #Example: '#likeforlike'
famous_account_name = "SOME_USERNAME"   #Example: 'cristiano'
number_of_follows = 50
like_number = 250

# Make mode(s) equal to "on" for bot to activate given mode
# DISCLAIMER: only one mode can be activated at a time...
like_mode = "on"
follow_mode = "off"
comment_mode ="off"

# Create a list to be filled with random comments
comment_list = []
comment_list.append("Fantastic photo. Keep it up! :)")
comment_list.append("Great shot")
comment_list.append("Nice!!! :)")
comment_list.append("I like your page!")
comment_list.append("great stuff")


#------------------------------------------------------------------------------#
#                  DO NOT EDIT ANYTHING BELOW THIS STATEMENT!                  #
#------------------------------------------------------------------------------#

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random

#------------------------------------------------------------------------------#

def FollowBasedOnUsername(browser, famous_account_name, number_of_follows):

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

def FollowBasedOnHashtag(browser, hashtag, number_of_follows):

    # Creates list to hold usernames
    following_list = []

    # Sequence of code to reach hashtag
    search = browser.find_element_by_xpath("//input[@placeholder='Search']")
    search.send_keys(hashtag)
    sleep(2)
    search.send_keys(Keys.DOWN, Keys.ENTER)
    sleep(2)

    browser.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/article/header/div[2]/div[1]/div[2]/span[2]/button').click()
    username = browser.find_element_by_xpath()
    following_list.append()
    return None

#------------------------------------------------------------------------------#

def Comment(browser, comment_list):

    # Generates a random comment from list in beginning of file
    random_number = random.randint(0, len(comment_list))
    comment_section = browser.find_element_by_css_selector('textarea')
    comment_section.click()
    print(random_number)
    comment_section.send_keys(comment_list[random_number])

    ##url = "%smedia/%s/comments" % (base_url, media_id)
    """
    all_forms = browser.find_elements_by_tag_name('form')
    print(len(all_forms))
    for form in all_forms:
        try:
            browser.send_keys(comment_list[random_number])
        except:
            print('Failed to send comment. Trying again...')
    """
    #browser.send_keys(Keys.ENTER)
    return None

#------------------------------------------------------------------------------#

def LikeBasedOnHashtag(browser, like_number, commenting, comment_list):

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


# Navigates to Instagram
browser = webdriver.Chrome('C:/Users/turgec/OneDrive/Projects/chromedriver.exe')
browser.get('https://www.instagram.com')
sleep(1)


# Goes to login page
login_elem = browser.find_element_by_xpath('//article/div/div/p/a[text()="Log in"]')
login_elem.click()


# Inputs username and password into login and logs onto account
browser.find_element_by_xpath('//input[@name="username"]').send_keys(username)
browser.find_element_by_xpath('//input[@name="password"]').send_keys(password)
browser.find_element_by_xpath("//button[contains(.,'Log in')]").click()
print("\nLogin to @", username, '\'s account was successful.', sep='')
sleep(2)


# Enters popular hashtag in searchbar and hits enter, scrolls down to hit enter
search = browser.find_element_by_xpath("//input[@placeholder='Search']")
search.send_keys(popular_hashtag)
sleep(2)
search.send_keys(Keys.DOWN, Keys.ENTER)
print('Program reached hashtag page.\n')
sleep(2)

# Function calls determined from user input at beginning of file
if like_mode == "on" and comment_mode == "off":
    LikeBasedOnHashtag(browser, like_number, "off", comment_list)
elif (like_mode and comment_mode) == "on":
    LikeBasedOnHashtag(browser, like_number, "on", comment_list)
elif follow_mode == "on" and ((like_mode and comment_mode) == "off"):
    FollowBasedOnUsername(browser, famous_account_name, number_of_follows)
else:
    print("No mode specified.")

# Clean exit for driver
##browser.close()
print('\n|' + "-" * 42 + '|')
print("| Browser window closed. Program complete! |")
print('|' + "-" * 42 + '|')
