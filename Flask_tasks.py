
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

import os
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Folder to store uploaded files
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Allowed file extensions (optional)
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'pdf', 'txt', 'docx'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['file']
 
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(save_path)
        return jsonify({'message': 'File uploaded successfully', 'file_path': save_path}), 200
    else:
        return jsonify({'error': 'Invalid file type'}), 400

if __name__ == '__main__':
    # Create upload folder if it doesn't exist
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

    app.run(debug=True)





















