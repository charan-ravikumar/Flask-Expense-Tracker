from flask import Blueprint, render_template, request, flash,redirect,url_for
from flask_login import login_required, current_user
from .models import User,Expense
from . import db
from datetime import datetime

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def add_expense():
    all_expenses = Expense.query.filter_by(user_id=current_user.id).all()
    user = User.query.filter_by(id=current_user.id).first()
    if request.method == 'POST' :
        # email = request.form.get['email']
        amount = float(request.form['amount'])
        expensename = request.form['expensename']
        category = request.form['category']
        date = request.form['date']
        date_in = date # replace this string with whatever method or function collects your data
        date_processing = date_in.replace('T', '-').replace(':', '-').split('-')
        date_processing = [int(v) for v in date_processing]
        date_out = datetime(*date_processing)
        new_expense = Expense(amount = amount, expensename=expensename,category=category,date=date_out.replace(microsecond=0), user_id=current_user.id)  #providing the schema for the note 
        db.session.add(new_expense) #adding the note to the database 
        user.totalExpense += amount
        db.session.commit()
        flash('Expense added!', category='success')
        return redirect(url_for('views.add_expense'))
    return render_template("home.html",user=current_user,allExpense=all_expenses,totalExpense=user.totalExpense)

@views.route('/delete/<int:id>')
@login_required
def delete(id):
    expense = Expense.query.filter_by(id=id).first()
    user = User.query.filter_by(id=current_user.id).first()
    user.totalExpense -= expense.amount
    db.session.delete(expense)
    db.session.commit()
    return redirect(url_for('views.add_expense'))



