from flask import Flask, request

app = Flask(__name__)

@app.post('/login')
def create_user():
    fullname = request.json.get('fullname')
    phone = request.json.get('phone')
    email = request.json.get('email')
    username = request.json.get('username')
    password = request.json.get('password')

    if username == 'admin' and password == 'admin':
        return {'fullname': fullname, 'phone': phone, 'email': email}
    else:
        return 'Invalid username or password'
    
@app.post('/book')
def create_book():
    title = request.json.get('title')
    author = request.json.get('author')
    isbn = request.json.get('isbn')
    price = request.json.get('price')

    if not title:
        return 'Title is required'
    
    if not author:
        return 'Author is required'
    
    if not isbn:
        return 'ISBN is required'
    
    if not price:
        return 'Price is required'

    return {'title': title, 'author': author, 'isbn': isbn, 'price': price}