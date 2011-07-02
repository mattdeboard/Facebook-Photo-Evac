import optparse
import os
import re
import subprocess
import sys
import urllib2

import facepy

from mytoken import token, username

def get_photos(dl_dir):
    dest = os.path.abspath(dl_dir)
    p = re.compile(r"[,!'\ /]")
    fb_photos = find_photos()
    for album in fb_photos:
        albname = p.sub("_", album).lower()
        mk_album_dirs(dest, albname)
        folder = albname
        for img_url in fb_photos[album]['images']:
            img_name = img_url.split('/')[-1]
            url = urllib2.urlopen(img_url)
            
            with open("%s/%s/%s" % (dest, folder, img_name), 'w') as f:
                meta = url.info()
                filesize = int(meta.getheaders("Content-Length")[0])
                #print "Downloading: %s Bytes: %s" % (img_name, filesize)
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
                    #print status,
    
def find_photos():
    '''
    Creates a dictionary, with album id as key and a list of images
    in the album as the value.
    '''
    albums = {}
    graph = facepy.GraphAPI(token)
    my_albums = graph.get("%s/albums" % username)
    for album in my_albums:
        albums[album['name']] = {}
        albums[album['name']]['id'] = album['id']
        my_pics = graph.get("%s/photos?limit=100" % album['id'])
        albums[album['name']]['images'] = [pic['source'] for pic in my_pics]
    return albums

def mk_album_dirs(dest, album):
    '''
    Create a subfolder for each facebook album.
    '''
    if not os.path.exists("%s/%s" % (dest, album)):
        os.mkdir("%s/%s" % (dest, album))
    return

if __name__ == "__main__":
    d = os.getcwd()
    parser = optparse.OptionParser()
    parser.add_option("-d", "--dest", action="store", type="string",
                      dest="dest_dir", default=os.getcwd(),
                      help=("Specify the directory where you want your photos t"
                            "o be downloaded. This directory must already exist"
                            ". Photos will be downloaded to current working dir"
                            " by default."))
    args = sys.argv[1:]
    (options, args) = parser.parse_args(args)
    get_photos(options.dest_dir)
