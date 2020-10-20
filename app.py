
import os
from notion.client import NotionClient
from flask import Flask
from flask import request


app = Flask(__name__)

def trackWeather(token, URL, weather):
    # notion
    client = NotionClient(token)
    block = client.get_block(URL)
    block.title = weather


def createTweet(token, collectionURL, tweet, author, followers):
    # notion
    client = NotionClient(token)
    cv = client.get_collection_view(collectionURL)
    row = cv.collection.add_row()
    row.tweet = tweet
    row.author = author
    row.followers = followers


def createTask(token, collectionURL, description):
    # notion
    client = NotionClient(token)
    cv = client.get_collection_view(collectionURL)
    row = cv.collection.add_row()
    row.task = description


def createVoicemail(token, collectionURL, title, description, url, date):
    # notion
    client = NotionClient(token)
    cv = client.get_collection_view(collectionURL)
    row = cv.collection.add_row()
    row.title = title
    row.description = description
    row.attachments = attachments
    row.date = date


def createEmail(token, collectionURL, sender, subject, message_url):
    # notion
    client = NotionClient(token)
    cv = client.get_collection_view(collectionURL)
    row = cv.collection.add_row()
    row.sender = sender
    row.subject = subject
    row.message_url = message_url


@app.route('/twitter', methods=['GET'])
def twitter():
    tweet = request.args.get('tweet')
    author = request.args.get('author')
    followers = request.args.get('followers')
    token_v2 = os.environ.get("TOKEN")
    url = os.environ.get("URL")
    createTweet(token_v2, url, tweet, author, followers)
    return f'added {tweet} to Notion'


@app.route('/tasks', methods=['GET'])
def tasks():
    todo = request.args.get('task')
    token_v2 = os.environ.get("TOKEN")
    url = os.environ.get("URL")
    createTask(token_v2, url, todo)
    return f'added {todo} to Notion'


@app.route('/voicemail', methods=['GET'])
def voicemail():
    title = request.args.get('title')
    description = request.args.get('description')
    attachments = request.args.get('attachments')
    date = request.args.get('date')
    token_v2 = os.environ.get("TOKEN")
    url = os.environ.get("URL")
    createVoicemail(token_v2, url, title, description, attachments, date)
    return f'added {title} voicemail to Notion'


@app.route('/createemail', methods=['GET'])
def gmailUrgentEmail():
    sender = request.args.get('sender')
    subject = request.args.get('subject')
    message_url = request.args.get('url')
    token_v2 = os.environ.get("TOKEN")
    url = os.environ.get("URL")
    createEmail(token_v2, url, sender, subject, message_url)
    return f'added email from {sender} to Notion'

@app.route('/getweather', methods=['GET'])
def getWeather():
    weather = str(request.args.get('weather'))
    token_v2 = os.environ.get("TOKEN")
    url = os.environ.get("URL")
    trackWeather(token_v2, url, weather)
    return f'added {weather} to Notion'


if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
