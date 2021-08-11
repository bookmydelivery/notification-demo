# This registration token comes from the client FCM SDKs.
from firebase_admin import messaging

registration_token = ''

# See documentation on defining a message payload.
message = messaging.Message(
    data={'notification': {
        'title': '`$FooCorp` up 1.43% on the day',
        'body': 'FooCorp gained 11.80 points to close at 835.67, up 1.43% on the day.'
    }, },
    token=registration_token,
)

# Send a message to the device corresponding to the provided
# registration token.
response = messaging.send(message)
# Response is a message ID string.
print('Successfully sent message:', response)
