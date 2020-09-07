playlist = '1,2,3,4,5'
song = playlist.split(',')
song.remove('3')

print(song)
new = ','.join(song)
print(new)