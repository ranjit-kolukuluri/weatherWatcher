**Problem Statement**: Build a custom Python script that fetches weather data from an API and loads the information into a Google Sheet.
                        The customer will input the Latitude and Longitude of a location and expects to get the Current Temperature, Windspeed, and timestamp of when the data was fetched from the weather API.
                        
**Inputs**: A Google sheet template with customer input and expected outcome columns. 

**Expected Outcome**: 

                      1. Create a copy of the Google sheet template

                      2. Read the requested latitudes and longitudes (from columns A and B).
                      
                      3. Fetch the latest weather information for each latitude/longitude.
                      
                      4. Write that information back into the sheet (into columns C, D, and E). Note that column E should just contain the timestamp of when the data was fetched from the weather API. 
**Solution**: 
