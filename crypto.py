from cryptography.fernet import Fernet
import json

with open("secret.key","rb") as file:
    key=file.read()

cipher=Fernet(key)

def encrypt_student(student):
    student_json= json.dumps(student)
    encrypted= cipher.encrypt(student_json.encode())
    return encrypted

def decrypt_student(encrypted):
    decrypted_json=cipher.decrypt(encrypted).decode()
    student=json.loads(decrypted_json)
    return student

