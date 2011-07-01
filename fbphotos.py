import os
import urllib2

import facepy

from mytoken import token, username

def get_photos(dl_dir=os.getcwd()):
    fb_photos = find_photos()
    for album_id in fb_photos:
        for img_url in fb_photos[album_id]:
            img_name = img_url.split('/')[-1]
            url = urllib2.urlopen(img_url)
            
            with open("%s/%s" % (dl_dir, img_name), 'w') as f:
                meta = url.info()
                filesize = int(meta.getheaders("Content-Length")[0])
                print "Downloading: %s Bytes: %s" % (img_name, filesize)
                filesize_dl = 0
                blocksize = 8192
                while True:
                    buff = url.read(blocksize)
                    if not buff:
                        break

                    filesize_dl += blocksize
                    f.write(buff)
                    status = r"%10d [%3.2f%%]" % (filesize_dl,
                                                  filesize_dl * 100. / filesize)
                    status = status + chr(8)*(len(status)+1)
                    print status,
    
def find_photos():
    '''
    Creates a dictionary, with album id as key and a list of images
    in the album as the value.
    '''
    photos = {}
    graph = facepy.GraphAPI(token)
    my_albums = graph.get("%s/albums" % username)
    album_ids = [a['id'] for a in my_albums]
    for aid in album_ids:
        my_pics = graph.get("%s/photos?limit=100" % aid)
        pic_urls = [pic['source'] for pic in my_pics]
        photos[aid] = pic_urls

    return photos


if __name__ == "__main__":
    get_photos()
