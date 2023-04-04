from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
from collections import Counter


opt = webdriver.ChromeOptions()
opt.binary_location = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
opt.add_experimental_option("excludeSwitches", ['enable-automation'])
chromedriver_exe_location = os.path.join(os.getcwd(), r'chromedriver path')
profile_path = r'chrome profile path'
opt.add_argument('--user-data-dir={}'.format(profile_path))
opt.add_argument('--profile-directory={}'.format('DEFAULT'))
driver = webdriver.Chrome(chromedriver_exe_location, options=opt, service_args='')
bot = "bot_account"
victim = "victim_account"  #must follow with the bot or to be a public profile
driver.get(f'https://www.instagram.com/{victim}/')

time.sleep(3.5)

user_name = driver.find_element(By.XPATH, '/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/section[1]/main[1]/div[1]/header[1]/section[1]/div[1]/h2[1]').text
print("User: " + user_name)

try:
    num_followers = WebDriverWait(driver, 1).until(
        EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/section[1]/main[1]/div[1]/header[1]/section[1]/ul[1]/li[2]/a[1]/div[1]/span[1]/span[1]"))
    )
except:
    try:
        num_followers = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.XPATH,
                                            "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/section[1]/main[1]/div[1]/header[1]/section[1]/ul[1]/li[2]/a[1]/div[1]/span[1]/span[1]"))
        )
    except:
        num_followers = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.XPATH,
                                            "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/section[1]/main[1]/div[1]/header[1]/section[1]/ul[1]/li[2]/a[1]/div[1]/span[1]/span[1]"))
        )

# num_followers = driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/section[1]/main[1]/div[1]/header[1]/section[1]/ul[1]/li[2]/a[1]/div[1]/span[1]')
# num_followers.click()
print("Followers: " + num_followers.text)
num_followers = num_followers.text

if "," in num_followers:
    num_followers = num_followers.replace(',', '')
else:
    pass

int(num_followers)

try:
    num_following = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/section[1]/main[1]/div[1]/header[1]/section[1]/ul[1]/li[3]/a[1]/div[1]/span[1]/span[1]"))
    )
except:
    try:
        num_following = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.XPATH,
                                            "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/section[1]/main[1]/div[1]/header[1]/section[1]/ul[1]/li[3]/a[1]/div[1]/span[1]/span[1]"))
        )
    except:
        num_following = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.XPATH,
                                            "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/section[1]/main[1]/div[1]/header[1]/section[1]/ul[1]/li[3]/a[1]/div[1]/span[1]/span[1]"))
        )

# num_following = driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/section[1]/main[1]/div[1]/header[1]/section[1]/ul[1]/li[3]/a[1]/div[1]/span[1]')
print("Following: " + num_following.text)
num_following = num_following.text

if "," in num_following:
    num_following = num_following.replace(',', '')
else:
    pass

int(num_following)

followers = []

def find_followers():

    global followers
    # foll = driver.find_element(By.XPATH, '/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/section[1]/main[1]/div[1]/header[1]/section[1]/ul[1]/li[2]/a[1]/div[1]')
    # foll.click()

    followers = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div').text
    # print(followers)

    if bot in user_name:

        followers = followers.replace("Followers","")
        # followers = followers.replace("Remove","")
        # followers = followers.replace("Follow","")
        followers = followers.replace("Requested","")
        followers = followers.replace("Verified","")
        followers = followers.replace("·","")
        followers = followers.split("Suggestions For You")[0]
        followers = followers.split("\n")
        while("" in followers) :
            followers.remove("")

        fst = str(followers[0])
        # print(fst)
        # print(followers[0])
        x = [i for i, s in enumerate(followers) if s == "Remove"]
        y = x[1:] + [len(followers)]
        z = [followers[i:j] for i, j in zip(x, y)]
        # print(z[0])
        del z[-1]
        result = [i[1:] for i in z]
        followers = list(list(zip(*result))[0])
        followers.append(fst)

        print("Followers, first refresh: ")
        print(followers)
        print(len(followers))

    else:

        followers = followers.replace("Followers", "")
        followers = followers.replace("Remove","")
        # followers = followers.replace("Following", "")
        # followers = followers.replace("Follow","")
        # followers = followers.replace("Requested", "")
        followers = followers.replace("Verified", "")
        followers = followers.replace("Hashtags", "")
        followers = followers.replace("·", "")
        followers = followers.replace("People", "")
        followers = followers.split("Suggestions For You")[0]
        followers = followers.split("\n")
        # print(followers)
        while ("" in followers):
            followers.remove("")

        elem1 = followers[0]
        # print(elem1)
        del followers[:2]

        # print(followers)

        specific_strings = ["Following", "Follow", "Requested"]
        sublists = []
        current_sublist = []

        for item in followers:
            if item in specific_strings:
                sublists.append(current_sublist)
                current_sublist = []
            else:
                current_sublist.append(item)

        # append the last sublist
        sublists.append(current_sublist)

        # print(sublists)

        followers = [i[:1] for i in sublists]
        followers = [j for i in followers for j in i]

        if elem1 == bot:
            followers_1.insert(0,elem1)
        else:
            pass

        print("Followers, first refresh: ")
        print("")
        print(followers)
        print(len(followers))

