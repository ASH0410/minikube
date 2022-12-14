# Minikube-Flask-Application

Minikube is a lightweight Kubernetes implementation that deploys a simple cluster containing only one node.

Flask is a small and lightweight Python web framework that provides useful tools and features that make creating web applications in Python.

*******************************************
Server Specification
------------------------

OS: Amazon Linux v2 [kernel-5.10, hvm-2.0.20220912.1-x86_64-gp2]<br/>
Architecture	: x86-64 <br/>
vCPU			    : 4 <br/>
Memory			  : 16 GB <br/>
Disk			    : 08 GB <br/>
Accessibility	: Public <br/>

*******************************************

Installation on Amazon Linux EC2 Instances
------------------------------------------

minikube version: 1.27.1 <br/>
kubectl version	: 1.25.3 <br/>
docker version	: 20.10.17 <br/>
git version	: 2.37.1 <br/>

------------------
Installation Steps
------------------

Step 1. 

    sudo yum update -y

Step 2. Install Minikube, which is used to create cluster

    curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
    sudo install minikube-linux-amd64 /usr/local/bin/minikube

Step 3. Check minikube version

    minikube version

Output ||   <br/>

    minikube version: v1.27.0
    commit: 4243041b7a72319b9be7842a7d34b6767bbdac2b


Step 4. Install Kubeclt command line client for minikube, which is used to interact with kubernete’s cluster

    curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
    sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl

Step 5. Check Kubectl Version

    kubectl version

Output || <br/>

    Client Version: version.Info{Major:"1", Minor:"25", GitVersion:"v1.25.2", GitCommit:"5835544ca568b757a8ecae5c153f317e5736700e", GitTreeState:"clean", BuildDate:"2022-09-21T14:33:49Z", GoVersion:"go1.19.1", Compiler:"gc", Platform:"linux/amd64"} <br/>
    Kustomize Version: v4.5.7 <br/>
    Server Version: version.Info{Major:"1", Minor:"25", GitVersion:"v1.25.0", GitCommit:"a866cbe2e5bbaa01cfd5e969aa3e033f3282a8a2", GitTreeState:"clean", BuildDate:"2022-08-23T17:38:15Z", GoVersion:"go1.19", Compiler:"gc", Platform:"linux/amd64"} <br/>


**NOTE: <br/>
  -Minikube is use to start/stop/delete the K8s Cluster <br/>
  -Kubectl is use to configure cluster**

Step 6. Install and start docker engine, configuring as a minikube drivers.

    sudo yum install docker -y
    sudo systemctl enable docker && sudo systemctl start docker
    sudo usermod -aG docker $USER && newgrp docker


Step 11. Install git

    sudo yum install git -y
    git --version

Output || <br/>

    git version 2.37.1
  
******************************************************
Start Configuration
-----------------------------------------------------
$ git clone https://github.com/ASH0410/minikube.git

### File Structure
	    minikube
	    ├── app1
	    │   ├── app1-CronJob.yml
	    │   ├── app1-Deployment.yml
	    │   ├── app1-HPA.yml
	    │   ├── app1-Ingress.yml
	    │   ├── app1-NS.yml
	    │   ├── app1-RBAC.yaml
	    │   ├── app1-RBAC.yml
	    │   ├── app1-Service.yml
	    │   ├── default-backend-Deployment.yml
	    │   ├── default-backend-Service.yml
	    │   ├── default-flask-backend
	    │   │   ├── app.py
	    │   │   ├── Dockerfile
	    │   │   └── requirements.txt
	    │   ├── flask-docker-app1
	    │   │   ├── app.py
	    │   │   ├── Dockerfile
	    │   │   └── requirements.txt
	    │   └── kustomization.yml
	    ├── app2
	    │   ├── app2-CronJob.yml
	    │   ├── app2-Deployment.yml
	    │   ├── app2-HPA.yml
	    │   ├── app2-Ingress.yml
	    │   ├── app2-NS.yml
	    │   ├── app2-RBAC.yml
	    │   ├── app2-Service.yml
	    │   ├── flask-docker-app2
	    │   │   ├── app.py
	    │   │   ├── Dockerfile
	    │   │   └── requirements.txt
	    │   └── kustomization.yml
	    ├── kubernetes.pem
	    └── README.md




$ cd minikube

$ minikube start --driver=docker <br/>

Output || <br/>

    * Enabled addons: default-storageclass, storage-provisioner
    * Done! kubectl is now configured to use "minikube" cluster and "default" namespace by default 

$ minikube status

Output || <br/>

    minikube
    type: Control Plane
    host: Running
    kubelet: Running
    apiserver: Running
    kubeconfig: Configured

$ kubectl cluster-info

