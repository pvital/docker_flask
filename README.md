# docker_flask
Docker setup to start a Flask project.

## Building the Docker image

To build the Docker image, do:

```
# docker build -t <img_name>:latest .
```

where `<img_name>` is the name of the Docker image for your project.

## Running the Docker image

To run the Docker image created before, execute:

```
# docker run -d \
  -p 8080:8080 \
  --mount type=bind,source="$PROJ_DIR",target=/app \
  --name <app_name> \
  <img_name>:latest
```

where:

* `$PROJ_DIR` is the path to the project directory, 
* `<app_name>` specifies a name with which you can refer to your container in 
subsequent commands,
* `<img_name>` is the name of the Docker image you built in the previous step.

Now the Flask service is responding on port 8080 of your localhost. Point
your browser to http://127.0.0.1:8080/ and enjoy the magic.

If you want to see the output of the Flask console, execute the previous
command without the '-d' argument, and you will see the following output:

```
# docker run \
  -p 8080:8080 \
  --mount type=bind,source="$PROJ_DIR",target=/app \
  --name <app_name> \
  <img_name>:latest

 * Serving Flask app "server" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 955-219-155
 ```

To terminate the execution, just type CTRL+C in the same console.
