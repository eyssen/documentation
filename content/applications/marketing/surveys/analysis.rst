===============
Survey analysis
===============

After surveys have been created and sent to participants, it is only a matter of time before the
responses start to come in. When they do, it is important to know where and how to analyze them in
the Odoo *Surveys* application.

Fortunately, Odoo provides numerous ways to view survey responses, allowing users to access and
analyze survey responses as they are submitted.

See results
===========

Upon opening the :menuselection:`Surveys` application, the main dashboard reveals a list of all the
surveys in the database, along with pertinent information related to each one.

By default, every survey line showcases its number of :guilabel:`Questions`, :guilabel:`Average
Duration`, and how many participants have :guilabel:`Registered` or :guilabel:`Completed` the
survey.

There are also elements showing the percentage of how many participants :guilabel:`Passed` (if a
*Required Score (%)* was configured), or how many participants became :guilabel:`Certified` (if the
*Is a Certification* option was configured).

.. note::
   To learn more about the different analytical elements found on the :guilabel:`Surveys` dashboard,
   check out the :doc:`Survey Essentials <../surveys/create>` documentation.

On the :guilabel:`Surveys` dashboard, to the far-right of each survey line displayed in the default
list view, there is a :guilabel:`See results` button.

.. screenshot:: surveys-analysis-see-results-button
   :menu: Surveys ‣ Surveys
   :shows: A survey kanban card with the See results button visible on it.
   :highlight: The See results button (red frame).
   :data: Demo survey 'Product Feedback' with about 20 participations; certification survey 'Odoo 18 Basics'.
   :module: survey
   :notes: English UI, light theme, 1440px width.

When the :guilabel:`See results` button is clicked, a new browser tab opens, revealing a separate
page filled with all of that particular survey's results and responses, with an informative
:guilabel:`Results Overview` and some filtering drop-down menus at the top.

.. screenshot:: surveys-analysis-results-page
   :menu: Surveys ‣ Surveys ‣ See results
   :shows: The survey results page in the browser with the Results Overview block and the per-question results below it.
   :data: Survey 'Product Feedback' with about 20 completed participations.
   :module: survey
   :notes: English UI, light theme, 1440px width.

At the top of the page, there is an :guilabel:`Edit Survey` link, in the middle of a blue header
banner. When clicked, Odoo returns the user to the survey form for that particular survey.

Beneath that, is the title of the survey, and its description, if one was configured for it on its
survey form.

To the right of the survey title, there are two drop-down menus with various filtering options,
which can be used to personalize and segment the survey results in a number of different ways.

The first filter drop-down menu is set on the default :guilabel:`All Surveys` option, meaning the
results below are showing results and responses from all the submitted surveys, regardless if they
have been fully completed or not.

When that drop-down menu is clicked open, another option, :guilabel:`Completed surveys`, appears.

.. screenshot:: surveys-analysis-all-surveys-dropdown
   :menu: Surveys ‣ Surveys ‣ See results
   :shows: The All surveys drop-down menu on the results page, listing the other surveys to switch to.
   :highlight: The All surveys drop-down menu (red frame).
   :data: Demo survey 'Product Feedback' with about 20 participations; certification survey 'Odoo 18 Basics'.
   :module: survey
   :notes: English UI, light theme, 1440px width.

With that drop-down menu open, the number corresponding to each filter option appears to the right
of each option.

To the right of that drop-down menu of filter options, is another drop-down menu of filter options
that can be used to further customize the results showcased on this page.

That drop-down menu is set to the :guilabel:`Passed and Failed` option, by default. This option
shows the results and responses from all participants who have passed or failed this particular
survey.

.. note::
   This second drop-down menu of filter options **only** appears if the survey being analyzed has a
   *Scoring* option configured, or if the *Is a Certification* feature has been enabled.

When that second drop-down menu of filter options is clicked open, two additional options appear:
:guilabel:`Passed only` and :guilabel:`Failed only`.

.. screenshot:: surveys-analysis-passed-failed-dropdown
   :menu: Surveys ‣ Surveys ‣ See results
   :shows: The Passed and Failed drop-down menu on the results page of a scored survey.
   :highlight: The Passed and Failed drop-down menu (red frame).
   :data: Certification survey 'Odoo 18 Basics' with passed and failed participations.
   :module: survey
   :notes: English UI, light theme, 1440px width.

Each option would filter the results below to only show responses from participants who have passed
the survey, or who have failed the survey, respectively.

Directly beneath the survey title, there is a :guilabel:`Print` button. When clicked, the entire
results page can be printed.

The :guilabel:`Results Overview` section is below the survey title, filter option drop-down menus,
and :guilabel:`Print` button.

.. screenshot:: surveys-analysis-results-overview
   :menu: Surveys ‣ Surveys ‣ See results
   :shows: The Results Overview block showing the number of registered, completed and average duration values.
   :highlight: The Results Overview block (red frame).
   :data: Demo survey 'Product Feedback' with about 20 participations; certification survey 'Odoo 18 Basics'.
   :module: survey
   :notes: English UI, light theme, 1440px width.

