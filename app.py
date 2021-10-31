from flask import Flask, request, redirect, session, render_template
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import time
import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


app = Flask(__name__)

# A welcome message to test our server
@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run()
