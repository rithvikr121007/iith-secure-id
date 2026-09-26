from flask import Flask, render_template, request
from crypto import encrypt_student, decrypt_student
import qrcode
import cv2
import csv


app = Flask(__name__)

students={}

with open("students.csv",newline="")as file:
    reader=csv.DictReader(file)

    for row in reader:
        students[row["roll_no"]]=row["name"]


@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        roll_no = request.form["roll_no"].lower()
        name=students.get(roll_no)
        if name is None:
             return render_template(
                "index.html",
                 error="Roll number not found"
              )
        branch_codes = {
             "ep": "Engineering Physics",
             "cs": "Computer Science",
              "me": "Mechanical Engineering",
             "ee": "Electrical Engineering",
             "es": "Engineering Science",
             "ic": "Instrumentation and Control",
             "ch": "Chemical Engineering"
            }
        branch_code=roll_no[:2]
        department = branch_codes.get(branch_code)

        student = {
            "roll_no": roll_no,
            "name": name,
            "department": department
        }

        encrypted = encrypt_student(student)

        qr = qrcode.make(encrypted)

        qr.save("static/student_id.png")

        return render_template(
            "index.html",
            qr_generated=True
        )

    return render_template("index.html")


@app.route("/verify", methods=["GET", "POST"])
def verify():

    if request.method == "POST":

        file = request.files["qr_image"]

        file.save("uploaded_qr.png")

        image = cv2.imread("uploaded_qr.png")

        detector = cv2.QRCodeDetector()

        data, points, _ = detector.detectAndDecode(image)

        if data:

            encrypted = data.encode()

            student = decrypt_student(encrypted)

            return render_template(
                "verify.html",
                verified=True,
                student=student
            )

        else:

            return render_template(
                "verify.html",
                verified=False
            )

    return render_template("verify.html")

@app.route("/verify-data", methods=["POST"])
def verify_data():
    data = request.json["data"]

    print("QR DATA RECEIVED:")
    print(data)

    try:
        encrypted = data.encode()
        student = decrypt_student(encrypted)

        print("DECRYPTION SUCCESS:")
        print(student)

        return {
            "verified": True,
            "student": student
        }

    except Exception as error:

        print("DECRYPTION ERROR:")
        print(error)

        return {
            "verified": False,
            "error": str(error)
        }

@app.route("/api/v1/verify", methods=["POST"])
def api_verify():
    data = request.json["qr_data"]

    try:
        encrypted = data.encode()
        student = decrypt_student(encrypted)

        return {
            "verified": True,
            "student": student
        }

    except Exception:
        return {
            "verified": False
        }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)