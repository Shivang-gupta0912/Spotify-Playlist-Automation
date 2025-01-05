# Spotify Playlist Automation  

This repository contains two Python scripts that automate the creation of Spotify playlists:  
1. **Billboard to Spotify**  
2. **Top Tracks Playlist**  

## 1. Billboard to Spotify  

### Overview  
This script automates the creation of Spotify playlists from Billboard's Top 100 songs on a specified date.  

### Key Features  
- Scrapes Billboard's Top 100 songs for a given date using web scraping techniques.  
- Integrates with Spotify's Web API to search for songs and create a playlist in the user's Spotify account.  
- Ask for a date and authenticate with Spotify.  

### Prerequisites  
- Python 3.x  
- Required libraries: `requests`, `BeautifulSoup`, `spotipy`, `python-dotenv`
- Spotify Developer Account for API credentials.  

## 1. Top Tracks Playlist 

### Overview  
This script generates a Spotify playlist of your favorite songs by leveraging Spotify's Web API.  

### Key Features  
- Fetches the user's top tracks from Spotify based on their listening history and preferences.
- Creates a new playlist in the user's Spotify account with the fetched top tracks.
- Offers a seamless user experience with interactive prompts and API integration. 

### Prerequisites  
- Python 3.x
- Required libraries: spotipy, python-dotenv.
- Spotify Developer Account for API credentials. 

## Installation

1. Clone the repository to your local machine:
   ```bash
   git clone <repository_url>
   cd <repository_name>

2. Install the required libraries:
   ```bash
   pip install -r requirements.txt

3. Create a .env file and add your Spotify credentials:
    ```.env
    CLIENT_ID=your_spotify_client_id
    CLIENT_SECRET_CODE=your_spotify_client_secret
    USER_NAME=your_spotify_username

4. Run the scripts:
- For Billboard to Spotify:
    ```bash
    python billboard_to_spotify/main.py
- For Top Tracks Playlist:
    ```bash
    python top_tracks_playlist/main.py

## Contributing

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Create a new Pull Request.

## Reference
This project uses Spotify's Web API for playlist creation and song fetching. You can learn more about it here:
[Spotify Web API Documentation](https://developer.spotify.com/documentation/web-api)

[Shivang Gupta]