
I'm going to be hitting the eject button on Facebook soon, but the one thing I really wanted to save was my photos, and move them over to Picasa for Google+. There's no easy (or at least obvious) way to export all your photos in one fell swoop. So, I wrote a Python script that will do so.

It will download all of your pictures from your Facebook account, and store them in whatever directory you specify (default is your current working directory). Additionally, this script will create a subdirectory for each album, and tuck each photo into the appropriate subdir. This way, when you go to upload them to Picasa, you can just create whatever Picasa folder, and just "select all" in a particular album subdirectory for easy uploadin'.

------------------
Usage Instructions
------------------

1. Go `here <http://developers.facebook.com/docs/reference/api/>`_, scroll down to the second list of links (e.g. "Friends", "News feed", "Profile feed (Wall)", etc.). Click on any link in that list.
2. Copy the token string after "?access_token=" to your clipboard.
3. Open mytoken.py and update the value of the "token" variable with your token from the clipboard.
4. Update the value of "username" in mytoken.py with your Facebook username.
5. Run `python fbphotos.py [-d destination_dir]`. Change `destination_dir` to wherever you want to download the files. By default it is in your current working directory. If the default destination is fine, don't specificy that argument. 
6. All of your images from all of your albums will be downloaded, and automatically segmented into appropriate subdirectories, named to correspond to Facebook albums.


If you spot any bumps or hiccups, please let me know. I suspect the regex that handles substring substitution is a weakspot, but it worked for me. Also, if you have any suggestions to make this better, easier, let me know. This is pretty quick and dirty.
