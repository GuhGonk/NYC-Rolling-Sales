import process as proc
import db_connect
connection = db_connect.start_conn()

if __name__ == "__main__":
    while True:
        print("""
               ------
              | Menu |
               ------\n
            1) NYC Rolling Sales
            2) CPI
            3) Interest Rate
            4) Consumer Metrics
            5) Labor
            6) exit
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
                db_connect.write_db(FRB_H15, 'FRB_H15')
                db_connect.write_db(overnight, 'overnight_rates')
                db_connect.write_db(freddiemac, 'freddiemac')
                print("Interest Rate data uploaded to database\n")
            case "4":
                print("Consumer Metrics in progress")
            case "5":
                nonfarmSA = proc.labor.labor_pl('data/economic/labour/CES0000000001_2002-2024.xlsx', 12)
                civ_empSA = proc.labor.labor_pl('data/economic/labour/LNS12000000_2002_2024.xlsx', 11)
                unempSA = proc.labor.labor_pl('data/economic/labour/LNS14000000_2002-2024.xlsx', 11)
                db_connect.write_db(nonfarmSA, 'nonfarmSA')
                db_connect.write_db(civ_empSA, 'civ_empSA')
                db_connect.write_db(unempSA, 'unempSA')
                print("Nonfarm Payrolls, Civilian Employment, and Unemployment data uploaded to database\n")
            case "6":
                print("Exiting...")
                break
            case "test":
                print("TESTING")
                print(db_connect.check_table_exists('rolling_sales', connection))
                break
                