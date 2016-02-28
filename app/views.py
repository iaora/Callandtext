from flask import render_template, flash, redirect, request, url_for
from twilio.rest import TwilioRestClient

from app import app, db
from app.models import Person
from urllib2 import urlopen
import random

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html');
    if request.method == 'POST':
        print "kumquat"
        out_phone_number = request.form['out_phone']

        #if no phone number 
        if out_phone_number is None:
            return render_template('error.html')
        if not is_number(out_phone_number):
            return render_template('error.html')
        print "peaches"
        print out_phone_number
        account_sid = "AC067524dad918b6a9db9867f79aaa30de"
        auth_token  = "fc941e15bd560bd15dd9ec17d6bdb9e4"

        client = TwilioRestClient(account_sid, auth_token)

        print "apples"

        choice = request.form['choice']
        print choice
        if choice == 'Call':
            print "bannanananana"

            client.calls.create(url="http://demo.twilio.com/docs/voice.xml",
                                    to="+1" + out_phone_number,
                                    from_="+18623079011")

            print "raspberries"
            return render_template('success.html',
                                    out_phone=out_phone_number,
                                    choice=choice)
        if choice == 'Text':
            print "blurple"
            client.messages.create(to='+1'+out_phone_number,
                                   from_='+18623079011',
                                   body=request.form['body'])

            print "white"
            return render_template('success.html', 
                                    out_phone=out_phone_number,
                                    choice=choice)

    return render_template('error.html')



def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
