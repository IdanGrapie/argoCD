## argoCD


# Start Minikube:
  minikube start

# Install Argo CD:
  kubectl create namespace argocd
  kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml


# Expose Argo CD UI via NodePort:
Change the Argo CD Server service type to NodePort:
 kubectl patch svc argocd-server -n argocd -p '{"spec": {"type": "NodePort"}}'


# Get the NodePort:
 kubectl get svc argocd-server -n argocd -o=jsonpath='{.spec.ports[?(@.name=="http")].nodePort}'

# Access Argo CD UI:
 minikube service argocd-server -n argocd --url

# Log into Argo CD UI:
The default username is admin.
To get the password, use:
 kubectl get secret argocd-initial-admin-secret -n argocd -o jsonpath="{.data.password}" | base64 -d
