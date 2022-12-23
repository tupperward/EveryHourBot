# EveryHourBot
A Mastodon bot written in python that powers @hourlymilbhats@botsin.space using Mastodon.py

Thanks to [thunderysteak](https://github.com/thunderysteak) for making the original JS version of this app. This fork is practically a new app itself, but I wanna give credit where it's due.

## Dependencies
- Docker
- a directory full of [valid images](https://www.iana.org/assignments/media-types/media-types.xhtml#image). (Don't worry, it's pretty much everything.)

OR

- Python 3.10
- `pip install -r requirements.txt`
- a directory full of jpgs

## Quick Start using Docker
1. [Install Docker](https://docs.docker.com/engine/install/)
1. `docker run -d --env EHB_ACCESS_TOKEN=<foo> --env EHB_DOMAIN=<bar> --volume /full/path/to/media:/ehb/media tupperward/everyhourbot:mastodon`

###Alternatively:
1. Clone the repository to a local directory. 
1. Set the your respective `ACCESS_TOKEN` and `URL` environment variables.
1. Populate the `media` directory with [valid images](https://www.iana.org/assignments/media-types/media-types.xhtml#image).
1. `python mstdn.py`