import os
from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv()  # Loads .env file


# Twilio Account SID and Auth Token
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                    body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                    from_=os.environ['TWILIO_NUMBER'],
                    to=os.environ['RECEIVER_NUMBER']
                )

print(message.sid)
