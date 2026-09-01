# Screenshot shot-list — `follow_up.rst`

Capture these on a demo DB with the `account_payment_followup` module installed and a few
overdue customer invoices. Crop tightly to the relevant panel, light theme, English UI.

| File | Where | Must contain |
|------|-------|--------------|
| `levels-list.png` | Accounting ▸ Configuration ▸ Accounting ▸ Follow-up Levels | The 7 seeded levels (Due Days 0/1/8/15/30/45/60); Send Email / Send SMS / Send Letter / Show Interest / Automatic / Final columns, with Automatic unticked on every row |
| `level-form.png` | One level opened (e.g. *Repeated Reminder*) | Left: Level Name / Due Days / Automatic / Final-Legal. Right: Send Email + Email Template / Send SMS + SMS Template / Send Letter / Attach Overdue Invoices / Show Late-payment Interest |
| `interest-settings.png` | Accounting ▸ Configuration ▸ Settings | "Late-payment Interest on Reminders" expanded: rate % field + Collection fee (B2B) toggle + amount |
| `partner-tab.png` | Customer form ▸ *Payment Follow-up* tab | Follow-up Status (In Need of Action), Next Follow-up Date, Follow-up Responsible, Total Overdue / Total Due, internal note, **Send Reminder** button |
| `invoice-bulk.png` | Accounting ▸ Customers ▸ Invoices (Overdue filter) | Several rows ticked, Actions (gear) menu open, **Send Payment Reminder** highlighted |
| `report.png` | Generated follow-up letter PDF | Company header, overdue-invoice table, totals, interest + collection-fee block |
| `log.png` | Accounting ▸ Reporting ▸ Payment Follow-up | Rows with Date / Customer / Level / Channel / Invoices / Note |
