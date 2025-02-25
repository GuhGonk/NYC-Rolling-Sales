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