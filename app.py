from flask import Flask, render_template, request, redirect, url_for
import easyocr
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload(): 
    if 'file' not in request.files:
        return redirect(request.url)
    
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)

    language = request.form['language']
    reader = easyocr.Reader([language])

    results = reader.readtext(file_path)
    extracted_text = ' '.join([text for (_, text, _) in results])

    return render_template('result.html', text=extracted_text)

@app.route('/admin13871387', methods=['GET'])
def admin():
    images = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('admin.html', images=images)

@app.route('/delete_all', methods=['POST'])
def delete_all():
    for filename in os.listdir(app.config['UPLOAD_FOLDER']):
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        os.remove(file_path)
    return redirect(url_for('admin'))

if __name__ == '__main__':
    app.run(debug=True)
