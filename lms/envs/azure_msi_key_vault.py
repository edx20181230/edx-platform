import requests
import json


def get_configs_from_keyvault(request_uri=None,payload=None,key_vault_url=None,key_name=None,api_version=None):
    """
    Read configurations from azure key vault
    """
    try:
        request_url = "{}/secrets/{}?api-version={}".format(key_vault_url, key_name, api_version)
        # get access token with Azure MSI 
        result = requests.get(request_uri, params=payload, headers={'Metadata': 'true'})
        access_token = result.json()['access_token']

        # get value from Azure keyvault using access token
        headers_credentials = {'Authorization': 'Bearer' + ' ' + (access_token)}
        response = requests.get(request_url, headers=headers_credentials)
        secrets = json.loads(response.json()['value'])

    except:
        secrets = {}

    return secrets
