# Project Overview
This is an analysis project looking at the NYC Rolling Sales data provided by the NYC government (https://www.nyc.gov/site/finance/property/property-annualized-sales-update.page).
It used to be CSVs but have shifted to only having PDFs and Excels sometime around 2023-2024.

## Goals
* A webpage for a dashboard UI
* Using regression techniques to project future sales trends
* Find correlation between economic & political events and property sales

Stretch-Goals:
* Connecting it to an AI-agent so I can automate myself out of a job

# Pre-processing:
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

# Data Notes
## Borough:
    1 - Manhattan
    2 - Bronx
    3 - Brooklyn 
    4 - Queens
    5 - Staten Island

## Building Class Category
    https://www.nyc.gov/assets/finance/jump/hlpbldgcode.html
    
    A - One Family
    B - Two Family
    C - Walk Up Apartments
    D - Elevator Apartments
    E - Warehouses
    F - Factories and Industrial Buildings
    G - Garages
    H - Hotel
    I - Hospitals and Health Facilities
    J - Theatres
    K - Store Buildings
    L - Lofts
    M - Religious Facilities
    N - Asylums and Homes
    O - Office Buildings
    P - Indoor Public Assembly & Cultural Facilities
    Q - Outerdoor Recreational Facilities
    R - Condominiums
    S - Transportation Facilities
    U - Utility Bureau Properties
    V - Vacant Land
    W - Educational Facilities
    Y - Government/City Departments
    Z - Misc. Building Classifications

## FRB_H15
Units are all Percent:_Per_Year

H15/H15/RIFLGFCM01_N.B, Market yield on U.S. Treasury securities at 1-month constant maturity, quoted on investment basis

## Bureau of Labor Statistics

CES0000000001 - Total Nonfarm Employment Seasonally Adjusted
LNS12000000 - Civillian Employment Seasonally Adjusted
LNS14000000 - Unemployment Rate Seasonally Adjusted

CUUR0000SA0 - CPI for All Urban Consuumers (CPI-U) 1982-84=100 (Unadjusted)
CUUR0000SA0L1E - CPI-U/Less Food and Energy (Unadjusted)

# Setting up the database
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
* treasury_rates
* 