from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Nairobi, Kenya',
    'salary': 'Ksh. 200, 000'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Nairobi, Kenya',
    'salary': 'Ksh. 300, 000'
  },
  {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Remote',
    'salary': 'Ksh. 150, 000'
  },
  {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'Hybrid',
    'salary': 'Ksh. 150, 000'
  }
]

@app.route("/")
def home():
  return render_template('home.html', jobs=JOBS)

@app.route("/jobs")
def jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
