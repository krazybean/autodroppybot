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


#### Speed it up...
If you would like to take advantage of redis local caching, feel free to use this dependency
instead: 

[redis branch](https://github.com/krazybean/InstaPy/tree/redis)

also submitted as a pull request:

[pull request](https://github.com/timgrossmann/InstaPy/pull/4440)

Install and run as usual.
