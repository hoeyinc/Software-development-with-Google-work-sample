"""A video player class."""

from .video_library import VideoLibrary
from .video_playlist import Playlist
from collections import defaultdict
import random

class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self._playlist = Playlist()
        self.playing_object = None
        self.playing_id = None
        self.playback = None

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        all_videos =[]
        
        print("Here's a list of all available videos:")
        for video in self._video_library._videos:
            video_object = self._video_library._videos.get(video, None)
            video_title = str(video_object._title)
            video_id = str(video_object.video_id)
            video_tags = " ".join(video_object.tags)
            video_text_object = video_title + " (" + video_id + ") [" + video_tags + "]"
            all_videos.append(video_text_object)
            
        for i in sorted(all_videos): print("  "+i)
        
    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        if self._video_library._videos.get(video_id, None) == None:
            print("Cannot play video: Video does not exist")
        else:
            if self.playing_object != None:
                print("Stopping video: "+str(self.playing_object._title))
            self.playing_id = video_id
            self.playing_object = self._video_library._videos.get(video_id, None)
            self.playback = "Playing"
            print("Playing video: "+str(self.playing_object._title))
        
    
    def stop_video(self):
        """Stops the current video."""
        if self.playing_object != None:
            print("Stopping video: " +str(self.playing_object._title))
            self.playing_object = None
            self.playing_id = None
            self.playback = None
        else:
            print("Cannot stop video: No video is currently playing")

    def play_random_video(self):
        """Plays a random video from the video library."""
        video_objects = []
        if self.playing_object != None:
            print("Stopping video: " +str(self.playing_object._title))
        for video in self._video_library._videos:
            video_objects.append(self._video_library._videos.get(video, None))
        self.playing_object = random.choice(video_objects)
        self.playing_id = self.playing_object.video_id
        print("Playing video: "+str(self.playing_object._title))

    def pause_video(self):
        """Pauses the current video."""
        if self.playback == "Playing":
            print("Pausing video: "+str(self.playing_object._title))
            self.playback = "Paused"
        elif self.playback == "Paused":
            print("Video already paused: "+str(self.playing_object._title))
        else:
            print("Cannot pause video: No video is currently playing")

    def continue_video(self):
        """Resumes playing the current video."""
        if self.playback == "Playing":
            print("Cannot continue video: Video is not paused")
        elif self.playback == "Paused":
            print("Continuing video: "+str(self.playing_object._title))
            self.playback == "Playing"
        else:
            print("Cannot continue video: No video is currently playing")

    def show_playing(self):
        """Displays video currently playing."""
        if self.playing_object != None:
            if self.playback != "Paused":
                print("Currently playing: " + str(self.playing_object._title) + " (" + str(self.playing_object.video_id) + ") [" + " ".join(self.playing_object.tags) + "]")
            else:
                print("Currently playing: " + str(self.playing_object._title) + " (" + str(self.playing_object.video_id) + ") [" + " ".join(self.playing_object.tags) + "] - PAUSED")  
        else:
            print("No video is currently playing")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if playlist_name.strip() == playlist_name:
            if playlist_name.upper() not in [x.upper() for x in self._playlist.playlist_names]:
                self._playlist.playlist_names.append(playlist_name)
                self._playlist.playlists[playlist_name.upper()] = []
                print("Successfully created new playlist: "+str(playlist_name))
            else:
                print("Cannot create playlist: A playlist with the same name already exists")
        else:
            print("Cannot create playlist: A playlist with the same name already exists")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        if playlist_name.upper() not in [x.upper() for x in self._playlist.playlist_names]:
            print("Cannot add video to "+str(playlist_name)+": Playlist does not exist")
        else:
            if self._video_library._videos.get(video_id, None) == None:
               print("Cannot add video to "+str(playlist_name)+": Video does not exist")
            else:
                video = self._video_library._videos.get(video_id, None)
                playlist = self._playlist.playlists.get(playlist_name.upper())
                if video in playlist:
                    print("Cannot add video to "+str(playlist_name)+": Video already added")
                else:
                    self._playlist.playlists[playlist_name.upper()].append(video)
                    print("Added video to "+str(playlist_name)+": "+ str(video._title))
        
    def show_all_playlists(self):
        """Display all playlists."""
        if self._playlist.playlist_names == []:
            print("No playlists exist yet")
        else:
            print("Showing all playlists:")
            for i in sorted(self._playlist.playlist_names): print (i) 

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        playlist_videos = []
        if playlist_name.upper() not in [x.upper() for x in self._playlist.playlist_names]:
            print("Cannot show playlist "+str(playlist_name)+": Playlist does not exist")
        elif self._playlist.playlists.get(playlist_name.upper()) == []:
            print("Showing playlist: "+str(playlist_name)+"\n  No videos here yet")
        else:
            for video in self._playlist.playlists.get(playlist_name.upper()):
                video_title = str(video._title)
                video_id = str(video.video_id)
                video_tags = " ".join(video.tags)
                video_text_object = video_title + " (" + video_id + ") [" + video_tags + "]"
                playlist_videos.append(video_text_object)
            print("Showing playlist: "+str(playlist_name))
            for i in playlist_videos : print (i)
        
    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        if playlist_name.upper() not in [x.upper() for x in self._playlist.playlist_names]:
            print("Cannot remove video from "+str(playlist_name)+": Playlist does not exist")
            
        else:
            all_video_ids = []
            for video in self._video_library._videos:
                video_object = self._video_library._videos.get(video, None)
                all_video_ids.append(str(video_object.video_id))
            if video_id not in all_video_ids:
                print("Cannot remove video from "+str(playlist_name)+": Video does not exist")
            else:
                playlist_videos = {}
                for video in self._playlist.playlists.get(playlist_name.upper()):
                    pvideo_title = str(video._title)
                    pvideo_id = str(video.video_id)
                    playlist_videos[pvideo_id] = video, pvideo_title
                if video_id not in playlist_videos:
                    print("Cannot remove video from "+str(playlist_name)+": Video is not in playlist")
                else:
                    self._playlist.playlists[playlist_name.upper()].remove(playlist_videos[video_id][0])
                    print("Removed video from "+str(playlist_name)+": "+str(playlist_videos[video_id][1]))

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if playlist_name.upper() not in [x.upper() for x in self._playlist.playlist_names]:
            print("Cannot clear playlist "+str(playlist_name)+": Playlist does not exist")
        else:
            self._playlist.playlists[playlist_name.upper()] = []
            print("Successfully removed all videos from "+str(playlist_name))

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if playlist_name.upper() not in [x.upper() for x in self._playlist.playlist_names]:
            print("Cannot delete playlist "+str(playlist_name)+": Playlist does not exist")
        else:
            for name in self._playlist.playlist_names:
                if name.upper() == playlist_name.upper():
                    self._playlist.playlist_names.remove(name)
            self._playlist.playlists.pop(playlist_name.upper())
            print("Deleted playlist: "+str(playlist_name))

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        all_videos_and_titles = {}
        all_video_titles = []
        for video in self._video_library._videos:
            video_object = self._video_library._videos.get(video, None)
            all_video_titles.append(str(video_object._title.upper()))
            all_videos_and_titles[str(video_object._title.upper())] = video_object
        if search_term.upper() not in "".join(str(i) for i in all_video_titles):
                print("No search results for "+str(search_term))
        else:
            search_results = []
            video_titles_and_id = {}
            for title in all_videos_and_titles:
                if search_term.upper() in title:
                    video_object = all_videos_and_titles[title]
                    video_title = str(video_object._title)
                    video_id = str(video_object.video_id)
                    video_tags = " ".join(video_object.tags)
                    video_text_object = video_title + " (" + video_id + ") [" + video_tags + "]"
                    video_titles_and_id[video_title] = video_id
                    search_results.append(video_text_object)
                    
            print("Here are the results for "+str(search_term)+":")
            for count,i in enumerate(sorted(search_results)): print("  "+str(count+1)+") "+i)

            print("Would you like to play any of the above? If yes, specify the number of the video.")
            print("If your answer is not a valid number, we will assume it's a no.")
            user_choice = input()
            if user_choice.isdigit():
                number = int(user_choice)
                if int(user_choice) >= 1 and int(user_choice) <= len(search_results):
                    self.play_video(list(sorted(video_titles_and_id.items()))[number-1][1])
            
        
    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        all_videos_and_titles = {}
        all_video_tags = []
        for video in self._video_library._videos:
            video_object = self._video_library._videos.get(video, None)
            all_video_tags.append((" ".join(video_object.tags)).upper())
            all_videos_and_titles[str(video_object._title.upper())] = video_object
        if video_tag.upper() not in "".join(str(i) for i in all_video_tags):
                print("No search results for "+str(video_tag))
        else:
            search_results = []
            video_titles_and_id = {}
            for item in all_videos_and_titles:
                if video_tag.upper() in (" ".join(all_videos_and_titles[item].tags)).upper():
                    video_object = all_videos_and_titles[item]
                    video_title = str(video_object._title)
                    video_id = str(video_object.video_id)
                    video_tags = " ".join(video_object.tags)
                    video_text_object = video_title + " (" + video_id + ") [" + video_tags + "]"
                    video_titles_and_id[video_title] = video_id
                    search_results.append(video_text_object)
                    
            print("Here are the results for "+str(video_tag)+":")
            for count,i in enumerate(sorted(search_results)): print("  "+str(count+1)+") "+i)

            print("Would you like to play any of the above? If yes, specify the number of the video.")
            print("If your answer is not a valid number, we will assume it's a no.")
            user_choice = input()
            if user_choice.isdigit():
                number = int(user_choice)
                if int(user_choice) >= 1 and int(user_choice) <= len(search_results):
                    self.play_video(list(sorted(video_titles_and_id.items()))[number-1][1])

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
