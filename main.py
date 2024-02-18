# pip install -r requirements.txt
from flask import Flask, render_template, request, url_for, redirect
import json
import requests
from PIL import Image
from io import BytesIO


def main():
    app = Flask(__name__)

    @app.route('/')
    @app.route('/index')
    def index():
        with open("static\\json\\tasks.json", encoding='utf-8') as f:
            data = json.load(f)
        list_ = data['main']
        return render_template('index.html', list=list_, len=len, str=str)

    @app.route('/delete', methods=['POST'])
    def delete():
        request_data = request.get_json()
        text = request_data['text']
        with open("static\\json\\tasks.json", encoding='utf-8') as f:
            data = json.load(f)
        list_ = data['main'][:]
        del list_[list_.index(str.strip(text))]
        data['main'] = list_
        with open("static\\json\\tasks.json", encoding='utf-8', mode='w') as f:
            json.dump(data, f)
        return '{"response": "nice"}'

    @app.route('/create', methods=['POST'])
    def create():
        request_data = request.get_json()
        text = request_data['text']
        with open("static\\json\\tasks.json", encoding='utf-8') as f:
            data = json.load(f)
        list_ = data['main'][:]
        list_.append(str.strip(text))
        data['main'] = list_
        with open("static\\json\\tasks.json", encoding='utf-8', mode='w') as f:
            json.dump(data, f)
        return '{"response": "nice"}'

    @app.route('/new')
    def new():
        return render_template('new_task.html')

    @app.errorhandler(404)
    def not_found_error(error):
        data = requests.get('https://http.cat/404.jpg')
        a = Image.open(BytesIO(data.content))
        a.save('static/img/four.jpg')
        return redirect(url_for('static', filename='/img/four.jpg'))
    app.run()


if __name__ == '__main__':
    main()
