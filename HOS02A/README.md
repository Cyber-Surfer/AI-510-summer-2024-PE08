# Build image
`docker image build -t flask_docker_image .`

# Run container
`docker run --rm -p 3456:3456 flask_docker_image`
or
`docker run -d --rm -p 3456:3456 flask_docker_image`

# Stop container
`docker ps`
`docker stop {container_name}`