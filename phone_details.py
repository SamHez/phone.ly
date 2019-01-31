"""
CLI BASED TOOL TO FIND ANY PHONES SPECS
WRITTEN BY - SAMUEL EPODOI
API USED: https://fonoapi.freshpixl.com

"""


#imports
import requests
import urllib.parse

#API URL && API Token
api_url = 'https://fonoapi.freshpixl.com/v1/getdevice?token=befa6d4f8e07dc4f85bbb8f18ec8ad246e186fc0a6cd3948&'

#Print credits
print (
  "\n=======================================\nPhone.ly(Get the details of any mobile device) \nWRITTEN BY - SAM EPODOI 💕 \nAPI USED - https://fonoapi.freshpixl.com\n=======================================\n"
)


try :

  def repeat():
    #Device
    device = input("Enter The Device Name📱 🌟 : ")

    #Add parameters to the url usung urllib
    url = api_url + urllib.parse.urlencode({'device': device })
    json_data = requests.get(url).json()

    #Print Device Details
    print(
      "\n*****************************\nDevice Details\n*****************************"
      "\nDevice Name: " + json_data[0]['DeviceName'],
      "\nBrand: " + json_data[0]['Brand'],
      "\nAnnounced: " + json_data[0]['announced'],
      "\nStatus: " + json_data[0]['status'],
      "\nDimensions: " + json_data[0]['dimensions'],
      "\nStorage: " + json_data[0]['internal'],
      "\nWeight: " + json_data[0]['weight'],
      "\nSim: " + json_data[0]['sim'],
      "\nPhoneSize: " + json_data[0]['size'],
      "\nMemoryCard: " + json_data[0]['card_slot'],
      "\nMessaging: " + json_data[0]['messaging'],
      "\nBattery: " + json_data[0]['battery_c'],
      "\nColors: " + json_data[0]['colors'],
      "\nOS: " + json_data[0]['os'],
      "\nCamera: " + json_data[0]['primary_'] 
     
    
    
    )
    print("\n*******************************************************************************\n")
  while True:
    repeat()

except Exception as e:
  print ("\n############################################################")
  print("# Awww snap😢 \n# Please try again\n# Make sure to put spaces between the different words/numbers etc..\n# and put the full phone name (no shotcuts) ")
  print ("##############################################################\n")
