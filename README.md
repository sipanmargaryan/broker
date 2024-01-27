## Setup

Make sure you have `docker` and `docker-compose` installed on your machine.

Create `.env` file using `.env_template`.

Commands on linux and macos  enviroments

To build the project

    make

To run the migrations
    
    make migrate

To run the project

    make run

To jump into container migrate database

    $ make shell

To stop running containers

    make stop

To run test
    
    make test