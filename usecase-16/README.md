# Use Case 16: Detect and Fix Configuration Drift

## Objective
Detect configuration drift between Git desired state and live Kubernetes resources, then restore the approved configuration using Argo CD.

## Tools Used
- Terraform: Created and manages the Kubernetes namespace.
- Kubernetes: Runs the application Deployment, Pods, ConfigMap and Service.
- GitLab: Stores the desired Kubernetes manifests.
- Argo CD: Monitors Git and detects configuration differences.

## Architecture
1. Terraform creates the claims-drift-lab namespace.
2. Kubernetes manifests define the application with two replicas.
3. GitLab stores the desired configuration on the Usecase_16 branch.
4. Argo CD monitors the Git repository and deploys the manifests.
5. A manual kubectl scale command changes the live Deployment from two replicas to three.
6. Argo CD detects the difference and reports OutOfSync.
7. Argo CD synchronization restores the Deployment to two replicas.

## Drift Simulation
kubectl scale deployment/usecase16-demo -n claims-drift-lab --replicas=3

## Drift Detection
Argo CD reported:
- Sync status: OutOfSync
- Health status: Healthy

The live replica count was three, while the Git manifest specified two.

## Drift Resolution
Argo CD synchronization was triggered through the Kubernetes Application resource.

Final result:
- Argo CD: Synced
- Health: Healthy
- Deployment: 2/2 ready
- Running Pods: 2

## Terraform Validation
The final Terraform plan reported:

No changes. Your infrastructure matches the configuration.

## Conclusion
Successfully demonstrated configuration drift simulation, detection, and recovery. Git remained the source of truth for the desired Kubernetes application configuration, and Argo CD restored the live state to match Git.
