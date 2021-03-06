import praw
from config import api
from config import account
from datetime import datetime

# To access the bot. Makes a Reddit instance and returns it using PRAW
def bot_login():

    # Get's all of the api/account data from your personal config.py file
    # config.py should have the following format:
    #
    # api = {
    #    'client_id':'',
    #    'client_secret': ''
    # }
    #
    # account = {
    #    'username': '',
    #    'password': ''
    # }


    id = api['client_id']
    secret = api['client_secret']
    user = account['username']
    pass_word = account['password']

    reddit = praw.Reddit(client_id=id,
                         client_secret=secret,
                         username=user,
                         password=pass_word,
                         user_agent='RedditNotificationBot')
    print("RedditNotifcationBot v.1.0.0")
    return reddit

# Helper functions

# Your username input
def redditor(reddit):
    username = str(input('Add your username: '))
    return reddit.redditor(username)

# The subreddit you want notifications from
def reddit_community(reddit):
    reddit_page = str(input('Add a subreddit: '))
    return reddit.subreddit(reddit_page)

# The current time on your pc
def local_time():
    return datetime.now()

# Will send a message notifying the user of a new post. If username is invalid it will restart the log in process
def send_notification(reddit, redditor, title, link, subreddit):
    try:
        redditor.message("New post from {}".format(subreddit),
                         "{} {}".format(title, link))
    except:
        print("Invalid Username. Try again")
        setup()

# Main functions

# Will check the subreddit the user has chosen and see if there are any new post from the start of the code
def stream(submission, reddit, redditor, init_time, subreddit):
    title = submission.title
    link = submission.url
    post_time = datetime.fromtimestamp(submission.created_utc)
    if(post_time > init_time):
        send_notification(reddit, redditor, title, link, subreddit)
        print("----------------------------------")
        print(title)
        print(link)

# Sets up the bot and has the user put in their username and their subreddit of choice
# If subreddit is invalid it will restart the log in process
def setup():
    reddit = bot_login()
    print("Enter your username and a subreddit you would like to get notifications from")
    while True:
        try:
            user = redditor(reddit)
            subreddit = reddit_community(reddit)
            init_time = local_time()
            for submission in subreddit.stream.submissions():
                stream(submission, reddit, user, init_time, subreddit)
        except KeyboardInterrupt:
            print("\nThank you for using RedditNotificationBot! Goodbye!")
            break
        except:
            print("Invalid subreddit. Try again")
            continue

# Where everything starts
def main():
    setup()

# Runs the main function as soon as you start up the program via command line
if __name__ == '__main__':
    main()
