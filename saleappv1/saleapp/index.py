from flask import render_template

from saleappv1.saleapp import dao
from saleappv1.saleapp import app


@app.route('/')

def index():
    categories = dao.load_categories()
    products = dao.load_products()
    return render_template('index.html', categories= categories, product=products)

if __name__=='__main__':
    app.run(debug=True)