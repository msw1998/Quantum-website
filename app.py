from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def landing():
    return render_template('landing.html')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/quantum-flow')
def quantum_flow():
    return render_template('quantum-flow.html')

@app.route('/q-simulate')
def q_simulate():
    return render_template('q-simulate.html')

@app.route('/pulse-solver')
def pulse_solver():
    return render_template('pulse-solver.html')

@app.route('/planck-optimize')
def planck_optimize():
    return render_template('planck-optimize.html')

if __name__ == '__main__':
    app.run(debug=True)
