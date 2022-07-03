from datetime import datetime
from dateutil.relativedelta import relativedelta
   

date_after_month = datetime.today()+ relativedelta(months=1)
fromdate=datetime.today().strftime('%m/%d/%Y')
enddate=date_after_month.strftime('%d/%m/%Y')
# print(fromdate)
# print(enddate)

# start_date = datetime.strptime(fromdate, "%m/%d/%Y").strftime('%m/%d/%Y')
# end_date = datetime.strptime("07/23/1993", "%m/%d/%Y").strftime('%m/%d/%Y')
# print(type(start_date))
# print(end_date)
print(abs((end_date-start_date).days))