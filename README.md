Jevois HTML Interface
===

A HTML-based Jevois interface that helps the users/developers better streaming Jevois and controling it. Currently, it alsow the user to
- Stream Jevois on a webpage.
- Get the information of Jevois.
- Select the videomapping easily with a dropdown selector.
- Execute commands and check the return message easily.

Requirements
---
- Jevois.
- Python.
- Flask. Install it with `pip install flask`.

Usage
---
- Connect Jevois.
- Run `run.py` with administrative permission (`sudo python run.py` or `sudo FLASK_APP=run.py flask run`).
- Open your browser and access the url shown in the console (`127.0.0.1:5000` by default).

Advanced usage
---
- Broadcast your Jevois to the world:
  - Deploy the server on `0.0.0.0`. (`sudo FLASK_APP=run.py flask run --host 0.0.0.0 --port 12345`).

Possible extensions
---
- More controls via HTML components:
  - Other commands in `jevois-cmd` can also be built with HTML components (e.g. `setpar`, `getpar`, `setcam`, `getcam`).
  - We can parse all options from `jevois-cmd help` and visualize them as HTML components. I already built a selector for `videomapping`.
- Build Jevois application with HTML5:
  - Jevois outputs information with `jevois.sendSerial`.
  - Python receives information with `serial.Serial` with [pySerial](http://pythonhosted.org/pyserial/)
  - (Check [this video](https://www.youtube.com/watch?v=TlFrDv5FJo0) to see how I connect Jevois with a neural network to compose.)
  - HTML fetches information from Python server with AJAX.
