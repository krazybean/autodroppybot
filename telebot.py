import os
import sys
import time

from telethon import TelegramClient, events, utils
from instapy import smart_run

# FILE IS A WIP DON'T JUDGE ME!!


ccb_news_channel = 1117452205
ccb_chat_channel = 1071339795
ccb_drop_channel = 1167028876
ccb_drop_bot = 'CCBLIKESDROP'
key_phrase = 'First 10 people to leave their IG'
drop_phrase_start = 'Round Started'
drop_phrase_end = 'Drop Phase Closed'
instagram_link = 'https://www.instagram.com/'
my_insta_name = 'juanthejust'

drop_list = []
drop_phase = True


def get_env(name, message, cast=str):
    if name in os.environ:
        return os.environ[name]
    while True:
        value = input(message)
        try:
            return cast(value)
        except ValueError as e:
            print(e, file=sys.stderr)
            time.sleep(1)


session = os.environ.get('TG_SESSION', 'droppy')

# TELEGRAM API DETAILS
api_id = get_env('TG_API_ID', 'Enter your API ID: ', int)
api_hash = get_env('TG_API_HASH', 'Enter your API hash: ')

# INSTAGRAM DETAILS
insta_username = os.environ.get('insta_username')
insta_password = os.environ.get('insta_password')
proxy = None

client = TelegramClient(session, api_id, api_hash, proxy=proxy).start()


def event_checks(event):
    flag = False
    if event.message.is_channel:
        if hasattr(event.message.to_id, 'channel_id'):
            if event.message.to_id.channel_id == ccb_news_channel:
                if key_phrase in event.text:
                    flag = True
    return flag


def drop_event_check(event, sender, event_name):
    if event_name not in ['open', 'close']:
        return False
    if event_name == 'open':
        drop_phrase = drop_phrase_start
    else:
        drop_phrase = drop_phrase_end
    flag = False
    if event.message.to_id.channel_id == ccb_drop_channel:
        if utils.get_display_name(sender) == ccb_drop_bot:
            if drop_phrase in event.text or instagram_link in event.text:
                flag = True
    return flag


def is_instalink(event):
    if instagram_link in event.text:
        drop_list.append(event.text)


def drop_list_reset():
    drop_list = []


async def run_drop(link_list):
    with smart_run(session):
        """ Activity flow """
        # general settings
        session.set_relationship_bounds(enabled=False)
        session.set_skip_users(skip_private=False)
        session.set_do_like(True, percentage=100)
        session.set_sleep_reduce(percentage=100)
        session.interact_by_users(link_list,
                                  amount=2,
                                  randomize=False)


def clean_list(drop_list):
    dl = list()
    splitter = 'https://www.instagram.com/'
    for line in drop_list:
        if splitter in line:
            dl.append(line.split(splitter)[1].strip('\n'))
    return dl


@client.on(events.NewMessage())
async def handler(event):
    global drop_list
    global drop_phase
    try:
        sender = await event.get_sender()
        # print(event.message.to_id.channel_id)  # Channel ID
        name = utils.get_display_name(sender)
        if drop_event_check(event, sender, 'open'):
            drop_list_reset()
            drop_phase = True
            print(event.message.is_channel)
            print(event.text)
            print(name, 'said', event.text, '!')
            print('\n-------------------------------\n')
        if drop_event_check(event, sender, 'close'):
            # drop_phase = False
            is_instalink(event)
            print(event.message.is_channel)
            print(event.text)
            print(name, 'said', event.text, '!')
            print('\n-------------------------------\n')
        if drop_list and drop_phase and instagram_link not in event.text:
            participate = False
            new_list = []
            for link in drop_list[0].split(' '):
                if my_insta_name in link:
                    participate = True
                if participate:
                    print(drop_list)
                    new_list = [name[1].strip('\n') for name in link.split(instagram_link)]
                    print(new_list)
            print("Running DROP LIST")
            await run_drop(new_list)
            drop_phase = False
            drop_list = []
        if event_checks(event):
            print("DING DING TIME TO POST!!!")
        print(f"event from {name}")
    except NameError as e:
        print(e)
try:
    print('(Press Ctrl+C to stop this)')
    client.run_until_disconnected()
finally:
    client.disconnect()