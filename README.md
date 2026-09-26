# IITH Secure ID

A secure digital campus identity system that uses encrypted QR codes to generate and verify student identities.

## Problem

Traditional campus ID barcodes can potentially be recreated if someone knows a student's roll number.

IITH Secure ID protects student identity data using encryption before encoding it into a QR code.

## Features

- Secure student ID generation
- Encrypted student information
- QR code generation
- QR verification using image upload
- Live camera QR scanning
- Web-based verification
- API endpoint for integration with other campus systems

## How It Works

1. An authorized student roll number is entered.
2. The system retrieves the student's information from the student database.
3. The student information is encrypted using Fernet encryption.
4. The encrypted data is encoded into a QR code.
5. The QR code can be scanned using the verification system.
6. The encrypted data is decrypted by the authorized system.
7. The student's identity is displayed after successful verification.

## Tech Stack

- Python
- Flask
- Cryptography
- OpenCV
- QR Code
- HTML
- CSS
- JavaScript

## Project Structure

```text
iith-secure-id/
│
├── app.py
├── crypto.py
├── generate_key.py
├── students.csv
├── requirements.txt
├── .gitignore
├── README.md
│
├── templates/
│   ├── index.html
│   └── verify.html
│
└── static/
    └── style.css

```
## Local Setup

Follow these steps to run the project locally.

1. Clone the repository

Open a terminal and run:

git clone https://github.com/rithvikr121007/iith-secure-id.git

Then move into the project directory:

cd iith-secure-id
2. Install the required dependencies

Make sure Python is installed on your system.

Install the required Python packages:

pip install -r requirements.txt
3. Generate the encryption key

Run:

python generate_key.py

This creates a file named:

secret.key

The application uses this key to encrypt and decrypt student identity data.

Important: Do not upload secret.key to GitHub.

4. Start the application

Run:

python app.py

The Flask development server will start.

5. Open the application

Open a web browser and visit:

http://127.0.0.1:5000/

The IITH Secure ID application should now be running locally.

Using the Application
Generate a Secure ID
Open the Generate ID page.
Enter a valid student roll number from students.csv.
Click Generate Secure ID.
The system retrieves the student's information.
The information is encrypted.
A QR code containing the encrypted data is generated.
Verify an ID
Open the Verify ID page.
You can either:
Start the camera and scan the QR code, or
Upload an image containing the QR code.
The system reads the QR code.
The encrypted data is sent to the verification system.
The system attempts to decrypt the data.
If verification succeeds, the student's identity is displayed.
Demo Data

The repository contains a students.csv file with dummy student data for demonstration purposes.

Example:

roll_no,name
ep26btech12001,Arjun Mehta

Use the roll numbers available in students.csv when testing the application.

Security

The project uses Fernet symmetric encryption to protect student identity information before it is encoded into the QR code.

The encryption key is stored locally in secret.key and is excluded from the Git repository using .gitignore.

Knowing a student's roll number alone does not provide the encryption key required to create a valid encrypted credential.

API

The application includes an API endpoint for QR verification that can be used by other campus systems.

This can allow services such as:

Library
Hostel
Mess
Other campus services

to integrate with the identity verification system.

Future Improvements
API authentication
Credential expiry
Credential revocation
Dynamic QR codes
Stronger production-grade identity verification
Integration with additional campus services
