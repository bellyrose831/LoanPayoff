#sources
#airtable api docs: https://pyairtable.readthedocs.io/en/stable/tables.html
#airtable link: https://airtable.com/appUKKwJXXkEF1xvh/tblctK0jy3jj28XhT/viwbM8ipV21WMU3Ib?blocks=hide
#airtable tokens: https://airtable.com/create/tokens
#deployment link: https://dashboard.render.com/

#pip install flask
#run using "python app.py"
# pip install pyairtable

from flask import Flask, render_template
from pyairtable import Api
import os

app = Flask(__name__)

@app.route('/')
def main():
    api = Api(os.environ.get("AIRTABLE_API_KEY"))
    table = api.table('appUKKwJXXkEF1xvh', 'tblctK0jy3jj28XhT')
    results = table.all()
    return render_template('home.html', test=results)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)