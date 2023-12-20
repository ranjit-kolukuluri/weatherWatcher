# OpenMeteo Weather Data to Google Sheets Integration 

### Problem Statement: 
Build a custom Python script that fetches weather data from an API and loads the information into a Google Sheet.
When the script is run, the latest temperature, windspeed, and time should be refreshed in the Google Sheets with latitude and longitude inputs from the same sheet using the openmeteo.com API.

### Inputs: 
- A Google sheet template with input and expected outcome columns.
- openmeteo.com API reference

### Expected Outcome: 
- Read the requested latitudes and longitudes (from columns A and B).
- Fetch the latest weather information for each latitude/longitude.
- Write that information back into the sheet (into columns C, D, and E). Column E will contain the timestamp of when the data was fetched from the weather API. 

### Solution:
Develop a Python script that integrates OpenMeteo weather data with a Google Sheets spreadsheet. It should retrieve weather information based on latitude and longitude coordinates provided in the Google sheet from the OpenMeteo API and update the Google Sheet with the obtained data.
Use Google Sheets API by setting up the required authentication and authorization modules and use OpenMeteo's open API to retrieve Temperature, Windspeed, and the timestamp.

Following are the steps to achieve the expected outcome:

#### Prerequisites & Dependencies:

**Code Editor and Python Env Setup**
- IntelliJ Idea: New Project 
- Configure Python Interpreter: 3.10
- Setup virtual environment and specify the path
- Create a new Python file weatherWatcher.py
- Setup GitHub repo and push the code
  
**Google Sheets Authentication setup**
- Create a new account at https://console.cloud.google.com/
- Create a new project
- Enable Google Sheets API and Google Drive API
- Create Credentials by selecting the "Service Account key" option and setting up the Editor role at the Project level
- Create and download the Json file containing the service account credentials
- Create a copy of the input Google Sheets template and copy the sheet ID and sheet title. (https://docs.google.com/spreadsheets/d/1kmZ1R2r6dbf1iasRiURvhmNW_Xq37CiG7grKuZ9Qj9A/edit?usp=sharing) 
- Share the sheet with the email ID associated with the Service Account

**Install and import the required Python libraries** 
```
gspread: For accessing Google Sheets.
pip install gspread

google-auth: For handling Google Cloud authentication.
pip install google-auth

requests: For making HTTP requests to the OpenMeteo API.
pip install requests

google-auth-oauthlib: For handling OAuth2 authentication.
pip install google-auth-oauthlib

arrow: For working with dates and times in a more human-readable format
pip install arrow

```
  
### Python Script: weatherWatcher.py

**authenticate_gspread() method**
- Build credentials object to authenticate to Google Sheets API by using the service account json file and setting up the scope to ['https://www.googleapis.com/auth/spreadsheets']
- The method returns the authentication object
  
**get_weather() method**
- Construct the api endpoint using the reference from (https://open-meteo.com/)
- Build the method to take longitude, latitude, and current as the input arguments
- Parse the response to get the temperature, windspeed, and time from the 'current' dictionary object
- Convert the temperature, windspeed, and time based on the expected format
- Method will return a list with temperature, windspeed, and time
  
**main() method**
- Establish Google Sheets authentication by passing the JSON file path with service account credentials to the authenticate_gspread() method
- Create string variables with Google Sheet ID and title values
- Open the worksheet by sheet ID and load the values to the latitude and longitude variables
- Iterate through the rows and update weather information to a list object
- Update the worksheet rows with the weather data to the corresponding rows and columns

### Final Step: Run the Python script to execute the main() method to retrieve the weather information and update the Google Sheet
