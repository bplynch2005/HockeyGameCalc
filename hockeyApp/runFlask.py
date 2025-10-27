import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), 'pyProgs'))

from app import app
if __name__ == "__main__":
    app.run(host = '0.0.0.0', debug = True)
