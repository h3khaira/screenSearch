
# screenSearch

screenSearch is a tool that allows for fast reverse image searching of screenshots taken by the user.

**Note**: This tool is not compatible with Python 2.

# How to set-up:
  * First create a local clone using `git clone https://github.com/h3khaira/screenSearch.git`

  * Then install the dependencies using `pip install -r requirements.txt`

  * Now you can use the tool by running `python main.py` in the home directory

# Usage:

Running `python main.py` opens up the following widget:
![Widget Picture](https://github.com/h3khaira/screenSearch/blob/master/resources/widget.PNG "Widget Picture")

Press `Select Region` to highlight the area of your screen which you would like to capture. Click and drag your mouse to select the region for capture.

Then, press `Take Screenshot`, which will promply capture the specified region of your screen and perform a reverse image search on google. The widget will then shut down.
