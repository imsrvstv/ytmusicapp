class UtilityYTMusic:
	def __init__(self, instance):
		self.ytmusic = instance

	def searchSong(self, searchQuery):
		searchData =  self.ytmusic.search(searchQuery)
		details = []
		for i in searchData:
			temp = dict()
			try:
				temp['title'] = i['title']
				temp['songid'] = i['videoId']
				temp['imgurl'] = i['thumbnails'][0]['url']
				details.append(temp)
			except:
				pass
		return details

	def createPlaylist(self, playlistName, playlistDescription=""):
		self.ytmusic.create_playlist(playlistName, playlistDescription)
		return True

	def searchPlaylist(self):
		searchData = self.ytmusic.get_library_playlists()
		details = []
		for i in searchData:
			temp = dict()
			try:
				temp['playlistid'] = i['playlistId']
				temp['title'] = self.ytmusic.get_playlist(i['playlistId'])['title']
				details.append(temp)
			except:
				pass
		return details

	def addSongToPlaylist(self, playlistId, listOfSongs):
		self.ytmusic.add_playlist_items(playlistId, listOfSongs, duplicates=True)
		return True