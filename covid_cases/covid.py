import requests
import json
from datetime import datetime
from statistics import mean
from collections import defaultdict
import os

def read_state_codes(filename):
    # Reading the state codes from the provided file path
    with open(filename, 'r') as file:
        # returning a list of state codes
        return [line.strip() for line in file if line.strip()]

def fetch_covid_data(state_code):
    # getting COVID data for a given state and saving it to a JSON file
    url = f"https://api.covidtracking.com/v1/states/{state_code.lower()}/daily.json"
    
    # making a request to the API and converting it to a JSON format
    response = requests.get(url)
    data = response.json()
    
    # writing the JSON date to a file and saving it to my covid_cases folder
    folder_path = "/Users/dawson/Documents/GitHub/USU_coursework/Covid_Cases"
    file_path = os.path.join(folder_path, f"{state_code.lower()}.json")
    
    with open(file_path, "w") as f:
        json.dump(data, f)
    
    return data

def analyze_covid_data(state_code, data):
    #Analyze COVID data for a given state and return statistics with descriptive keys
 
    # extracting the daily positive cases and saving it to a list 
    daily_cases = [day['positiveIncrease'] if day['positiveIncrease'] is not None else 0 for day in data]
    
    # calculating the average number of new daily confirmed cases
    avg_daily_cases = mean(daily_cases) if daily_cases else 0
    
    
    # finding the date with the highest new number of covid cases
    max_cases_day = max(data, key=lambda x: x['positiveIncrease'] if x['positiveIncrease'] is not None else 0)
    max_cases_date = datetime.strptime(str(max_cases_day['date']), "%Y%m%d").strftime("%Y-%m-%d")
   
    
    # finding the most recent date with no new covid cases
    no_cases_dates = [day for day in data if day['positiveIncrease'] == 0]
    most_recent_no_cases = "No such date" if not no_cases_dates else datetime.strptime(str(no_cases_dates[0]['date']), "%Y%m%d").strftime("%Y-%m-%d")
    

    # grouping daily cases by month
    monthly_cases = defaultdict(int)
    for day in data:
        date = datetime.strptime(str(day['date']), "%Y%m%d")
        month_key = date.strftime("%Y-%m")
        monthly_cases[month_key] += day['positiveIncrease'] if day['positiveIncrease'] is not None else 0
    
    # finding which month has the highest and lowest new cases
    if monthly_cases:
        max_month = max(monthly_cases, key=monthly_cases.get) 
        min_month = min(monthly_cases, key=monthly_cases.get) 
    else: 
        max_month = "No data"   
        min_month = "No data"
    
    
    # Return a dictionary of stats with descriptive keys
    return {
        "state_code": state_code,
        "average_daily_cases": avg_daily_cases,
        "max_cases_date": max_cases_date,
        "most_recent_no_cases": most_recent_no_cases,
        "max_month": max_month,
        "min_month": min_month
    }

def main():
    #reading the state codes from the states_territories.txt file
    state_codes = read_state_codes("/Users/dawson/Documents/GitHub/USU_coursework/Covid_Cases/states_territories.txt")
    
    for state in state_codes:
        # fetching and analyzing the data for each state
        data = fetch_covid_data(state)
        analysis = analyze_covid_data(state, data)
        
        # Output the results
        print("\nCovid confirmed cases statistics")
        print(f"State name: {state}")
        print(f"Average number of new daily confirmed cases for the entire state dataset: {analysis['average_daily_cases']:.2f}")
        print(f"Date with the highest new number of covid cases: {analysis['max_cases_date']}")
        print(f"Most recent date with no new covid cases: {analysis['most_recent_no_cases']}")
        print(f"Month with the highest new number of covid cases: {analysis['max_month']}")
        print(f"Month with the lowest new number of covid cases: {analysis['min_month']}")
   
# running the main finction when the script is executed
if __name__ == "__main__":
    main()