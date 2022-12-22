from mastodon import Mastodon
from apscheduler.schedulers.background import BackgroundScheduler as bs
from random import randrange
import config, os

#This is what will track all of our media in a list so we can pop a random item when we want.
index = []

# Create the Mastodon API object
try:
  mastodon = Mastodon(
    client_id = config.client_id,
    client_secret=config.client_secret,
    access_token=config.access_token,
    api_base_url=config.url
    )
except:
  print("Could not log into Mastodon with the given credentials.")

def index_images() ->list:
  """Makes a list of all images in a directory
  
  Saves data to global variable `index` to be used later.
  """
  global index
  index = os.listdir("./media")

def select_random_image() -> str:
  """Pops one item from the global variable `index`

  This prevents us from having to positively check that a file has been used by simply removing it from the selection pool.
  """
  global index
  if index == []: 
    index_images()
  result = index.pop(randrange(len(index)))
  return result

def make_post():
  """Selects a random image and makes a media post"""
  image = select_random_image()
  mastodon.media_post("./media/{}".format(image))

if __name__ == "__main__":
  print("I LIVE!!!")
  index_images()
  make_post()
  bs.start()
  bs.add_job(make_post(), 'interval', hours=1)