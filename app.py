from flask import Flask, jsonify
import aws_controller

app = Flask(__name__)

table='bobTable'
item='1942Casablanca'

@app.route('/')
def index():
    html=f"""This is the main page.
        <br> These links are for demo only.  If you use this as an api, route directly to the link that returns your data
        <br>  In this case the "get all of the data" link
        <br>  If you are running this locally remember that you will want to remove /dev from the url.
            <br> <a href=/dev/do_items/>Only do this once</a> 
            <br> <a href=/dev/get-all>get all of the data</a>"""
    return html
    
@app.route('/get-items/')
def get_items():
    return jsonify(aws_controller.get_item())

@app.route('/get-all/')
def get_all():
    return jsonify(aws_controller.get_all())
#example comment
# @app.route('/do_items')
# def do_items(table):
#     response=aws_controller.create_table(table)
#     return response

@app.route('/do_items/')
def do_items():
    response=aws_controller.create_table()
    return response

if __name__ == '__main__':
    app.run()
