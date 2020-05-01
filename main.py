import sys
sys.path.insert(1, "./scripts")
import uploadImage as u
import webbrowser
import screenshot

# upload the image and creates a link on imgur
image = u.uploadImage('./resources/screenshot.jpg')
imageLink = image['link']
imageId = image['id']

# reverse image search the image on google images
url = "https://images.google.com/searchbyimage?image_url=" + imageLink
webbrowser.open_new_tab(url)

# delete the image using the image ID
u.deleteImage(imageId)
