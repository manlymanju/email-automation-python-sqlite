# CPaaS Email Processing System


## Overview
A backend CPaaS-style email processing system built using Python and SQLite.  
The system simulates how real-world communication platforms queue, process, retry, and report email delivery.

## Features
- Email queue with database-backed persistence
- Status lifecycle: PENDING → FAILED → SENT
- Retry mechanism with max retry limits
- Simulated email sender (no external SMTP dependency)
- SQL-based analytics and reporting

## Tech Stack
- Python
- SQLite
- SQL
- Time-based simulation

## System Flow
1. Emails are inserted into the queue (PENDING)
2. Pending emails are processed
3. Failed emails are retried up to a max retry limit
4. Final status is updated in the database
5. Reports are generated using SQL queries

## Key Learnings
- Database schema design
- Backend workflow orchestration
- Retry control and failure handling
- Writing analytical SQL queries
- Building CPaaS-style systems
