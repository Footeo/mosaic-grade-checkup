# Mosaic Grade Checkup

Fetches grades quickly from McMaster University Mosaic student portal

### Installation:

To use mosiac grade checkup:
1. You must have Python installed (at least 3.7.3).
2. You must install the selenium web driver library using Python installer. You can use the command below to install it.
`python -m pip install selenium`
3. You must install chromium web driver which can be found here (any version should work).
`https://chromedriver.chromium.org/downloads`

### Usage:

1. Download the project and open the `fetch.py` file in your text editior of choice. *Edit the username, password.*
2. *Edit the chromedriver path* as noted in the fetch.py file. Make sure to include chromedriver.exe at the end of the path, then save your changes.
3. Run the main.py file and you should see the following:  

<!-- ![What is this](img/Homescreen_v01.png | width = 100) -->
<img src="https://github.com/Footeo/mosaic-grade-checkup/blob/main/img/Homescreen_v01.png" width=350>  
4. Press continue then select one option from the tickboxes shown:  

<!-- ![What is this](img/Mainscreen_v01.png | width = 100) -->
<img src="https://github.com/Footeo/mosaic-grade-checkup/blob/main/img/Mainscreen_v01.png" width=350>  
5. Wait for the driver to run in the background and watch the grades come in! (on a good day it takes about 10 seconds, on a fast computer and internet connection max 5 seconds)  

<!-- ![What is this](img/Results_v01.png | width = 100) -->
<img src="https://github.com/Footeo/mosaic-grade-checkup/blob/main/img/Results_v01.png" width=300>

### Notes:  
I created a batch `.bat` file for myself, to lauch the program quickly, I recommend doing this as well.

### Credits:

Created by Oliver Foote  
Can be contacted on LinkedIn: (https://www.linkedin.com/in/oliver-foote/)