# find_followers()
# exit()

def findfollowing():

    global following
    following = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div').text

    if bot in user_name:
        following = following.replace("Following", "")
        following = following.replace("People", "")
        following = following.replace("Hashtags", "")
        following = following.replace("Verified", "")
        following = following.split("\n")

        while("" in following) :
            following.remove("")

        x = [i for i, s in enumerate(following) if s == "Following"]
        y = x[1:] + [len(following)]
        z = [following[i:j] for i, j in zip(x, y)]
        # print(z[-1])
        del z[-1]
        result = [i[1:] for i in z]
        following = list(list(zip(*result))[0])

        print("")
        print("Following:")
        print(following)
        print(len(following))

    else:

        following = following.replace("following", "")
        following = following.replace("Remove", "")
        # following = following.replace("Following", "")
        # following = following.replace("Follow","")
        # following = following.replace("Requested", "")
        following = following.replace("Verified", "")
        following = following.replace("Hashtags", "")
        following = following.replace("·", "")
        following = following.replace("People", "")
        following = following.split("Suggestions For You")[0]
        following = following.split("\n")
        while ("" in following):
            following.remove("")

        elem1 = following[0]
        # print(elem1)
        del following[:2]

        # print(following)

        specific_strings = ["Following", "Follow", "Requested"]
        sublists = []
        current_sublist = []

        for item in following:
            if item in specific_strings:
                sublists.append(current_sublist)
                current_sublist = []
            else:
                current_sublist.append(item)

        # append the last sublist
        sublists.append(current_sublist)

        # print(sublists)

        following = [i[:1] for i in sublists]
        following = [j for i in following for j in i]

        if elem1 == bot:
            following.insert(0,elem1)
        else:
            pass

        print("")
        print("Following:")
        print("")
        print(following)
        print(len(following))

def scroll_list_1():
    time.sleep(2)
    fBody = driver.find_element(By.CLASS_NAME, '_aano')
    scroll = 0
    while scroll < int(num_followers)/3:

        driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody)
        time.sleep(1.5)
        scroll += 1

    fList  = driver.find_elements(By.CLASS_NAME, "_aano")

    print("End scroll")

followers1 = driver.find_element(By.XPATH, '/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/section[1]/main[1]/div[1]/header[1]/section[1]/ul[1]/li[2]/a[1]/div[1]')
followers1.click()

time.sleep(3)

scroll_list_1()
find_followers()

close = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/button")
close.click()

driver.refresh()
time.sleep(5)

print("")
print("Followers: ")
print(followers)
print("")


time.sleep(3)

following1 = driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/section[1]/main[1]/div[1]/header[1]/section[1]/ul[1]/li[3]/a[1]/div[1]/span[1]/span[1]")
following1.click()

def scroll_list_2():
    time.sleep(2)
    fBody = driver.find_element(By.CLASS_NAME, '_aano')
    scroll = 0
    while scroll < int(num_following)/3:

        driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody)
        time.sleep(1.5)
        scroll += 1

    fList  = driver.find_elements(By.CLASS_NAME, "_aano")

    print("End scroll")

scroll_list_2()
findfollowing()

close = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/button")
close.click()
time.sleep(3)

print("--------------------------------------------------------------------------------------------------------------")
print("--------------------------------------------------------------------------------------------------------------")

