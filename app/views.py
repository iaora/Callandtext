from flask import render_template, flash, redirect, request, url_for
from app import app, db, client
from app.models import Person
from urllib2 import urlopen
import random
import time

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

        print "apples"

        choice = request.form['choice']
        repeat = request.form['repeat']
        i = 0
        if repeat is None:
            repeat = 1
        print choice
        print repeat
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
            
            while i < int(repeat):
                print i
                client.messages.create(to='+1'+out_phone_number,
                                   from_='+18623079011',
                                   body=request.form['body'])
                time.sleep(5)
                i=i+1

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
