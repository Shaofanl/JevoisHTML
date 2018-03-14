Jevois HTML Interface
===

A HTML-based Jevois Interface 

Requirements:
- Jevois.
- Python.
- Flask. Install with `pip install flask`.

Usage:
- Connect Jevois.
- Run `run.py` with administrative permission (`sudo python run.py` or `sudo FLASK_APP=run.py flask run`).
- Open your browser and access the url shown in the console (`127.0.0.1:5000` by default).


Advanced usage:
- Broadcast your Jevois to the world:
  - Deploy the server on `0.0.0.0` port. (`sudo FLASK_APP=run.py flask run --host 0.0.0.0 --port 12345`).

Future work:
- Build Jevois application with HTML5
  - Jevois outputs information with `jevois.sendSerial`.
  - Python receives information with `serial.Serial` with [pySerial](http://pythonhosted.org/pyserial/)
  - HTML fetches from Python server with AJAX.
