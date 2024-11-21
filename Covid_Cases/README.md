# COVID-19 Data Analysis

## Overview

This project involves performing analysis on the number of COVID-19 cases across 50 U.S. states and 5 U.S. territories using the **COVID Tracking Project's public API**. The goal of this assignment is to work with Web JSON APIs, retrieve and process data, and perform analysis on the COVID-19 statistics for each state and territory.

The program retrieves data from the COVID Tracking Project API and performs the following calculations for each state:

1. **Average number of new daily confirmed cases** for the entire dataset.
2. **Date with the highest number of new confirmed COVID cases.**
3. **Most recent date with no new COVID cases.**
4. **Month with the highest new number of COVID cases.**
5. **Month with the lowest new number of COVID cases.**

The data is output to the console and saved in a JSON file for each state/territory.

## Requirements

### Programming Requirements:
- The program must interact with the [COVID Tracking API](https://covidtracking.com/data/api) to retrieve COVID-19 data.
- The API response is in JSON format, which will be parsed into a Python dictionary for analysis.
- Perform the specified calculations on the COVID-19 data for each state and territory.
- Save the JSON data for each state/territory as `<state>.json`.

### Other Requirements:
- Use **procedural programming** for this assignment (object-oriented programming is not required).
- Follow the **style and naming conventions** used in the class.
- Use descriptive variable names, proper spacing, and indentation to ensure your code is easy to follow.
- Include **comments** that explain what your program does.

## File Structure

- **hw5_covid.py**: The main Python script that fetches, processes, and analyzes COVID-19 data.
- **states_territories.txt**: A text file containing the list of U.S. state and territory codes.

## API Information

You will use the following URL format to retrieve data from the API:

- **Base URL**: `https://api.covidtracking.com/v1/states/{state_code}/daily.json`
  - Replace `{state_code}` with the appropriate state/territory code (e.g., `ut` for Utah).

For example:
- Utah: `https://api.covidtracking.com/v1/states/ut/daily.json`
- California: `https://api.covidtracking.com/v1/states/ca/daily.json`

The API returns daily COVID-19 data for each state/territory, including the number of confirmed cases and the date of each data point.

## How to Run

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/covid-data-analysis.git
    cd covid-data-analysis
    ```

2. **Install dependencies** (if needed):
    If you haven't installed the required libraries, use `pip` to install `requests` (for API calls) and `json` (for working with JSON data). Typically, `json` is included in Python's standard library, but you'll need `requests`:
    ```bash
    pip install requests
    ```

3. **Run the program**:
    Run the Python script to fetch and analyze COVID-19 data for each state/territory:
    ```bash
    python hw5_covid.py
    ```

4. **Output**:
    - The program will output the following statistics for each state/territory:
      - **Average number of new daily confirmed cases**.
      - **Date with the highest new number of confirmed cases**.
      - **Most recent date with no new COVID cases**.
      - **Month with the highest new number of confirmed cases**.
      - **Month with the lowest new number of confirmed cases**.
    - The program will also save the JSON data in a file named `<state>.json` for each state/territory.

## Example Output

```bash
State: Utah
- Average number of new daily confirmed cases: 150
- Date with the highest new number of COVID cases: 2020-12-05
- Most recent date with no new COVID cases: 2021-01-01
- Month with the highest new number of COVID cases: December 2020
- Month with the lowest new number of COVID cases: May 2020
```
## How the Program Works

### 1. Fetch Data:
- The program reads the list of state codes from `states_territories.txt` and retrieves COVID-19 data for each state/territory using the [COVID Tracking API](https://covidtracking.com/data/api).

### 2. Data Processing:
- The data for each state is parsed from **JSON format** into a Python dictionary.
- Calculations are made for:
  - **Average new daily confirmed cases**.
  - **Date with the highest number of cases**.
  - **Most recent date with no new cases**.
  - **The months with the highest and lowest new case totals**.

### 3. Saving Data:
- The raw **JSON data** for each state/territory is saved in a file named `<state_code>.json`.

### 4. Output:
- Results are displayed on the console for each state/territory.

## Contact

For any questions or feedback, feel free to contact me at [dawsontfield@gmail.com](mailto:dawsontfield@gmail.com).

