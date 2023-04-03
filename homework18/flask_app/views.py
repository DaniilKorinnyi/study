from flask_app import app
from flask import Flask, redirect, url_for, render_template, request, abort
import random

@app.route('/hello')
def hello():
    app.logger.info('Request received for hello endpoint.')
    return 'Hello, world!'

@app.route('/users')
def users():
    name_list = ["Alice", "Bob", "Charlie", "Dave", "Eve", "Frank", "Grace", "Heidi", "Ivan", "Jack", "Karen", "Liam",
             "Molly", "Nancy", "Oliver", "Pam", "Quinn", "Rachel", "Steve", "Tom", "Uma", "Victor", "Wendy", "Xander",
             "Yara", "Zara"]
    users = "<ul>"
    for name in random.sample(name_list, random.randint(1, len(name_list))):
        users += f"<li>{name}</li>"
    users += "</ul>"
    return users


@app.route('/books')
def books():
    book_list = ["The Great Gatsby", "To Kill a Mockingbird", "1984", "The Catcher in the Rye", "Animal Farm",
             "Pride and Prejudice", "Lord of the Flies", "The Hobbit", "The Lord of the Rings",
             "The Hitchhiker's Guide to the Galaxy", "The Da Vinci Code", "Harry Potter and the Philosopher's Stone",
             "The Hunger Games", "The Diary of a Young Girl", "The Alchemist", "One Hundred Years of Solitude",
             "Brave New World", "Fahrenheit 451", "The Picture of Dorian Gray", "Dracula", "Frankenstein",
             "The Adventures of Sherlock Holmes", "Alice's Adventures in Wonderland", "The War of the Worlds",
             "Treasure Island"]
    books = "<ul>"
    for book in random.sample(book_list, random.randint(1, len(book_list))):
        books += f"<li>{book}</li>"
    books += "</ul>"
    return books

@app.route('/users/<int:id>')
def get_user(id):
    if id % 2 == 0:
        return f"User with ID {id} exists"
    else:
        return "404 Not Found", 404

@app.route('/books/<title>')
def get_book(title):
    transformed_title = title.capitalize()
    return transformed_title

@app.route('/params')
def params():
    res = '<ul>'
    for key, value in request.args.items():
        res += f'<li>{key} - {value}</li>'
    res += '</ul>'
    return f'<div>{res}</div>'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username and password:
            return redirect('/users')
        else:
            abort(400, 'Missing username or password')
    else:
        return '''
        <form method="POST" action="/login">
            <label for="username">Username:</label>
            <input type="text" id="username" name="username" required><br><br>
            <label for="password">Password:</label>
            <input type="password" id="password" name="password" required><br><br>
            <input type="submit" value="Login">
        </form>
'''
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404 Not Found</h1><p>The requested page could not be found.</p>", 404

@app.errorhandler(500)
def internal_server_error(e):
    return "<h1>500 Internal Server Error</h1><p>An error occurred while processing the request.</p>", 500

@app.route('/')
def other():
    return '''
        <h1>Hello!</h1>
        <p>Below are links to other pages:</p>
        <ul>
            <li><a href="/login">Login</a></li>
            <li><a href="/users">List of users</a></li>
            <li><a href="/books">List of books</a></li>
            <li><a href="/params">Other</a></li>
        </ul>
'''

