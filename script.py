from flask import Flask

app = Flask(__name__)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

@app.route('/')
def home():
    number = 5  # Change this number to test different factorials
    result = factorial(number)
    return f"<h1>✅ Factorial of {number} is {result}</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
