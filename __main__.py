import praw
import argparse
import unixpornposte.redditpost
import unixpornposte.riceDetails
import elliesImgurUploader.imgurUploader as imgurUploader
import os

def get_args():
    folderhelpstring="folder must contain images and a details file"
    p = argparse.ArgumentParser()
    p.add_argument('folder')
    return p.parse_args()

def upload_scrots(directory : str, title : str) -> str:
    """
    takes directory of images as an argument
    and returns url of imgur album
    """
    return imgurUploader.main([ f'{directory}/{i}' for i in os.listdir(directory) if i.endswith('.png')], title)[1]

def main(folder : str) -> str:
    credentials_file = f'{os.environ.get("HOME")}/.config/unixpornposter/redditCreds'
    with open(credentials_file) as f:
        credentials = eval(f.read())
    title, comment = riceDetails.main(folder)
    link = upload_scrots(folder, title)
    submission = redditpost.main(title, 'riceporn', credentials, url=link)
    submission.reply(comment)
    return submission.permalink

if __name__ == '__main__':
    a = get_args()
    print(f'https://reddit.com{main(a.folder)}')
