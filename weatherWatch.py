import gspread
import requests
from google.auth import exceptions
from google.oauth2 import service_account
import math
import arrow


def get_weather(latitude, longitude, current):
    base_url = "https://api.open-meteo.com/v1/forecast"
    endpoint_url = f"{base_url}?latitude={latitude}&longitude={longitude}&current={current}"

    try:
        # Send GET request to OpenMeteo API
        response = requests.get(endpoint_url)

        if response.status_code == 200:
            # Parse JSON response
            data = response.json()

            # Extract temperature, wind speed, and time from the response
            temperature = math.ceil((9 / 5) * float(data['current']['temperature_2m']) + 32)
            wind_speed = data['current']['wind_speed_10m']
            time = arrow.get(data['current']['time']).to('US/Pacific').format('YYYY-MM-DD hh:mm A')

            return [f"{temperature} F", f"{wind_speed} mph", time]
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return None

    except Exception as e:
        print(f"Error: {e}")
        return None


def authenticate_gspread(credentials_file):
    try:
        # Load credentials from the service account JSON file
        credentials = service_account.Credentials.from_service_account_file(
            credentials_file,
            scopes=['https://www.googleapis.com/auth/spreadsheets']
        )
    except exceptions.MultipleFilesFoundError:
        print("Error: Multiple JSON files found. Specify the correct path to the service account JSON file.")
        exit()
    except FileNotFoundError:
        print(f"Error: Service account JSON file not found at '{credentials_file}'.")
        exit()

    # Authenticate using the credentials
    return gspread.service_account(filename=credentials_file)


def main():
    # Specify the path to the service account JSON file
    credentials_file = '/Users/ranjit.kolukuluri/Documents/API/getweather-408520-839d6553eee3.json'
    # Authenticate with Google Sheets API
    gc = authenticate_gspread(credentials_file)

    # Specify Google Sheet title and ID
    sheet_title = 'Weather Data from Openmeteo'
    spreadsheet_id = '1kmZ1R2r6dbf1iasRiURvhmNW_Xq37CiG7grKuZ9Qj9A'

    try:
        # Open the specified Google Sheet
        worksheet = gc.open_by_key(spreadsheet_id).sheet1
    except gspread.exceptions.SpreadsheetNotFound:
        print(f"Error: Google Sheet with title '{sheet_title}' not found.")
        exit()

    # Get latitude and longitude values from the sheet
    latitude = worksheet.col_values(1)[1:]
    longitude = worksheet.col_values(2)[1:]
    rows_to_update = []

    # Iterate through the rows and update weather information
    for latitude, longitude in zip(latitude, longitude):
        weather = get_weather(float(latitude), float(longitude), "temperature_2m,wind_speed_10m")
        #print(weather)
        rows_to_update.append(weather)

    # Update the Google Sheet with the retrieved weather information
    if rows_to_update:
        worksheet.update(f'C2:F{len(rows_to_update) + 1}', rows_to_update)

if __name__ == "__main__":
    # Execute the main function when the script is run
    main()
