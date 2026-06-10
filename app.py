from flask import Flask, request, jsonify

app = Flask(__name__)

# Route 4: /add-student
@app.route('/add-student', methods=['POST'])
def add_student():
    student = request.get_json()

    return jsonify({
        "message": "Student added successfully",
        "student": student
    }), 201

if __name__ == '__main__':
    app.run(debug=True)