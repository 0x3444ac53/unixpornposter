import argparse
import katfetch

def make_comment(deets : dict) -> str:
    """
    args should be in format
    "thing title" : ("link title", "link")
    """
    link_template = "+ **{}**: [{}]({})\n"
    template = "+ **{}**: {}\n"
    comment = []
    for i in deets.keys():
        if type(deets[i]) is tuple:
            comment.append(link_template.format(i.capitalize(), deets[i][0], deets[i][1]))
        elif type(deets[i]) is str:
            comment.append(template.format(i.capitalize(), deets[i]))
    return "".join(comment)

def get_deets(file_path : str, gen=False) -> tuple:
    """
    gets deets from file
    and returns a tuple with the format
    (title, deets)
    """
    generated = {}
    if gen:
        generated = {
            'shell' : str(katfetch.get_shell.subprocess.Popen(["echo $SHELL"], shell=True, stdout=katfetch.get_shell.subprocess.PIPE).communicate()[0], 'utf-8').strip().split('/')[-1],
            'wm' : katfetch.get_wm.wm(),
            'terminal' : katfetch.get_term.term(),
            'distro' : katfetch.distro.name()}
    with open(file_path) as f:
        deets = eval(f.read())
    final_deets = {}
    for i in generated.keys():
        final_deets[i] = generated[i]
    for i in deets.keys():
        final_deets[i.lower()] = deets[i]
    title = f'[{deets["wm"]}] {deets["title"]}'
    del final_deets['title']
    del final_deets['wm']
    return (title, final_deets)

def get_args():
    p = argparse.ArgumentParser()
    p.add_argument('-p', '--path', nargs='?')
    p.add_argument('--details', nargs='?', default="deets.py")
    p.add_argument('--dry_run', action='store_true')
    return p.parse_args()

def main(folder : str, gen=False):
    title, details = get_deets(f'{folder}/details', gen)
    return title, make_comment(details)
