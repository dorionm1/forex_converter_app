from flask import Flask, request, render_template, flash, redirect
from flask_debugtoolbar import DebugToolbarExtension
from forex_python.converter import CurrencyRates, CurrencyCodes
from decimal import *

app = Flask(__name__)

app.config["SECRET_KEY"] = "key"
debug = DebugToolbarExtension(app)
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
@app.route("/")
def home_page():
    return render_template("home_page.html")

@app.route("/conversion", methods=["POST"])
def conversion():
    c = CurrencyRates()
    cc = CurrencyCodes()
    currfrom = request.form["currcode_from"]
    currto = request.form["currcode_to"]
    amount = request.form["amount"]
    from_curr_sym = cc.get_symbol(currfrom)
    to_curr_sym = cc.get_symbol(currto)
    from_is_valid_cc = cc.get_currency_name(currfrom)
    to_is_valid_cc = cc.get_currency_name(currto)

    if from_is_valid_cc == None and to_is_valid_cc == None:
        flash(
            f"Not a valid Code: {currfrom} Please visit https://www.iban.com/currency-codes for a full list of Currency Codes"
        )
        flash(
            f"Not a valid Code: {currto} Please visit https://www.iban.com/currency-codes for a full list of Currency Codes"
        )
        flash(f"Not a valid Amount: {amount}")
        return redirect("/")
    if from_is_valid_cc == None:
        flash(f"Not a valid Code: {currfrom}")
        return redirect("/")
    if to_is_valid_cc == None:
        flash(f"Not a valid Code: {currto}")
        return redirect("/")
    else:
        conversion = c.convert(currfrom, currto, Decimal(f'{amount}'))
        roundedconv = round(conversion, 2)

        return render_template(
            "conversion.html",
            currfrom=currfrom,
            currto=currto,
            amount=amount,
            roundedconv=roundedconv,
            from_curr_sym=from_curr_sym,
            to_curr_sym=to_curr_sym,
        )
