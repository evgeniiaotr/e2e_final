from flask import Flask, request

app = Flask(__name__)

@app.route("/predict_price", methods = ['GET'])
def predict():
    args = request.args
    open_plan = args.get('open plan', default = -1, type = int)
    rooms = args.get('rooms', default= -1, type = int)
    area = args.get('area', default= -1, type = float)
    renovation = args.get('renovation', default= -1, type = int)

    responce = "open plan:{}, rooms:{}, area:{}, renovation:{}".format(open_plan, rooms, area, renovation)

    return responce


if __name__ == '__main__':
    app.run(debug=True, port=6555, host='0.0.0.0')
