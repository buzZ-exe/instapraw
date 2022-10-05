import praw
from instabot import Bot
import random, requests
import config

bot = Bot()
bot.login(username = config.username, password = config.password)

reddit = praw.Reddit(client_id = config.client_id,
                    client_secret = config.client_secret,
                    user_agent = config.user_agent)

meme = reddit.subreddit('memes').hot()
meme_post = random.randint(1, 50)
for i in range(0, meme_post):
    submission = next(x for x in meme if x.stickied == False)
    extension = submission.url[len(submission.url) - 3 :].lower()
    if 'gif' not in extension:
        pass
    else:
        continue

r = requests.get(submission.url)    
with open('post.jpeg', 'wb') as f:
    f.write(r.content)
print("Image Downloaded!")
print()

caption = submission.title + '\n.\n.\n.\nPosted by: u/ ' + str(submission.author) + '\n\n #memes #dankmemes #reddit #funny #robot #bot'
bot.upload_photo('post.jpeg', caption = caption)
bot.logout()

input('Press any key to continue...')