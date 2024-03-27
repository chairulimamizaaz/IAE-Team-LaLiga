from flask import Flask, render_template
import requests

app = Flask(__name__)

API_KEY = '617142fb8931f75b2940fc7bd977059955a65f1e9b30b090c0f76a204c4829cd'
LEAGUE_ID = 302  
API_TEAMS_URL = f"https://apiv3.apifootball.com/?action=get_teams&league_id={LEAGUE_ID}&APIkey={API_KEY}"

@app.route('/')
def index():
    response = requests.get(API_TEAMS_URL)
    if response.status_code == 200:
        teams = response.json()
        return render_template('index.html', teams=teams)
    else:
        return "Failed to fetch data from API", 500

@app.route('/team/<int:team_id>')
def team_detail(team_id):
    team_detail_url = f"https://apiv3.apifootball.com/?action=get_teams&team_id={team_id}&APIkey={API_KEY}"
    response = requests.get(team_detail_url)
    if response.status_code == 200:
        team_data = response.json()[0] 
        return render_template('team_detail.html', team=team_data)
    else:
        return "Failed to fetch team data from API", 500

if __name__ == '__main__':
    app.run(debug=True)

    