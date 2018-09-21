#Import the relevant packages
import requests, json
import sys

a="""+-------------------------------------------------------------------------------------------------------------------+
|                                      Visit the Dynatrace API Documentation at                                     |
| https://www.dynatrace.com/support/help/dynatrace-api/timeseries/how-do-i-fetch-the-metrics-of-monitored-entities/ |
+-------------------------------------------------------------------------------------------------------------------+"""

#Print the API doc banner
print(a+"\n")

#Give users the options to choose an endpoint
print("Please choose which endpoint you wish to query:" + "\n" + "-"*47 + "\n" + "1. Prod API Endpoint\n2. QA API Endpoint\n\n")

#Define your tenant/environment information here to determine the endpoint. This should be a string object.
envOne = ""
envTwo = "" 

#Set up the while loop to ensure users can only enter number 1 or 2
url = 0

while url != 1 or 2:
	try:
		url = int(input("Please choose either 1 or 2: "))
		if url == 1:
			url = envOne + "/api/v1/timeseries"
			apiToken = input("\nPaste your PROD API Token here: ")
			break
		elif url == 2:
			url = envTwo + "/api/v1/timeseries"
			apiToken = input("\nPaste your QA API Token here: ")
			break
	except ValueError:
		print("Please try again!")

	
#Give the user the option to input relevant information for the API query	
relativeTime = input("Input your desired relativeTime [hour, day, month]: ")
aggregationType = input("Input your desired aggregationType [avg, sum, min, max, count, median, percentile]: ")
queryMode = input("Input your desired queryMode [series, total]: ")
timeseriesId = input("Input your desired timeseriesId: ")
	
#Format the JSON POST body
data = json.dumps({'relativeTime': relativeTime, 'aggregationType': aggregationType, 'queryMode': queryMode, 'timeseriesId': timeseriesId})


#Set the request headers 
headers = {'Content-Type': 'application/json', 'Authorization': 'Api-Token '+ apiToken}

#Make the post request to the API endpoint. Pass in the url chosen in the beginning plus the body and headers.
r = requests.post(url, data=data, headers=headers, verify=False) #verify=False is to circumvent any SSL cert issues.

#Check if the status code returns 200, and if it does prompt the user to save a file for the payload.
if r.status_code == 200:
	print("\nSuccess!\n")
	answer=input("Would you like to save the payload to a file? [y/n]: ")
#If the user chooses to save the payload, offer a format for the file to be saved in.	
	if answer == "y":
		extension = input("\nWhat format would you like to output? (txt, json, csv, etc.): ")
		sys.stdout = open('api_output.'+extension, 'w')
		print(r.text)
#If the status code is not http 200, print the error to the terminal.
else:
	print("\n" + r.text)