import subprocess
from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def index():
    result = subprocess.run(['infracost', 'breakdown', '--path=terraform/plan.json'], capture_output=True, text=True)
    cost_output = result.stdout
    return render_template('index.html', cost_output=cost_output)
