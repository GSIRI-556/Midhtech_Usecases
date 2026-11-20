# Configuration Drift Decision

## Root Cause
A manual kubectl scale command changed the live Kubernetes Deployment from 2 replicas to 3 replicas.

## Impact
The live Kubernetes configuration no longer matched the approved Git configuration.

## Detection
Argo CD detected the difference and reported the application as OutOfSync.

## Decision
Git wins because no approved change to the desired replica count was committed.

## Resolution
Argo CD will synchronize the application with Git and restore the Deployment to 2 replicas.
