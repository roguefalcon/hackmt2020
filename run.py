#!/usr/bin/python3

import os
from application import main



main.app.run(debug=True, host='0.0.0.0', port=5000, threaded=True)
