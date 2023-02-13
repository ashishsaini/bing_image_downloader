import sys
from bing_image_downloader import downloader
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

def validate(key):
    # validate key in header
    if key == "nasf98h0dh2023@@":
        return True
    return False

# create flask api to return images 
@app.route("/search",  methods=['GET'])
def search():
    key = request.headers.get('key')
    if not validate(key):
        return jsonify({"error": "Invalid key"})
    query = request.args.get('query')
    limit = 10
    
    try:
        limit = int(request.args.get('limit'))
    except Exception as e:
        print(e)
     
    print("query: ", query)
    print("filter: ", filter)
    links = downloader.download(query, limit=limit,  output_dir='dataset', adult_filter_off=True, force_replace=False, timeout=10, verbose=True)
    print("links: ", links)
    result = {"links": links}
    return json.dumps(result)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=3000,threaded=True)
