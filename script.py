def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Calculate factorial
number = 5
result = factorial(number)

# Generate an HTML page with the result
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Factorial Calculator</title>
    <style>
        body {{ font-family: Arial, sans-serif; text-align: center; padding: 50px; }}
        h1 {{ color: #4CAF50; }}
    </style>
</head>
<body>
    <h1>✅ Factorial of {number} is {result}</h1>
</body>
</html>
"""

# Save to an HTML file
with open("index.html", "w") as f:
    f.write(html_content)

print("✅ HTML page generated successfully!")
