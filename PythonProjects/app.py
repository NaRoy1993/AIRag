from flask import Flask, render_template, request, jsonify
import PyPDF2

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    message = request.json.get('message')
    # Here you would send the message to your AI API and get a response
    # For demonstration, we'll just echo the message back
    response = {"response": f"You said: {message}"}
    return jsonify(response)

@app.route('/upload_file', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file and file.filename.endswith('.pdf'):
        content = ""
        try:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                content += page.extract_text() + "\n"
            return jsonify({"content": content})
        except Exception as e:
            return jsonify({"error": str(e)})
    return jsonify({"error": "Invalid file format"})

if __name__ == "__main__":
    app.run(debug=True)