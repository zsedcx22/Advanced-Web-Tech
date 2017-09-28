from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
  return "HAHAHAHAHAHA"

@app.route("/pain/")
def pain():
  return "spicy"
#aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
