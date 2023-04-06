# docker_flask
Docker setup to start a Flask project.

## Supported tags and respective `Dockerfile` links

(See ["What's the difference between 'Shared' and 'Simple' tags?" in the FAQ](https://github.com/docker-library/faq#whats-the-difference-between-shared-and-simple-tags).)

All images use the Debian Slim images from 
[Python](https://hub.docker.com/_/python) project as the source.

## Simple tags

-	[`latest`, `python-3.11.2`](./Dockerfile)
-	[`latest-app`, `python-3.11.2-app`](./Dockerfile.app)
-	[`gunicorn`](./Dockerfile.gunicorn)
-	[`python-3.9.2`](./Dockerfile.python-3.9.2)
-	[`python-3.9.2-app`](./Dockerfile.app-3.9.2)
- `dev`

## How to use this image

### Create a `Dockerfile` in your Python app project

```dockerfile
FROM pvital/docker_flask:latest

WORKDIR /usr/src/app

COPY . .

EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["-m", "flask", "run", "--host=0.0.0.0"]
```

You can then build and run the Docker image:

```console
$ docker build -t <img_name>:[tag] .
$ docker run -it --rm -p 8080:5000 --name <app_name> <img_name>:[tag]
```

where:

* `<img_name>` is the name of the Docker image for your project.
* `[tag]` is an optional alias for this image. The default is `latest`.
* `<app_name>` specifies a name with which you can refer to your container in 
subsequent commands.


### Run a simple Flask project

For many simple, single Flask projects, you may find it inconvenient to write a
complete `Dockerfile`. In such cases, you can run a Flask application by using
the `docker_flask` image directly:

```console
$ docker run -it --rm \
  -p 8080:5000 \
  --mount type=bind,source="$PROJ_DIR",target=/app \
  --name <app_name> \
  pvital/docker_flask:latest
```

where:

* `$PROJ_DIR` is the path to the project directory. 
* `<app_name>` specifies a name with which you can refer to your container in 
subsequent commands.

Now the Flask service is responding on port 8080 of your local host. Point
your browser to http://127.0.0.1:8080/ and enjoy the magic. If you want the 
application to listen to a different port, substitute the number 8080 from the
command above with the desired one.

If you want to run the Flask application in a daemonized mode, execute the
command with the `-d` argument:

```console
$ docker run -d --rm \
  -p 8080:5000 \
  --mount type=bind,source="$PROJ_DIR",target=/app \
  --name <app_name> \
  pvital/docker_flask:latest
 ```

To terminate the execution, just type CTRL+C in the same console.
