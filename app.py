import pandas as pd
from pandasql import sqldf
from pandasql import load_births

births = load_births()
# print(sqldf("select * from births where births > 250000 limit 5;", locals()))

query = "select date(date) as dob, sum(births) as 'Total births' from births group by date limit 5";
# print(sqldf(query))


def getdob_births(query_param):
    return sqldf(query_param)


print(getdob_births(query))






print('Welcome to sql server')