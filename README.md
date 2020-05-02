
# screenSearch

screenSearch is a tool that allows for fast reverse image searching of screenshots taken by the user.

**Note**: This tool is not compatible with Python 2.

# How to set-up:
  * First create a local clone using `git clone https://github.com/h3khaira/screenSearch.git`

  * Then install the dependencies using `pip install -r requirements.txt`

  * Obtain the necessary API credentials in order to use imgur as the image hosting service for this tool.
    * You need to acquire a `Client ID` and `Client Secret`, which can be obtained by following [this guide](https://api.imgur.com/oauth2/addclient "guide")
    * You also need to obtain an Access token and Refresh token, which can be obtained by registering this application through postman, as shown in [this guide](https://apidocs.imgur.com/?version=latest)

  * Create a file called `keys.py` and insert the credentials obtained in the previous step. **Note**: This will give the tool read/write access to your imgur account:

     ```
     clientID = <Your Client ID>
     clientSecret = <Your Client Secret>
     accessToken = <Your Access Token>
     refreshToken = <Your Refresh Token>
     ```

     Then create a folder called `resources` and save the file in that folder.

  * Now you can use the tool by running `python main.py` in the home directory
