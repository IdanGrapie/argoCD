# argoCD


## Start Minikube:
  minikube start

## Install Argo CD:
  kubectl create namespace argocd
  
  kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml


## Expose Argo CD UI via NodePort:
Change the Argo CD Server service type to NodePort:

kubectl patch svc argocd-server -n argocd -p '{"spec": {"type": "NodePort"}}'


## Get the NodePort:
 kubectl get svc argocd-server -n argocd -o=jsonpath='{.spec.ports[?(@.name=="http")].nodePort}'

## Access Argo CD UI:
 minikube service argocd-server -n argocd --url

## Log into Argo CD UI:
The default username is admin.

To get the password, use:

kubectl get secret argocd-initial-admin-secret -n argocd -o jsonpath="{.data.password}" | base64 -d

## log into the argoCD

In the Argo CD UI, go to 'Settings' and then 'Repositories'.
Connect repo, change to https and add your git url.
Give it a name, and if you're repo is private you need to add user and password or use a token.
Finish up by pressing connect.

## Create new app

Go to the Applications, press on NEW APP,
    Application Name: Choose a name for your Argo CD application.
    Project: Select the Argo CD project to associate with the application (default is usually fine).
    Source Repo URL: Select the repository you just connected.
    Revision: Set the branch name or commit SHA to track (e.g., main or master).
    Path: Specify the directory in your repository where your Kubernetes manifests are located. (no need for absolute path)
    Destination Cluster URL: Set the cluster where you want to deploy the application.
    Destination Namespace: Specify the Kubernetes namespace to deploy the application into.

    
