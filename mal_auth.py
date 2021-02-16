import secrets
import requests


client_ID = 'YOUR_CLIENT_ID'
client_Secret = "YOUR_CLIENT_SECRET"


# accessing mal api 
# generate code_challenge and code verifier for auth
# This function is dev by ZeroCrystal's (url : https://myanimelist.net/blog.php?eid=835707)
def get_new_code_verifier() -> str:
    token = secrets.token_urlsafe(100)
    return token[:128]

# build url : 
def auth_url(client_id, code_challenge):
    app = "https://myanimelist.net/v1/oauth2/authorize?response_type=code&client_id={}&code_challenge={}".format(client_id, code_challenge)
    print("Application : {}\n\n".format(app))
    # click on Allow button
    # take the parameter code in the url after clicking on allow

def generate_token(client_id, client_secret, code, code_verifier):
    params = {
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': 'authorization_code',
        'code': code,
        'code_verifier': code_verifier
    }
    req = requests.post('https://myanimelist.net/v1/oauth2/token', data=params)
    print("Status ", req.status_code)
    rep_json = req.json()
    print('Nice\n')
    token = rep_json['access_token']
    refresh_token = rep_json['refresh_token']
    expiration = rep_json['expires_in']

    print(f"Informations : \n-access-token : {token}\n-refresh_token : {refresh_token}\n-expiration : {expiration}\n You can now call mal api\nSaving token in token.txt...")
    fic = open('token.txt', 'w')
    fic.write(token)
    _fic = open('refresh_token.txt', 'w')
    _fic.write(refresh_token)

    
code_verifier = code_challenge = get_new_code_verifier()
auth_url(client_ID, code_challenge)
code = input('Code : ')
generate_token(client_ID, client_Secret, code, code_verifier)
