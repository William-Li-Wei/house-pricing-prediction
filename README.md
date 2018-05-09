# House Pricing Prediction

### house-pricing: 
the tasks and partial solutions.


### composetest:

learn and test docker-compose, to create multiple containers.

The plan was to start from the most basic example that, only a mySql container and a web container are created. Practice the configuration so that 2 containers are connected.

Then find a way to manage them via K8s

### Kubernetes-multi-contaienr-pod

A example to demonstrate the concept of packaging multiple containers into a single pod.

- Web Pod has a Python Flas container and a Redis container
- DB Pod has a MySQL container
- When data is retrieved trough the Python REST API, it first checks within Redis cache before accessing MySQL
- Each time data is fetched from MySQL, it gets cached in the Redis container of the same Pod as the Python Flask container
- When the additional Web Pods are launched manually or through a Replica Set, co-located pairs of Python Flask and Redis containers are scheduled together

more details at https://github.com/janakiramm/Kubernetes-multi-container-pod

Can't make it running. Is it because I'm running minikube?

### orchestrate-with-kubernetes

An online lab course from google to teach kubernetes basics, deployment and so on.

the deployment file at ./house-pricing/Deployment/app.pod.yaml was composed based on this example.