mutual = []
dont_follow_back = []
just_followers = []

def main():

    global just_followers
    global mutual
    global dont_follow_back


    try:
        mutual = list(set(followers).intersection(following))
        print("Mutual followers:" + str(len(mutual)))
        print("")
        print(mutual)
        # print(len(mutual))
    except:
        pass

    print("--------------------------------------------------------------------------------------------------------------")

    dont_follow_back = list(set(following) - set(followers))
    print("Don't follow back:" + str(len(dont_follow_back)))
    print("")
    print(dont_follow_back)
    # print(len(dont_follow_back))

    print("--------------------------------------------------------------------------------------------------------------")

    just_followers = list(set(followers) - set(following))
    print("Just followers:" + str(len(just_followers)))
    print("")
    print(just_followers)
    # print(len(just_followers))

    print("--------------------------------------------------------------------------------------------------------------")

main()

first_elements_1 = []
first_elements_2 = []
first_elements_3 = []
first_elements_4 = []
first_elements_5 = []

def post_1():

    post_n = driver.find_element(By.XPATH, "(//div[contains(@class,'_aagw')])[1]")
    post_n.click()

def post_2():

    post_n = driver.find_element(By.XPATH, "(//div[contains(@class,'_aagw')])[2]")
    post_n.click()

def post_3():

    post_n = driver.find_element(By.XPATH, "(//div[contains(@class,'_aagw')])[3]")
    post_n.click()

def post_4():
    post_n = driver.find_element(By.XPATH, "(//div[contains(@class,'_aagw')])[4]")
    post_n.click()

def post_5():

    post_n = driver.find_element(By.XPATH, "(//div[contains(@class,'_aagw')])[5]")
    post_n.click()

