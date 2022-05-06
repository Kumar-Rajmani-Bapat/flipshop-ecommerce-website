__author__ = 'Maruf Maniruzzaman'


import logging
import collections

import urlparse
import urllib2
import urllib
from datetime import *
import base64
import hmac
import hashlib
from urllib2 import HTTPError

import xml.etree.cElementTree as ET

from payment import Base

logger = logging.getLogger(__name__)


class SimplePay(Base):

    def __init__(self, access_key, secret_key, request_url, fps_url):
        Base.__init__(self)
        self.access_key = access_key
        self.secret_key = secret_key
        self.request_url = request_url
        self.FPS_URL = fps_url

    def create_form_inputs(self, amount, description, referenceId=None, immediateReturn=None, returnUrl=None,
                           abandonUrl=None, process_immediate=None, ipnUrl=None, collect_shipping_address=None):

        form_inputs = {'accessKey': self.access_key, 'amount': str(amount), 'description': description,
                       "signatureVersion": "2", "signatureMethod": "HmacSHA256"}

        if referenceId is not None:
            form_inputs['referenceId'] = str(referenceId)
        if immediateReturn is not None:
            form_inputs['immediateReturn'] = str(immediateReturn)
        if returnUrl is not None:
            form_inputs['returnUrl'] = returnUrl
        if abandonUrl is not None:
            form_inputs['abandonUrl'] = abandonUrl
        if process_immediate is not None:
            form_inputs['process_immediate'] = process_immediate
        if ipnUrl is not None:
            form_inputs['ipnUrl'] = ipnUrl

        if collect_shipping_address is not None:
            form_inputs['collectShippingAddress'] = str(collect_shipping_address)

        signature = self.generate_signature(self.secret_key, "POST", form_inputs, self.request_url)
        form_inputs['signature'] = signature

        return form_inputs

    def generate_form(self, form_inputs, request_url):
        assert isinstance(form_inputs, dict)
        inputs = ['<input type="image" src="https://authorize.payments.amazon.com/pba/images/payNowButton.png" border="0" />']

        for key in form_inputs.keys():
            value = form_inputs[key]
            if value:
                inputs.append('<input type="hidden" name="{0}" value="{1}" />'.format(key, value))

        inputs_str = "\n    ".join(inputs)
        form_str = '<form action="{0}" method="POST">\n    '.format(request_url) + inputs_str + '\n</form>\n'

        return form_str

    def verify_success_return(self, data, success_url):
        """
        This function verifies a success return from Amazon.
        It queries Amazon to make sure the response was valid.

        :param data: all query key/values as dict (something like request.GET.urlencode())
        :param success_url: url that was set as success_url while creating input form
        :return: Status as either "VerifyFailed" or Success
        """

        if not self.verify_signature(data, "GET", success_url):
            logger.error("Validation of Amazon request failed.")
            return "VerifyFailed"

        return "Success"

    def execute_fps(self, action, method, **params):
        """
        Make a request against the FPS api.
        """

        values = {"AWSAccessKeyId": self.access_key,
                  "SignatureMethod": "HmacSHA256",
                  "SignatureVersion": 2,
                  "Timestamp": datetime.utcnow().isoformat() + '-00:00',
                  "Version": "2008-09-17",
                  "Action": action}
        values.update(params)
        values["Signature"] = self.generate_signature(self.secret_key, method, values, self.FPS_URL)
        url = "%s?%s" % (self.FPS_URL, urllib.urlencode(values))
        request = urllib2.Request(url)
        try:
            req = urllib2.urlopen(request)
            response = req.read()
        except HTTPError, e:
            if e.code == 400:
                response = e.read()
            else:
                raise
        return response

    def verify_signature(self, raw_data, http_method, endpoint_uri):

        response = self.execute_fps(
            "VerifySignature",
            http_method,
            UrlEndPoint=endpoint_uri,
            HttpParameters=raw_data)

        xml = ET.XML(response)
        el = xml.find(".//{http://fps.amazonaws.com/doc/2008-09-17/}VerificationStatus")
        return el is not None and el.text == "Success"

    @staticmethod
    def generate_signature(secret_key, verb, values, request_url):
        """
        Generate signature for call. (same signature is used for CBUI call)

        NOTE: Python's urlencode doesn't work for Amazon. Spaces need to be %20
        and not +. This only affects the signature generation, not the
        key/values submitted.
        """
        keys = values.keys()
        keys.sort()

        sorted_values = collections.OrderedDict([(k, values[k]) for k in keys])
        query = urllib.urlencode(sorted_values)
        query = query.replace("+", "%20")
        parsed = urlparse.urlsplit(request_url)
        base = "%(verb)s\n%(hostheader)s\n%(requesturi)s\n%(query)s" % {
               "verb": verb.upper(),
               "hostheader": parsed.hostname.lower(),
               "requesturi": parsed.path,
               "query": query}
        s = hmac.new(secret_key, base, hashlib.sha256)
        return base64.encodestring(s.digest())[:-1]
