
 #1. #Create a Flask API endpoint (/greet) that accepts a name query parameter and returns a personalized 
# # greeting in JSON format. If no name is provided, return a generic greeting.

# from flask import Flask, request, jsonify
# app = Flask(__name__)

# @app.route('/greet', methods=['GET'])
# def greet():
#     name = request.args.get('bharath') 
#     if name:
#         greeting = f"Hello, {name}!"
#     else:
#         greeting = "Hello this is bharath, i have successfully run the code try next code!"
    
#     return jsonify({'greeting': greeting})

#2.# # #Build an API to manage a to-do list. Implement endpoints for:
# #        * GET /todos: Retrieve all to-do items.
# #         * POST /todos: Add a new to-do item (accepting JSON data).
# #        * PUT /todos/<int:todo_id>: update an existing to-do.
# #        * DELETE /todos/<int:todo_id>: Delete a to-do item

# from flask import Flask, jsonify, request, abort
# app = Flask(__name__)

# # insert the data
# todos = [
#     {"id": 1, "task": "Learn Flask", "done": False},
#     {"id": 2, "task": "Build API", "done": False},
#     {"id": 3, "task": "Test app", "done": False}
# ]

# # get the data
# @app.route('/todos', methods=['GET'])
# def get_todos():
#     return jsonify(todos)

# # create new todo
# @app.route('/todos', methods=['POST'])
# def create_todo():
#     new_todo = {
#         "id": todos[-1]['id'] + 1 if todos else 1,  
#         "task": request.json['task'],              
#         "done": False
#     }
#     todos.append(new_todo)
#     return jsonify(new_todo) 


# @app.route('/todos/<int:todo_id>', methods=['PUT'])
# def update_todo(todo_id):
#     for todo in todos:
#         if todo['id'] == todo_id:
#             todo['task'] = request.json.get('task', todo['task'])
#             todo['done'] = request.json.get('done', todo['done'])
#             return jsonify(todo)

#     return jsonify({'error': 'Todo not found'})

# @app.route('/todos/<int:todo_id>', methods=['DELETE'])
# def delete_todo(todo_id):
#     for todo in todos:
#         if todo['id'] == todo_id:
#             todos.remove(todo)
#             return ({"message":"todo deleted successfully"})
#         return ({"error":"todo not found"})
    
# if __name__ == '__main__':
#     app.run(debug=True)


#3.  *Basic Calculator API:*
#Develop an API with endpoints for basic arithmetic operations (/add, /subtract, /multiply, /divide). 
#Each endpoint should accept two numerical parameters and return the result

# from flask import Flask, request, jsonify
# app = Flask(__name__)

# @app.route('/add')
# def add():
#     a=request.args.get('a',type=int)
#     b=request.args.get('b',type=int)
#     return jsonify({'result':a+b})

# @app.route('/sub')
# def sub():
#     a=request.args.get('a',type=int)
#     b=request.args.get('b',type=int)
#     return jsonify({'result':a-b})

# @app.route('/mul')
# def mul():
#     a=request.args.get('a',type=int)
#     b=request.args.get('b',type=int)
#     return jsonify({'result':a*b})

# @app.route('/divide')
# def divide():
#     a=request.args.get('a',type=int)
#     b=request.args.get('b',type=int)
#     return jsonify({'result':a/b})

# if __name__ == '__main__':
#     app.run(debug=True)

#4.  File Upload API:*
#Create an API endpoint that allows users to upload files (e.g., images, documents). 
#Store the uploaded files on the server and return a URL or file path in the response.

# import os
# from flask import Flask, request, jsonify
# from werkzeug.utils import secure_filename

# app = Flask(__name__)

# # Folder to store uploaded files
# UPLOAD_FOLDER = 'uploads'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# # Allowed file extensions (optional)
# ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'pdf', 'txt', 'docx'}

# def allowed_file(filename):
#     return '.' in filename and \
#            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# @app.route('/upload', methods=['POST'])
# def upload_file():
#     if 'file' not in request.files:
#         return jsonify({'error': 'No file part in the request'}), 400

#     file = request.files['file']
 
#     if file.filename == '':
#         return jsonify({'error': 'No file selected'}), 400

#     if file and allowed_file(file.filename):
#         filename = secure_filename(file.filename)
#         save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#         file.save(save_path)
#         return jsonify({'message': 'File uploaded successfully', 'file_path': save_path}), 200
#     else:
#         return jsonify({'error': 'Invalid file type'}), 400

# if __name__ == '__main__':
#     # Create upload folder if it doesn't exist
#     if not os.path.exists(UPLOAD_FOLDER):
#         os.makedirs(UPLOAD_FOLDER)

