# Use Case 12: Secret Rotation Without Breaking the Application

## Objective
Implement secure API token rotation using HashiCorp Vault and Kubernetes Secrets without exposing secret values.

## Tools Used
- HashiCorp Vault
- Kubernetes
- kubectl
- Docker Desktop
- OpenSSL
- Git

## Architecture

Vault KV v2
    |
    | API token
    v
Kubernetes Secret: claims-usecase12-secret
    |
    | API_TOKEN environment variable
    v
Deployment: claims-backend
    |
    v
Backend Pod

## Implementation Steps

1. Started Vault in development mode.
2. Generated an initial API token using OpenSSL.
3. Stored the initial token in Vault KV v2.
4. Created a Kubernetes Secret from the initial token.
5. Connected the Secret to the claims-backend Deployment.
6. Generated a new API token and stored it as Vault Version 2.
7. Updated the Kubernetes Secret with the rotated token.
8. Restarted the backend Deployment.
9. Verified that the Pod loaded the rotated token.
10. Compared Vault and Pod token values without displaying them.
11. Verified application health using the API endpoint.
12. Audited project files to ensure secret values and Vault tokens were not exposed.
13. Deleted the Kubernetes Secret to test the controlled failure scenario.
14. Confirmed that the replacement Pod failed because the Secret was missing.
15. Recovered the Secret from Vault Version 2.
16. Restarted the Deployment and verified successful recovery.

## Verification

- Vault initialized and unsealed.
- Vault secret Version 1 and Version 2 created.
- Kubernetes Secret successfully synchronized.
- Backend Pod loaded API_TOKEN.
- Vault and Pod token values matched.
- Application returned HTTP 200 OK after rotation.
- Controlled failure was confirmed when the Kubernetes Secret was deleted.
- Application recovered successfully after restoring the Secret from Vault.

## Evidence

See the evidence directory for command outputs and verification records.

## Security Notes

- Used lab-only API tokens.
- Never printed secret values.
- Removed temporary secret variables after use.
- Did not store raw tokens or Vault root tokens in project files.
- Used metadata and verification results as evidence.
