# Blue-Green Deployment – Stop Signals

Stop promotion or roll back to Blue if any of the following occurs:

1. A deployment fails to become Ready.
2. Readiness probes repeatedly fail.
3. The Service has no ready endpoints.
4. The application returns HTTP 5xx errors or unexpected HTTP responses.
5. Green shows materially higher latency than Blue.
6. Pods enter CrashLoopBackOff or repeatedly restart.
7. Application exceptions or dependency failures occur.
8. Critical business operations such as login or claim creation fail.

## Recovery Procedure
1. Inspect Pod readiness and logs.
2. Inspect the Service selector and EndpointSlice.
3. Apply the Blue selector patch:
   `kubectl patch service usecase14-service -n claims-k8s-lab --type=merge --patch-file=usecase-14/traffic/blue-selector-patch.yaml`
4. Verify that the Service selects Blue.
5. Verify that the EndpointSlice points to the Blue Pod.
6. Test the application through the Kubernetes Service.
