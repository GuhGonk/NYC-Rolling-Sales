# db_setup.py
* Req: db_connect.py, process.py
* Starts up the connection to SQL server then does CLI options

# process.py
## byBoro class
pd_load_in(), pl_load_in()
* Reads through the folder containing the rolling sales excels from NYC gov and combines them into a single consolidated file/table to work with or to use to setup database
* Uses either pandas or polars depending on function used
* polars version is most up to date

## cpi class
pl_load_in(path)
* Reads in the excel file