This section of the results page provides a summarized collection of useful survey-related data and
metrics for quick analysis.

Question analysis
-----------------

Directly beneath the :guilabel:`Results Overview` section is where the results and responses of the
survey are found.

.. note::
   The various sections of the survey, if there were any, appear at the top of their corresponding
   questions on the results page, as well, for added organization.

Every question that was a part of the survey is shown, along with an in-depth breakdown, and visual
representation, of how it was answered by participants, beneath the :guilabel:`Results Overview`
section.

Each question is displayed above its corresponding results. To the left of the question is an
:guilabel:`👁️ (eye)` icon. When clicked, Odoo hides the visual and data-related results and
responses. When clicked again, that question's visual and data-related results re-appear.

To the far-right of the question, there are indicators to see how many participants
:guilabel:`Responded` and how many :guilabel:`Skipped` the question.

.. screenshot:: surveys-analysis-responded-skipped-indicators
   :menu: Surveys ‣ Surveys ‣ See results
   :shows: A question block on the results page with the Responded and Skipped counters above the answers.
   :highlight: The Responded and Skipped counters (red frame).
   :data: Demo survey 'Product Feedback' with about 20 participations; certification survey 'Odoo 18 Basics'.
   :module: survey
   :notes: English UI, light theme, 1440px width.

If the question required the participant to enter in their own answer, without any options to choose
from, like entering a specific number or date, for example, there is also an indicator to showcase
how many users answered the question :guilabel:`Correct`.

.. screenshot:: surveys-analysis-correct-indicator
   :menu: Surveys ‣ Surveys ‣ See results
   :shows: A scored question on the results page where the correct answer is marked with a green Correct label.
   :highlight: The Correct label (red frame).
   :data: Certification survey 'Odoo 18 Basics'.
   :module: survey
   :notes: English UI, light theme, 1440px width.

.. note::
   Even if there is no configured *correct* response for question of this nature, the
   :guilabel:`Correct` indicator still appears, although, it displays a `0`.

   This would occur for opinion-based questions, like `When would be a good time to hold another
   sale?`

If there is only one correct response to a multiple choice question, those results and responses are
represented by a :guilabel:`Pie Graph`. The correct answer is indicated by a :guilabel:`✔️
(checkmark)` icon next to the correct answer option, in the legend above the graph.

.. screenshot:: surveys-analysis-pie-graph-results
   :menu: Surveys ‣ Surveys ‣ See results
   :shows: The results of a single-choice question shown as a pie chart with the answer legend.
   :data: Question with three answer options.
   :module: survey
   :notes: English UI, light theme, 1440px width.

If there are multiple correct answer options (or no correct answers at all) for a multiple choice
question, those results and responses are represented by a :guilabel:`Bar Graph`.

.. screenshot:: surveys-analysis-bar-graph-results
   :menu: Surveys ‣ Surveys ‣ See results
   :shows: The results of a multiple-choice question shown as a bar chart with one bar per answer option.
   :data: Question with four answer options.
   :module: survey
   :notes: English UI, light theme, 1440px width.

Each multiple choice question has a :guilabel:`Graph` tab and an :guilabel:`Data` tab. The
graph-related tab is shown by default.

The :guilabel:`Data` tab shows all the provided :guilabel:`Answer` options for the question. The
:guilabel:`User Choice` (with percentages and votes) along with the :guilabel:`Score` of each
option.

.. screenshot:: surveys-analysis-data-tab
   :menu: Surveys ‣ Surveys ‣ See results
   :shows: The Data tab of a question's results, listing the answers with their user counts and percentages.
   :highlight: The Data tab (red frame).
   :data: Demo survey 'Product Feedback' with about 20 participations; certification survey 'Odoo 18 Basics'.
   :module: survey
   :notes: English UI, light theme, 1440px width.

Other question types, wherein there were no answer options for the participant to choose from, there
is a :guilabel:`Most Common` tab and an :guilabel:`All Data` tab.

The :guilabel:`Most Common` tab shows the :guilabel:`User Responses`, the :guilabel:`Occurrence`,
and the :guilabel:`Score` (if applicable).

.. screenshot:: surveys-analysis-most-common-tab
   :menu: Surveys ‣ Surveys ‣ See results
   :shows: The Most Common tab of a free-text question's results, listing the most frequent answers.
   :highlight: The Most Common tab (red frame).
   :data: Demo survey 'Product Feedback' with about 20 participations; certification survey 'Odoo 18 Basics'.
   :module: survey
   :notes: English UI, light theme, 1440px width.

The :guilabel:`All Data` tab shows a list of all the submitted responses to that particular
question.

.. screenshot:: surveys-analysis-all-data-tab
   :menu: Surveys ‣ Surveys ‣ See results
   :shows: The All Data tab of a free-text question's results, listing every individual answer.
   :highlight: The All Data tab (red frame).
   :data: Demo survey 'Product Feedback' with about 20 participations; certification survey 'Odoo 18 Basics'.
   :module: survey
   :notes: English UI, light theme, 1440px width.

