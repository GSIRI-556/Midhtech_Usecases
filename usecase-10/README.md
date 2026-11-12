\# Use Case 10 – Jenkins Agent Failure and Recovery



\## Objective

Simulate a Jenkins agent failure, observe how a pipeline behaves when no executor is available, restore the agent, and verify that the pipeline runs successfully after recovery.



\## Environment

\- Jenkins running in Docker

\- Docker CLI available inside the Jenkins container

\- Harbor container registry running on port 8082

\- Jenkins URL: http://localhost:8081

\- Jenkins pipeline job: `usecase-10-agent-recovery`



\## Implementation and validation



1\. Verified that the Docker CLI was available inside the Jenkins container.

2\. Verified that the Jenkins container could reach Harbor at `host.docker.internal:8082`.

3\. Executed the baseline Jenkins pipeline successfully.

4\. Simulated an agent failure by marking the Jenkins Built-In Node temporarily offline.

5\. Triggered the pipeline and verified that it remained queued while no executor was available.

6\. Restored the Built-In Node to online status.

7\. Verified successful pipeline execution after recovery.



\## Harbor connectivity note

The Harbor registry endpoint returned HTTP 401 Unauthorized when queried without credentials. This is the expected response for an unauthenticated registry request and confirms that the endpoint was reachable. The pipeline checks Harbor connectivity; it does not perform an authenticated image push.



\## Screenshots



| File | Description |

|---|---|

| `01-environment-setup.png` | Docker CLI and Harbor connectivity checks |

| `02-jenkins-baseline-success.png` | Baseline pipeline success |

| `03-job-queued.png` | Pipeline waiting while the agent was offline |

| `04-agent-restored.png` | Jenkins agent restored |

| `05-agent-recovery-success.png` | Pipeline success after recovery |



Screenshots are available in `evidence/screenshots/`.



\## Result

The agent failure and recovery scenario was successfully demonstrated. The pipeline waited when no executor was available and ran after the Jenkins Built-In Node was restored online.

