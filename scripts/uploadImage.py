import requests as r

client_id = 'c68e3c744266e70'


def uploadImage(pathToImage):
    headers = {'Authorization': 'Client-ID %s' % client_id}

    payload = {
        'type': 'file',
        'title': 'screenSearch Screenshot',
        'description': 'image uploaded by the screenSearch project'
    }

    files = {'image': open(pathToImage, 'rb')}

    try:
        response = r.post("https://api.imgur.com/3/upload",
                          json=payload,
                          headers=headers,
                          files=files)
    except r.exceptions.RequestException as e:
        raise SystemExit(e)

    return (response.json())


def deleteImage(deleteHash):
    headers = {'Authorization': 'Client-ID %s' % client_id}
    try:
        response = r.delete("https://api.imgur.com/3/image/" + deleteHash,
                            headers=headers)
    except r.exceptions.RequestException as e:
        raise SystemExit(e)
    return (response.json())
