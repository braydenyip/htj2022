# htj2022
Hack the Job Project 2022

Team: Valgrind my Mind\
Members: 5

## Using Spotify's API:
braydenyip.github.io/htj2022

### Idea 1: Outputs 1st liked track and most liked artist
Incorporating Spotify's Web API, Spotipy, to list the liked songs of a user. This information is then used to describe to the user what their first saved track was, as well as which artist they have the most songs saved.
- TO DO's: Save only the 1st liked song, tally the most common artist (maybe?).

### Idea 2: Outputs most common mood
Incorporating the Spotipy API to organize the liked songs of a user into mood categories. Using "loudness" and "tempo" from 'sections' in Spotify's Audio Analysis json to create a range for each user input to have it's own custom result. Results will be created from a list of moods and their related ranges (loudness + tempo), and print which mood is the most popular for the user. 
- TO DO's: Find out how to pull json with values from track's audio features, calculate a formula to pair with moods and print most occuring (ie. counter for each mood).

### Idea 3: Outputs song for inputted mood
Incorporating Spotify's Web API, Spotipy, to list songs that match a user's mood. These categories are stored in a dictionary of moods with associated songs. These moods will be calculated using energy < float >, mode < 0 or 1 >, and loudness. 
- TO DO's: Find out how to pull json with values from track's audio features, calculate formula to pair with moods, print out a song(s) for each mood.

______________________________________
Backend References:
https://developer.spotify.com/documentation/web-api/reference/#/operations/get-audio-features  
https://spotipy.readthedocs.io/en/2.19.0/

Frontend & Linking References:
https://www.youtube.com/watch?v=kng-mJJby8g  
https://www.youtube.com/watch?v=dam0GPOAvVI  
https://www.w3schools.com/html/html_examples.asp 
https://www.youtube.com/watch?v=gu2jyJ6oIdk
