import requests, json

#Prep request header and URL
authJson={
'X-Auth-Token': 'D1E83724-DE6B-4542-B425-BB8232528F75', #Replace with actual API token
'content-type': 'application/json'
}
b9StrongCert = False #Set to True if the CbP server has a signed IIS cert
url = 'https://10.0.0.253/api/bit9platform/v1/fileRule' # Replace with Cb Protection server DNS/IP

#Contents of the API request being made
data = {'hash': '9717F5BC0B1A692A80D2955B5313F9C0959999DBDD250196B1DEFFF191965AD0', 'fileState': 3}
r = requests.post(url, json.dumps(data), headers=authJson, verify=b9StrongCert)
r.raise_for_status() # Check if the call was successful
fileRule = r.json() # get resulting file rule object in JSON
