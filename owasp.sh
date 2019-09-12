echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
docker build -t omuga/bmborrowedjango_web .
docker run -d --name bmborrowed -t omuga/bmborrowedjango_web
sleep 15