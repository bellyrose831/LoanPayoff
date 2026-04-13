#sources
#airtable api docs: https://pyairtable.readthedocs.io/en/stable/tables.html
#airtable link: https://airtable.com/appUKKwJXXkEF1xvh/tblctK0jy3jj28XhT/viwbM8ipV21WMU3Ib?blocks=hide
#airtable tokens: https://airtable.com/create/tokens
#deployment link: https://dashboard.render.com/

#run using "python app.py"

from flask import Flask, render_template, request
from pyairtable import Api
import pandas as pd
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    api = Api(os.environ.get("AIRTABLE_API_KEY"))
    table = api.table('appUKKwJXXkEF1xvh', 'tblctK0jy3jj28XhT')
    
    if request.method == 'POST':
        formAnswers = request.form
        table.create({'Date': formAnswers['date'], 'Amount': int(formAnswers['amount'])})


    response = table.all() 
    data = []
    for record in response:
        data.append(record['fields'])
        print(record)
        print(record['fields'])

    data = pd.DataFrame(data)
    print(data)
    return render_template('home.html', column_names=data.columns.values,row_data=list(data.values.tolist()), zip=zip)

@app.route('/LoanDetails')
def details():
    return render_template('details.html', remBalance = 5000, estPayoffDate = "June 1, 2028", minPayment = 200, interest = 0, extraPayments = 0, nextPaymentAmt = 200, nextPaymentDate = "May 1, 2026")

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)