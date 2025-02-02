from flask import Flask,render_template
app=Flask(__name__)
JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Bengaluru, India',
        'salary': 'Rs. 10,00,000'
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Delhi, India',
        'salary': 'Rs. 15,00,000'
    },
    {
        'id': 3,
        'title': 'Software Engineer',
        'location': 'Hyderabad, India',
        'salary': 'Rs. 12,00,000'
    }
]

@app.route('/')
def helloworld():
  return render_template("home.html" ,jobs=JOBS) 

if __name__=="__main__":
  app.run(host='0.0.0.0',port=8080)
  

