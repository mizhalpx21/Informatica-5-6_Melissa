weekly_playlist = ["Blinding Lights", "Levitating", "As It Was", "Heat Waves", "Good 4 u"]
print("Weekly paylist: ", weekly_playlist)

print("Requested song: Drivers License ")
weekly_playlist.append("Drivers License")

print("Song added at the beginning of the playlist: Bohemian Rhapsody ")
weekly_playlist.insert(0, "Bohemian Rhapsody")

print("Removing this song from the playlist: Good 4 u")
weekly_playlist.remove("Good 4 u")
weekly_playlist.index("Levitating")
weekly_playlist.count("As it was")
print(weekly_playlist)

print("Playlist in reverse: ")
trowback_thursday = weekly_playlist
trowback_thursday.reverse()
print(trowback_thursday)

print("Playlist in alphabetical order: ")
trowback_thursday = weekly_playlist
trowback_thursday.sort()

print(weekly_playlist)
