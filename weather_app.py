"""
Name: Gaurav Vivek Kolekar
Mavs Id: 1001267145
"""
from tkinter import *

from bs4 import BeautifulSoup
import requests
import datetime
from time import strftime

lat_data = None
long_data = None


def find_weather():

    print_info = ''
    global lat_data
    global long_data

    if lat_data is None and long_data is None:
        lat_data = lat_entry.get()
        long_data = long_entry.get()
    # print(lat_data, long_data)
    tommorow = datetime.datetime.now() + datetime.timedelta(days=1)

    url = 'https://graphical.weather.gov:443/xml/SOAP_server/ndfdXMLserver.php'
    headers = {'content-type': 'text/xml'}
    body = """<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/" SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
    <SOAP-ENV:Body>
    <ns3591:NDFDgen xmlns:ns3591="uri:DWMLgen">
    <latitude xsi:type="xsd:string">{}</latitude>
    <longitude xsi:type="xsd:string">{}</longitude>
    <product xsi:type="xsd:string">time-series</product>
    <startTime xsi:type="xsd:string">{}</startTime>
    <endTime xsi:type="xsd:string">{}</endTime>
    <Unit xsi:type="xsd:string">e</Unit>
    <weatherParameters>
    <maxt xsi:type="xsd:boolean">1</maxt>
    <mint xsi:type="xsd:boolean">1</mint>
    <temp xsi:type="xsd:boolean">0</temp>
    <td xsi:type="xsd:boolean">0</td>
    <pop12 xsi:type="xsd:boolean">1</pop12>
    <qpf xsi:type="xsd:boolean">0</qpf>
    <sky xsi:type="xsd:boolean">0</sky>
    <snow xsi:type="xsd:boolean">0</snow>
    <wspd xsi:type="xsd:boolean">1</wspd>
    <wdir xsi:type="xsd:boolean">1</wdir>
    <wx xsi:type="xsd:boolean">0</wx>
    <waveh xsi:type="xsd:boolean">0</waveh>
    <icons xsi:type="xsd:boolean">1</icons>
    <critfireo xsi:type="xsd:boolean">0</critfireo>
    <dryfireo xsi:type="xsd:boolean">0</dryfireo>
    <rhm xsi:type="xsd:boolean">0</rhm>
    <apt xsi:type="xsd:boolean">0</apt>
    <tcwspdabv34i xsi:type="xsd:boolean">0</tcwspdabv34i>
    <tcwspdabv50i xsi:type="xsd:boolean">0</tcwspdabv50i>
    <tcwspdabv64i xsi:type="xsd:boolean">0</tcwspdabv64i>
    <tcwspdabv34c xsi:type="xsd:boolean">0</tcwspdabv34c>
    <tcwspdabv50c xsi:type="xsd:boolean">0</tcwspdabv50c>
    <tcwspdabv64c xsi:type="xsd:boolean">0</tcwspdabv64c>
    <conhazo xsi:type="xsd:boolean">0</conhazo>
    <ptornado xsi:type="xsd:boolean">0</ptornado>
    <phail xsi:type="xsd:boolean">0</phail>
    <ptstmwinds xsi:type="xsd:boolean">0</ptstmwinds>
    <pxtornado xsi:type="xsd:boolean">0</pxtornado>
    <pxhail xsi:type="xsd:boolean">0</pxhail>
    <pxtstmwinds xsi:type="xsd:boolean">0</pxtstmwinds>
    <ptotsvrtstm xsi:type="xsd:boolean">0</ptotsvrtstm>
    <ptotxsvrtstm xsi:type="xsd:boolean">0</ptotxsvrtstm>
    <tmpabv14d xsi:type="xsd:boolean">0</tmpabv14d>
    <tmpblw14d xsi:type="xsd:boolean">0</tmpblw14d>
    <tmpabv30d xsi:type="xsd:boolean">0</tmpabv30d>
    <tmpblw30d xsi:type="xsd:boolean">0</tmpblw30d>
    <tmpabv90d xsi:type="xsd:boolean">0</tmpabv90d>
    <tmpblw90d xsi:type="xsd:boolean">0</tmpblw90d>
    <prcpabv14d xsi:type="xsd:boolean">0</prcpabv14d>
    <prcpblw14d xsi:type="xsd:boolean">0</prcpblw14d>
    <prcpabv30d xsi:type="xsd:boolean">0</prcpabv30d>
    <prcpblw30d xsi:type="xsd:boolean">0</prcpblw30d>
    <prcpabv90d xsi:type="xsd:boolean">0</prcpabv90d>
    <prcpblw90d xsi:type="xsd:boolean">0</prcpblw90d>
    <precipa_r xsi:type="xsd:boolean">0</precipa_r>
    <sky_r xsi:type="xsd:boolean">0</sky_r>
    <td_r xsi:type="xsd:boolean">0</td_r>
    <temp_r xsi:type="xsd:boolean">0</temp_r>
    <wdir_r xsi:type="xsd:boolean">0</wdir_r>
    <wspd_r xsi:type="xsd:boolean">0</wspd_r>
    <wgust xsi:type="xsd:boolean">0</wgust>
    <iceaccum xsi:type="xsd:boolean">0</iceaccum>
    <maxrh xsi:type="xsd:boolean">0</maxrh>
    <minrh xsi:type="xsd:boolean">0</minrh>
    </weatherParameters>
    </ns3591:NDFDgen>
    </SOAP-ENV:Body>
    </SOAP-ENV:Envelope>""".format(lat_data, long_data, datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
                                   tommorow.strftime("%Y-%m-%dT%H:%M:%S"))
    response = requests.post(url, data=body, headers=headers)
    # print(response)
    # print(type(response.content))
    data = response.content.decode('utf-8')
    data_greater = data.replace('&lt;', '<')
    data_lesser = data_greater.replace('&gt;', '>')
    # print(type(data_lesser))
    soup = BeautifulSoup(data_lesser, 'lxml')
    # print(soup)

    max_temp = soup.find('temperature', {'type': '"maximum"'}).text.split('\n')[2]
    # print(max_temp)
    print_info += 'Maximum temperature (F):\n{}\n'.format(max_temp)

    min_temp = soup.find('temperature', {'type': '"minimum"'}).text.split('\n')[2]
    # print(min_temp)
    print_info += 'Minimum temperature (F):\n{}\n'.format(min_temp)

    probability_of_precipitation = soup.find('probability-of-precipitation').text
    # print(probability_of_precipitation)
    print_info += probability_of_precipitation

    wind_speed = soup.find('wind-speed').text
    # print(wind_speed)
    print_info += wind_speed

    wind_direction = soup.find('direction').text
    # print(wind_direction)
    print_info += wind_direction

    weather_icon = soup.find('icon-link').text
    # print(weather_icon)
    print_info += weather_icon

    # print(print_info)
    display_textarea.insert(END, print_info)


