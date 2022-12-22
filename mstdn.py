from mastodon import Mastodon
from apscheduler.schedulers.background import BackgroundScheduler as bs
from random import randrange
import config, os

#This is what will track all of our media in a list so we can pop a random item when we want.
index = []

# Create the Mastodon API object

mastodon = Mastodon(
    access_token = config.access_token,
    api_base_url = "https://" + config.url
  )

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
  global index
  image = select_random_image()
  path = "./media/{}".format(image)
  print("Selected image is: " + path)
  mastodon.status_post(status=None, media_ids=[mastodon.media_post(path, mime_type="image/jpg", file_name=image)])

if __name__ == "__main__":
  print("I LIVE!!!")
  index_images()
  make_post()
  bs.start()
  bs.add_job(make_post(), 'interval', hours=1)