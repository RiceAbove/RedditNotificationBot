# 🤖 Reddit Notification Bot 🤖

A Reddit bot that uses Python and PRAW (Python Reddit API Wrapper) to send the user a notification, via Reddit inbox, of a new post in any existing subreddit. 

# UPDATE (March 10, 2021)
After over 2 years, RedditNotificationBot has finally reached EOL. This is my very first side project ever, and will always have a special place in my heart. The original inspriation for this bot would be to get notifications whenever a new post would come into `r/FREE`, since getting free stuff from that subreddit is from a first come first serve basis. With little knowledge of networks & Python, creating this was a fun way to get my foot in the door with learning about making requests & accessing an API. So much has changed in these past 2 years, & I will always look back at this project as the starting point of my journey into creating fun projects. If I ever want to make a new version of this project, I will create a RedditNotificationBot-v2.

## About

This is one of my first side projects that I am proud to make and share with you guys. Learning how to make a reddit bot was not only fun but helped me gain the knowledge and experience with using an API/API wrapper for the first time. If there is any errors or improvement that you want to make to this don't hesitate to request a pull. I would love to collaborate with other people and learn :-)

## Built With

* Python
* [PRAW](https://praw.readthedocs.io/en/latest/) - Python Reddit API Wrapper

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

The only thing you need to install is PRAW & to have a config.py file. Install these using requirements.txt as shown below 
```
$ pip3 install -r requirements.txt
```
For config.py, have the following format
```
api = {
    'client_id':'',
    'client_secret': ''
}

account = {
    'username': '',
    'password': ''
}
```

### Installing

Just clone the repository to your local machine and run it via command
prompt

```
$ git clone https://github.com/RiceAbove/RedditNotificationBot.git
```
and run it via command prompt
```
$ python3 main.py
```

### Using the Bot

In order to use the bot, you will have to create your own [reddit app](https://www.reddit.com/prefs/apps/)

For more information about creating a bot, [go here](https://www.pythonforengineers.com/build-a-reddit-bot-part-1/)

## Contributing Guide
Please read [CONTRIBUTING.md](CONTRIBUTING.md), [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md), & [PULL_REQUEST_TEMPLATE.md](PULL_REQUEST_TEMPLATE.md) on the process for submitting pull requests.

## Contributors

* **Gico Carlo Evangelista** - [RiceAbove](https://github.com/RiceAbove), evangelsitagico@gmail.com - Creator 

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
