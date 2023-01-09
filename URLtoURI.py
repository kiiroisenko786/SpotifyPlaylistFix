import spotify_uri

urls = open("songurls.txt", "r")
uris = open("uris.txt", "a+")

for url in urls:
    uris.write(spotify_uri.formatURI(url)+"\n")