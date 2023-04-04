# Instagram-tracker
A python scripts that will track any Instagram account

Required:
Python
Selenium webdriver
An Instagram account
A victim under 10k followers or following, with public profile (or a profile followed by our Instagram account) 

Walkthrough:

Just modify on the first line of code chromedriver path, chrome profile path and Chrome path.
After that you must enter the Instagram account used by you as BOT and a victim account.
First time when you login you must enter the BOT account password and save it to the browser, close the browser and restart the script.
Wait for the script to go through all the followers and likes.
If you want to count only followers/following lists without likes, just comment the code.

Most probably due to Instagram updates, it will be required to modify some of the XPATHs from the code.

A python selenium script that will track any Instagram account under 10000 followers.

It will compare followers and following lists and will split them into 3 other lists: 

- Don't follow back
- Mutual
- Just followers

It will track the likes from last 5 photos ( it can be any of the last 5 photos, just comment the functions any of likes_1, likes_n etc ) and will count likes from every photos.

It will find and sort the users that usually likes most of the pictures and make 3 new lists with users that likes a photo and are found in any of the above-mentioned lists.

With this innovation you can make an idea about the accounts with which a user interacts.

Due to Instagram privacy update from few years ago, the visibility of the accounts name that likes a photo it's limited to 100. Also the visibility of the accounts in any of the following and followers lists is limited to ~90%, so it cannot be an exact match on the external accounts. It will give you the exact details only if your account is the account that you login.
