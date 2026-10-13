=============================
AI search and command palette
=============================

Two shortcuts put the assistant at your fingertips: you can describe a search in
your own words, and you can ask a question from anywhere with the command
palette. Both need a configured chat model and the :guilabel:`AI: User` group.

Search with AI
==============

1. Open any list, kanban or other view with a search bar and click the
   magic-wand button :guilabel:`Search with AI` in the search bar.
2. Write what you are looking for as a sentence, for example "quotations over
   5,000 euros from last quarter, grouped by salesperson", and press Enter.
3. The assistant turns the sentence into ordinary search facets (filters and
   grouping) on the current view. You can remove or change them like any other
   facet.

When you ask for everything about a topic (for example "everything about
consignment stock"), the assistant does not look for your exact words. It lists
a few short word stems in your language, adds synonyms and the English term
(for the Hungarian question above: *bizomány*, *konszignáci* and *consignment*),
and keeps the records whose name or description contains **any** of the stems,
ignoring upper and lower case. Up to eight stems are used, each at least three
characters long. They are looked up in the free-text fields that the list has,
such as name, description, note, comment, reference, email, subject and body.

The proposed search is checked against the fields of the view and your rights
before it is applied. If the assistant suggests something the view cannot use,
you get a message instead of a wrong result. The button is hidden in pop-up
dialogs.

Command palette
===============

Press :kbd:`Ctrl+K` (:kbd:`Cmd+K` on a Mac) to open the command palette.

- Type ``?`` followed by your question and press Enter (:guilabel:`Ask the AI
  assistant...`). The AI panel opens and answers it.
- In the default list, any longer free text you type (twelve characters or more)
  also offers an :guilabel:`Ask AI` entry, so you can turn a search that found
  nothing into a question.
- :guilabel:`Open the AI assistant` opens the panel without a question.

.. note::
   Questions asked this way are ordinary assistant conversations: they appear
   under :menuselection:`AI --> Conversations` and follow the same access rules
   and limits (see :doc:`panel`).
