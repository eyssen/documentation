==========================
Create leads from bookings
==========================

With the *Appointment (CRM)* (``appointment_crm``) module, an approved booking can automatically
create a lead or an opportunity in the :doc:`CRM <../../sales/crm>` pipeline, so that the sales team
follows up on the customers who booked a meeting.

Configuration
=============

Go to :menuselection:`Appointments --> Configuration --> Appointment Types`, open the relevant type,
and enable :guilabel:`Create CRM Lead`.

In :guilabel:`Lead Title`, define the title of the lead created. Use `{customer}` as a placeholder
for the customer name, e.g. `New appointment: {customer}`.

.. screenshot:: productivity-appointments-create-lead
   :menu: Appointments ‣ Configuration ‣ Appointment Types
   :shows: An appointment type form with the "Create CRM Lead" checkbox enabled and the "Lead Title" field showing the template with the {customer} placeholder.
   :highlight: The "Create CRM Lead" setting (red frame).
   :data: Type "Consultation", lead title "New appointment: {customer}".
   :module: appointment_crm
   :notes: English UI, light theme, 1440px width, crop to the setting.

Use the leads
=============

When a booking of that type is approved, Odoo creates the lead with the customer's contact details
and the answers given while booking, and links it to the booking in the :guilabel:`Related Lead`
field. Opening the field brings the salesperson directly to the pipeline record.

.. note::
   Leads are created on approval, so bookings that stay :guilabel:`Requested`, or that are rejected,
   do not generate a lead.
