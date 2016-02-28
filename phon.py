# Download the Python helper library from twilio.com/docs/python/install
from twilio.rest import TwilioRestClient

    # Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC067524dad918b6a9db9867f79aaa30de"
auth_token  = "fc941e15bd560bd15dd9ec17d6bdb9e4"
client = TwilioRestClient(account_sid, auth_token)
    
call = client.calls.create(url="http://demo.twilio.com/docs/voice.xml",
                           to="+19737389532",
                           from_="+18623079011")
print call.sid
