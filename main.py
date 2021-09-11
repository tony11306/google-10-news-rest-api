from flask import Flask, jsonify
from flask_restful import Api, Resource
from news_crawler import TopTenNews, News
import datetime
import json

PORT = 5000
DELPOY_HOST = '0.0.0.0'
app = Flask(__name__)
api = Api(app)
api.app.config['RESTFUL_JSON'] = {
    'ensure_ascii': False
}

class TenNews(Resource):
    def get(self, keyword: str):
        all_news = TopTenNews(keyword)

        def map_to_dict(news: News):
            return {
                'title': news.title,
                'media': news.media,
                'time ago': news.time_ago,
                'url': news.url
            }

        response = jsonify({
            'total news count': all_news.news_count,
            'news_array': list(map(map_to_dict, all_news.news)),
        })
        # print(response)
        return response

        
api.add_resource(TenNews, '/ten_news/<string:keyword>')
if __name__ == '__main__':
    app.config['JSON_AS_ASCII'] = False
    app.config['JSONIFY_MINETYPE'] = 'application/json;charset=utf-8'
    print(f'\nstarting time: {datetime.datetime.now()}\n')
    app.run(host=DELPOY_HOST, port=PORT)