def likes_1():
    # Click the 'likes' button to show the list of users who liked the post
    time.sleep(3)
    search_string = "others"
    search_string_2 = "likes"

    try:
        elements = driver.find_element(By.XPATH, "//*[contains(text(), '{}')]".format(search_string))
        elements.click()
    except:
        elements = driver.find_element(By.XPATH, "//*[contains(text(), '{}')]".format(search_string_2))
        elements.click()

    # like_n = driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/article[1]/div[1]/div[2]/div[1]/div[1]/div[2]/section[2]/div[1]/div[2]/div[1]/a[1]/div[1]")
    # like_n.click()

    time.sleep(3)

    try:
        scroll = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div/div")
    except:
        scroll = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[3]/div/div")

    scroll_origin = ScrollOrigin.from_element(scroll)

    scroll_pause_time = 55  # Set your desired scrolling time
    start_time = time.time()
    # likes_count = ""
    data_list = []

    while (time.time() - start_time) < scroll_pause_time:

        ActionChains(driver) \
            .scroll_from_origin(scroll_origin, 0, 300) \
            .perform()
        # likes_count = driver.find_elements(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]')

        # likes_count = driver.find_elements(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[3]')

        private = driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]").text

        if ("can see the total number of people who liked this post." in private):
            likes_count = driver.find_elements(By.XPATH,
                                               '/html/body/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[3]')

        else:
            likes_count = driver.find_elements(By.XPATH,
                                               '/html/body/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]')

        for element in likes_count:
            data_list.append(element.text)

        time.sleep(1.5)

    # print(data_list)

    merged_string = ' '.join(data_list)
    new_string = merged_string.replace('\n', ' ')

    # print(new_string)

    def split_string(string, delimiter, delimiter2, delimiter3):

        sublists = []
        sublist = []
        for word in string.split():
            if (word == delimiter) or (word == delimiter2) or (word == delimiter3):
                sublists.append(sublist)
                sublist = []
            else:
                sublist.append(word)
        sublists.append(sublist)
        return sublists

    string = new_string
    delimiter = "Following"
    delimiter2 = "Follow"
    delimiter3 = "Requested"
    sublists = split_string(string, delimiter, delimiter2, delimiter3)

    # print(sublists)

    unique_sublists = []
    for sublist in sublists:
        if sublist not in unique_sublists:
            unique_sublists.append(sublist)
    # print(unique_sublists)

    nonempty_sublists = [sublist for sublist in unique_sublists if sublist != []]
    # print(nonempty_sublists)

    global first_elements_1
    first_elements_1 = []

    for sublist in nonempty_sublists:
        first_elements_1.append(sublist[0])
    print(first_elements_1)
    print(len(first_elements_1))

    close_1 = driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/button[1]/div[1]/*[name()='svg'][1]")
    close_1.click()
    close_2 = driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]")
    close_2.click()

def likes_2():
    # Click the 'likes' button to show the list of users who liked the post
    time.sleep(4)
    search_string = "others"
    search_string_2 = "likes"

    try:
        elements = driver.find_element(By.XPATH, "//*[contains(text(), '{}')]".format(search_string))
        elements.click()
    except:
        elements = driver.find_element(By.XPATH, "//*[contains(text(), '{}')]".format(search_string_2))
        elements.click()

    time.sleep(3)

    try:
        scroll = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div/div")
    except:
        scroll = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[3]/div/div")

    scroll_origin = ScrollOrigin.from_element(scroll)

    scroll_pause_time = 55  # Set your desired scrolling time
    start_time = time.time()
    # likes_count = ""
    data_list = []

    while (time.time() - start_time) < scroll_pause_time:

        ActionChains(driver) \
            .scroll_from_origin(scroll_origin, 0, 300) \
            .perform()
        # likes_count = driver.find_elements(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]')

        # likes_count = driver.find_elements(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[3]')

        private = driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]").text

        if ("can see the total number of people who liked this post." in private):
            likes_count = driver.find_elements(By.XPATH,
                                               '/html/body/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[3]')

        else:
            likes_count = driver.find_elements(By.XPATH,
                                               '/html/body/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]')

        for element in likes_count:
            data_list.append(element.text)

        time.sleep(1.5)

    # print(data_list)

    merged_string = ' '.join(data_list)
    new_string = merged_string.replace('\n', ' ')

    # print(new_string)

    def split_string(string, delimiter, delimiter2, delimiter3):

        sublists = []
        sublist = []
        for word in string.split():
            if (word == delimiter) or (word == delimiter2) or (word == delimiter3):
                sublists.append(sublist)
                sublist = []
            else:
                sublist.append(word)
        sublists.append(sublist)
        return sublists

    string = new_string
    delimiter = "Following"
    delimiter2 = "Follow"
    delimiter3 = "Requested"
    sublists = split_string(string, delimiter, delimiter2, delimiter3)

    # print(sublists)

    unique_sublists = []
    for sublist in sublists:
        if sublist not in unique_sublists:
            unique_sublists.append(sublist)
    # print(unique_sublists)

    nonempty_sublists = [sublist for sublist in unique_sublists if sublist != []]
    # print(nonempty_sublists)

    global first_elements_2
    first_elements_2 = []

    for sublist in nonempty_sublists:
        first_elements_2.append(sublist[0])
    print(first_elements_2)
    print(len(first_elements_2))

    close_1 = driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/button[1]/div[1]/*[name()='svg'][1]")
    close_1.click()
    close_2 = driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]")
    close_2.click()

def likes_3():
    # Click the 'likes' button to show the list of users who liked the post
    time.sleep(4)
    search_string = "others"
    search_string_2 = "likes"

    try:
        elements = driver.find_element(By.XPATH, "//*[contains(text(), '{}')]".format(search_string))
        elements.click()
    except:
        elements = driver.find_element(By.XPATH, "//*[contains(text(), '{}')]".format(search_string_2))
        elements.click()

    time.sleep(3)

    try:
        scroll = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div/div")
    except:
        scroll = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[3]/div/div")

    scroll_origin = ScrollOrigin.from_element(scroll)

    scroll_pause_time = 55  # Set your desired scrolling time
    start_time = time.time()
    # likes_count = ""
    data_list = []

    while (time.time() - start_time) < scroll_pause_time:

        ActionChains(driver) \
            .scroll_from_origin(scroll_origin, 0, 300) \
            .perform()
        # likes_count = driver.find_elements(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]')

        # likes_count = driver.find_elements(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[3]')

        private = driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]").text

        if ("can see the total number of people who liked this post." in private):
            likes_count = driver.find_elements(By.XPATH,
                                               '/html/body/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[3]')

        else:
            likes_count = driver.find_elements(By.XPATH,
                                               '/html/body/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]')

        for element in likes_count:
            data_list.append(element.text)

        time.sleep(1.5)

    # print(data_list)

    merged_string = ' '.join(data_list)
    new_string = merged_string.replace('\n', ' ')

    # print(new_string)

    def split_string(string, delimiter, delimiter2, delimiter3):

        sublists = []
        sublist = []
        for word in string.split():
            if (word == delimiter) or (word == delimiter2) or (word == delimiter3):
                sublists.append(sublist)
                sublist = []
            else:
                sublist.append(word)
        sublists.append(sublist)
        return sublists

    string = new_string
    delimiter = "Following"
    delimiter2 = "Follow"
    delimiter3 = "Requested"
    sublists = split_string(string, delimiter, delimiter2, delimiter3)

    # print(sublists)

    unique_sublists = []
    for sublist in sublists:
        if sublist not in unique_sublists:
            unique_sublists.append(sublist)
    # print(unique_sublists)

    nonempty_sublists = [sublist for sublist in unique_sublists if sublist != []]
    # print(nonempty_sublists)

    global first_elements_3
    first_elements_3 = []

    for sublist in nonempty_sublists:
        first_elements_3.append(sublist[0])
    print(first_elements_3)
    print(len(first_elements_3))

    close_1 = driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/button[1]/div[1]/*[name()='svg'][1]")
    close_1.click()
    close_2 = driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]")
    close_2.click()

def likes_4():
    # Click the 'likes' button to show the list of users who liked the post
    time.sleep(4)
    search_string = "others"
    search_string_2 = "likes"

    try:
        elements = driver.find_element(By.XPATH, "//*[contains(text(), '{}')]".format(search_string))
        elements.click()
    except:
        elements = driver.find_element(By.XPATH, "//*[contains(text(), '{}')]".format(search_string_2))
        elements.click()

    time.sleep(3)

    try:
        scroll = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div/div")
    except:
        scroll = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[3]/div/div")

    scroll_origin = ScrollOrigin.from_element(scroll)

    scroll_pause_time = 55  # Set your desired scrolling time
    start_time = time.time()
    # likes_count = ""
    data_list = []

    while (time.time() - start_time) < scroll_pause_time:

        ActionChains(driver) \
            .scroll_from_origin(scroll_origin, 0, 300) \
            .perform()
        # likes_count = driver.find_elements(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]')

        # likes_count = driver.find_elements(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[3]')

        private = driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]").text

        if ("can see the total number of people who liked this post." in private):
            likes_count = driver.find_elements(By.XPATH,
                                               '/html/body/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[3]')

        else:
            likes_count = driver.find_elements(By.XPATH,
                                               '/html/body/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]')

        for element in likes_count:
            data_list.append(element.text)

        time.sleep(1.5)

    # print(data_list)

    merged_string = ' '.join(data_list)
    new_string = merged_string.replace('\n', ' ')

    # print(new_string)

    def split_string(string, delimiter, delimiter2, delimiter3):

        sublists = []
        sublist = []
        for word in string.split():
            if (word == delimiter) or (word == delimiter2) or (word == delimiter3):
                sublists.append(sublist)
                sublist = []
            else:
                sublist.append(word)
        sublists.append(sublist)
        return sublists

    string = new_string
    delimiter = "Following"
    delimiter2 = "Follow"
    delimiter3 = "Requested"
    sublists = split_string(string, delimiter, delimiter2, delimiter3)

    # print(sublists)

    unique_sublists = []
    for sublist in sublists:
        if sublist not in unique_sublists:
            unique_sublists.append(sublist)
    # print(unique_sublists)

    nonempty_sublists = [sublist for sublist in unique_sublists if sublist != []]
    # print(nonempty_sublists)

    global first_elements_4
    first_elements_4 = []

    for sublist in nonempty_sublists:
        first_elements_4.append(sublist[0])
    print(first_elements_4)
    print(len(first_elements_4))

    close_1 = driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/button[1]/div[1]/*[name()='svg'][1]")
    close_1.click()
    close_2 = driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]")
    close_2.click()

def likes_5():
    # Click the 'likes' button to show the list of users who liked the post
    time.sleep(4)
    search_string = "others"
    search_string_2 = "likes"

    try:
        elements = driver.find_element(By.XPATH, "//*[contains(text(), '{}')]".format(search_string))
        elements.click()
    except:
        elements = driver.find_element(By.XPATH, "//*[contains(text(), '{}')]".format(search_string_2))
        elements.click()

    time.sleep(3)

    try:
        scroll = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div/div")
    except:
        scroll = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[3]/div/div")

    scroll_origin = ScrollOrigin.from_element(scroll)

    scroll_pause_time = 55  # Set your desired scrolling time
    start_time = time.time()
    # likes_count = ""
    data_list = []

    while (time.time() - start_time) < scroll_pause_time:

        ActionChains(driver) \
            .scroll_from_origin(scroll_origin, 0, 300) \
            .perform()
        # likes_count = driver.find_elements(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]')

        # likes_count = driver.find_elements(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[3]')

        private = driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]").text

        if ("can see the total number of people who liked this post." in private):
            likes_count = driver.find_elements(By.XPATH,
                                               '/html/body/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[3]')

        else:
            likes_count = driver.find_elements(By.XPATH,
                                               '/html/body/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]')

        for element in likes_count:
            data_list.append(element.text)

        time.sleep(1.5)

    # print(data_list)

    merged_string = ' '.join(data_list)
    new_string = merged_string.replace('\n', ' ')

    # print(new_string)

    def split_string(string, delimiter, delimiter2, delimiter3):

        sublists = []
        sublist = []
        for word in string.split():
            if (word == delimiter) or (word == delimiter2) or (word == delimiter3):
                sublists.append(sublist)
                sublist = []
            else:
                sublist.append(word)
        sublists.append(sublist)
        return sublists

    string = new_string
    delimiter = "Following"
    delimiter2 = "Follow"
    delimiter3 = "Requested"
    sublists = split_string(string, delimiter, delimiter2, delimiter3)

    # print(sublists)

    unique_sublists = []
    for sublist in sublists:
        if sublist not in unique_sublists:
            unique_sublists.append(sublist)
    # print(unique_sublists)

    nonempty_sublists = [sublist for sublist in unique_sublists if sublist != []]

    # print(nonempty_sublists)
    global first_elements_5
    first_elements_5 = []

    for sublist in nonempty_sublists:
        first_elements_5.append(sublist[0])
    print(first_elements_5)
    print(len(first_elements_5))

    close_1 = driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]/div[1]/button[1]/div[1]/*[name()='svg'][1]")
    close_1.click()
    close_2 = driver.find_element(By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]")
    close_2.click()

print("Post 1 likes: ")
post_1()
likes_1()
print("--------------------------------------------------------------------------------------------------------------")

print("Post 2 likes: ")
post_2()
likes_2()
print("--------------------------------------------------------------------------------------------------------------")

print("Post 3 likes: ")
post_3()
likes_3()
print("--------------------------------------------------------------------------------------------------------------")

print("Post 4 likes: ")
post_4()
likes_4()
print("--------------------------------------------------------------------------------------------------------------")

print("Post 5 likes: ")
post_5()
likes_5()
print("--------------------------------------------------------------------------------------------------------------")

total_likes = first_elements_1 + first_elements_2 + first_elements_3 + first_elements_4 + first_elements_5

print(total_likes)

counts = {}  # Define an empty dictionary to store the element counts

for elem in mutual:
    count = total_likes.count(elem)
    counts[elem] = count

sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)

print("")
print("Target users: ")
print("")
for elem, count in sorted_counts:
    print(f"{elem}: {count}")


counts_2 = {}  # Define an empty dictionary to store the element counts

for elem in just_followers:
    count = total_likes.count(elem)
    counts_2[elem] = count

sorted_counts = sorted(counts_2.items(), key=lambda x: x[1], reverse=True)

print("")
print("Non target users: ")
print("")
for elem, count in sorted_counts:
    print(f"{elem}: {count}")

print("")
counts_3 = {}  # Define an empty dictionary to store the element counts

for elem in dont_follow_back:
    count = total_likes.count(elem)
    counts_3[elem] = count

sorted_counts = sorted(counts_3.items(), key=lambda x: x[1], reverse=True)

print("")
print("Suspicious behavior: ")
print("")
for elem, count in sorted_counts:
    print(f"{elem}: {count}")