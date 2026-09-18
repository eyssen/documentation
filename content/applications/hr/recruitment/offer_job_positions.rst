===================
Offer job positions
===================

After an applicant has successfully passed the various interview stages, the recruitment team is
ready to make an offer and, once it is accepted, to create the employee record.

.. seealso::
   Refer to the :doc:`recruitment <../recruitment>` documentation for details on the various stages
   of the recruitment process.

Record the proposed salary
==========================

Open the applicant's card by going to the :menuselection:`Recruitment app` and clicking the job
position card, then the applicant.

The :guilabel:`Proposed` salary and the :guilabel:`Expected` salary are recorded on the applicant
form, each with an :guilabel:`Extra` field for the advantages that go with the amount, such as a
company car or a meal allowance. Both amounts are visible to recruitment users only.

.. screenshot:: hr-recruitment-proposed-salary
   :menu: Recruitment ‣ (job position) ‣ (open an applicant)
   :shows: The applicant form with the Expected and Proposed salary fields and their Extra fields filled in.
   :highlight: The Proposed salary and its Extra field (red frame).
   :data: Applicant "János Tóth" for "Warehouse Coordinator"; expected 620 000 HUF, proposed 600 000 HUF, extra "company phone".
   :module: hr_recruitment
   :notes: English UI, light theme, 1440px width. Use invented applicant data.

Contract proposal
=================

When the offer is ready to be made, move the applicant to the :guilabel:`Contract Proposal` stage:
drag the card into that column in the kanban view of the job position, or open the applicant and
click the stage in the status bar at the top of the form.

Send the offer to the applicant from the chatter of the applicant form: click :guilabel:`Send
message`, or use the :icon:`fa-expand` :guilabel:`(expand)` button to open the full composer and
select an email template. Attach the contract document with the :icon:`fa-paperclip`
:guilabel:`(paperclip)` button.

.. tip::
   The offer email is easier to reuse as an :doc:`email template <../../general/companies/email_template>`
   containing the agreed wording, with the amounts filled in per applicant.

.. _recruitment/offer_job_positions/contract-signed:

Contract signed
===============

Once the applicant has accepted the offer and the contract has been signed outside the database,
move the applicant to the :guilabel:`Contract Signed` stage. A green :guilabel:`HIRED` banner
appears in the upper-right corner of both the applicant's card and form.

.. screenshot:: hr-recruitment-hired-banner
   :menu: Recruitment ‣ (job position) ‣ (open an applicant)
   :shows: An applicant form in the Contract Signed stage with the green HIRED banner in the upper-right corner.
   :highlight: The HIRED banner (red frame).
   :data: Applicant "János Tóth", stage Contract Signed.
   :module: hr_recruitment
   :notes: English UI, light theme, 1440px width.

.. _recruitment/new-employee:

Create employee
===============

Once the applicant has been hired, create their employee record: click the :guilabel:`Create
Employee` button in the upper-left corner of the applicant's form.

An employee form appears, pre-filled with the information from the applicant's card. Fill out the
rest of the form — for the details of each field, refer to the :doc:`../employees/new_employee`
documentation — and save it. The employee record is then available in the **Employees** app, where
the :doc:`contract <../employees/contracts>` is created.

.. note::
   The :guilabel:`Create Employee` button is only available to users with the
   :guilabel:`Employee Manager` or :guilabel:`Administrator` access right of the **Employees** app.
