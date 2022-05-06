import requests
from digishop.settings import EMAIL_SERVICE_ENDPOINT, EMAIL_SENDER_NAME, EMIAL_SENDER_EMAIL, EMAIL_API_KEY

import  json



def sendEmail(name, email, subject, htmlContent):
    payload = {
        "sender": {
            "name": EMAIL_SENDER_NAME,
            "email": EMIAL_SENDER_EMAIL
        },
        "to": [
            {
                "email": email,
                'name': name

            }
        ],
        'replyTo': {
            "email": EMIAL_SENDER_EMAIL,
            "name": EMAIL_SENDER_NAME
        },
        "htmlContent": htmlContent,
        'subject': subject
    }

    headers = {
        'accept': "application/json",
        'content-type': "application/json",
        'api-key': EMAIL_API_KEY
    }

    response = requests.request("POST",
                                EMAIL_SERVICE_ENDPOINT,
                                data=json.dumps(payload),
                                headers=headers)

    return response
