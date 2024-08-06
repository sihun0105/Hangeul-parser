import os
from langchain_teddynote.document_loaders import HWPLoader
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def api():
    file = request.files.get('file')
    if file:
        file_path = f"./{file.filename}"
        try:
            file.save(file_path)
            loader = HWPLoader(file_path)
            docs = loader.load()
            extracted_text = docs[0].page_content[:2000]
            response = jsonify({"extracted_text": extracted_text})
        except Exception as e:
            response = jsonify({"error": str(e)}), 500
        finally:
            if os.path.exists(file_path):
                os.remove(file_path)
        return response
    else:
        return jsonify({"error": "No file uploaded"}), 400

if __name__ == '__main__':
    app.run(debug=True)
