==================
Post job positions
==================

After a job position has been :doc:`created and configured <new_job>`, the next step is to share it,
so that prospective applicants can apply.

Job positions can be published on the :ref:`company website <post-job/website>`. Applications that
arrive from an external job board by email are turned into applicant records by the
:ref:`job board emails <post-job/boards>`.

.. _post-job/website:

Publish to website
==================

To publish a job listing on the company's website, first a setting must be enabled in the
**Recruitment** app. Navigate to :menuselection:`Recruitment app --> Configuration --> Settings`,
and enable the :guilabel:`Online Posting` option. Click the :guilabel:`Save` button after making any
changes.

.. note::
   The :guilabel:`Online Posting` is only available if the :doc:`Website <../../websites/website>`
   application is also installed.

Once the setting has been enabled, open the main **Recruitment** dashboard by navigating to
:menuselection:`Recruitment app --> Applications --> By Job Position`. A toggle appears in the
lower-left corner of every job position card, and indicates whether the role is :guilabel:`Not
Published` or :guilabel:`Published`.

Click on the toggle to change the current state of the job position. When a job position is
published, a green :guilabel:`PUBLISHED` banner appears in the top-right corner of the card.

To view the listing on the website, click the :icon:`oi-launch` :guilabel:`Job Page` in the
lower-right corner of the job card.

.. _post-job/boards:

Job board emails
================

When a job position is also advertised on a job board such as LinkedIn or Indeed, the job board
usually lets the visitor apply directly from its own page and forwards the application by email,
from a fixed address such as `jobs-listings@linkedin.com`.

Odoo reads those emails with a regular expression (*regex*) rule — an instruction that matches text
in the email — and creates the applicant record from what it captures.

.. example::
   The regex rule for :guilabel:`LinkedIn` (emails received from `jobs-listings@linkedin.com`) is
   :guilabel:`New application:.*from (.*)`. It tells Odoo to capture everything after the word
   `from`.

   An email with the subject `New application: Job ID 123 from John Doe` captures `John Doe` and
   creates an applicant record for `John Doe`.

To see the configured job board emails, go to :menuselection:`Recruitment app --> Configuration -->
Job Boards --> Emails`. Three are preconfigured: :guilabel:`LinkedIn`, :guilabel:`Jobsdb` and
:guilabel:`Indeed`.

Create a job board email
------------------------

Click :guilabel:`New` on the :guilabel:`Emails` page and fill in:

- :guilabel:`Name`: the name of the platform, such as `Glassdoor`.
- :guilabel:`Email`: the address the applications arrive from. Applications received from this
  address are **not** linked to an existing contact.
- :guilabel:`Regex`: the rule that extracts the applicant's name from the subject or the body of the
  email.

.. screenshot:: hr-recruitment-job-board-email
   :menu: Recruitment ‣ Configuration ‣ Job Boards ‣ Emails ‣ New
   :shows: A job board email form with the platform name, the sender address and the regex rule filled in.
   :highlight: The Regex field (red frame).
   :data: Platform "Glassdoor", email "noreply@glassdoor.com", regex "New application:.*from (.*)".
   :module: hr_recruitment
   :notes: English UI, light theme, 1440px width.
