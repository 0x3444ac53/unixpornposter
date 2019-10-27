import praw
import argparse

def get_args():
    p = argparse.ArgumentParser()
    p.add_argument('subreddit')
    p.add_argument('title')
    p.add_argument('--nsfw', action='store_true')
    p.add_argument('-u', '--url', nargs='?')
    p.add_argument('-t', '--selftext', nargs='?')
    p.add_argument('-f', '--from-file', nargs='?')
    return p.parse_args()

def comment_on_post(submission : praw.models.Submission, comment : str):
    return submission.reply(comment)

def get_reddit_instance(credentials : dict) -> praw.models.reddit:
    return praw.Reddit(**credentials)

def main(title : str, subreddit_name : str, creds : dict, **kwargs) -> praw.models.Submission:
    reddit = get_reddit_instance(creds)
    subreddit = reddit.subreddit(subreddit_name)
    return subreddit.submit(title, **kwargs)

if __name__ == '__main__':
    a = vars(get_args())
    title = a['title']
    subreddit = a['subreddit']
    del a['subreddit']
    del a['title']
    if a['from_file'] is not None:
        a['selftext'] = read_file(a['from_file'])
    del a['from_file']
    giant_cock = {key : value for key, value in a.items() if value is not None}
    print(giant_cock)
    post = main(title, subreddit, **giant_cock)
