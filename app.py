
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


def createCheck(token, collectionURL, name, ref, nameOnCheck, amount, invoice, description, attachment):
    # notion
    client = NotionClient(token)
    cv = client.get_collection_view(collectionURL)
    row = cv.collection.add_row()
    row.name = name
    row.ref = ref
    row.nameOnCheck = nameOnCheck
    row.amount = amount
    row.invoice = invoice
    row.description = description
    row.attachment = attachment


def createTask(token, collectionURL, description):
    # notion
    client = NotionClient(token)
    cv = client.get_collection_view(collectionURL)
    row = cv.collection.add_row()
    row.task = description


def createVoicemail(token, collectionURL, title, description, phone, attachments, date):
    # notion
    client = NotionClient(token)
    cv = client.get_collection_view(collectionURL)
    row = cv.collection.add_row()
    row.title = title
    row.description = description
    row.phone = phone
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


@app.route('/checks', methods=['GET'])
def checks():
    name = request.args.get('name')
    ref = request.args.get('ref')
    nameOnCheck = request.args.get('nameOnCheck')
    amount = request.args.get('amount')
    invoice = request.args.get('invoice')
    description = request.args.get('description')
    attachment = request.args.get('attachment')
    token_v2 = os.environ.get("TOKEN")
    url = os.environ.get("CHECKSURL")
    createCheck(token_v2, url, name, ref, nameOnCheck, amount, invoice, description, attachment)
    return f'added {name} to Notion'


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
    phone = request.args.get('phone')
    attachments = request.args.get('attachments')
    date = request.args.get('date')
    token_v2 = os.environ.get("TOKEN")
    url = os.environ.get("VOICEMAILURL")
    createVoicemail(token_v2, url, title, description, phone, attachments, date)
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
