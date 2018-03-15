from flask import Flask, render_template, request, jsonify
import os
import subprocess

# create app
app = Flask(__name__)

cmdpath = os.path.join(os.path.abspath('./'), 'execute-jevois-cmd')

def execute(cmd):
    try:
        result = subprocess.run([cmdpath, cmd], stdout=subprocess.PIPE)
        result = result.stdout.decode('utf-8')
    except:  # python legacy
        result = subprocess.Popen(["jevois-cmd", "info"], stdout=subprocess.PIPE)
        result = result.communicate()[0]
    return result

# define routes
@app.route('/')
def index():
    return render_template('index.html')


# AJAX API
@app.route('/jevois_info')
def jevois_info():
    info = execute('info')
    return info


@app.route('/jevois_mappings')
def jevois_mappings():
    mappings = execute('listmappings')

    options = mappings.split('\r\n')[2:-2]
    options.insert(0, 'Default - OUT: YUYV 320x240 @ 60fps CAM: YUYV 320x240 @ 60fps')
    msg = '<option>'+'</option><option>'.join(options)+'</option>'
    return msg


@app.route('/jevois_cmd', methods=["POST"])
def jevois_cmd():
    cmd = request.form['cmd']
    result = execute(cmd)
    return jsonify({'res': result})
