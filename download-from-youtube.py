#today we will learn how to dwnload audio and video from youtube and grab all information about playlist

import pafy     #this module will help us to grab information and download video and audio

from pprint import  pprint #this will help us to pretty-print dictonary format

####################### lets Download video  ####################
# link="https://www.youtube.com/watch?v=oOWVyuZ-_gM"                 #now let put the link of video to download here

# v=pafy.new(link) 

# video=v.getbest() #now with this line will get the best quality of video to download

# path=r"C:\Users\MoKHleS\Desktop\Tutorial"          # in this step lets choose the path to download 

# video.download(path)   #now in this line will put the path and download the video lets see













# ####################### lets learn how to Download audio from youtube  ####################
# link="https://www.youtube.com/watch?v=oOWVyuZ-_gM"    #like we do before put the link here

# v=pafy.new(link) 

# audio=v.getbestaudio("m4a") # and now we will get the best quality of audio as type m4a

# path=r"C:\Users\MoKHleS\Desktop\Tutorial"     #here we put the path

# audio.download(path) #now lets download and see















#########   now let know how to grab all information about video    ####################

# # url of video 
# link = "https://www.youtube.com/watch?v=oOWVyuZ-_gM"

# # instant created 
# video = pafy.new(link) 
  
# # here we will print the title of video 
# print(video.title) 
  
# # print rating 
# print(video.rating) 
  
# # print viewcount 
# print(video.viewcount) 
  
# # print author & video length 
# print(video.author, video.length) 

# #like we see it is very easy to grab all inforamtion about video like title ...







##########  Now lets learn how to grab information for all play list video ############

#put url of playlist here
link="https://www.youtube.com/watch?v=SlPhMPnQ58k&list=PL4o29bINVT4EG_y-k5jGoOu3-Am8Nvi10"
play = pafy.get_playlist(link)

#now like we see before we will print the information of playlist 
# # print title of playlist
# print("title ",play['title']) #like this we will print the title of playlist

# #the author of the playlist
# print("author ",play['author'])

# #print the length of playlist
# print("length of playlist ",len(play["items"])) #lets see output

#now lets print information about video of playlist for example lets print the information about video number 3


videonumber=3 #put here the number of video you want to grab all infomation about it
#pprint(play["items"][videonumber]["playlist_meta"]) #it will return a dictonary of information

#it a dictionary information about video if you want for example to know number of like choose the key to print the value
#lets see how many likes 
pprint(play["items"][videonumber]["playlist_meta"]["likes"])


#now the video is end i will put the link of this file in the description chekout and try by your self to learn anf if you want more option see the documentaion of pafy 






 