import random
import string
from flask import Flask, jsonify, request

app = Flask(__name__)


def generate_password(length, include_uppercase, include_digits, include_special_chars):
    character_set = string.ascii_lowercase
    if include_uppercase:
        character_set += string.ascii_uppercase
    if include_digits:
        character_set += string.digits
    if include_special_chars:
        character_set += string.punctuation

    password = ''.join(random.choice(character_set) for _ in range(length))
    return password


def password_strength(password):
    has_lowercase = any(c in string.ascii_lowercase for c in password)
    has_uppercase = any(c in string.ascii_uppercase for c in password)
    has_digit = any(c in string.digits for c in password)
    has_special_char = any(c in string.punctuation for c in password)

    strength = 0
    if has_lowercase:
        strength += 1
    if has_uppercase:
        strength += 1
    if has_digit:
        strength += 1
    if has_special_char:
        strength += 1

    return strength


@app.route('/generate_password', methods=['POST'])
def generate_password_endpoint():
    length = int(request.json.get('length', 12))
    include_uppercase = request.json.get('include_uppercase', True)
    include_digits = request.json.get('include_digits', True)
    include_special_chars = request.json.get('include_special_chars', True)

    password = generate_password(
        length, include_uppercase, include_digits, include_special_chars)
    return jsonify({'password': password})


@app.route('/password_strength', methods=['POST'])
def password_strength_endpoint():
    password = request.json.get('password', '')

    strength = password_strength(password)
    return jsonify({'strength': strength})
