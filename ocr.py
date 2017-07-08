########### Python 3.6 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64, json
from urllib.request import urlopen
###############################################
#### Update or verify the following values. ###
###############################################

# Replace the subscription_key string value with your valid subscription key.
subscription_key = '3164548630cc481292b82213a219e8ca'

# Replace or verify the region.
# You must use the same region in your REST API call as you used to obtain your subscription keys.
# For example, if you obtained your subscription keys from the westus region, replace 
# "westcentralus" in the URI below with "westus".
#
# NOTE: Free trial subscription keys are generated in the westcentralus region, so if you are using
# a free trial subscription key, you should not need to change this region.
uri_base = 'westcentralus.api.cognitive.microsoft.com'

headers = {
    # Request headers.
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': subscription_key,
}

params = urllib.parse.urlencode({
    # Request parameters. The language setting "unk" means automatically detect the language.
    'language': 'unk',
    'detectOrientation ': 'true',
})

# The URL of a JPEG image containing text.
body = "{'url':'https://i.stack.imgur.com/vrkIj.png'}"

try:
    # Execute the REST API call and get the response.
    conn = http.client.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')
    conn.request("POST", "/vision/v1.0/ocr?%s" % params, body, headers)
    #response = conn.getresponse()
    #data = response.read()

    # 'data' contains the JSON data. The following formats the JSON data for display.
    #parsed = json.loads(data)
    response = conn.getresponse().read().decode('utf8')
    parsed = json.loads(response)

    print ("Response:")
    print (json.dumps(parsed, sort_keys=True, indent=2))
    conn.close()

except Exception as e:
    print('Error:')
    print(e)
####################################