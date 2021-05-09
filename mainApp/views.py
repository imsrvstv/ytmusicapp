from django.shortcuts import render, redirect
from ytmusicapi import YTMusic
from .Scripts.mainBackend import UtilityYTMusic

ytMusicObject = YTMusic('mainApp/headers_auth.json')
utilityObject = UtilityYTMusic(ytMusicObject)

def home(request):
    return render(request, 'index.html', {"createdPlay": False, "addedSong": False})

def midPro(request):
    global utilityObject
    selectedPlaylist = request.POST['playlist']
    temp = request.POST['songids']
    listOfSongs = list(temp.split())
    # print(listOfSongs)
    # print(selectedPlaylist)
    utilityObject.addSongToPlaylist(selectedPlaylist, listOfSongs)
    return render(request, 'index.html', {"createdPlay": False, "addedSong": True})

def searchResult(request):
    global utilityObject
    searchQuery = request.POST['songName']
    searchData = utilityObject.searchSong(searchQuery)
    searchPlaylist = utilityObject.searchPlaylist()
    context = {
        "data":searchData,
        "data1":searchPlaylist
    }
    return render(request, 'searchResult.html', context)

def midPro1(request):
    global utilityObject
    playlistTitle = request.POST['playtitle']
    playlistDesc = request.POST['playdesc']
    # print(playlistTitle)
    # print(playlistDesc)
    utilityObject.createPlaylist(playlistTitle, playlistDesc)
    return render(request, 'index.html', {"createdPlay":True, "addedSong":False})

def createPlaylist(request):
    return render(request, 'createPlaylist.html')