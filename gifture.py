from multiprocessing import Event
import requests
import json
import argparse
import random
import os
import urllib.request
import pyglet
import pyglet.window.key
from dotenv import load_dotenv

def configure():
    load_dotenv()

def get_gifs():
    # set the apikey and limit
    apikey = os.getenv('api_key')  # click to set to your apikey
    lmt = 10    # set number of gifs to return
    ckey = "my_test_app"  # set the client_key for the integration and use the same value for all API calls

    search_term = "excited"
    r = requests.get(
        "https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" % (search_term, apikey, ckey,  lmt))

    # gif_list = []

    def dl_gif(url, file_path, file_name):
        full_path = file_path + file_name + '.gif'
        urllib.request.urlretrieve(url, full_path)

    if r.status_code == 200:
        gif_json_data = json.loads(r.content)
        for each in gif_json_data['results']:
            gif = (each['media_formats']['gif']['url'])
            # gif_description = (each['content_description'])
            url = gif
            index = gif_json_data['results'].index(each)
            file_name = (f'gif{index}')

            dl_gif(url, 'images/', file_name)   
    else:
        gif_json_data = None


def update_image(dt):
    ani = pyglet.resource.animation(random.choice(image_paths))
    sprite.image = ani
    sprite.scale_x = max(sprite.height, 720) / min(sprite.height, 720)
    sprite.scale_y = max(sprite.width, 720) / min(sprite.width, 720)
    window.clear()


def get_image_paths(input_dir='.'):
    paths = []
    for root, dirs, files in os.walk(input_dir, topdown=True):
        for file in sorted(files):
            if file.endswith(('gif')):
                path = f'images/{file}'
                paths.append(path)
    return paths


window = pyglet.window.Window(width=720, height=720)
# window = pyglet.window.Window(width=720, height=720, fullscreen=True)

@window.event
def on_draw():
    window.clear()
    sprite.draw()

if __name__ == '__main__':
    configure()
    parser = argparse.ArgumentParser()
    parser.add_argument('dir', help='directory of images', nargs='?', default=os.getcwd())
    args = parser.parse_args()
    if len(get_image_paths(args.dir)) == 0:
        get_gifs()
    image_paths = get_image_paths(args.dir)
    ani = pyglet.resource.animation(random.choice(image_paths))
    sprite = pyglet.sprite.Sprite(ani)
    H_ratio = max(sprite.height, 720) / min(sprite.height, 720)
    W_ratio = max(sprite.width, 720) / min(sprite.width, 720)
    sprite.scale = min(H_ratio, W_ratio)

    pyglet.clock.schedule_interval(update_image, 6.0)

    pyglet.app.run()