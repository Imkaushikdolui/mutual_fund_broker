# Mutual Fund Broker Web Application

This is a web application for a Mutual Fund Broker that displays the latest mutual fund data in a user-friendly interface. The application fetches data from a public API and presents it in a tabular format, allowing users to filter the data based on the fund family and scheme type.

## Features

- **Responsive Design**: The application is built with a responsive design, ensuring optimal viewing and user experience across different devices and screen sizes.
- **Data Filtering**: Users can filter the displayed mutual fund data by selecting a specific fund family from a dropdown menu. Additionally, the application automatically filters for open-ended schemes.
- **Interactive Table**: The data is presented in an interactive table, allowing users to sort and search through the various columns.
- **Scheme Details**: Each scheme in the table is linked to a detailed view, providing comprehensive information about the selected scheme.
- **Purchase Simulation**: On the scheme details page, users can simulate the purchase of units by entering the desired quantity. The application will calculate and display the total value based on the current net asset value (NAV).

## Technologies Used

- **Frontend**: HTML, CSS (Bootstrap), JavaScript (jQuery)
- **Data Source**: [RapidAPI Mutual Fund NAV API](https://rapidapi.com/omwealth-omwealth-default/api/latest-mutual-fund-nav/)
- **Third-party Libraries**:
  - [Bootstrap](https://getbootstrap.com/) (CSS framework)
  - [DataTables](https://datatables.net/) (jQuery plugin for enhanced tables)

## Getting Started

To run the application locally, follow these steps:

1. Clone the repository or download the source code files.
2. Ensure you have a modern web browser installed.
3. Open the `index.html` file in your web browser.

Note: The application relies on a public API for fetching mutual fund data. If the API is no longer available or has changed, some functionality may be affected.


## Follow these steps to set up and run the application:

###  1. Create and activate a virtual environment

#### On Windows:

```
python -m venv venv
venv\Scripts\activate
```

#### On Linux/macOS:

```
python3 -m venv venv
source venv/bin/activate
```

### 2. Install dependencies

Install the required Python packages by running:

```
pip install -r requirements.txt
```

### 3. Run the application

Start the FastAPI server with the following command:

```
uvicorn main:app --reload
```

### 4. Use the creds in .env for loggin into the website.

http://127.0.0.1:8000 -> enter this into your browser to land on website.
