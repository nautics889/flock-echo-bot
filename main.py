"""Echo-bot for Flock messenger.

An example of Flock application.


:copyright: (c) nautics889
"""

import os
import time
from typing import Dict
from urllib.parse import urlencode

import requests
import uvicorn
from fastapi import FastAPI, Response, status, BackgroundTasks

DELAY_AFTER_INSTALL = 2


def init_chat(user_id):
    """Initialize chat with Flock user.

    :param user_id: Flock user ID.
    :return: None
    """
    time.sleep(DELAY_AFTER_INSTALL)
    data = {
        "to": user_id,
        "text": "You have successfully installed echo bot!",
        "token": os.environ["BOT_TOKEN"],
    }
    requests.post(
        "https://api.flock.co/v1/chat.sendMessage",
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        data=urlencode(data),
        timeout=15.0)


def do_echo(user_id, msg):
    """Simply repeats after Flock user.

    :param user_id: Flock user ID.
    :param msg: Message that user has sent to bot.
    :return: None
    """
    data = {
        "to": user_id,
        "text": msg,
        "token": os.environ["BOT_TOKEN"],
    }
    requests.post(
        "https://api.flock.co/v1/chat.sendMessage",
        headers={"Content-Type": "application/x-www-form-urlencoded"},
        data=urlencode(data),
        timeout=15.0)


def dispatcher(payload: Dict, response: Response, bg_tasks: BackgroundTasks):
    """Entry point function for handling callbacks from Flock.

    :param payload: Deserialized JSON data from Flock. Contains event
                    information.
    :param response: Object that represents the response on request.
    :param bg_tasks: Facade for background tasks.
    :return: None
    """
    evt = payload.get('name')
    user_id = payload.get('userId')
    if evt == "app.install":
        response.status_code = status.HTTP_201_CREATED
        bg_tasks.add_task(
            init_chat, user_id)

    elif evt == "chat.receiveMessage":
        do_echo(user_id, payload.get("message", {}).get("text", "null"))
        response.status_code = status.HTTP_200_OK


def main():
    app = FastAPI()
    app.post('/')(dispatcher)

    uvicorn.run(app, host=os.environ.get('HOST', '0.0.0.0'),
                port=os.environ.get('PORT', 8273))


if __name__ == '__main__':
    main()
