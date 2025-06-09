# Deploying vLLM Inference Service on OpenShift AI Cluster

## Login to cluster

Launch OpenShift Console and copy the `oc login...` command.

## PVC Setup

A PVC with the name "{username}-pvc" is already created during the environment setup. We will make use of the same PVC to download model weights.


## Deploy LLM Service

Update `.spec.template.spec.volumes[0].persistentVolumeClaim.claimName` to "{username}-pvc" based on your username.

```
oc apply -f deployment.yaml
oc get pods

oc apply -f service.yaml
oc get service

oc apply -f route.yaml
oc get route
```