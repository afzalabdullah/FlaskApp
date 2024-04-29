from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection string
client = MongoClient("mongodb+srv://MERN:mernstack@cluster0.36bh8a0.mongodb.net/CloudComputing?retryWrites=true&w=majority")
db = client.get_database()

# Collection name
collection = db['data']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        data = {
            'name': request.form['name'],
            'email': request.form['email'],
            'message': request.form['message']
        }
        collection.insert_one(data)
        return 'Data inserted successfully.'

if __name__ == '__main__':
    app.run(debug=True)
