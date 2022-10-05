#To remove the excess files that are generated after posting
#Need to run manually after each post (for now)

import os, shutil

dir = "config"
remove_me = "post.jpeg.REMOVE_ME"
fail = "post.jpeg"

if os.path.exists(dir):
    try:
        shutil.rmtree(dir)
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))
        input('Press any key...')
if os.path.exists(remove_me):
    try:
        os.remove(remove_me)
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))
        input('Press any key...')
if os.path.exists(fail):
    try:
        os.remove(fail)
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))
        input('Press any key...')