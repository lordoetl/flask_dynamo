from flask import Flask, jsonify
import aws_controller

app = Flask(__name__)


@app.route('/')
def index():
    
    return "This is the main page.<br> <a href='/get-items'> get items</a> "
    
@app.route('/get-items')
def get_items():
    return jsonify(aws_controller.get_item('gaming_nationals_zaf'))

@app.route('/do_items')
def do_items():
    response=aws_controller.create_table()
    return response

if __name__ == '__main__':
    app.run()