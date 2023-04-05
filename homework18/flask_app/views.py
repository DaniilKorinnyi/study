from flask_app import app
from flask import Flask, redirect, url_for, render_template, request, abort, session
import random

app.secret_key = b'secret'
@app.route('/hello')
def hello():
    app.logger.info('Request received for hello endpoint.')
    return 'Hello, world!'

@app.route('/users')
def users():
    name_list = ["Alice", "Bob", "Charlie", "Dave", "Eve", "Frank", "Grace", "Heidi", "Ivan", "Jack", "Karen", "Liam",
             "Molly", "Nancy", "Oliver", "Pam", "Quinn", "Rachel", "Steve", "Tom", "Uma", "Victor", "Wendy", "Xander",
             "Yara", "Zara"]
    users = random.sample(name_list, random.randint(1, len(name_list)))
    return render_template('users.html', users=users)


@app.route('/books')
def books():
    book_list = ["The Great Gatsby", "To Kill a Mockingbird", "1984", "The Catcher in the Rye", "Animal Farm",
             "Pride and Prejudice", "Lord of the Flies", "The Hobbit", "The Lord of the Rings",
             "The Hitchhiker's Guide to the Galaxy", "The Da Vinci Code", "Harry Potter and the Philosopher's Stone",
             "The Hunger Games", "The Diary of a Young Girl", "The Alchemist", "One Hundred Years of Solitude",
             "Brave New World", "Fahrenheit 451", "The Picture of Dorian Gray", "Dracula", "Frankenstein",
             "The Adventures of Sherlock Holmes", "Alice's Adventures in Wonderland", "The War of the Worlds",
             "Treasure Island"]
    books = random.sample(book_list, random.randint(1, len(book_list)))
    return render_template('books.html', books=books)

@app.route('/users/<int:id>')
def get_user(id):
    return render_template('usersid.html', id=id)

@app.route('/books/<title>')
def get_book(title):
    transformed_title = title.capitalize()
    return render_template('bookstitle.html', title=transformed_title)

@app.route('/params')
def params():
    return render_template('params.html', params=request.args)


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

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404 Not Found</h1><p>The requested page could not be found.</p>", 404

@app.errorhandler(500)
def internal_server_error(e):
    return "<h1>500 Internal Server Error</h1><p>An error occurred while processing the request.</p>", 500

@app.route('/general')
def other():
    return render_template('general.html')


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('username', None)
    return redirect('/login')


@app.route('/')
def base():
    return render_template('base.html')
