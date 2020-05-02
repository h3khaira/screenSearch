import sys
from os import remove
from time import sleep
sys.path.insert(1, "./scripts")
import uploadImage as u
import webbrowser
import screenshot

forcedExit = False
# upload the image and creates a link on imgur
try:
    image = u.uploadImage('./resources/screenshot.jpg')
    imageLink = image['link']
    imageId = image['id']
except UnboundLocalError:
    print("No screenshot found")
    forcedExit = True

if not forcedExit:
    # reverse image search the image on google images
    url = "https://images.google.com/searchbyimage?image_url=" + imageLink
    webbrowser.open_new_tab(url)

    # add delay to allow for image upload and search to finish
    sleep(0.5)
    # delete the image using the image ID
    u.deleteImage(imageId)
    remove('./resources/screenshot.jpg')
