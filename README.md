# argoCD
Start Minikube:

Run minikube start to ensure Minikube is running.
Install Argo CD:

Apply the Argo CD installation manifests:
ruby
Copy code
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
Expose Argo CD UI via NodePort:

Change the Argo CD Server service type to NodePort:
css
Copy code
kubectl patch svc argocd-server -n argocd -p '{"spec": {"type": "NodePort"}}'
Get the NodePort:

Retrieve the NodePort assigned to the Argo CD Server service:
arduino
Copy code
kubectl get svc argocd-server -n argocd -o=jsonpath='{.spec.ports[?(@.name=="http")].nodePort}'
Access Argo CD UI:

Use Minikube to get the IP address:
Copy code
minikube ip
Access the Argo CD UI by opening a browser and navigating to http://<minikube-ip>:<node-port>.
Log into Argo CD UI:

The default username is admin.
Get the password by running:
bash
Copy code
kubectl get pods -n argocd -l app.kubernetes.io/name=argocd-server -o name | cut -d'/
