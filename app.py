from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        try:
            x = float(request.form['x'])
            y = float(request.form['y'])
            operation = request.form['operation']
            
            if operation == 'add':
                result = x + y
            elif operation == 'subtract':
                result = x - y
            elif operation == 'multiply':
                result = x * y
            elif operation == 'divide':
                if y != 0:
                    result = x / y
                else:
                    result = 'Error: Cannot divide by zero'
        except ValueError:
            result = 'Invalid input'
    
    return render_template('index.html', result=result)

# The corrected line
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)