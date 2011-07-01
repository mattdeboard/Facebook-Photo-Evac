
------------------
Usage Instructions
------------------

1. Go `here <http://developers.facebook.com/docs/reference/api/>`_, scroll down to the second list of links (e.g. "Friends", "News feed", "Profile feed (Wall)", etc.). Click on any link in that list.
2. Copy the token string after "?access_token=" to your clipboard.
3. Open mytoken.py and update the value of the "token" variable with your token from the clipboard.
4. Update the value of "username" in mytoken.py with your Facebook username.
5. Run `python fbphotos.py destination_dir`. Change `destination_dir` to wherever you want to download the files. By default it is in your current working directory. If the default destination is fine, don't specificy that argument. You must create the destination directory before downloading.
6. All of your images from all of your albums will be downloaded.
