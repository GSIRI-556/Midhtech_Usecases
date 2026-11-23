# Use Case 17 - Build Backup and Restore Evidence

## Objective
Demonstrate PostgreSQL backup creation, controlled data deletion,
database restoration, and recovery verification.

## Environment
- Kubernetes namespace: claims-k8s-lab
- Database: PostgreSQL
- Database deployment: claims-db
- Backend service: claims-backend

## Test Scope
- Table: public.usecase17_backup_test
- Test Record ID: 1701

## Implementation
1. Created a dedicated test table.
2. Inserted test record 1701.
3. Created a table-scoped PostgreSQL backup using pg_dump.
4. Verified the backup artifact and SHA-256 checksum.
5. Deleted only the test record.
6. Verified that the record count became zero.
7. Restored the SQL backup using psql.
8. Verified that record 1701 was recovered.
9. Checked backend application health.
10. Recorded backup and restore durations.
11. Documented RTO and RPO.

## Results
- Backup duration: 0 seconds
- Restore duration: 1 second
- Recovery verification: PASS
- Application health: HTTP 200 OK

## Backup Artifact
backups/usecase17_backup_test.sql

## Evidence
Execution outputs, checksum, timings, and recovery verification
are available in the evidence directory.
