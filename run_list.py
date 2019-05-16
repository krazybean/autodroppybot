""" Auto-dropping (likes) bot usage """
import os
from instapy import InstaPy
from instapy import smart_run

insta_username = os.environ.get('insta_username')
insta_password = os.environ.get('insta_password')
file_name = 'test.txt'

session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False)


def get_friendslist(file_name):
    fl = list()
    fh = open(file_name, 'r').readlines()
    splitter = 'https://www.instagram.com/'
    for line in fh:
        if splitter in line:
            fl.append(line.split(splitter)[1].strip('\n'))
    return fl


friendslist = get_friendslist(file_name)

with smart_run(session):
    session.set_relationship_bounds(enabled=False)
    session.set_skip_users(skip_private=False)
    session.set_do_like(True, percentage=100)
    session.set_sleep_reduce(percentage=100)
    session.interact_by_users(friendslist,
                              amount=2,
                              randomize=False)

