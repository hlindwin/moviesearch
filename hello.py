from flask import Flask
import os
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
    
if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    #port = int(os.environ.get("PORT", 8082)) # 8080, 8081, 8082
    #app.run(host='127.0.0.1', port=port)