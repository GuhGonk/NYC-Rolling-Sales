import pandas as pd
import polars as pl
import os

class byBoro:
    @classmethod
    def pd_load_in(self):
        excel_files = [file for file in os.listdir('data/by_borough')]
        dfs = []
        
        columns = ['BOROUGH', 'NEIGHBORHOOD', 'BUILDING CLASS CATEGORY',
                  'TAX CLASS AT PRESENT', 'BLOCK', 'LOT', 'EASE-MENT',
                  'BUILDING CLASS AT PRESENT', 'ADDRESS', 'APARTMENT NUMBER',
                  'ZIP CODE', 'RESIDENTIAL UNITS', 'COMMERCIAL UNITS',
                  'TOTAL UNITS', 'LAND SQUARE FEET', 'GROSS SQUARE FEET',
                  'YEAR BUILT', 'TAX CLASS AT TIME OF SALE',
                  'BUILDING CLASS AT TIME OF SALE', 'SALE PRICE', 'SALE DATE']

        for f in excel_files:
            file_path = os.path.join('data/by_borough', f)
            
            if any(num in str(file_path) for num in ['03','04','05','06','07','08','09','10']):
                df = pd.read_excel(file_path, skiprows=range(0,3))
            elif '11' in str(file_path):
                df = pd.read_excel(file_path, skiprows=range(0,4))
            elif any(num in str(file_path) for num in ['12','13','14','15','16','17','18','19']):
                df = pd.read_excel(file_path, skiprows=range(0,4))
                df.columns = columns
            elif any(num in str(file_path) for num in ['20','21', '22', '23']):
                df = pd.read_excel(file_path, skiprows=range(0,6))
                df.columns = columns

            mask = (
                df['BOROUGH'].notna() & 
                df['NEIGHBORHOOD'].notna() & 
                df['BLOCK'].notna() & 
                df['LOT'].notna() &
                (df['BOROUGH'] != '') &
                (df['NEIGHBORHOOD'] != '') &
                (df['BLOCK'] != '') &
                (df['LOT'] != '')
            )

            df = df[mask]   
            dfs.append(df)
            print(f'{file_path} __ LOADED !')
        return pd.concat(dfs, ignore_index=True)
    
    def pl_load_in():
        excel_files = [file for file in os.listdir('data/by_borough')]
        dfs = []
        
        columns = ['BOROUGH', 'NEIGHBORHOOD', 'BUILDING CLASS CATEGORY',
                  'TAX CLASS AT PRESENT', 'BLOCK', 'LOT', 'EASE-MENT',
                  'BUILDING CLASS AT PRESENT', 'ADDRESS', 'APARTMENT NUMBER',
                  'ZIP CODE', 'RESIDENTIAL UNITS', 'COMMERCIAL UNITS',
                  'TOTAL UNITS', 'LAND SQUARE FEET', 'GROSS SQUARE FEET',
                  'YEAR BUILT', 'TAX CLASS AT TIME OF SALE',
                  'BUILDING CLASS AT TIME OF SALE', 'SALE PRICE', 'SALE DATE']

        counter = 0

        for f in excel_files:
            try:
                file_path = os.path.join('data/by_borough', f)
                
                if any(num in str(file_path) for num in ['03','04','05','06','07','08','09','10']):
                    df = pl.read_excel(source = file_path, engine = "calamine", read_options = {"header_row": 3})
                elif '11' in str(file_path):
                    df = pl.read_excel(source = file_path, engine = "calamine", read_options = {"header_row": 4})
                elif any(num in str(file_path) for num in ['12','13','14','15','16','17','18','19']):
                    df = pl.read_excel(source = file_path, engine = "calamine", read_options = {"header_row": 4})
                elif any(num in str(file_path) for num in ['20','21', '22', '23']):
                    df = pl.read_excel(source = file_path, engine = "calamine", read_options = {"header_row": 6})
                
                # Rename the columns
                df.columns = columns
                
                # Ensuring data type uniformity
                schema = {
                    'BOROUGH': pl.Int64,
                    'NEIGHBORHOOD': pl.Utf8,
                    'BUILDING CLASS CATEGORY': pl.Utf8,
                    'TAX CLASS AT PRESENT': pl.Utf8,
                    'BLOCK': pl.Int64,
                    'LOT': pl.Int64,
                    'EASE-MENT': pl.Utf8,
                    'BUILDING CLASS AT PRESENT': pl.Utf8,
                    'ADDRESS': pl.Utf8,
                    'APARTMENT NUMBER': pl.Utf8,
                    'ZIP CODE': pl.Int64,
                    'RESIDENTIAL UNITS': pl.Int64,
                    'COMMERCIAL UNITS': pl.Int64,
                    'TOTAL UNITS': pl.Int64,
                    'LAND SQUARE FEET': pl.Int64,
                    'GROSS SQUARE FEET': pl.Int64,
                    'YEAR BUILT': pl.Int64,
                    'TAX CLASS AT TIME OF SALE': pl.Int64,
                    'BUILDING CLASS AT TIME OF SALE': pl.Utf8,
                    'SALE PRICE': pl.Int64,
                    'SALE DATE': pl.Date
                }

                df = df.with_columns([
                    pl.col(col_name).cast(dtype, strict=False) for col_name, dtype in schema.items()
                ])

                df = df.with_columns([
                    pl.col(col_name).str.strip_chars() 
                    for col_name, dtype in schema.items() 
                    if dtype == pl.Utf8
                ])

                # Filter out rows with null or empty values
                df = df.filter(
                    (pl.col('BOROUGH').is_not_null()) &
                    (pl.col('NEIGHBORHOOD').is_not_null()) &
                    (pl.col('BLOCK').is_not_null()) &
                    (pl.col('LOT').is_not_null())
                )
                
                dfs.append(df)
                counter += 1
                if counter % 10 == 0 :
                    print(f'{counter, file_path} __ LOADED !')
            except Exception as e:
                print(f'\n ERROR \n {file_path}\n')
                print(e)
            
        return pl.concat(dfs)
    
class cpi:
    def pd_load_in(path):
        df = pd.read_excel(path, skiprows=11)
        return(df)
    
    def pl_load_in(path):
        df = pl.read_excel(source=path, engine="calamine", read_options={"header_row": 11})
        return(df)
    
class interestRate:
    def HR15_pl(path):
        df = pl.read_csv(path, skip_rows = 5)
        cols = ['Time Period','1M', '3M', '6M', '1Y', '2Y', '3Y', '5Y', '7Y', '10Y', '20Y', '30Y']
        df.columns = cols
        return(df)
    
    def overnight_rates_pl(path):
        cols = ['Intra Day - Low (%)', 'Intra Day - High (%)', 'Standard Deviation (%)']
        cols_to_drop = ['30-Day Average SOFR', '90-Day Average SOFR', '180-Day Average SOFR', 'SOFR Index']

        df = pl.read_excel(
            source=path,
            schema_overrides={col: pl.Float64 for col in cols},
            infer_schema_length=None
        )
        df = df.drop(pl.col(cols_to_drop))
        df = df.filter(pl.col("Effective Date") != "")
        df = df.with_columns(pl.col("Effective Date").str.strptime(pl.Date, format="%m/%d/%Y"))

        return(df)

