# This file is only needed to satisfy Render's default configuration
# It redirects Render's standard Django WSGI approach to our FastAPI app

import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import the FastAPI app
from main import app

# Create a WSGI app that Render can use
from uvicorn.workers import UvicornWorker

# This will be imported by Gunicorn
application = app
