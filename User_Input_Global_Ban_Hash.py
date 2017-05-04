import requests, json

user_inputs = {}
Server = input("Enter the FQDN or IP of your Cb Protection Server : ")
API = input('Enter your API Token : ')
Hash = input('Enter the SHA256 of the file to ban : ')

#Prep request header and URL
authJson={
'X-Auth-Token': '{0}'.format(API), #Replace with actual API token
'content-type': 'application/json'
}
b9StrongCert = False #Set to True if the CbP server has a signed IIS cert
url = 'https://{0}/api/bit9platform/v1/fileRule'.format(Server) # Replace with server DNS/IP

#Contents of the API request being made
data = {'hash': '{0}'.format(Hash), 'fileState': 3}
r = requests.post(url, json.dumps(data), headers=authJson, verify=b9StrongCert)
r.raise_for_status() # Check if the call was successful
fileRule = r.json() # get resulting file rule object in JSON
