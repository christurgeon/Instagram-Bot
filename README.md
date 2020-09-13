# Instagram-Crawler

Before attempting to run the bot, make sure that you have the necessary libraries installed.

```
pip install selenium
pip install argparse
```
Next make sure that you have ```chromedriver.exe``` downloaded and set the path to this executable in the variable **CHROMEDRIVER_PATH**. You can find compatible chromedriver versions for your Google chrome application [here](https://chromedriver.chromium.org/downloads).

## Like Mode

This mode works by searching all posts containing the hashtag stored in the variable **HASHTAG** and liking each post up to the number specified. Optionally, this mode can be used with a comment mode to drop in a random comment.

Only allowing likes:
```
python bot.py like
```
Allowing likes and comments:
```
python bot.py like comment
```
## Follow Mode

This mode works by going to the Instagram page of the user stored in the variable **TARGET_ACCOUNT_NAME** and following a specified number of accounts who also follow this user. By passing in a command argument like so you will enable the follow mode. 

```
python bot.py follow
```

## Notes

If the program breaks while trying to navigate Instagram, then most likely Instagram has updated their website and the selection of web elements from DOM needs to be changed. Please email me at **turgeonchris3@gmail.com** if you would like me to take a look and patch the bug.
