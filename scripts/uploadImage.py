from imgurpython import ImgurClient
import sys
sys.path.insert(1, "./resources")
import keys

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


def deleteImage(imageId):
    try:
        client.delete_image(imageId)
    except:
        print("Failed to delete image")
