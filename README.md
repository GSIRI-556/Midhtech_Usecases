# 3-Tier Architecture – Claims Management Application

## 1. Project Overview

The Claims Management Application is a three-tier web application developed using React, Flask, and PostgreSQL.

The application allows users to register, log in, create claims, and manage claim information.

This project is also used to implement and understand DevOps tools and practices through multiple use cases.

## 2. Application Architecture

The application follows a three-tier architecture.

```text
                 USER / BROWSER
                       |
                       v
                REACT FRONTEND
                  (Nginx)
                localhost:8083
                       |
                  REST API / JSON
                       |
                       v
                 FLASK BACKEND
                  (Gunicorn)
                localhost:5001
                       |
                    SQL
                       |
                       v
                  POSTGRESQL
                   Port 5432
                       |
                       v
                    claimsdb
```

### Tier 1 – Presentation Layer
- React frontend.
- Nginx web server.
- Provides login, registration, and claims management interface.

### Tier 2 – Application Layer
- Python and Flask.
- Gunicorn application server.
- Handles API requests and application logic.
- Communicates with PostgreSQL.

### Tier 3 – Database Layer
- PostgreSQL 17.
- Stores user and claims information.
- Generates claim numbers automatically.

## 3. Technologies Used

- React 18
- Python 3.12
- Flask
- Gunicorn
- PostgreSQL 17
- Docker
- Docker Compose
- Nginx
- Git
- GitHub
- GitLab

## 4. Project Structure

```text
3-Tier-Architecture/
|
|-- backend/
|   |-- app.py
|   |-- test_app.py
|   |-- requirements.txt
|   |-- Dockerfile
|
|-- frontend/
|   |-- src/
|   |-- Dockerfile
|   |-- nginx.conf
|   |-- package.json
|
|-- database/
|   |-- Dockerfile
|   |-- init-docker.sql
|   |-- docker-init/
|       |-- init-docker.sql
|
|-- docker-compose.yml
|-- .env
|-- .env.example
|-- .gitignore
|-- README.md
```

## 5. Use Case 03 – Run the App Locally and Prepare Config

### Objective

The objective of this use case is to run the complete three-tier application locally using Docker Compose and verify communication between the frontend, backend, and PostgreSQL database.

### Implementation

- Created Dockerfiles for frontend, backend, and database.
- Configured Docker Compose to manage all three services.
- Configured environment variables using `.env`.
- Created `.env.example` as a safe configuration template.
- Configured Nginx to forward API requests to the backend.
- Configured PostgreSQL initialization SQL.
- Created a named Docker volume for database persistence.
- Configured PostgreSQL health checks.
- Used Gunicorn to run the Flask application.
- Configured the backend container to run as a non-root user.

### Environment Configuration

The project uses the following environment variables:

| Variable | Purpose |
|---|---|
| COMPOSE_PROJECT_NAME | Compose project name |
| POSTGRES_DB | PostgreSQL database name |
| POSTGRES_USER | PostgreSQL username |
| POSTGRES_PASSWORD | PostgreSQL password |
| BACKEND_HOST_PORT | Backend host port |
| FRONTEND_HOST_PORT | Frontend host port |

The actual `.env` file contains local configuration values and is excluded from Git.

The `.env.example` file provides placeholder values for configuration.

**Security:** Never commit the actual `.env` file or real passwords to Git.

### Docker Compose Services

| Service | Container Name | Host Port |
|---|---|---|
| Frontend | claims-local-frontend | 8083 |
| Backend | claims-local-backend | 5001 |
| Database | claims-local-database | Internal 5432 |

### Application Communication

1. The user accesses the React frontend through the browser.
2. Nginx serves the frontend application.
3. Nginx forwards `/api/` requests to the Flask backend.
4. Flask processes the request.
5. The backend communicates with PostgreSQL using the Docker service name `database`.
6. PostgreSQL stores and returns the requested information.

## 6. Running the Application Using Docker Compose

### Build and Start Services

```bash
docker compose up -d --build
```

### Check Running Containers

```bash
docker compose ps
```

### Access the Application

Frontend:

```text
http://localhost:8083
```

Backend health endpoint:

```text
http://localhost:5001/api/health
```

### Stop Services

```bash
docker compose stop
```

### Stop and Remove Containers

```bash
docker compose down
```

## 7. Backend API Verification

### Health Check

```bash
curl http://localhost:5001/api/health
```

Expected response:

```json
{
  "service": "claims-backend",
  "status": "healthy"
}
```

