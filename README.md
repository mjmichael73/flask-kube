# flask-kube

### Docker commands:
    docker build -t flask-kube-app:1.0.0 .
    docker run -d -p 80:5000 --name flask-kube-app flask-kube-app:1.0.0
    docker push flask-kube-app:latest

### minikube:
I'm using ubuntu and I've installed minikube.
    minikube start
    minikube dashboard
    minikube ip
    minikube ssh
    minikube kubectl -- get deployments
    minikube kubectl -- get pods
    minikube kubectl -- delete deployment deployment_name
    minikube kubectl -- apply -f deployment.yml

### Note:
If you are getting ImagePullBackOff in your local cluster, try to push your Docker image
into a Container Registry.


# TODO:
- Adding tests for source code.
- Adding nginx and uwsgi. 
- Optimizing docker image.
- Analysing docker image security.
- Adding Pre-commit
- ...
