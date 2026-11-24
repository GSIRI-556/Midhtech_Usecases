Use Case 18 – Troubleshoot Pipeline Logging Failure



\## 1. Objective



The objective of this use case was to troubleshoot and restore a Kubernetes-based application logging pipeline. The work involved identifying logging issues, examining application and pod logs, checking the logging configuration, recovering log collection, and verifying that application logs were successfully available in Loki.



\## 2. Environment and Tools



\- Kubernetes – container orchestration

\- kubectl – Kubernetes troubleshooting

\- Grafana – log visualization

\- Loki – log aggregation and storage

\- Grafana Alloy – log collection

\- Docker Desktop – local Kubernetes environment

\- Windows CMD – command execution



\## 3. Kubernetes Namespace



Namespace: `claims-logging-lab`



Main components:



\- Grafana

\- Loki

\- Alloy

\- Use Case 18 demo application



\## 4. Problem Description



The application generated log messages, but the expected logs were not consistently available through the logging pipeline.



The issue required investigation of application logs, Kubernetes pod status, logging configuration, and Loki query results.



\## 5. Troubleshooting Steps



\### Step 1 – Check Kubernetes resources



Command:



```bash

kubectl get pods -n claims-logging-lab

```



Checked the status of Grafana, Loki, Alloy, and the demo application.



\### Step 2 – Inspect application logs



Checked the demo application's pod logs to confirm whether the application was generating log messages.



\### Step 3 – Investigate logging configuration



Compared the controlled configuration and documented the differences in:



`evidence/03-controlled-config-difference.txt`



\### Step 4 – Verify the failure condition



Generated a test request and checked the corresponding Loki query to document the missing log condition.



\### Step 5 – Restore the logging pipeline



Applied the recovery configuration and verified that the logging pipeline resumed collecting application logs.



\### Step 6 – Verify Loki readiness



Command:



```bash

curl -i http://127.0.0.1:13100/ready

```



Expected response:



```text

HTTP/1.1 200 OK

ready

```



\### Step 7 – Verify the recovered application log



Queried Loki using the service label:



```logql

{service\_name="usecase18-demo"}

```



Final verification query:



```logql

{service\_name="usecase18-demo"} |= "uc18-final-20261124-153741"

```



The final query successfully returned the matching application log.



\## 6. Final Verification



Final request ID:



`uc18-final-20261124-153741`



Application response:



```json

{

&#x20; "status": "logged",

&#x20; "request\_id": "uc18-final-20261124-153741",

&#x20; "service": "claims-demo"

}

```



Loki returned one matching log entry for the final request ID.



\## 7. Evidence Structure



The evidence directory contains the following:



\- Known application log response

\- Pod log verification

\- Controlled configuration comparison

\- Broken logging response and Loki query

\- Recovery response and Loki query

\- Final successful log response and Loki query

\- Final request ID

\- Screenshots of Grafana, Loki, Kubernetes resources, and final verification



Screenshots are stored in:



`evidence/screenshots/`



\### Screenshot files



1\. `01-grafana-login.png`

2\. `02-grafana-loki-datasource.png`

3\. `03-grafana-explore-logs.png`

4\. `04-kubernetes-pods-running.png`

5\. `05-kubernetes-services.png`

6\. `06-loki-readiness.png`

7\. `07-final-log-response.png`

8\. `08-final-loki-query-success.png`

9\. `09-demo-application-status.png`



\## 8. Result



The logging pipeline recovery was verified successfully. Loki readiness returned HTTP 200, and the final application log was successfully retrieved using its unique request ID.



The troubleshooting process and verification results were documented with supporting evidence.



\## 9. Conclusion



This use case provided practical experience in troubleshooting Kubernetes logging pipelines, inspecting application and pod logs, understanding Grafana Alloy and Loki integration, comparing configurations, and validating log recovery using LogQL queries.

:::

