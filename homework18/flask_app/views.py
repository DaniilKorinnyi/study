from flask_app import app, db
import os
from flask import Flask, redirect, url_for, render_template, request, abort, session, jsonify
from .models import User, Book, Purchase

app.secret_key = os.getenv('SECRET_KEY')


@app.route('/users')
def users():
    users = User.query.all()
    current = session.get('user')
    if current:
        return render_template('users.html', users=users)
    else:
        return redirect(url_for('login'))

@app.route('/users', methods=['POST'])
def create_user():
    user = User(
        name=request.json.get('name'),
        age=request.json.get('age')
    )
    db.session.add(user)
    db.session.commit()
    return 'User created', 201

@app.route('/users/<int:id>')
def get_user(id):
    users = User.query.get(id)
    current = session.get('user')
    if current:
        return render_template('usersid.html', users=users, id=id)
    else:
        return redirect(url_for('login'))

# _______________________________________________________________________

@app.route('/books')
def books():
    books = Book.query.all()
    current = session.get('user')
    if current:
        return render_template('books.html', books=books)
    else:
        return redirect(url_for('login'))
@app.route('/books', methods=['POST'])
def create_book():
    book = Book(
        title=request.json.get('title'),
        author=request.json.get('author'),
        price=request.json.get('price')
    )
    db.session.add(book)
    db.session.commit()
    return 'Book added', 201


@app.route('/books/<int:id>')
def get_book(id):
    books = Book.query.get(id)
    current = session.get('user')
    if current:
        return render_template('booksid.html', books=books, id=id)
    else:
        return redirect(url_for('login'))


# _______________________________________________________________________


@app.route('/purchases')
def purchases():
    purchases = Purchase.query.all()
    current = session.get('user')
    if current:
        return render_template('purchases.html', purchases=purchases)
    else:
        return 404

@app.route('/purchases', methods=['POST'])
def create_purchases():
    purchase = Purchase(
    user_id=request.json.get('user_id'),
    book_id=request.json.get('book_id'),
    total_price=request.json.get('total_price')
    )
    db.session.add(purchase)
    db.session.commit()
    return 'Purchase added', 201

@app.route('/purchases/<int:id>')
def purchase_id(id):
    purchases = Purchase.query.get(id)
    current = session.get('user')
    if current:
        return render_template('purchasesid.html', purchases=purchases, id=id)
    else:
        return redirect(url_for('login'))

# _______________________________________________________________________

@app.route('/')
def base():
    return render_template('base.html')

@app.route('/general')
def other():
    current = session.get('user')
    if current:
        return render_template('general.html', current=current)
    else:
        return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        app.logger.info(request.form.get('username'))
        username = request.form.get('username')
        session['user'] = username
        return redirect('/general')
    else:
        abort(400, 'Missing username or password')

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('user', None)
    return redirect('/login')

@app.route('/params')
def params():
    current = session.get('user')
    if current:
        return render_template('params.html', params=request.args)
    else:
        return redirect(url_for('login'))

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404 Not Found</h1><p>The requested page could not be found.</p>", 404

@app.errorhandler(500)
def internal_server_error(e):
    return "<h1>500 Internal Server Error</h1><p>An error occurred while processing the request.</p>", 500




