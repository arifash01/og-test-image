import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    """Serves a simple hello world message."""
    return 'Hello, this is the WORKING revision!'

if __name__ == "__main__":
    # Cloud Run provides the PORT environment variable
    port = int(os.environ.get('PORT', 8080))
    
    # Run the app, listening on all interfaces
    app.run(debug=True, host='0.0.0.0', port=port)