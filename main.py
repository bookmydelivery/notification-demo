registration_token = ''

import requests
import json

server_token = ""
deviceToken = registration_token

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'key=' + server_token,
}

body = {
    'notification': {'title': 'Sending push form python script',
                     'body': 'New Message'
                     },
    'to':
        deviceToken,
    'priority': 'high',
    #   'data': dataPayLoad,
}
response = requests.post("https://fcm.googleapis.com/fcm/send", headers=headers, data=json.dumps(body))
print(response.status_code)

print(response.json())
