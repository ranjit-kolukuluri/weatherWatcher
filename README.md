# OpenMeteo Weather Data to Google Sheets Integration 

### Problem Statement: 
Build a custom Python script that fetches weather data from an API and loads the information into a Google Sheet.
The customer will input the Latitude and Longitude of a location and expects to get the Current Temperature, Windspeed, and timestamp of when the data was fetched from the weather API.
                        
### Inputs: 
A Google sheet template with customer input and expected outcome columns. 

### Expected Outcome: 
1. Create a copy of the Google sheet template
2. Read the requested latitudes and longitudes (from columns A and B).
3. Fetch the latest weather information for each latitude/longitude.
4. Write that information back into the sheet (into columns C, D, and E). Note that column E should just contain the timestamp of when the data was fetched from the weather API. 

### Solution:
Develop a Python script that integrates OpenMeteo weather data with a Google Sheets spreadsheet. It should retrieve weather information based on latitude and longitude coordinates provided in the Google sheet from the OpenMeteo API and update the Google Sheet with the obtained data.
Use Google Sheets API by setting up the required authentication and authorization modules and use OpenMeteo's open API to retrieve Temperature, Windspeed, and the timestamp when the data is refreshed.

Following are the steps to achieve the expected outcome:

#### Prerequisites & Dependencies:

**Code Editor and Python Env Setup**


**Install and import the required Python libraries** 
```
gspread: For accessing Google Sheets.
pip install gspread

google-auth: For handling Google Cloud authentication.
pip install google-auth

requests: For making HTTP requests to the OpenMeteo API.
pip install requests


```


