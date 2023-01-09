# SpotifyPlaylistFix
Just a quick fix to resolve my issue with my Spotify playlist

Not a project, but I thought it would be beneficial to upload to Github should I decide to expand on it or need it later.

## Function
The function of this essentially was to just to fix my issue with my Spotify playlist that was originally copied from an old account
and therefore no longer retained its functionality of "date added" order. So all this does is retrieve the URI of each track from its URL,
then use the Spotipy library to create a new playlist and add everything in order. The 1 second delay was initally just a test to see
if it made a difference in ordering when compared to just pushing them all as a list into the playlist, but it worked after the initial
try so I left it like that.

Safe to say it was successful!
