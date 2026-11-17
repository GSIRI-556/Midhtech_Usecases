# Use Case 14 – Blue-Green Deployment in Kubernetes

## Objective
Implement Blue-Green deployment using Kubernetes Deployments and Services.
Deploy a stable Blue version and a new Green version, test Green independently,
switch production traffic, simulate a readiness failure, recover traffic, and
roll back to Blue.

## Environment
- Docker Desktop Kubernetes
- Kubernetes namespace: claims-k8s-lab
- Container image: nginx:1.27-alpine
- Deployment strategy: Blue-Green
- Traffic management: Kubernetes Service selectors
- Health validation: Readiness probes
- Verification: kubectl, EndpointSlices, HTTP requests

## Components
- usecase14-blue: Stable application version
- usecase14-green: New release candidate
- usecase14-bad: Deployment with a deliberately failing readiness probe
- usecase14-service: Main Service used for traffic switching
- usecase14-green-preview: Preview Service for testing Green

## Implementation Steps
1. Deploy Blue and verify HTTP 200.
2. Deploy Green while keeping Blue active.
3. Test Green through its preview Service.
4. Promote Green by changing the main Service selector.
5. Simulate readiness failure using the Bad deployment.
6. Restore traffic to Green and verify successful requests.
7. Roll back to Blue using the saved selector patch.

## Traffic Switching
Traffic is controlled by changing the selector of usecase14-service.

- Blue: version=blue
- Green: version=green
- Bad: version=bad

The EndpointSlice is inspected to verify which Pod is selected and whether
its endpoint is ready.

## Failure Simulation
The Bad deployment uses the readiness probe path:
`/deliberately-unhealthy`

Nginx returns HTTP 404 for this path. Kubernetes therefore marks the Pod
Not Ready and the EndpointSlice reports ready=false.

## Recovery and Rollback
The main Service selector was restored to Green and an in-cluster request
returned GREEN Version 2.

The selector was then changed to Blue. A request from the Green Pod through
the main Service returned BLUE Version 1, confirming successful rollback.

## Evidence
See the evidence and screenshots directories for verification records.

## Cleanup
After reviewing and preserving the evidence, remove only the Use Case 14
resources if cleanup is required. Do not delete the shared namespace.
