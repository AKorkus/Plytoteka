from flask import Flask, request, render_template, redirect, url_for

from forms import ExpensesForm
from models import expenses

app = Flask(__name__)
app.config["SECRET_KEY"] = "nininini"


@app.route("/expenses/", methods=["GET", "POST"])
def expenses_list():
    form = ExpensesForm()
    error = ""
    expenses.suma()
    if request.method == "POST":
        if form.validate_on_submit():
            expenses.create(form.data)
            expenses.save_all()
        return redirect(url_for("expenses_list"))

    return render_template("expenses.html", form=form, expenses=expenses.all(), error=error, sum=expenses.suma())


@app.route("/expenses/<int:expense_id>/", methods=["GET", "POST"])
def todo_details(expense_id):
    expense = expenses.get(expense_id - 1)
    form = ExpensesForm(data=expense)

    if request.method == "POST":
        if form.validate_on_submit():
            expenses.update(expense_id - 1, form.data)
        return redirect(url_for("expenses_list"))
    return render_template("expense.html", form=form, expense_id=expense_id)


# LAUNCH.........................................................................................................................
if __name__ == "__main__":
    app.run(debug=False)
