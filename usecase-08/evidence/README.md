# Use Case 08 - Evidence

## Objective
Demonstrate application monitoring, centralized logging, alerting, and recovery using Prometheus, Grafana, Loki, and Grafana Alloy.

## Validation Results

1. Prometheus successfully scraped the Claims backend.
2. Grafana dashboard displayed application monitoring metrics.
3. Grafana Explore displayed backend Docker logs collected through Alloy and Loki.
4. ClaimsBackendDown alert changed to FIRING when the backend was stopped.
5. The alert cleared after the backend was restarted.
6. Backend health endpoint returned healthy after recovery.

## Screenshots

| File | Description |
|---|---|
| 01-prometheus-target-up.png | Prometheus backend target is UP |
| 02-grafana-dashboard.png | Grafana monitoring dashboard |
| 03-loki-logs.png | Backend logs in Grafana Explore |
| 04-alert-firing.png | ClaimsBackendDown alert firing |
| 05-alert-recovery.png | Alert cleared after recovery |
| 06-backend-healthy.png | Backend health check successful |

## Alert Configuration

Alert: ClaimsBackendDown

Expression:
`up{job="claims-backend"} == 0`

Duration: 30 seconds

Severity: critical

## Result
Monitoring, centralized logging, backend failure detection, alert firing, and recovery validation were successfully tested.