### Get Claims

```bash
curl http://localhost:5001/api/claims
```

### Create Claim

Claims can be created through the frontend application.

The backend receives the request and stores the claim in PostgreSQL.

## 8. Database Verification

### Check PostgreSQL Readiness

```bash
docker compose exec database pg_isready -U claimsuser -d claimsdb
```

### View Database Tables

```bash
docker compose exec database psql -U claimsuser -d claimsdb -c "\dt"
```

### View Stored Claims

```bash
docker compose exec database psql -U claimsuser -d claimsdb -c "SELECT id, claim_number, customer_name, amount, status FROM claims ORDER BY id;"
```

The database contains the `users` and `claims` tables.

Claim numbers are generated automatically using a PostgreSQL trigger.

Example:

```text
CLM-0001
CLM-0002
CLM-0003
```

## 9. Application Logs

View logs of all services:

```bash
docker compose logs
```

View individual service logs:

```bash
docker compose logs database
docker compose logs backend
docker compose logs frontend
```

These logs help identify startup issues, API errors, database connection problems, and application failures.

## 10. Database Failure Simulation

To understand application failure handling, PostgreSQL was stopped temporarily.

Stop the database:

```bash
docker compose stop database
```

Test the claims API:

```bash
curl -i http://localhost:5001/api/claims
```

The claims API returns an error because PostgreSQL is unavailable.

The backend and frontend containers remain running.

## 11. Database Recovery

Restart PostgreSQL:

```bash
docker compose start database
```

Check database health:

```bash
docker compose ps
```

Verify PostgreSQL readiness:

```bash
docker compose exec database pg_isready -U claimsuser -d claimsdb
```

Test the claims API again:

```bash
curl http://localhost:5001/api/claims
```

The application successfully retrieves the previously stored claims after database recovery.

## 12. Data Persistence Verification

A named Docker volume is configured for PostgreSQL:

```text
claims-local-postgres-data
```

The volume stores database information outside the database container.

To verify persistence, the containers were removed and recreated.

Remove containers:

```bash
docker compose down
```

Start the application again:

```bash
docker compose up -d
```

Verify previously created claims:

```bash
docker compose exec database psql -U claimsuser -d claimsdb -c "SELECT id, claim_number, customer_name, amount, status FROM claims ORDER BY id;"
```

The previously created records remained available after the full container restart.

**Important:** Do not use `docker compose down -v` during the persistence test because it removes the named database volume.

## 13. Application Testing

### Frontend Tests

Run from the frontend directory:

```bash
cd frontend
npm test
```

Result:

- 3 frontend tests passed.

### Backend Tests

Run from the project root:

```bash
docker compose run --rm backend python -m pytest -p no:cacheprovider
```

Result:

- 1 backend test passed.

## 14. Use Case 03 Completion Status

- [x] Frontend Dockerfile configured.
- [x] Backend Dockerfile configured.
- [x] Database Dockerfile configured.
- [x] Environment configuration prepared.
- [x] `.env` excluded from Git.
- [x] Docker Compose configured.
- [x] All three services started successfully.
- [x] Frontend application verified.
- [x] Backend health API verified.
- [x] PostgreSQL connectivity verified.
- [x] Claims created through the frontend.
- [x] Database records verified.
- [x] Application logs reviewed.
- [x] Database outage simulated.
- [x] Database recovery verified.
- [x] Database persistence after container restart verified.
- [x] Frontend tests passed (3/3).
- [x] Backend tests passed (1/1).

## 15. DevOps Roadmap

The Claims Management Application will be used as the reference application for the following DevOps workflow:

```text
Git
 |
 v
GitHub / GitLab
 |
 v
Jenkins CI/CD
 |
 v
Automated Testing
 |
 v
SonarQube
 |
 v
Trivy
 |
 v
Docker
 |
 v
Harbor
 |
 v
Kubernetes
 |
 v
Helm / Argo CD
 |
 v
Vault
 |
 v
Prometheus / Grafana
 |
 v
Logs / Alerts
 |
 v
Site Reliability Engineering
```

## 16. Conclusion

Use Case 03 demonstrated how to run a three-tier application locally using Docker Compose.

The frontend, backend, and PostgreSQL services communicated successfully. Environment configuration, application testing, logging, database failure recovery, and persistent storage were verified.

This use case provides the foundation for further CI/CD, container security, Kubernetes deployment, monitoring, and Site Reliability Engineering implementations.