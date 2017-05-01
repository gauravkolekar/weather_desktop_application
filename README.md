# About the Repository
This repository contains the code that I wrote to understand how tkinter works in python. I have created a very simple weather application that takes Latitude and Longitude from the user and displays the some information in the display area. I have used Python request library to send a request to National Weather Service SOAP server. I parse the returned XML for required information and display it in the display read. To the parse the returned XML I have used Beautiful Soup Python Library.

# Required Python Libraries
beautifulsoup4==4.5.3
lxml==3.7.3
requests==2.13.0

Please pip install the above libraries.
You can also install the libraries from the given requirements.txt file using pip -r command.
pip -r requirements.txt

# How to run the code:
To run the code use the command python weather_app.py
The code uses tkinter library from python. Please enter the latitude and longitude. Hit 'ENTER' button you will the required
data. If you hit 'RESET' button it will go get the new data if its has been updated on the SOAP server.