If a question is looking for participants to enter a numerical value as a response,
:guilabel:`Maximum`, :guilabel:`Minimum`, and :guilabel:`Average` indicators appear to the far-right
of the results tabs.

.. screenshot:: surveys-analysis-max-min-avg-indicator
   :menu: Surveys ‣ Surveys ‣ See results
   :shows: A numerical question's results with the Maximum, Minimum and Average indicators above the answer list.
   :highlight: The Maximum, Minimum and Average indicators (red frame).
   :data: Numerical question with about 20 answers.
   :module: survey
   :notes: English UI, light theme, 1440px width.

A :guilabel:`filter` icon is also present either to the right of the :guilabel:`User Choice` column
in a :guilabel:`Data` tab, or to the far-right of a :guilabel:`User Response` line in an
:guilabel:`All Data` tab.

.. screenshot:: surveys-analysis-filter-icon
   :menu: Surveys ‣ Surveys ‣ See results
   :shows: An answer line on the results page with the filter icon that appears when hovering over it.
   :highlight: The filter icon next to the answer (red frame).
   :data: Demo survey 'Product Feedback' with about 20 participations; certification survey 'Odoo 18 Basics'.
   :module: survey
   :notes: English UI, light theme, 1440px width.

When that :guilabel:`filter` icon is clicked, Odoo returns the user to the top of the results page,
with that chosen filter applied, showing the results of each question for participants who submitted
that particular answer for that specific question.

.. screenshot:: surveys-analysis-applied-filter
   :menu: Surveys ‣ Surveys ‣ See results
   :shows: The results page with a filter applied, shown as a removable chip above the Results Overview block.
   :highlight: The applied filter chip (red frame).
   :data: Demo survey 'Product Feedback' with about 20 participations; certification survey 'Odoo 18 Basics'.
   :module: survey
   :notes: English UI, light theme, 1440px width.

Therefore, showcasing the remaining results for participants who answered that specific question in
the same way. To remove that filter, and reveal all the results once again, click :guilabel:`Remove
all filters` or click the :guilabel:`✖️ (X)` icon in the filter box at the top of the results page.

Participations
==============

To view a consolidated list of participation results for a specific survey, navigate to
:menuselection:`Surveys app`, select the desired survey from the list, and click the
:guilabel:`Participations` smart button at the top of the survey form.

.. screenshot:: surveys-analysis-participations-smart-button
   :menu: Surveys ‣ Surveys ‣ (survey)
   :shows: A survey form with the Participations smart button at the top showing the number of participations.
   :highlight: The Participations smart button (red frame).
   :data: Demo survey 'Product Feedback' with about 20 participations; certification survey 'Odoo 18 Basics'.
   :module: survey
   :notes: English UI, light theme, 1440px width.

Doing so reveals a separate :guilabel:`Participations` page, showcasing the participants for that
specific survey, along with a collection of pertinent information related to each one.

.. screenshot:: surveys-analysis-participations-page-singular-survey
   :menu: Surveys ‣ Surveys ‣ (survey) ‣ Participations
   :shows: The participation list of one survey with the Participant, Status, Score and Date columns.
   :data: About 20 participations of 'Product Feedback'.
   :module: survey
   :notes: English UI, light theme, 1440px width.

Here, users can view information related to individual participants who took that specific survey.
If they desire to see a more detailed breakdown of their various answers and responses, they can
click on any participant, and Odoo reveals a separate page showing that participant's survey
details, along with their submitted answers.

.. screenshot:: surveys-analysis-individual-participant-page
   :menu: Surveys ‣ Participations ‣ (participation)
   :shows: One participation's form with the Survey, Contact, Email, Status, Score and the answers given.
   :highlight: The Status and Score fields (red frame).
   :data: One completed participation.
   :module: survey
   :notes: English UI, light theme, 1440px width.

To view a consolidated list of all participants of every survey in the database, navigate to
:menuselection:`Surveys app --> Participations`. Here, every survey in the database is shown in a
default nested list. Beside each survey title has the number of participants in parenthesis.

.. screenshot:: surveys-analysis-participations-page-all-surveys
   :menu: Surveys ‣ Participations
   :shows: The Participations list of all surveys, grouped by survey.
   :data: Participations of two surveys.
   :module: survey
   :notes: English UI, light theme, 1440px width.

When a survey is un-nested from this list, by clicking the survey title, the corresponding
participants, along with their response-related data for that survey, appear on the page.

The :guilabel:`Participations` page can also be viewed in a Kanban layout, as well.

.. screenshot:: surveys-analysis-participations-page-kanban-view
   :menu: Surveys ‣ Participations
   :shows: The Participations kanban grouped by survey, each card showing the participant and the status.
   :data: Participations of two surveys.
   :module: survey
   :notes: English UI, light theme, 1440px width.

.. seealso::
   - :doc:`create`
   - :doc:`scoring`
