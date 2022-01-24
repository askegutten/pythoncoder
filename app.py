# oppgave 1

print("hello world")

from flask importFlask, render_template

app=Flask(__name__)

@app.route(‘/’)

def home():
  return render_template(“index.html”)

if __name__ ==’__main__’:
  app.run(debug=True)
