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