Output || <br/>

    Kubernetes control plane is running at https://192.168.49.2:8443
    CoreDNS is running at https://192.168.49.2:8443/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy

$ kubectl apply -k app1/

Output || <br/>

	namespace/app1-ns created
	serviceaccount/app1-sa-cron-runner created
	role.rbac.authorization.k8s.io/app1-cron-runner created
	rolebinding.rbac.authorization.k8s.io/app1-cron-runner created
	service/app1-service created
	service/default-backend-service created
	deployment.apps/app1 created
	deployment.apps/default-backend created
	cronjob.batch/app1-pod-scale-down-job created
	cronjob.batch/app1-pod-scale-up-job created
	horizontalpodautoscaler.autoscaling/app1-hpa created
	ingress.networking.k8s.io/app1-ingress created
	
$ kubectl apply -k app2/

Output || <br/>

	namespace/app2-ns created
	serviceaccount/app2-sa-cron-runner created
	role.rbac.authorization.k8s.io/app2-cron-runner created
	rolebinding.rbac.authorization.k8s.io/app2-cron-runner created
	service/app2-service created
	deployment.apps/app2 created
	cronjob.batch/app2-pod-scale-down-job created
	cronjob.batch/app2-pod-scale-up-job created
	horizontalpodautoscaler.autoscaling/app2-hpa created
	ingress.networking.k8s.io/app2-ingress created


$ kubectl get ns

Output || <br/>

	NAME              STATUS   AGE
	app1-ns           Active   126m
	app2-ns           Active   126m
	default           Active   138m
	ingress-nginx     Active   121m
	kube-node-lease   Active   138m
	kube-public       Active   138m
	kube-system       Active   138m

**NOTE:**<br/>
- Using **`NAMESPACE`**, we can effectivly manage netowrk policy separately for each appliaction

$ minikube addons enable metrics-server

Output || <br/>

	* metrics-server is an addon maintained by Kubernetes. For any concerns contact minikube on GitHub.
	You can view the list of minikube maintainers at: https://github.com/kubernetes/minikube/blob/master/OWNERS
	  - Using image k8s.gcr.io/metrics-server/metrics-server:v0.6.1
	* The 'metrics-server' addon is enabled

**NOTE:**<br/>
- Enable **`metrics-server`** to get metrics data from Pods, otherwise targets:unknown

$ kubectl get all -o wide -n=app1-ns

Output ||  <br/>


	NAME                                   READY   STATUS    RESTARTS   AGE     IP           NODE       NOMINATED NODE   READINESS GATES
	pod/app1-5b66886c88-689xg              1/1     Running   0          9m      172.17.0.5   minikube   <none>           <none>
	pod/app1-5b66886c88-nz72q              1/1     Running   0          8m44s   172.17.0.9   minikube   <none>           <none>
	pod/app1-5b66886c88-zgt9q              1/1     Running   0          9m      172.17.0.3   minikube   <none>           <none>
	pod/default-backend-597d886bcc-n55ms   1/1     Running   0          9m      172.17.0.6   minikube   <none>           <none>
	pod/default-backend-597d886bcc-xm268   1/1     Running   0          9m      172.17.0.4   minikube   <none>           <none>

	NAME                              TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)   AGE   SELECTOR
	service/app1-service              ClusterIP   10.106.3.93     <none>        80/TCP    9m    app=app1
	service/default-backend-service   ClusterIP   10.107.253.41   <none>        80/TCP    9m    app=default

	NAME                              READY   UP-TO-DATE   AVAILABLE   AGE   CONTAINERS   IMAGES                                     SELECTOR
	deployment.apps/app1              3/3     3            3           9m    app1         d4cregistry/flask-app1:latest              app=app1
	deployment.apps/default-backend   2/2     2            2           9m    default      d4cregistry/default-flask-backend:latest   app=default

	NAME                                         DESIRED   CURRENT   READY   AGE   CONTAINERS   IMAGES                                     SELECTOR
	replicaset.apps/app1-5b66886c88              3         3         3       9m    app1         d4cregistry/flask-app1:latest              app=app1,pod-template-hash=5b66886c88
	replicaset.apps/default-backend-597d886bcc   2         2         2       9m    default      d4cregistry/default-flask-backend:latest   app=default,pod-template-hash=597d886bcc

	NAME                                           REFERENCE         TARGETS   MINPODS   MAXPODS   REPLICAS   AGE
	horizontalpodautoscaler.autoscaling/app1-hpa   Deployment/app1   1%/60%    3         10        3          9m

	NAME                                    SCHEDULE     SUSPEND   ACTIVE   LAST SCHEDULE   AGE   CONTAINERS       IMAGES                   SELECTOR
	cronjob.batch/app1-pod-scale-down-job   0 18 * * *   False     0        <none>          9m    bitnamikubectl   bitnami/kubectl:latest   <none>
	cronjob.batch/app1-pod-scale-up-job     0 13 * * *   False     0        <none>          9m    bitnamikubectl   bitnami/kubectl:latest   <none>

