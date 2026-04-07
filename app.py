#sources
#airtable api docs: https://pyairtable.readthedocs.io/en/stable/tables.html
#airtable link: https://airtable.com/appUKKwJXXkEF1xvh/tblctK0jy3jj28XhT/viwbM8ipV21WMU3Ib?blocks=hide
#airtable tokens: https://airtable.com/create/tokens
#deployment link: https://dashboard.render.com/

#run using "python app.py"

from flask import Flask, render_template
from pyairtable import Api
import pandas as pd
import os

app = Flask(__name__)

@app.route('/')
def main():
    api = Api(os.environ.get("AIRTABLE_API_KEY"))
    table = api.table('appUKKwJXXkEF1xvh', 'tblctK0jy3jj28XhT')
    response = table.all() 
    #this comes through as a list of dicts (each record = a dict), want to change to pandas DF

    data = []
    for record in response:
        data.append(record['fields'])
        print(record)
        print(record['fields'])

    data = pd.DataFrame(data)
    print(data)
    return render_template('home.html', test=data)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)