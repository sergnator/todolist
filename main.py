# pip install -r requirements.txt
from flask import Flask, render_template, request
import json


def main():
    app = Flask(__name__)

    @app.route('/')
    @app.route('/index')
    def index():
        with open("static\\json\\tasks.json", encoding='utf-8') as f:
            data = json.load(f)
        list_ = data['main']
        return render_template('index.html', list=list_, len=len, str=str)

    app.run()

    @app.route('/delete', methods=['POST'])
    def delete():
        request_data = request.get_json()
        text = request_data['text']
        with open("static\\json\\tasks.json", encoding='utf-8') as f:
            data = json.load(f)
        list_ = data['main'][:]
        del list_[list_.index(text)]
        data['main'] = list_



if __name__ == '__main__':
    main()