**NOTE:**<br/>
- **`HorizontalPodAutoscaler[HPA]`** manages the replicas of the Deployment, and updated **`sepc.replicas`** field of Deployment by its own **`spec.minReplicas`**
- **`CronJob`** will trigger HPA, and update **`spec.minReplicas`**
- **`cronjob.batch/app1-pod-scale-up-job`** will  scale-up "app1" pods "At 13:00 UTC Everyday" due to peaks of usage during the day
- **`cronjob.batch/app1-pod-scale-down-job`** will  scale-up "app1" pods "At 18:00 UTC Everyday" due to out of peaks of usage.
- After triggred, HPA evaluates the metrics configuration to scale-up and scale-down pods


$ kubectl get all -o wide -n=app2-ns

Output ||  <br/>


	NAME                        READY   STATUS    RESTARTS   AGE     IP            NODE       NOMINATED NODE   READINESS GATES
	pod/app2-56c9ffb5bf-2r7qk   1/1     Running   0          8m20s   172.17.0.7    minikube   <none>           <none>
	pod/app2-56c9ffb5bf-f5dkv   1/1     Running   0          8m20s   172.17.0.8    minikube   <none>           <none>
	pod/app2-56c9ffb5bf-kxmlm   1/1     Running   0          8m5s    172.17.0.11   minikube   <none>           <none>

	NAME                   TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)   AGE     SELECTOR
	service/app2-service   ClusterIP   10.103.241.17   <none>        80/TCP    8m20s   app=app2

	NAME                   READY   UP-TO-DATE   AVAILABLE   AGE     CONTAINERS   IMAGES                          SELECTOR
	deployment.apps/app2   3/3     3            3           8m20s   app2         d4cregistry/flask-app2:latest   app=app2

	NAME                              DESIRED   CURRENT   READY   AGE     CONTAINERS   IMAGES                          SELECTOR
	replicaset.apps/app2-56c9ffb5bf   3         3         3       8m20s   app2         d4cregistry/flask-app2:latest   app=app2,pod-template-hash=56c9ffb5bf

	NAME                                           REFERENCE         TARGETS   MINPODS   MAXPODS   REPLICAS   AGE
	horizontalpodautoscaler.autoscaling/app2-hpa   Deployment/app2   1%/60%    3         10        3          8m20s

	NAME                                    SCHEDULE    SUSPEND   ACTIVE   LAST SCHEDULE   AGE     CONTAINERS       IMAGES                   SELECTOR
	cronjob.batch/app2-pod-scale-down-job   0 0 * * 6   False     0        <none>          8m20s   bitnamikubectl   bitnami/kubectl:latest   <none>
	cronjob.batch/app2-pod-scale-up-job     0 0 * * 1   False     0        <none>          8m20s   bitnamikubectl   bitnami/kubectl:latest   <none>

**NOTE:**<br/>
- **`HorizontalPodAutoscaler[HPA]`** manages the replicas of the Deployment, and updated **`sepc.replicas`** field of Deployment by its own **`spec.minReplicas`**
- **`CronJob`** will trigger HPA, and update **`spec.minReplicas`**
- **`cronjob.batch/app2-pod-scale-up-job`** will  scale-up "app2" pods "At 00:00 UTC on Monday" due to higher usage during the week versus the weekend
- **`cronjob.batch/app2-pod-scale-down-job`** will  scale-down "app2" pods “At 00:00 UTC on Saturday” due to out of peaks of usage.
- After triggred, HPA evaluates the metrics configuration to scale-up and scale-down pods

$ minikube addons enable ingress

Output || <br/>


      * ingress is an addon maintained by Kubernetes. For any concerns contact minikube on GitHub.
      You can view the list of minikube maintainers at: https://github.com/kubernetes/minikube/blob/master/OWNERS
        - Using image k8s.gcr.io/ingress-nginx/kube-webhook-certgen:v1.1.1
        - Using image k8s.gcr.io/ingress-nginx/kube-webhook-certgen:v1.1.1
        - Using image k8s.gcr.io/ingress-nginx/controller:v1.2.1
      * Verifying ingress addon...
      * The 'ingress' addon is enabled

$ minikube addons enable ingress-dns

Output || <br/>


      * ingress-dns is an addon maintained by Google. For any concerns contact minikube on GitHub.
      You can view the list of minikube maintainers at: https://github.com/kubernetes/minikube/blob/master/OWNERS
        - Using image gcr.io/k8s-minikube/minikube-ingress-dns:0.0.2
      * The 'ingress-dns' addon is enabled


