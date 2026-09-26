# IITH Secure ID

A secure digital campus identity system that uses encrypted QR codes to generate and verify student identities.

## Problem

Traditional campus ID barcodes can potentially be recreated if someone knows a student's roll number.

IITH Secure ID addresses this by protecting student identity data using encryption before encoding it into a QR code.

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
2. The system retrieves the student's information from the authorized student database.
3. The student information is encrypted using Fernet encryption.
4. The encrypted data is encoded into a QR code.
5. The QR code can be scanned using the verification system.
6. The encrypted data is decrypted only by the authorized system.
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
app.py              # Flask web application
crypto.py           # Encryption and decryption logic
generate_key.py     # Generates the encryption key
students.csv        # Demo student database
requirements.txt    # Python dependencies

templates/
    index.html      # ID generation page
    verify.html     # ID verification page

static/
    style.css       # Website styling