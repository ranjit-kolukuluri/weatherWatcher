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

**Google Sheets Authentication setup**
- Create a new account at https://console.cloud.google.com/
- Create a new project
- Enable Google Sheets API and Google Drive API
- Create Credentials by selecting the "Service Account key" option and set up the Editor role at Project level
- Create and download the Json file containing the service account credentials
  

