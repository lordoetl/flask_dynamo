from flask import Flask, jsonify
import aws_controller

app = Flask(__name__)

table='bobTable'
item='1942Casablanca'

@app.route('/')
def index():
    html=f"""This is the main page.<br> <a href=/get-items/{table}/{item}> get items</a>
            <br> <a href=/do_items/{table}>Only do this once</a> 
            <br> <a href=/get-all/{table}>get all of the data</a>"""
    return html
    
@app.route('/get-items/<table>/<item>')
def get_items(table,item):
    return jsonify(aws_controller.get_item(table,item))

@app.route('/get-all/<table>')
def get_all(table):
    return jsonify(aws_controller.get_all(table))

# @app.route('/do_items')
# def do_items(table):
#     response=aws_controller.create_table(table)
#     return response

@app.route('/do_items/<table>')
def do_items(table):
    response=aws_controller.create_table(table)
    return response

if __name__ == '__main__':
    app.run()