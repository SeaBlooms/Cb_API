import requests, json

#Prep request header and URL
authJson={
'X-Auth-Token': 'D1E83724-XXXX-XXXX-XXXX-BB8232528F75', #Replace with actual API token
'content-type': 'application/json'
}
b9StrongCert = False #Set to True if the CbP server has a signed IIS cert
url = 'https://10.xx.xx.xx/api/bit9platform/v1/fileRule' # Replace with Cb Protection server DNS/IP

#Contents of the API request being made
data = {'hash': 'XXXXFAA5BA63D03039A0B614D2ED724C9C3DD724A1F487F3B6B5B8C280F9DE74', 'fileState': 3}
r = requests.post(url, json.dumps(data), headers=authJson, verify=b9StrongCert)
r.raise_for_status() # Check if the call was successful
fileRule = r.json() # get resulting file rule object in JSON
