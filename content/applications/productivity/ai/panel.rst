============
The AI panel
============

The AI panel is the everyday way to talk to the assistant. It opens from the AI
bubble in the top bar of the backend, from :menuselection:`AI -->
Conversations`, or from the command palette (see :doc:`search_and_commands`).
When you open it on a record, the assistant sees that record and offers quick
prompts that fit it.

Everything the assistant reads or changes goes through the same access gate as
your own Odoo rights: it can never see or do more than you can, and an
administrator can narrow it further (see :doc:`feature_access`).

Quick prompts
=============

When a record form is open, a row of small buttons appears above the message
box: the quick prompts. One click sends the stored instruction, for example
"Summarise" or "Next best action". Hover a button to read the instruction it
sends. Prompts made for the current model come first; generic prompts come last,
and a specific prompt can replace a generic one.

Administrators manage them under :menuselection:`AI --> Configuration -->
Behavior --> Quick Prompts`: name, instruction, the model they belong to,
whether they need a single open record, the groups that see them and the generic
prompt they replace. Many app modules ship their own prompts (see
:doc:`app_integrations`); you can edit or archive them.

Conversation options
====================

The sliders button (:guilabel:`Conversation options`) opens a small drawer. Your
choices are remembered for the next conversations.

- :guilabel:`Think longer` asks the model for extended reasoning. Answers are
  slower and cost more, but hard questions get better results. It only has an
  effect on models flagged as reasoning-capable (see
  :doc:`models_and_providers`).
- :guilabel:`Show the steps the assistant takes` adds a collapsed "N steps" line
  under each answer. Open it to see which tools were called, whether each call
  was allowed and how long it took. Use it to understand or check an answer.
- :guilabel:`Changes to data:` chooses how this conversation handles changes.
  :guilabel:`Follow the AI settings` uses the global write mode;
  :guilabel:`Always ask me first` turns every change into a proposal you
  confirm; :guilabel:`Apply without asking` skips the confirmation step. The
  last choice only appears when an administrator has enabled it, and rules that
  force confirmation still win.

Confirming changes
==================

When the assistant wants to create, update or delete something and confirmation
is required, it does not change the data. A card with a plain-language summary
appears under :guilabel:`Pending changes`. Click :guilabel:`Confirm` to apply
the change in your name, or :guilabel:`Cancel` to drop it. All open proposals
are also listed under :menuselection:`AI --> Write Proposals`, and a proposal
that nobody answers expires after the configured lifetime.

The :guilabel:`Records created or updated` button lists the records the
assistant touched in this conversation, with links.

What the assistant can show
===========================

- Record cards: for a list of records (up to 20) it shows compact clickable
  cards with the name and a few key fields instead of a long text list.
- Pictures: ask for an image and, if an image model is configured, the result
  appears under the answer and is stored with the conversation.
- Navigation: it can open the list, pivot or graph you ask for, with the
  filters, grouping and measures it understood, and it can change the search of
  the view you are looking at (add or remove filters, grouping, ordering).
- Dates: "last quarter" or "three working days from now" are computed with your
  time zone and company calendar instead of being guessed.
- Menus: it can tell you where in the menu tree a feature lives, limited to the
  menus you can see.

Files
=====

Use :guilabel:`Attach files` to add images and documents to your message. The
assistant can read the text of a PDF or office document you are allowed to read,
and look at pictures. Open :guilabel:`Conversation files` to see everything
attached to the conversation. Allowed types and the maximum size are set in the
AI settings.

Delegating to specialist agents
===============================

An agent can hand a sub-task to a specialist agent, and the everyday assistant
can consult agents that an administrator made available to it ("ask the
accounting agent"). The sub-task runs as you, in its own conversation, and the
specialist can use only the capabilities that both agents and you have:
delegation never widens rights. You see the sub-task in the panel with a
:guilabel:`Back` link to return to the main conversation. Delegation goes at
most two levels deep and cannot loop.

Administrators set this up on the agent form: :guilabel:`Can delegate to` lists
the specialists an agent may use, and :guilabel:`Available to the assistant`
makes an agent consultable from the everyday chat. Only agents without their own
user can be delegates.