#     app.run(debug=True)

# 5.*User Authentication API (Basic):*
#* Implement a simple user authentication system with endpoints for:
#* POST /register: Register a new user.
#* POST /login: Authenticate a user and return a simple token 
#(for testing purposes, a real world application would use JWTs).

# from flask import Flask, request, jsonify
# import uuid

# app = Flask(__name__)

# # In-memory user store: { username: password }
# users = {}

# # In-memory token store: { token: username }
# tokens = {}

# @app.route('/register', methods=['POST'])
# def register():
#     data = request.json
#     username = data.get('nagabharath')
#     password = data.get('bharath146')

#     if not username or not password:
#         return jsonify({'error': 'Username and password are required'}), 400

#     if username in users:
#         return jsonify({'error': 'User already exists'}), 400

#     users[username] = password
#     return jsonify({'message': 'User registered successfully'}), 201

# @app.route('/login', methods=['POST'])
# def login():
#     data = request.json
#     username = data.get('bharath')
#     password = data.get('rockstar123')

#     if users.get(username) == password:
#         token = str(uuid.uuid4())  
#         tokens[token] = username
#         return jsonify({'message': 'Login successful', 'token': 3097}), 200
#     else:
#         return jsonify({'error': 'Invalid username or password'}), 401

# if __name__ == '__main__':
#     app.run(debug=True)

# 6. Use a database (e.g., SQLite, PostgreSQL) and Flask to create an API for managing a book library. 
# Implement endpoints to:
#         * Add a book.
#         * Retrieve a book by ID.
#         * Retrieve all books.
#         * Update book information.
#         * Delete a book.

# from flask import Flask, request, jsonify
# import mysql.connector

# app = Flask(__name__)

# # Connect to MySQL
# def get_connection():
#     return mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="Bharath196",
#         database="book"
#     )

# # Add a book
# @app.route("/books", methods=["POST"])
# def add_book():
#     data = request.get_json()
#     conn = get_connection()
#     cursor = conn.cursor()
#     cursor.execute(
#         "INSERT INTO book_details (title, author, year, genre) VALUES (%s, %s, %s, %s)",
#         (data["health is wealth"], data["bharath"], data["2024"], data["health"])
#     )
#     conn.commit()
#     book_id = cursor.lastrowid
#     cursor.close()
#     conn.close()
#     return jsonify({"message": "Book added", "id": book_id}), 201

# # Get a book by ID
# @app.route("/books/<int:book_id>", methods=["GET"])
# def get_book(book_id):
#     conn = get_connection()
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM book_details WHERE id = %s", (book_id,))
#     row = cursor.fetchone()
#     cursor.close()
#     conn.close()

#     if row:
#         return jsonify({
#             "id": row[0],
#             "title": row[1],
#             "author": row[2],
#             "year": row[3],
#             "genre": row[4]
#         })
#     else:
#         return jsonify({"error": "Book not found"}), 404

# # Get all books
# @app.route("/books", methods=["GET"])
# def get_all_books():
#     conn = get_connection()
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM book_details")
#     rows = cursor.fetchall()
#     cursor.close()
#     conn.close()

#     books = []
#     for row in rows:
#         books.append({
#             "id": row[0],
#             "title": row[1],
#             "author": row[2],
#             "year": row[3],
#             "genre": row[4]
#         })

#     return jsonify(books)

# # Update a book
# @app.route("/books/<int:book_id>", methods=["PUT"])
# def update_book(book_id):
#     data = request.get_json()
#     conn = get_connection()
#     cursor = conn.cursor()
#     cursor.execute(
#         "UPDATE book_details SET title=%s, author=%s, year=%s, genre=%s WHERE id=%s",
#         (data["title"], data["author"], data["year"], data["genre"], book_id)
#     )
#     conn.commit()
#     affected = cursor.rowcount
#     cursor.close()
#     conn.close()

#     if affected == 0:
#         return jsonify({"error": "Book not found"}), 404
#     return jsonify({"message": "Book updated successfully"})

# # Delete a book
# @app.route("/books/<int:book_id>", methods=["DELETE"])
# def delete_book(book_id):
#     conn = get_connection()
#     cursor = conn.cursor()
#     cursor.execute("DELETE FROM book_details WHERE id=%s", (book_id,))
#     conn.commit()
#     affected = cursor.rowcount
#     cursor.close()
#     conn.close()

#     if affected == 0:
#         return jsonify({"error": "Book not found"}), 404
#     return jsonify({"message": "Book deleted successfully"})

# if __name__ == "__main__":
#     app.run(debug=True)

















