### 🔥 The Most Powerfull Userbot 🔥

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/f7c51539e67b483bb8d7749acca51d3a)](https://app.codacy.com/gh/mama-userbot/mama-userbot?utm_source=github.com&utm_medium=referral&utm_content=mama-userbot/mama-userbot&utm_campaign=Badge_Grade_Settings)
[![Python 3.6](https://img.shields.io/badge/Python-3.6%20or%20newer-blue.svg)](https://www.python.org/downloads/release/python-360/)
![GitHub repo size](https://img.shields.io/github/repo-size/mama-userbot/mama-userbot)
[![HitCount](http://hits.dwyl.com/mama-userbot/mama-userbot.svg)](http://hits.dwyl.com/mama-userbot/mama-userbot)
[![Contact Me](https://img.shields.io/badge/Telegram-Contact%20Me-informational)](https://t.me/mama_bad_op)


# The Mama Userbot

This is a userbot made for telegram. I made this userbot with help of all other userbots available in telegram. All credits goes to its Respective Owners....

This is the one and only official Mama Userbot made by [@mama_bad_op](https://t.me/mama_bad_op) Also join support channel and group :- https://t.me/mama_userbot_support Enjoy Your Bot!!💝
[![mama-userbot logo](https://telegra.ph/file/49d69e7a65c2bb384c747.jpg)](https://t.me/mama_userbot_support)


### The owner would not be responsible for any kind of bans due to the bot...


# FORK AT YOUR OWN RISK

# Credits
### • [Hell_UserBot](https://github.com/HellBoy-op/HellBot)
## One and only Highly inspired me..
## Official Support
<a href="https://t.me/HellBot_Official"><img src="Unknown wight, [07.01.21 17:24]
https://img.shields.io/badge/Join-Support%20Channel-red.svg?style=for-the-badge&logo=Telegram"></a>
<a href="https://t.me/mama_userbot_support"><img src="https://img.shields.io/badge/Join-Support%20Group-blue.svg?style=for-the-badge&logo=Telegram"></a>

##  🏡 Set-Up 🏡

### 💠 The Easy Way

<a href="https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2Fmama-userbot%2Fmama-userbot&template=https%3A%2F%2Fgithub.com%2Fmama-userbot%2Fmama-userbot" rel="nofollow" style="background-color: initial; box-sizing: border-box; color: #0366d6; text-decoration-line: none;"><img alt="Deploy" data-canonical-src="https://www.herokucdn.com/deploy/button.svg" src="https://camo.githubusercontent.com/83b0e95b38892b49184e07ad572c94c8038323fb/68747470733a2f2f7777772e6865726f6b7563646e2e636f6d2f6465706c6f792f627574746f6e2e737667" style="border-style: none; box-sizing: initial; max-width: 100%;" /></a></div>

### 💠 The Normal Way 

Simply clone the repository and run the main file:
```sh
git clone https://github.com/mama-userbot/mama-userbot
cd mama-userbot
virtualenv -p /usr/bin/python3 venv
. ./venv/bin/activate
pip install -r requirements.txt
# <Create local_config.py with variables as given below>
python3 -m userbot
```

An example `local_config.py` file could be:

**Not All of the variables are mandatory**

__The Userbot should work by setting only the first two variables__

```python3
from heroku_config import Var

class Development(Var):
  APP_ID = 6
  API_HASH = "eb06d4abfb49dc3eeb1aeb98ae0f581e"
```

### UniBorg Configuration

The UniBorg Config is situated in `userbot/uniborgConfig.py`.

**Heroku Configuration**
Simply just leave the Config as it is.

**Local Configuration**
Fortunately there are no Mandatory vars for the UniBorg Support Config.

## Mandatory Vars

- Only two of the environment variables are mandatory.
- This is because of `telethon.errors.rpc_error_list.ApiIdPublishedFloodError`
    - `APP_ID`:   You can get this value from https://my.telegram.org
    - `API_HASH`:   You can get this value from https://my.telegram.org
- The userbot will not work without setting the mandatory vars.
