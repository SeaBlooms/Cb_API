import time
from datetime import datetime
import sys
import os

# Include our common folder, presumably peer of current folder
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'common'))
import bit9api

bit9 = bit9api.bit9Api(
    "https://10.xx.xx.xx",  # Replace with actual Bit9 server URL
    token="D1E83724-xxxx-xxxx-xxxx-BB8232528F75",  # Replace with actual Bit9 API user token
    ssl_verify=False  # Don't validate server's SSL certificate. Set to True unless using self-signed cert on IIS
)

# Setup our arguments (these could be, for example, passed from the command line)
targetPolicyName = "POLICY_NAME"  # Target policy name
computerCondition = ['name:DOMAIN\HOSTNAME']  # Condition for computers to move

# Find our destination policy by name
destPolicies = bit9.search('v1/policy', ['name:'+targetPolicyName])
if len(destPolicies)==0:
    raise ValueError("Cannot find destination policy "+targetPolicyName)

# Our condition is "The computer with the defined hostname"
comps = bit9.search('v1/computer', computerCondition)
for c in comps:  # Move each returned computer to the defined policy
    print("Moving computer %s from policy %s to policy %s" %
          (c['name'], c['policyName'], targetPolicyName))
    c['policyId'] = destPolicies[0]['id']
bit9.update('v1/computer', c)