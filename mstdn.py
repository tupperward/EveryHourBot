from mastodon import Mastodon
from random import randrange
from time import sleep
import os, config

#This is what will track all of our media in a list so we can pop a random item when we want.
index = []

# Create the Mastodon API object

mastodon = Mastodon(
    access_token = config.access_token,
    api_base_url = "https://" + config.domain
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
  print("\nSelected image is: " + image)
  extension = os.path.splitext(path)[1].strip('.')
  attempts = 0
  while attempts <= 5:
    try:
      # TODO Make it so I can make a caption for the image.
      mastodon.status_post(status=None, media_ids=[mastodon.media_post(path, mime_type="image/{}".format(extension), file_name=image)])
      print("Success!")
    except Exception as e:
      attempts += 1
      if attempts == 5:
        print("\nAttempted 5 times. Skipping this hour.")
        break
      else:
        print("\nThis is attempt {}".format(attempts))
        print("Failed to create post. Sleeping 5 seconds and retrying.")
        print(e)
        sleep(5)
        continue
    else:
      print("See you later, Space Cowboy.\n")
      break

if __name__ == "__main__":
    print("\nI LIVE!!!")
    index_images()
    print ("\nList of all {} available files in /ehb/media: ".format(len(index)) + "\n\n" + str(os.listdir("./media")))
    while True:
      make_post()
      sleep(3600)