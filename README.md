## Unixporn Poster

Small cli tool for quickly making a post to [r/unixporn](https://reddit.com/r/unixporn)

### Installation & Setup

```shell
pip install unixpornposter
```

1. Create a new app at https://www.reddit.com/prefs/apps/ and get a `client_id` and `client_secret`

1. Create a file at `~/.config/unixpornposter/redditCreds` and populate it like this 

   ```python3
   {'client_id'     : 'your_client_id',
    'client_secret' : 'your_client_secret',
    'user_agent'    : 'a script',
    'username'      : 'your_username',
    'password'      : 'your_password'}
   ```

### Usage 

1. Make a rice directory

   ```
   sowmRice/
    ⮡ screenshot1.png
    ⮡ screenshot2.jpg
    ⮡ screenshot3.gif
    ⮡ details
   ```

   The details file is info for your post, inclusing the details comment information, and the title, it should look like this: 

   ```python3
   {"Wallpaper"   : ("Smoking Maid",         "https://www.pixiv.net/en/artworks/58837536"),
    "Terminal"    : ("st",                   "st.suckless.org"),
    "Colorscheme" : ("base16-unikitty-dark", "https://github.com/joshwlewis/base16-unikitty"),
    "Startpage"   : ("My Fork of ArchLabs",  "https://github.com/lifesgood123/.ArchLabs-homepage"),
    "title"       : "I can't wait to be done with this"
    }
   
   ```

   With the exception of the `title` entry, all other entries should have the format `‘Bullet Point Name' : (‘link_text', ‘link_url’)`

   you’re welcome to explore other formats, but it ***will*** make you details comment look strange

1. Run the poster

   `unixpornpost /rice/directory/here`



###### Todo

- Create more options for the details file format
- Design logging system to ensure no duplicate post are made