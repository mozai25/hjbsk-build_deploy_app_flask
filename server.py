from flask import Flask, render_template, request
# Import the Maths package here
from Maths.mathematics import summation, substraction, multiplication

app = Flask("Mathematics Problem Solver")

@app.route("/sum")
def sum_route():
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    # Write your code here
    result = summation(num1+num2)
    return result

@app.route("/sub")
def sub_route():
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    # Write your code here
    result = substraction(num1,num2)
    return result

@app.route("/mul")
def mul_route():
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    # Write your code here
    result = multiplication(num1,num2)
    return result  

@app.route("/")
def render_index_page():
    return render_template('index.html')
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
