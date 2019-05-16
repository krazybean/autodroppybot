# Auto Droppy Bot


### Instructions


#### Download
```commandline

$ git clone git@github.com:krazybean/autodroppybot.git
$ cd autodroppybot/

```

#### Virtualenv
`pipenv` used in this example to install dependencies

```commandline
$ pipenv --python=python3.7 install
$ pip install -r requirements.txt

```


#### Run it

```commandline
# Paste your drop link list into text.txt
...
# Put the instagram username/password into environment variables for that shell session
export insta_username=johndoe
export insta_password=abc123
# Run the script
python run_list.py

```


The total runtime depends on how many items are in the list, current implementation is to
go down the list and select the 2 most recent posts of the person in the drop list and like
their posts.


#### Example Output

```commandline
INFO [2019-05-16 00:14:45] [username]  Finished interacting on total of 162 images from 81 users! xD

INFO [2019-05-16 00:14:45] [username]  Liked: 20
INFO [2019-05-16 00:14:45] [username]  Already Liked: 1
INFO [2019-05-16 00:14:45] [username]  Commented: 0
INFO [2019-05-16 00:14:45] [username]  Followed: 0
INFO [2019-05-16 00:14:45] [username]  Already Followed: 0
INFO [2019-05-16 00:14:45] [username]  Inappropriate: 0
INFO [2019-05-16 00:14:45] [username]  Not valid users: 1


INFO [2019-05-16 00:14:45] [juanthejust]  Sessional Live Report:
        |> LIKED 20 images  |  ALREADY LIKED: 1
        |> COMMENTED on 0 images
        |> FOLLOWED 0 users  |  ALREADY FOLLOWED: 0
        |> UNFOLLOWED 0 users
        |> LIKED 0 comments
        |> REPLIED to 0 comments
        |> INAPPROPRIATE images: 0
        |> NOT VALID users: 1

On session start was FOLLOWING 2775 users & had 3098 FOLLOWERS
[Session lasted 12.57 minutes]

OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO
INFO [2019-05-16 00:14:45] [username]  Session ended!
oooooooooooooooooooooooooooooooooooooooooooooooooooooooo

```

#### Speed it up...
If you would like to take advantage of redis local caching, feel free to use this dependency
instead: 

[redis branch](https://github.com/krazybean/InstaPy/tree/redis)

also submitted as a pull request:

[pull request](https://github.com/timgrossmann/InstaPy/pull/4440)

Install and run as usual.
