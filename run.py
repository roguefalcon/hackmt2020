#!/usr/bin/python
import os
from application import main



main.app.run(debug=True, host='127.0.0.1', port=5000, threaded=True)