$ kubectl get ing -n=app1-ns

Output || <br/>


	NAME           CLASS   HOSTS   ADDRESS        PORTS   AGE
	app1-ingress   nginx   *       192.168.49.2   80      30m

$ kubectl get ing -n=app2-ns

Output || <br/>


	NAME           CLASS   HOSTS   ADDRESS        PORTS   AGE
	app2-ingress   nginx   *       192.168.49.2   80      123m


$ kubectl describe ingress -n=app1-ns

Output || <br/>


	Name:             app1-ingress
	Labels:           name=app1-ingress
	Namespace:        app1-ns
	Address:          192.168.49.2
	Ingress Class:    nginx
	**Default backend:  default-backend-service:80 (172.17.0.7:5000,172.17.0.9:5000)**
	Rules:
	  Host        Path  Backends
	  ----        ----  --------
	  *
		      /app1   app1-service:80 (172.17.0.3:5000,172.17.0.4:5000)
	Annotations:  nginx.ingress.kubernetes.io/rewrite-target: /
	Events:
	  Type    Reason  Age                From                      Message
	  ----    ------  ----               ----                      -------
	  Normal  Sync    35m (x2 over 36m)  nginx-ingress-controller  Scheduled for sync



$ kubectl describe ingress -n=app2-ns

Output || <br/>


	Name:             app2-ingress
	Labels:           name=app2-ingress
	Namespace:        app2-ns
	Address:          192.168.49.2
	Ingress Class:    nginx
	Default backend:  <default>
	Rules:
	  Host        Path  Backends
	  ----        ----  --------
	  *
		      /app2   app2-service:80 (172.17.0.5:5000,172.17.0.6:5000)
	Annotations:  nginx.ingress.kubernetes.io/rewrite-target: /
	Events:       <none>





$ curl http://192.168.49.2/app1

Output || <br/>
    ``<h2>Hello Minikube,</h2><h3>Welcome to Flask-App-ONE !!</h3><b>Pod-Hostname:</b> app1-54b94f8dcf-5nktq<br/>``

$ curl -I http://192.168.49.2/app2

Output || <br/>
    ``<h2>Hello Minikube,</h2><h3>Welcome to Flask-App-TWO !!</h3><b>Pod-Hostname:</b> app2-669fcd9f48-qzgr5<br/>``


**NOTE:**
- **Do local Forwarding to access application form outside**
- **`3.80.55.235` is public IP of server**
- **`kubernetes.pem` is private key of server**

<br/>

$ sudo ssh -i **`kubernetes.pem`** -L 0.0.0.0:80:192.168.49.2:80 -f -N ec2-user@**`3.80.55.235`**

<br/>

### Hit the below URLs from your browser

<br/>

**`http://3.80.55.235/`**

<h2>Hello Minikube,</h2><h3>This is Default-Page, using below convention to go the Application</h3><h4>Go to Flask-App-ONE : http://ip-address/app1</h4><h4>Go to Flask-App-TWO : http://ip-address/app2</h4><br/><b>Pod-Hostname:</b> default-backend-597d886bcc-hsv97<br/>
<br/>

**`http://3.80.55.235/app1`**
    <h2>Hello Minikube,</h2><h3>Welcome to Flask-App-ONE !!</h3><b>Pod-Hostname:</b> app1-54b94f8dcf-5nktq<br/>
<br/>

**`http://3.80.55.235/app2`**
   <h2>Hello Minikube,</h2><h3>Welcome to Flask-App-TWO !!</h3><b>Pod-Hostname:</b> app2-669fcd9f48-qzgr5<br/>

<br/>

*********************************************************
Update Applications & Build New Applications Docker Images
---------------------------------------------------------

- Open VS Code or any Coding Tool on your local machine
- Open "minikube" folder that already cloned from git repo to local machine

      cd /minikube

- Modify your Applications and build docker-container image
- Login to docker hub/registry once using commnad `docker login -u <username>`
- Run below command to build image, tag image and push to docker hub/ registry

      docker build -t flask-app1-img app1/flask-docker-app1/
      docker tag flask-app1-img d4cregistry/flask-app1
      docker push d4cregistry/flask-app1

     [For app2]

      docker build -t flask-app2-img app2/flask-docker-app2/
      docker tag flask-app2-img d4cregistry/flask-app2
      docker push d4cregistry/flask-app2

**NOTE:** <br/>
- **`As per Deployment.yaml configuration, pod-container always pull "latest" tagged docker-container images from docker repository`**

- Once docker image pushed to docker registry
- Go to `minikube server` and run below command to update pod-container image

      cd minikube
  <br/>
      
      kubectl rollout restart deployment/app1

  [For app2]

      kubectl rollout restart deployment/app2
