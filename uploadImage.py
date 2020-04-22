from imgurpython import ImgurClient
import keys
import requests as r

client_id = keys.clientID
client_secret = keys.clientSecret
access_token = keys.accessToken
refresh_token = keys.refreshToken

# allows the app to get write access to user account
client = ImgurClient(client_id, client_secret, access_token, refresh_token)


def uploadImage(pathToImage):
    config = {
        'name': 'screenshot',
        'title': 'screenshot',
        'description': 'screenshot to be searched'
    }
    try:
        image = client.upload_from_path(pathToImage, config=config, anon=False)
        print("Screenshot Link Created")
    except:
        print("Failed to upload image.")

    return (image)
