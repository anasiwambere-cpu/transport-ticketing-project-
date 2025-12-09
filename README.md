# 🚍 Transport Ticket Management System (Oracle SQL)

**Student Name:** Ndayisenga Anasi  
**Student ID:** 28423  
**Project Title:** Transport Ticket  
**Database:** Oracle SQL / PL/SQL  

---

## 📌 Project Description

This project is a **Transport Ticket Management System** built using **Oracle SQL and PL/SQL**.  
It allows management of:

- Passengers
- Buses
- Routes
- Schedules
- Tickets
- Payments
- Audit Logs

It also includes:
- Sequences
- Triggers
- Functions
- PL/SQL Package for ticket booking & cancellation

---

## ⚙️ Technologies Used

- Oracle Database
- SQL
- PL/SQL
- SQL Developer / SQL*Plus

---

## 📂 Database Objects

- Tables:
  - PASSENGERS
  - BUSES
  - ROUTES
  - SCHEDULES
  - TICKETS
  - PAYMENTS
  - AUDIT_LOG

- Sequences:
  - TICKET_SEQ
  - PAYMENT_SEQ

- PL/SQL:
  - Function: `calc_fare`
  - Package: `ticket_pkg`
  - Trigger: `trg_tickets_audit`

---

## 🚀 How To Run

1. Open **Oracle SQL Developer**
2. Connect to your database
3. Open `transport_ticket.sql`
4. Click **Run (F5)**
5. Test with:

```sql
EXEC ticket_pkg.book_ticket(1,1,'1A',1500);
SELECT * FROM tickets;
SELECT * FROM audit_log;
