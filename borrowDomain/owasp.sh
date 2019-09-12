- echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
- docker build -t omuga/bmborrowedjango_web .
- docker run -d --name bmborrowed -t omuga/bmborrowedjango_web
- sleep 15
after_script:
    - docker run --name owasp --link bmborrowed -t owasp/zap2docker-weekly zap-full-scan.py -t http://bmborrowed:8001