
from instamojo_wrapper import Instamojo
from minishop.settings import PAYMENT_API_AUTH_TOKEN,PAYMENT_API_KEY
api = Instamojo(api_key=PAYMENT_API_KEY,
                auth_token=PAYMENT_API_AUTH_TOKEN,endpoint='https://test.instamojo.com/api/1.1/')


# Create a new Payment Request
response = api.payment_request_create(
    amount='100',
    purpose='Testing..',
    send_email=True,
    email="paramsiddha@gmail.com",
    redirect_url="https://paramsiddha.wordpress.com"
    )
# print the long URL of the payment request.
url= response['payment_request']['longurl']

print(url)

'''
from instamojo_wrapper import Instamojo
from minishop.settings import PAYMENT_API_AUTH_TOKEN,PAYMENT_API_KEY
api = Instamojo(api_key=PAYMENT_API_KEY,
                auth_token=PAYMENT_API_AUTH_TOKEN)


# Create a new Payment Request
response = api.payment_request_create(
    amount='100',
    purpose='Payment',
    send_email=True,
    email="paramsiddha@gmail.com",
    redirect_url="https://paramsiddha.wordpress.com"
    )
# print the long URL of the payment request.
url= response['payment_request']['longurl']

print(url)
'''
