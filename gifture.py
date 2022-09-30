# to run type "python3 mojo_jojo.py" into cmd at the path where this file is
#Will need to 
#pip install pyglet
#pip install dropbox
#in cmd
import dropbox
import pyglet
import urllib

dbx = dropbox.Dropbox("dropbox key/code")
mojojojolocalfilename = "mojo_jojo.gif"
# from here we've signed into your dropbox account
# the dropbox path for the root for this dropbox script is
# Dropbox/Apps/Mojo_Jojo
# Which is where Mojo Jojo gifs should be placed

gif = dbx.files_get_temporary_link("/mojojojo1.gif")
testfile = urllib.request.URLopener()
testfile.retrieve(gif.link, mojojojolocalfilename)

# the path for pyglet.resource.animation where you placed this python file
sprite = pyglet.sprite.Sprite(pyglet.resource.animation(mojojojolocalfilename))

H_ratio = max(sprite.height, 720) / min(sprite.height, 720)
W_ratio = max(sprite.width, 720) / min(sprite.width, 720)

sprite.scale = min(H_ratio, W_ratio)

window = pyglet.window.Window(width=720, height=720, fullscreen=True)

def close(event):
    win.close()

@window.event
def on_draw():
    window.clear()
    sprite.draw()

pyglet.app.run()

##Things to expand on

##Dynamic resolution scaling

##Pull multiple gifs instead of a single one