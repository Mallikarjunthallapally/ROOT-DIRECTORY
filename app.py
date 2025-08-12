from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')

    # Dummy validation (in a real application, you'd perform more thorough validation)
    if username and email and password:
        return f"Registration successful for {username}!"
    else:
        return "Please fill in all the fields."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
