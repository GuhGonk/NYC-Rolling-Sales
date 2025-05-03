# Project Overview
This is an analysis project looking at the NYC Rolling Sales data provided by the NYC government (https://www.nyc.gov/site/finance/property/property-annualized-sales-update.page).
It used to be CSVs but have shifted to only having PDFs and Excels sometime around 2023-2024.

## Goals
* A webpage for a dashboard UI
* Using regression techniques to project future sales trends
* Find correlation between economic & political events and property sales

# Pre-processing (process.py):
## by_borough, 2003-2010 Files:
    same format
    Need to skip first 3 rows, pd.read_excel('__path__', skiprows=range(0,3))

## by_borough, 2011 - 2016 files .xls
    Skip first 4 rows, pd.read_excel('__path__', skiprows=range(0,4))

## by_borough, 2012 - 2023 files:
    delimiters appear in the column names for some reason
    df.columns = ['BOROUGH', 'NEIGHBORHOOD', 'BUILDING CLASS CATEGORY',
       'TAX CLASS AT PRESENT', 'BLOCK', 'LOT', 'EASE-MENT',
       'BUILDING CLASS AT PRESENT', 'ADDRESS', 'APARTMENT NUMBER',
       'ZIP CODE', 'RESIDENTIAL UNITS', 'COMMERCIAL UNITS',
       'TOTAL UNITS', 'LAND SQUARE FEET', 'GROSS SQUARE FEET',
       'YEAR BUILT', 'TAX CLASS AT TIME OF SALE',
       'BUILDING CLASS AT TIME OF SALE', 'SALE PRICE', 'SALE DATE']

# Setting up the database (db_connect.py, db_setup.py)
## terminal:
    initdb -D "__path__"
    pg_ctl -D "__path__" start
    createuser -s postgres
    createdb -U postgres nyc_rolling_sales
    psql -U postgres -d nyc_rolling_sales -f NYC_rolling_sales.sql

## Connecting it to pgAdmin:
    Right click "Servers"
        - "Register"
        - "Server"
    General tab:
        Name: nyc_rolling_sales
    Connection tab:
        Host: localhost
        Port: 5432
        Database: nyc_rolling_sales
        Username: postgres
        Password: __password_you_used__

## Firing up database
    Sometimes you might need to kill other PostgreSQL databases to get it up in running
        taskkill /F /IM postgres.exe
    
    pg_ctl -D "__path__" start

# Database
## Tables
* nyc_rolling_sales
* overnight_rates
* treasuries
