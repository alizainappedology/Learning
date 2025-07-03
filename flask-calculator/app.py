from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate')
def calculate():
    try:
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
        operator = request.args.get('operator')

        if operator == 'add':
            result = num1 + num2
        elif operator == 'sub':
            result = num1 - num2
        elif operator == 'mul':
            result = num1 * num2
        elif operator == 'div':
            if num2 == 0:
                return jsonify(error="Division by zero"), 400
            result = num1 / num2
        else:
            return jsonify(error="Invalid operator"), 400

        return jsonify(result=result)
    except Exception as e:
        return jsonify(error=str(e)), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
