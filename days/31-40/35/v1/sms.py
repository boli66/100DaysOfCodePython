import requests
from twilio.rest import Client

number = "+17865653686"
accountSID = "ACa90676daac1d85e50cc385a03bca361c"
auth_token = "0bcc43a36fe298873b526e11a017ea48"

client = Client(accountSID, auth_token)

message = client.messages.create(
  from_='+17865653686',
  body='Hello',
  to='+46793390907'
)

print(message.sid)