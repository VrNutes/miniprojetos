# Docker-compose
It now comes with Docker in a normal installation,
so you can set up your complete environment/infrastructure from a simple file called 'docker-compose.yml'.

## Main Commands

<strong>When should I use it?</strong><br/>
When you need to set up a project that has a docker-compose.yml file.
```sh
docker compose up -d # Set up all services described in docker-compose.yml
docker compose up -d <service_name> # Set up the specified service with configurations described in docker-compose.yml and its dependencies
docker compose up -d <service1_name> <service2_name> <service..._name> # Set up multiple specified services with configurations described in docker-compose.yml and their dependencies
```
<strong>When should I use it?</strong><br/>
When you have already set up a project that has a docker-compose.yml file and want to stop all containers.
```sh
docker compose down # Shut down services described in docker-compose.yml
docker compose down -v # Shut down services and destroy volumes described in docker-compose.yml
```