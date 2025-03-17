from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/sum', methods=['GET'])
def sum_numbers():
    try:
        # Get query parameters
        a = request.args.get('a', type=float)
        b = request.args.get('b', type=float)

        # Validate input
        if a is None or b is None:
            return jsonify({"error": "Missing parameters a or b"}), 400

        return jsonify({"sum": a + b})
    
    except ValueError:
        return jsonify({"error": "Invalid input. Please provide numbers."}), 400

if __name__ == '__main__':
    app.run(debug=True)