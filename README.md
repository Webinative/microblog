# microblog

A personal micro-blogging website.

## Dev Environment

You can run this project locally on your machine.

You will need,

1. [Docker](https://docs.docker.com/engine/install/)
1. [docker compose](https://docs.docker.com/compose/install/)

Once installed, run these commands,

```sh
# build the image
docker compose build

# bring up the containers
docker compose up -d

# run migrations and load the initial data
docker compose exec microblog-django bash init_alpha.sh
```

Visit [http://localhost:8000](http://localhost:8000) from your browser.

![screenshot](static/images/localhost_8000.png)

Other useful docker commands,

```sh
# check the status of containers
docker compose ps

# stop the containers
docker compose stop

# start the containers
docker compose start

# remove the containers
docker compose down
```

## Live Environment

You can deploy this project to a cloud server (VPS) with or without a docker runtime.

You will need,

1. Ubuntu OS (22.04 recommended)
1. Python 3.10.4
1. Django 4.2
1. Postgres 14.4
