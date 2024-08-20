from flask import Flask, render_template, request

app = Flask(__name__)

# Define the items and their respective percentages
items = {
    "kornfel stem": 16.24,   # 10%
    "bhar 7elo na3em": 17.52,  # 20%
    "kerfa na3ma": 12.52,  # 50%
    "bhar maje": 12.52,   # 20%
    "zanjabeel na3em": 12.52,
    "mele7 na3em dkma": 10,
    "joza el teeb na3em": 3.76,
    "hael na3em": 2.52,
    "khardal na3em": 12.52,
}

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Result route to calculate and display quantities
@app.route('/calculate', methods=['POST'])
def calculate():
    total_quantity = float(request.form['quantity'])
    quantities = {item: (percentage / 100) * total_quantity for item, percentage in items.items()}
    return render_template('result.html', quantities=quantities, total_quantity=total_quantity)

if __name__ == '__main__':
    app.run(debug=True)


