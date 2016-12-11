from flask import Flask, request
from flask_restful import Resource, Api
import json
import pyBulbDriver

app = Flask(__name__)
api = Api(app)

pyBulbDriver.scanForBulb("PLAYBULB COLOUR")

class pyBulbResource(Resource):
        def put(self,type):
                if type == "color":
                        bulb = json.loads(request.form['data'])
                        pyBulbDriver.setBulbColor(bulb['s'],bulb['r'],bulb['g'],bulb['b'])
                        return bulb
                elif type == "effect":
                        bulb = json.loads(request.form['data'])
                        pyBulbDriver.setBulbEffect(bulb['s'],
                                                   bulb['r'],bulb['g'],bulb['b'],
                                                   bulb['m'],bulb['on'],bulb['off'])
                        return bulb

api.add_resource(pyBulbResource, '/bulb/<string:type>')

@app.route("/")
def mainView():
        return str(pyBulbDriver.isConnected)

if __name__ == "__main__":
        app.run(host='0.0.0.0', port=5000, debug=True)
