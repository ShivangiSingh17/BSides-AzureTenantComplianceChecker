import requests, json

def checkLive(url: str) -> bool:
    try:
        response = requests.head(url, allow_redirects=True, timeout=5)
        if response.status_code == 200:
            return True
        else:
            return True
    except requests.exceptions.RequestException as e:
        return False
    
def getAuditSettings(id, token):
    url = "https://management.azure.com"+id+"/providers/Microsoft.Insights/diagnosticSettings?api-version=2021-05-01-preview"

    payload = {}
    headers = {
        'x-ms-client-session-id': '2ba9ad2625964024b1a616b69a016e40',
        'x-ms-command-name': 'Microsoft_Azure_Monitoring.',
        'Accept-Language': 'en',
        'Authorization': 'Bearer '+token.token,
        'x-ms-effective-locale': 'en.en-gb',
        'Content-Type': 'application/json',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
        'Cache-Control': 'no-cache',
        'x-ms-client-request-id': '3b8bdb93-184f-4ec4-bd6e-146cd85e6002',
        'Referer': ''
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    # print(response.json())
    
    if 'code' in response.json().keys() and response.json()['code'] == "ResourceTypeNotSupported":
        return []
    return response.json()['value']

def getDiskInfo(id, token):
    url = "https://management.azure.com/"+id+"?api-version=2023-10-02"

    payload = {}
    headers = {
    'x-ms-client-session-id': '2ba9ad2625964024b1a616b69a016e40',
    'x-ms-command-name': 'Microsoft_Azure_Monitoring.',
    'Accept-Language': 'en',
    'Authorization': 'Bearer '+token.token,
    'x-ms-effective-locale': 'en.en-gb',
    'Content-Type': 'application/json',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'Cache-Control': 'no-cache',
    'x-ms-client-request-id': '3b8bdb93-184f-4ec4-bd6e-146cd85e6002',
    'Referer': ''
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    # print(response.json())
    return response.json()['properties']
    
def getSecurityGroupRules(id,token):
    url = "https://management.azure.com/"+id+"?api-version=2023-09-01"

    payload = {}
    headers = {
    'x-ms-client-session-id': '2ba9ad2625964024b1a616b69a016e40',
    'x-ms-command-name': 'Microsoft_Azure_Monitoring.',
    'Accept-Language': 'en',
    'Authorization': 'Bearer '+token.token,
    'x-ms-effective-locale': 'en.en-gb',
    'Content-Type': 'application/json',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'Cache-Control': 'no-cache',
    'x-ms-client-request-id': '3b8bdb93-184f-4ec4-bd6e-146cd85e6002',
    'Referer': ''
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    # print(response.json())
    return response.json()['properties']['securityRules']

def getRoleAssignments(resource,token):
    url = "https://management.azure.com" + resource['id'] + "/providers/Microsoft.Authorization/roleAssignments?api-version=2022-04-01"

    payload = {}
    headers = {
    'x-ms-client-session-id': '2ba9ad2625964024b1a616b69a016e40',
    'x-ms-command-name': 'Microsoft_Azure_Monitoring.',
    'Accept-Language': 'en',
    'Authorization': 'Bearer '+token.token,
    'x-ms-effective-locale': 'en.en-gb',
    'Content-Type': 'application/json',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'Cache-Control': 'no-cache',
    'x-ms-client-request-id': '3b8bdb93-184f-4ec4-bd6e-146cd85e6002',
    'Referer': ''
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    return response.json()['value']

def getUsers(token):
    url = "https://graph.microsoft.com/v1.0/users"

    payload = {}
    headers = {
    'Accept-Language': 'en',
    'Authorization': 'Bearer '+token.token,
    'x-ms-effective-locale': 'en.en-gb',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'Accept': '*/*',
    'Referer': '',
    'x-ms-client-request-id': '221e598f-6ed0-4b0e-9ed4-af616624400c'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    x = response.json()['value']
    return [(x['userPrincipalName'],x['id']) for x in x]

def getApps(token):
    url = "https://graph.microsoft.com/v1.0/applications"

    payload = {}
    headers = {
    'Accept-Language': 'en',
    'Authorization': 'Bearer '+token.token,
    'x-ms-effective-locale': 'en.en-gb',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'Accept': '*/*',
    'Referer': '',
    'x-ms-client-request-id': '221e598f-6ed0-4b0e-9ed4-af616624400c'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    print(response)
    x = response.json()['value']
    return x

def getMFAStatus(token):
    users = getUsers(token)
    auth_status = {}
    for user in users:
        url = "https://graph.microsoft.com/beta/users/{}/authentication/methods".format(user[1])
        payload = {}
        headers = {
        'Accept-Language': 'en',
        'Authorization': 'Bearer '+token.token,
        'x-ms-effective-locale': 'en.en-gb',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
        'Accept': '*/*',
        'Referer': '',
        'x-ms-client-request-id': '221e598f-6ed0-4b0e-9ed4-af616624400c'
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        auth_methods = response.json()['value']
        # print(len(auth_methods))
        # for auth in auth_methods:
        #     if auth['@odata.type']!="#microsoft.graph.passwordAuthenticationMethod":
        if len(auth_methods) > 1:
            auth_status[user[0]] = True
        else:
            auth_status[user[0]] = False
    return auth_status

def getSubscriptions(token):
    url = "https://management.azure.com/subscriptions?api-version=2018-02-01"
    payload = {}
    headers = {
    'x-ms-client-session-id': '54dd9d1c22f541ed9bdd0814f13218e8',
    'x-ms-command-name': 'Microsoft_Azure_Billing.',
    'Accept-Language': 'en',
    'Authorization': 'Bearer '+token.token,
    'x-ms-effective-locale': 'en.en-gb',
    'Content-Type': 'application/json',
    'Accept': '*/*',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'Referer': '',
    'x-ms-client-request-id': '7df9bbbe-4ea3-46de-a157-77b6d49ee002'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    # print(response.json())
    return [(x['id'].split("/")[2],x['displayName']) for x in response.json()['value']]


def getResources(token, subscriptionIds):
    url = "https://management.azure.com/providers/Microsoft.ResourceGraph/resources?api-version=2021-03-01"

    payload = json.dumps({
    "subscriptions": subscriptionIds,
    "query": "Resources | project id, name, type, properties"
    })
    headers = {
    'Authorization': 'Bearer '+token.token,
    'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json()['data']

def getAuditCat(token,cat):
    url = "https://management.azure.com/api/invoke"

    payload = {}
    headers = {
    'x-ms-client-session-id': '2ba9ad2625964024b1a616b69a016e40',
    'x-ms-command-name': 'Microsoft_Azure_Monitoring.',
    'Accept-Language': 'en',
    'Authorization': 'Bearer '+token.token,
    'x-ms-effective-locale': 'en.en-gb',
    'Content-Type': 'application/json',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'Cache-Control': 'no-cache',
    'x-ms-path-query': cat,
    'x-ms-client-request-id': '3b8bdb93-184f-4ec4-bd6e-146cd85e6002',
    'Referer': ''
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    x = response.json()['value']
    return [x['name'] for x in x]
    
def getLogStatus(cat,cate,token):
    url = "https://management.azure.com/api/invoke"

    payload = {}
    headers = {
      'Accept-Language': 'en',
      'Authorization': 'Bearer '+token.token,
      'x-ms-effective-locale': 'en.en-gb',
      'Content-Type': 'application/json',
      'Accept': 'application/json, text/javascript, */*; q=0.01',
      'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
      'Cache-Control': 'no-cache',
      # 'x-ms-path-query': '/providers/'+ cat +'/diagnosticSettings?api-version=2017-04-01-preview',
      'x-ms-path-query': cat,
      'Referer': ''
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    c_info = {}
    all_cat = getAuditCat(cate)
    for i in all_cat:
      c_info[i] = [False,0]
    # print(response.json())
    audit_status = response.json()['value']
    if len(audit_status) > 0:
      for x in audit_status:
        for y in x['properties']['logs']:
          c_info[y['category']] = [y['enabled'],y['retentionPolicy']['days']]

    return c_info