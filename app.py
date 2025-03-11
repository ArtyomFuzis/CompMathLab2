from flask import Flask, request, make_response

import handlers

app = Flask(__name__)


@app.route('/api', methods=['POST'])
def hello_world():  # put application's code here
    try:
        if request.json["type"] == "equation":
            return handlers.handle_equation(request.json)
        elif request.json["type"] == "system":
            return handlers.handle_system(request.json)
        else:
            return make_response('Unable to handle this type of request', 400)
    except KeyError:
        return make_response("Unable to find field 'type' in your request", 400)


if __name__ == '__main__':
    app.run()
