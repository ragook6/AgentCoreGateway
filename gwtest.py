import requests
import json

CLIENT_ID = "5vjqer9evb9f1nkgdbned5b1r8"
CLIENT_SECRET = "acg7obfrap1apu0luasu175r347s4m0i2n4c4a0i80dth3dga1f"
TOKEN_URL = "https://us-west-2q9qogi9qn.auth.us-west-2.amazoncognito.com/oauth2/token"

def fetch_access_token(client_id, client_secret, token_url):
  response = requests.post(
    token_url,
    data="grant_type=client_credentials&client_id={client_id}&client_secret={client_secret}".format(client_id=client_id, client_secret=client_secret),
    headers={'Content-Type': 'application/x-www-form-urlencoded'}
  )
  print("This is Auth Token:", response.json()['access_token'])
  return response.json()['access_token']

def list_tools(gateway_url, access_token):
  headers = {
      "Content-Type": "application/json",
      "Authorization": f"Bearer {access_token}"
  }

  payload = {
      "jsonrpc": "2.0",
      "id": "list-tools-request",
      "method": "tools/list"
  }

  response = requests.post(gateway_url, headers=headers, json=payload)
  print("This is List Tools:", response.json())
  return response.json()

def call_tool(gateway_url, access_token, tool_name, arguments):
  headers = {
      "Content-Type": "application/json",
      "Authorization": f"Bearer {access_token}"  
  }

  payload = {
      "jsonrpc": "2.0",
      "id": "call-tool-request",
      "method": "tools/call",
      "params": {
          "name": tool_name,      # Tool identifier
          "arguments": arguments # Input parameters for the tool
      }
  }

  response_tool = requests.post(gateway_url, headers=headers, json=payload)
  print("Travel Package Details:", response_tool.json())
  return response_tool.json()

# Example usage
gateway_url = "https://gateway-quick-vacation-planner-ckdzxxixc0.gateway.bedrock-agentcore.us-west-2.amazonaws.com/mcp"
access_token = fetch_access_token(CLIENT_ID, CLIENT_SECRET, TOKEN_URL)
tools = list_tools(gateway_url, access_token)
print(json.dumps(tools, indent=2))

# Call the travel packages tool
tool_response = call_tool(gateway_url, access_token, "traveltool___get_travel_packages", {"city": "Mumbai"})
print(tool_response)