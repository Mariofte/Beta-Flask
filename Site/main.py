from flask import Flask
from flask import render_template

app = Flask(
    __name__, 
    template_folder = 'template',
    static_folder = 'static')

@app.route('/App')
def record():
    
    return render_template('record.html')

if __name__ == '__main__':
    app.run(debug=True, port=4400, host='0.0.0.0')