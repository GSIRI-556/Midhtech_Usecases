# Use Case 17 - RTO and RPO

## RTO - Recovery Time Objective
RTO is the maximum acceptable time to restore a service after a failure.

In this controlled test:
- Measured database restore duration: 1 second
- Recovery verification: PASS
- Backend health check: HTTP 200 OK

The measured restore duration does not represent the complete production RTO. Production recovery also includes failure detection, approval, preparation, restoration, and application validation.

## RPO - Recovery Point Objective
RPO is the maximum acceptable amount of data loss measured in time.

In this controlled test:
- Test record ID: 1701
- The record was backed up before deletion.
- The record was restored successfully.
- No changes were made to the test record between backup and deletion.

Therefore, the controlled test demonstrated recovery of the backed-up record without losing its recorded state. Production RPO depends on backup frequency and backup strategy.
