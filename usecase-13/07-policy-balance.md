# Use Case 13 Policy Balance

## Policy objective

Every container in a Kubernetes Deployment must define CPU and memory
requests and limits.

## Risk prevented

Requests make scheduling more predictable. Limits reduce the risk that one
container consumes resources needed by other workloads.

## Why the policy is useful

The rule checks an important deployment requirement before the manifest
reaches Kubernetes. Each failure names the exact missing field.

## Why the policy is not unnecessarily strict

The policy does not force one CPU or memory value. Each application team can
choose suitable values. The policy only requires the fields to exist.

## Result

Unsafe manifest: Blocked

Fixed manifest: Allowed

Fixed workload: Successfully deployed

Application test: HTTP 200 OK
