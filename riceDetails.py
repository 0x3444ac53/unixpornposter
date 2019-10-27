import argparse

def make_comment(deets : dict) -> str:
    """
    args should be in format
    "thing title" : ("link title", "link")
    """
    template = "+ **{}**: [{}]({})\n"
    comment = ""
    for i in deets.keys():
        comment = comment + template.format(i, deets[i][0], deets[i][1])
    return comment

def get_deets(file_path : str) -> tuple:
    """
    gets deets from file
    and returns a tuple with the format
    (title, deets)
    """
    with open(file_path) as f:
        deets = eval(f.read())
    title = deets['title']
    del deets['title']
    return (title, deets)

def get_args():
    p = argparse.ArgumentParser()
    p.add_argument('-p', '--path', nargs='?')
    p.add_argument('--details', nargs='?', default="deets.py")
    p.add_argument('--dry_run', action='store_true')
    return p.parse_args()

def main(folder : str):
    title, details = get_deets(f'{folder}/details')
    return title, make_comment(details)
