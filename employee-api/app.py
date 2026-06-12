from flask import Flask, jsonify, request
from flask_cors import CORS
import pymysql
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

# Database Connection
def get_connection():
    return pymysql.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        port=int(os.getenv("DB_PORT")),
        cursorclass=pymysql.cursors.DictCursor
    )

# Home
@app.route("/")
def home():
    return jsonify({
        "message": "Employee API Running"
    })

# Health Check
@app.route("/health")
def health():
    return jsonify({
        "status": "UP"
    })

# GET ALL EMPLOYEES
@app.route("/employees", methods=["GET"])
def get_employees():

    try:
        conn = get_connection()

        with conn.cursor() as cursor:
            cursor.execute("""
                SELECT *
                FROM employees
                ORDER BY id DESC
            """)

            employees = cursor.fetchall()

        conn.close()

        return jsonify(employees)

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500

# GET EMPLOYEE BY ID
@app.route("/employees/<int:id>", methods=["GET"])
def get_employee(id):

    try:
        conn = get_connection()

        with conn.cursor() as cursor:

            cursor.execute(
                "SELECT * FROM employees WHERE id=%s",
                (id,)
            )

            employee = cursor.fetchone()

        conn.close()

        if employee:
            return jsonify(employee)

        return jsonify({
            "message": "Employee not found"
        }), 404

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500

# CREATE EMPLOYEE
@app.route("/employees", methods=["POST"])
def create_employee():

    try:

        data = request.get_json()

        conn = get_connection()

        with conn.cursor() as cursor:

            cursor.execute(
                """
                INSERT INTO employees
                (
                    fullname,
                    email,
                    department,
                    salary
                )
                VALUES
                (%s,%s,%s,%s)
                """,
                (
                    data["fullname"],
                    data["email"],
                    data["department"],
                    data["salary"]
                )
            )

            conn.commit()

        conn.close()

        return jsonify({
            "message": "Employee created successfully"
        }), 201

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500

# UPDATE EMPLOYEE
@app.route("/employees/<int:id>", methods=["PUT"])
def update_employee(id):

    try:

        data = request.get_json()

        conn = get_connection()

        with conn.cursor() as cursor:

            cursor.execute(
                """
                UPDATE employees
                SET
                    fullname=%s,
                    email=%s,
                    department=%s,
                    salary=%s
                WHERE id=%s
                """,
                (
                    data["fullname"],
                    data["email"],
                    data["department"],
                    data["salary"],
                    id
                )
            )

            conn.commit()

        conn.close()

        return jsonify({
            "message": "Employee updated successfully"
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500

# DELETE EMPLOYEE
@app.route("/employees/<int:id>", methods=["DELETE"])
def delete_employee(id):

    try:

        conn = get_connection()

        with conn.cursor() as cursor:

            cursor.execute(
                "DELETE FROM employees WHERE id=%s",
                (id,)
            )

            conn.commit()

            if cursor.rowcount == 0:

                return jsonify({
                    "message": "Employee not found"
                }), 404

        conn.close()

        return jsonify({
            "message": "Employee deleted successfully"
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )