import process as proc
import db_connect
connection = db_connect.start_conn()

if __name__ == "__main__":
    while True:
        print("""__Menu__\n
            1) NYC Rolling Sales
            2) CPI
            3) Interest Rate
            4) Labor
            5) exit
            """)
        user_input = input("Choose: ")
        match user_input:
            case "1":
                path = 'data/by_borough'
                rolling_sales = proc.byBoro.pl_load_in(path)
                db_connect.write_db(rolling_sales, 'rolling_sales')
                print("rolling_sales table created and uploaded to database\n")
            case "2":
                cpiU_unadjusted = proc.cpi.pl_load_in('data/economic/cpi/CPI-U_unadjusted_2002-2024_CUUR0000SA0.xlsx')
                cpiU_unadjusted_lessFoodEnergy = proc.cpi.pl_load_in('data/economic/cpi/CPI-U_unadjusted_lessFoodEnergy_2002-2024_CUUR0000SA0L1E.xlsx')
                db_connect.write_db(cpiU_unadjusted, 'cpiU_unadjusted')
                db_connect.write_db(cpiU_unadjusted_lessFoodEnergy, 'cpiU_unadjusted_lessFoodEnergy')
                print('CPI Urban Unadjusted + CPI-U-U Less Food & Energy uploaded to database\n')
            case "3":
                FRB_H15 = proc.interestRate.HR15_pl('data/economic/interest_rate/FRB_H15.csv')
                overnight = proc.interestRate.overnight_rates_pl('data/economic/interest_rate/OvernightRates_NYFed.xlsx')
                freddiemac = proc.interestRate.mortgage_rates_pl('data/economic/interest_rate/freddiemac_mortgages.xlsx')
                