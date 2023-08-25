from flask import Flask
from flask_restful import Api,Resource
import requests
from flask_cors import CORS,cross_origin

app = Flask(__name__)
CORS(app)
api = Api(app)




class HelloWorld(Resource):
    def get(self,name):
        response = requests.get("https://www.jiosaavn.com/api.php?p=1&q="+name+"&_format=json&_marker=0&api_version=4&ctx=web6dot0&n=20&__call=search.getAlbumResults")
        return response.json()

class AppVersion(Resource):
    def get(self):
        return "1.0.0"
    
class GetMovieData(Resource):
    def get(self,name):
        response = requests.get("https://seapi.link/?type=search&query="+name+"&max_results=max_results")
        return response.json()

class SongDetails(Resource):
    def get(self,id):
        response = requests.get("https://www.jiosaavn.com/api.php?__call=webapi.get&token="+id+"&type=album&includeMetaTags=0&ctx=web6dot0&api_version=4&_format=json&_marker=0")
        return response.json()

class TrendingSongs(Resource):
    def get(self):
        response = requests.get("https://www.jiosaavn.com/api.php?__call=webapi.getLaunchData&api_version=4&_format=json&_marker=0&ctx=wap6dot0",headers={"accept-language":"en-US,en;q=0.9,te-IN;q=0.8,te;q=0.7"})
        return response.json()
    



api.add_resource(HelloWorld,"/helloworld/<string:name>")

api.add_resource(AppVersion,"/AppVersion/")

api.add_resource(GetMovieData,"/getmoviedata/<string:name>")

api.add_resource(SongDetails,"/songdetails/<string:id>")

api.add_resource(TrendingSongs,"/trendingsongs/")


if __name__ == "__main__":
    app.run(debug=True)
    