def find_weather_again():

    print_info = ''
    global lat_data
    global long_data

    tommorow = datetime.datetime.now() + datetime.timedelta(days=1)

    url = 'https://graphical.weather.gov:443/xml/SOAP_server/ndfdXMLserver.php'
    headers = {'content-type': 'text/xml'}
    body = """<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/" SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
    <SOAP-ENV:Body>
    <ns3591:NDFDgen xmlns:ns3591="uri:DWMLgen">
    <latitude xsi:type="xsd:string">{}</latitude>
    <longitude xsi:type="xsd:string">{}</longitude>
    <product xsi:type="xsd:string">time-series</product>
    <startTime xsi:type="xsd:string">{}</startTime>
    <endTime xsi:type="xsd:string">{}</endTime>
    <Unit xsi:type="xsd:string">e</Unit>
    <weatherParameters>
    <maxt xsi:type="xsd:boolean">1</maxt>
    <mint xsi:type="xsd:boolean">1</mint>
    <temp xsi:type="xsd:boolean">0</temp>
    <td xsi:type="xsd:boolean">0</td>
    <pop12 xsi:type="xsd:boolean">1</pop12>
    <qpf xsi:type="xsd:boolean">0</qpf>
    <sky xsi:type="xsd:boolean">0</sky>
    <snow xsi:type="xsd:boolean">0</snow>
    <wspd xsi:type="xsd:boolean">1</wspd>
    <wdir xsi:type="xsd:boolean">1</wdir>
    <wx xsi:type="xsd:boolean">0</wx>
    <waveh xsi:type="xsd:boolean">0</waveh>
    <icons xsi:type="xsd:boolean">1</icons>
    <critfireo xsi:type="xsd:boolean">0</critfireo>
    <dryfireo xsi:type="xsd:boolean">0</dryfireo>
    <rhm xsi:type="xsd:boolean">0</rhm>
    <apt xsi:type="xsd:boolean">0</apt>
    <tcwspdabv34i xsi:type="xsd:boolean">0</tcwspdabv34i>
    <tcwspdabv50i xsi:type="xsd:boolean">0</tcwspdabv50i>
    <tcwspdabv64i xsi:type="xsd:boolean">0</tcwspdabv64i>
    <tcwspdabv34c xsi:type="xsd:boolean">0</tcwspdabv34c>
    <tcwspdabv50c xsi:type="xsd:boolean">0</tcwspdabv50c>
    <tcwspdabv64c xsi:type="xsd:boolean">0</tcwspdabv64c>
    <conhazo xsi:type="xsd:boolean">0</conhazo>
    <ptornado xsi:type="xsd:boolean">0</ptornado>
    <phail xsi:type="xsd:boolean">0</phail>
    <ptstmwinds xsi:type="xsd:boolean">0</ptstmwinds>
    <pxtornado xsi:type="xsd:boolean">0</pxtornado>
    <pxhail xsi:type="xsd:boolean">0</pxhail>
    <pxtstmwinds xsi:type="xsd:boolean">0</pxtstmwinds>
    <ptotsvrtstm xsi:type="xsd:boolean">0</ptotsvrtstm>
    <ptotxsvrtstm xsi:type="xsd:boolean">0</ptotxsvrtstm>
    <tmpabv14d xsi:type="xsd:boolean">0</tmpabv14d>
    <tmpblw14d xsi:type="xsd:boolean">0</tmpblw14d>
    <tmpabv30d xsi:type="xsd:boolean">0</tmpabv30d>
    <tmpblw30d xsi:type="xsd:boolean">0</tmpblw30d>
    <tmpabv90d xsi:type="xsd:boolean">0</tmpabv90d>
    <tmpblw90d xsi:type="xsd:boolean">0</tmpblw90d>
    <prcpabv14d xsi:type="xsd:boolean">0</prcpabv14d>
    <prcpblw14d xsi:type="xsd:boolean">0</prcpblw14d>
    <prcpabv30d xsi:type="xsd:boolean">0</prcpabv30d>
    <prcpblw30d xsi:type="xsd:boolean">0</prcpblw30d>
    <prcpabv90d xsi:type="xsd:boolean">0</prcpabv90d>
    <prcpblw90d xsi:type="xsd:boolean">0</prcpblw90d>
    <precipa_r xsi:type="xsd:boolean">0</precipa_r>
    <sky_r xsi:type="xsd:boolean">0</sky_r>
    <td_r xsi:type="xsd:boolean">0</td_r>
    <temp_r xsi:type="xsd:boolean">0</temp_r>
    <wdir_r xsi:type="xsd:boolean">0</wdir_r>
    <wspd_r xsi:type="xsd:boolean">0</wspd_r>
    <wgust xsi:type="xsd:boolean">0</wgust>
    <iceaccum xsi:type="xsd:boolean">0</iceaccum>
    <maxrh xsi:type="xsd:boolean">0</maxrh>
    <minrh xsi:type="xsd:boolean">0</minrh>
    </weatherParameters>
    </ns3591:NDFDgen>
    </SOAP-ENV:Body>
    </SOAP-ENV:Envelope>""".format(lat_data, long_data, datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
                                   tommorow.strftime("%Y-%m-%dT%H:%M:%S"))
    response = requests.post(url, data=body, headers=headers)
    # print(response)
    # print(type(response.content))
    data = response.content.decode('utf-8')
    data_greater = data.replace('&lt;', '<')
    data_lesser = data_greater.replace('&gt;', '>')
    # print(type(data_lesser))
    soup = BeautifulSoup(data_lesser, 'lxml')
    # print(soup)

    max_temp = soup.find('temperature', {'type': '"maximum"'}).text.split('\n')[2]
    # print(max_temp)
    print_info += 'Maximum temperature (F):\n{}\n'.format(max_temp)

    min_temp = soup.find('temperature', {'type': '"minimum"'}).text.split('\n')[2]
    # print(min_temp)
    print_info += 'Minimum temperature (F):\n{}\n'.format(min_temp)

    probability_of_precipitation = soup.find('probability-of-precipitation').text
    # print(probability_of_precipitation)
    print_info += probability_of_precipitation

    wind_speed = soup.find('wind-speed').text
    # print(wind_speed)
    print_info += wind_speed

    wind_direction = soup.find('direction').text
    # print(wind_direction)
    print_info += wind_direction

    weather_icon = soup.find('icon-link').text
    # print(weather_icon)
    print_info += weather_icon

    # print(print_info)
    display_textarea.insert(END, print_info)


root = Tk()

# add the name for the window
root.title('Weather')

# creating lat label widget and adding to window
lat_label = Label(root, text='Latitude:')
lat_label.grid(row=0, column=0)

# creating text entry latitude
lat_entry = Entry(root)
lat_entry.grid(row=0, column=1)

# creating lat label widget and adding to window
long_label = Label(root, text='Longitude:')
long_label.grid(row=1, column=0)

# creating text entry longitude
long_entry = Entry(root)
long_entry.grid(row=1, column=1)

# create reset button widget and add it to root
reset_button = Button(None, text="RESET", command=find_weather_again)
reset_button.grid(row=3, column=0)

# create enter button widget and add it to root
enter_button = Button(None, text="ENTER", command=find_weather)
enter_button.grid(row=3, column=1)

# adding text area to display text
display_textarea = Text(root, height=20, width=50)
display_textarea.grid(row=4, columnspan=10)

# keep the GUI running forever
root.mainloop()
