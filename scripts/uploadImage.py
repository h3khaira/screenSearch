import json
import base64
import sys
import requests as r
sys.path.insert(1, "./resources")
import keys

client_id = keys.clientID
client_secret = keys.clientSecret
access_token = keys.accessToken
refresh_token = keys.refreshToken


def uploadImage(pathToImage):
    headers = {'Authorization': 'Client-ID %s' % client_id}
    with open(pathToImage, "rb") as img_file:
        base64String = base64.b64encode(img_file.read())
    payload = {'image': base64String, 'type': 'file'}

    response = r.post("https://api.imgur.com/3/upload",
                      json=payload,
                      headers=headers)

    print(response.json())

    return (response.json())


def deleteImage(imageId):
    try:
        client.delete_image(imageId)
    except:
        print("Failed to delete image")
