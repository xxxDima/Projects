from flask import Flask, url_for
from api_mysql import *
from json import dumps

app = Flask(__name__)


# @app.route('/api/all_data_db/')
# def all_data_db():
#     print(url_for('all_data_db'))
#     jsn_rows = dumps(rows)
#     return jsn_rows


@app.route('/api/moto_age/<int:age>')  # http://127.0.0.1:5000/api/moto_age/1989
def show_post(age):
    # show the post with the given id, the id is an integer
    jsn_age = dumps(connect(ages_moto(age)), ensure_ascii=False)
    return jsn_age


@app.route('/api/moto_price/<int:price>')  # http://127.0.0.1:5000/api/moto_price/100
def show_usd(price):
    # show the post with the given id, the id is an integer
    jsn_price = dumps(price_moto(price))
    return jsn_price


if __name__ == "__main__":
    app.run(debug=True)
