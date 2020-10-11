import praw
import argparse
from unixpornposter import redditpost, riceDetails
import elliesImgurUploader.imgurUploader as imgurUploader
import os

def get_args():
    p = argparse.ArgumentParser()
    p.add_argument('path', help='the folder where your rice files are located')
    p.add_argument('--subreddit', help='name of the subreddit you wanna post to, deafault is \'unixporn\'', default='unixporn', nargs='?')
    p.add_argument('-g', '--generate', help='uses the katfetch module to generte basic details', action='store_true')
    return p.parse_args()


def upload_scrots(directory : str, title : str) -> str:
    """
    takes directory of images as an argument
    and returns url of imgur album
    """
    return imgurUploader.main([ f'{directory}/{i}' for i in os.listdir(directory) if i.endswith('.png')], title)[1]

def main(folder : str, subreddit : str, gen=False) -> str:
    credentials_file = f'{os.environ.get("HOME")}/.config/unixpornposter/redditCreds'
    with open(credentials_file) as f:
        credentials = eval(f.read())
    title, comment = riceDetails.main(folder, gen=gen)
    link = upload_scrots(folder, title)
    submission = redditpost.main(title, subreddit, credentials, url=link)
    submission.reply(comment)
    return submission.permalink

if __name__ == '__main__':
    a = get_args()
    print(f'https://reddit.com{main(a.path, a.subreddit, gen=a.generate)}')
