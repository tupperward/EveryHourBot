# EveryHourBot
A Mastodon bot written in python that powers [@hourlymilbhats@botsin.space](https://botsin.space/@hourlymilbhats) using Mastodon.py

Thanks to [thunderysteak](https://github.com/thunderysteak) of [Possum Every Hour](https://twitter.com/possumeveryhour) for making the original JS version of this app. This fork is practically a new app itself, but I wanna give credit where it's due.

This can be used to post an image to Mastodon hourly. It is as reliable as the host instance's api, but has a built in 5x retry. It will only post images, no text and no alt-text that isn't already on the images. 

## Dependencies
- Docker
- a directory full of [valid images](https://www.iana.org/assignments/media-types/media-types.xhtml#image). (Don't worry, it's pretty much everything.)

OR

- Python 3.10
- `pip install -r requirements.txt`
- a directory full of [valid images](https://www.iana.org/assignments/media-types/media-types.xhtml#image).

## Quick Start using Docker
1. [Install Docker](https://docs.docker.com/engine/install/)
1. `docker run -d --env EHB_ACCESS_TOKEN=<foo> --env EHB_DOMAIN=<bar> --volume /full/path/to/media:/ehb/media tupperward/everyhourbot:latest`

##Alternatively:
1. Clone the repository to a local directory. 
1. Set the your respective `ACCESS_TOKEN` and `URL` environment variables.
1. Populate the `media` directory with [valid images](https://www.iana.org/assignments/media-types/media-types.xhtml#image).
1. `python mstdn.py`
