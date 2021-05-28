from flask import Flask
from flask_restful import Api,Resource
import requests

app = Flask(__name__)
api = Api(app)




class HelloWorld(Resource):
    def get(self,name):
        response = requests.get("https://www.jiosaavn.com/api.php?p=1&q="+name+"&_format=json&_marker=0&api_version=4&ctx=web6dot0&n=20&__call=search.getResults")
        return response.json()


api.add_resource(HelloWorld,"/helloworld/<string:name>")


if __name__ == "__main__":
    app.run(debug=True)
