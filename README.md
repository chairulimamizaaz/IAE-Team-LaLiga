# Flask API Provider for La Liga Teams

This application was created using the Flask framework with the Python programming language and consumes data from the [API Football](https://apifootball.com/), specifically from the Competitions and Teams APIs.

## Requirements

- `python==3.11.3`: The version of Python used to develop the application.
- `Flask==2.3.3`: Micro web framework for Python.
- `requests==2.26.0`: Library for making HTTP requests.

## Overview

The application fetches data from the API Football endpoint to display information about La Liga teams.

## Usage

1. **Install Dependencies:**
   - Ensure you have Python installed. You can download it [here](https://www.python.org/downloads/).
   - Install the required Python packages

2. **Run the Application:**
   - Start the Flask application by executing:
     ```
     python app.py
     ```

3. **Access the Application:**
   - Open your web browser and go to `http://localhost:5000/` to view the list of La Liga teams.
   - Click on a team to view its details.

## Code Explanation

The Flask application defines two routes:

- `/`: Displays the list of La Liga teams.
- `/team/<int:team_id>`: Displays the details of a specific team.

The application fetches data from the API Football endpoint using the provided API key and renders the retrieved data using HTML templates.

## Screenshots

![La Liga Teams](https://github.com/chairulimamizaaz/IAE-Team-LaLiga/blob/main/static/Cuplikan%20layar%202024-03-27%20075918.png)

The screenshot above shows the interface displaying La Liga teams.

## HTML Templates Explanation

### `index.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <!-- Meta tags -->
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>La Liga Clubs</title>
    <!-- CSS styles -->
    <style>
        /* CSS styles here */
    </style>
</head>
<body>
    <!-- Background image and overlay -->
    <div id="background"></div>
    <div id="overlay"></div>
    <!-- Main content -->
    <div id="content">
        <!-- La Liga logo -->
        <div id="laliga-card">
            <img id="laliga-logo" src="/static/LaLiga_logo_2023.svg.webp" alt="La Liga Logo">
        </div>
        <!-- List of La Liga teams -->
        <ul>
            <!-- Iterate through teams -->
            {% for team in teams %}
                <li>
                    <!-- Link to team details page -->
                    <a href="/team/{{ team.team_key }}">
                        <!-- Team badge and name -->
                        <img src="{{ team.team_badge }}" alt="{{ team.team_name }}">
                        <span>{{ team.team_name }}</span>
                    </a>
                </li>
            {% endfor %}
        </ul>
    </div>
</body>
</html>

<!DOCTYPE html>
<html lang="en">
<head>
    <!-- Meta tags -->
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ team.team_name }}</title>
    <!-- JavaScript function to replace broken image -->
    <script>
        function replaceBrokenImage(image) {
            image.onerror = '';
            image.src = '/static/92588_aitor-paredes.jpg'; 
            return true;
        }
    </script>
    <!-- CSS styles -->
    <style>
        /* CSS styles here */
    </style>
</head>
<body>
    <!-- Background image and overlay -->
    <div id="background"></div>
    <div id="overlay"></div>
    <!-- Main content -->
    <div id="content">
        <!-- Team details -->
        <div id="head-card">
            <!-- Team badge -->
            <img id="logo" src="{{ team.team_badge }}" alt="{{ team.team_name }}" width="200">
            <!-- Team information -->
            <div id="team-info">
                <h1>{{ team.team_name }}</h1>
                <!-- Team details list -->
                <ul>
                    <li>Country: {{ team.team_country }}</li>
                    <li>Founded: {{ team.team_founded }}</li>
                    <li>Venue: {{ team.venue.venue_name }}, {{ team.venue.venue_city }}</li>
                    <li>Capacity: {{ team.venue.venue_capacity }}</li>
                </ul>
            </div>
        </div>
        <!-- List of players -->
        <div id="player-cards">
            <!-- Iterate through players -->
            {% for player in team.players %}
            <div class="player-card">
                <!-- Player name -->
                <h2>{{ player.player_name }}</h2>
                <!-- Player image -->
                <img src="{{ player.player_image }}" alt="{{ player.player_name }}" width="50" onerror="replaceBrokenImage(this);">
                <!-- Player details -->
                <div class="player-details">
                    <p>Age: {{ player.player_age }}</p>
                    <p>Position: {{ player.player_type }}</p>
                    <p>Rating: {{ player.player_rating }}</p>
                </div>
            </div>
            {% endfor %}
        </div>
        <!-- Back button -->
        <button onclick="goBack()">Back</button>
    </div>
    <!-- JavaScript function to go back -->
    <script>
        function goBack() {
            window.history.back();
        }
    </script>
</body>
</html>

