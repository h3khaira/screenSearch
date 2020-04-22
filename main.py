# Note: in order to do a google image reverse image search, just type the URL https://images.google.com/searchbyimage?image_url= and add the image URL to the end
import uploadImage as u

image = u.uploadImage('test.jpg')
imageLink = image['link']
imageId = image['id']
