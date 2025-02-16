<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

</head>
<body>

<h1>Image to Text OCR Application</h1>

<p>This project is a simple web application that allows you to upload images and extract text from them. It is built using the Flask framework and the EasyOCR library.</p>

<h2>Features</h2>
<ul>
  <li><strong>Image Upload:</strong> Users can upload images.</li>
  <li><strong>Text Recognition:</strong> Extracts text from the uploaded image using EasyOCR.</li>
  <li><strong>Multi-language Support:</strong> Users can select the language for text recognition (Persian and English).</li>
  <li><strong>Image Management:</strong> An admin page to view and delete uploaded images.</li>
  <li><strong>Download Results:</strong> Allows downloading the extracted text in TXT and Word formats.</li>
</ul>

<h2>Prerequisites</h2>
<p>You need to have the following installed:</p>
<ul>
  <li>Python 3.x</li>
  <li>Flask</li>
  <li>EasyOCR</li>
</ul>

<h2>Installation</h2>
<pre><code>git clone https://github.com/yourusername/your-repo.git
cd your-repo</code></pre>
<p>Then install the dependencies:</p>
<pre><code>pip install -r requirements.txt</code></pre>

<h2>Running the Application</h2>
<p>To run the application, use the following command:</p>
<pre><code>python app.py</code></pre>
<p>Then visit <a href="http://127.0.0.1:5000">http://127.0.0.1:5000</a> to access the application.</p>

<h2>Usage</h2>
<ol>
  <li><strong>Upload Image:</strong> Click on the "Choose File" button, select an image, choose the desired language, and click "Submit".</li>
  <li><strong>View Results:</strong> After processing, the extracted text will be displayed. You can copy the text or download it in TXT and Word formats.</li>
  <li><strong>Manage Images:</strong> Go to the admin page to view and delete uploaded images.</li>
</ol>

<h2>Project Structure</h2>
<ul>
  <li><code>app.py</code>: The main application file.</li>
  <li><code>templates/</code>: Contains HTML files for web pages.</li>
  <li><code>uploads/</code>: A folder to store uploaded images.</li>
</ul>

<h2>Contributing</h2>
<p>If you would like to contribute to this project, please fork the repository and submit a Pull Request with your changes.</p>

<h2>License</h2>
<p>This project is licensed under the MIT License. Please see the LICENSE file for details.</p>

<h3>Thank you for using this project! If you have any questions, feel free to reach out.</h3>

</body>
</html>
