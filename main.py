from langchain_teddynote.document_loaders import HWPLoader
from flask import Flask, request, jsonify

# Initialize Flask app
app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def api():
    file = request.files.get('file')
    if file:
        # Save the uploaded file
        file_path = f"./{file.filename}"
        file.save(file_path)
        
        # Load the HWP document
        loader = HWPLoader(file_path)
        docs = loader.load()
        
        # Extract the text (assuming single document for simplicity)
        extracted_text = docs[0].page_content[:2000]
        
        # Return the extracted text as JSON response
        return jsonify({"extracted_text": extracted_text})
    else:
        return jsonify({"error": "No file uploaded"}), 400

if __name__ == '__main__':
    app.run(debug=True)
