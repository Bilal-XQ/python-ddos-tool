from flask import Flask, render_template_string
import threading
import time

app = Flask(__name__)

# A flag to check if the attack has started
attack_started = False

@app.route('/')
def home():
    global attack_started
    if attack_started:
        return """
        <html>
            <head>
                <title>CyberAtlas - Hacked</title>
            </head>
            <body>
                <h1>Website has been attacked!</h1>
                <p>The website is down due to the DDoS attack!</p>
            </body>
        </html>
        """
    return """
    <html>
        <head>
            <title>CyberAtlas Club</title>
        </head>
        <body>
            <h1>Welcome to CyberAtlas Club</h1>
            <img src="/static/images/cyberatlas-logo.jpg" alt="CyberAtlas Logo" style="width:200px;height:200px;">
            <p>This is the official page of the CyberAtlas Club. Join us to explore the world of cybersecurity!</p>
        </body>
    </html>
    """

# Route to manually trigger the DDoS attack
@app.route('/start_attack')
def start_attack():
    global attack_started
    attack_started = True
    return """
    <html>
        <head>
            <title>CyberAtlas - Attack Started</title>
        </head>
        <body>
            <h1>DDoS Attack Started!</h1>
            <p>The website is now under attack. The server will be overwhelmed soon.</p>
            <p><a href="/" style="color: blue; text-decoration: underline;">Go back to Home</a></p>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)