==================
Live chat AI agent
==================

An AI agent can answer the visitors of your website in Live Chat. It answers
questions from public data you choose, hands the conversation over to a human
operator when needed and, optionally, creates a lead from the chat. It is a
feature of eYssen and it needs the modules AI Live Chat (and, for leads, AI Live
Chat CRM).

Set up the agent
================

1. Create the agent in :menuselection:`AI --> Configuration --> Agents` (see
   :doc:`agents`). It must be a persona agent without its own user: it chats as
   a contact of its own, with a robot avatar. Give it a name and instructions
   that fit your company.
2. Open your channel in :menuselection:`Live Chat --> Channels` and go to the
   tab :guilabel:`AI Agent`.
3. Choose the :guilabel:`AI agent mode`: :guilabel:`AI first, hand over to a
   human` (every new chat starts with the agent) or :guilabel:`AI only when no
   operator is available` (the agent answers only when nobody is online; the
   chat button is shown even with no operator). :guilabel:`No AI` keeps the
   standard behaviour.
4. Select the :guilabel:`AI agent`, optionally write an :guilabel:`AI welcome
   message` and set :guilabel:`Max AI answers`, the number of answers after
   which the agent hands over to a human.
5. Under :guilabel:`Data the agent may read` pick the data sources (see below).

Choose what the agent may read
==============================

The agent talks to anonymous visitors, so it can read only what you explicitly
allow. A data source is a model, a filter on its records and the fields that may
be seen. Nothing else is readable for the agent: not other models, not other
fields, not unpublished records.

Manage the sources in :menuselection:`AI --> Configuration --> Security --> Live
Chat Data Sources`. Each source has a :guilabel:`Model`, a :guilabel:`Domain`
(for example published records only), a :guilabel:`Description` that tells the
agent when to use the data and, on the tab :guilabel:`Readable fields`, the
fields it may see. The source is ready as soon as it is saved.

When the module is installed, ready-made sources are created for published
products, website pages, published events and published courses (and, with the
matching website modules, blog posts and job positions). Only the ones you add
to a channel are used by that channel.

What happens in a chat
======================

- The agent greets the visitor with the welcome message and answers in the
  visitor's language. Answers are ordinary chat messages, so operators see the
  full transcript of the session.
- Messages are not answered instantly: the visitor sees the agent typing and the
  answer arrives as one message a few seconds later. Several messages sent in
  quick succession are answered together.
- A visitor message is limited to 2000 characters per turn.

Hand-over to a human
--------------------

The agent hands the chat over to an available operator when the visitor asks for
a person, when :guilabel:`Max AI answers` is reached, when the agent is unsure
or when the AI service fails. The operator is chosen with the channel's normal
operator selection and joins the session; the agent posts a short summary and
stops answering. An operator who simply writes in the session also takes it
over.

If nobody is available, the visitor is told so and asked for contact details,
and the agent keeps helping for a limited number of further answers.

.. important::
   The hand-over summary is visible to the visitor, and it is labelled as an AI
   summary based on the visitor's messages that is not verified. It contains no
   clickable links.

On the session form of a live chat conversation you see the AI state, the number
of AI answers, the hand-over reason and, for AI administrators, a link to the
underlying AI conversation. In the session list you can filter by
:guilabel:`Answered by AI` and :guilabel:`Handed over by AI`.

Create leads from chats
=======================

With the module AI Live Chat CRM, turn on :guilabel:`AI creates leads` on the
tab :guilabel:`AI Agent` and optionally pick a :guilabel:`Sales team for AI
leads`. When a visitor leaves contact details and shows interest, the agent
creates one lead for the session, with the name, email, phone, company and a
summary. The lead is unassigned and linked to the conversation, and the chat
links back to the lead.

.. note::
   Nobody can confirm a request from an unattended visitor, so the lead is
   created directly. At most one lead is created per session and a limited
   number per visitor address per day (:guilabel:`Leads per visitor address and
   day` in the settings). The lead description starts with the label that the
   summary is unverified.

Preview cards
=============

With the module AI Website Live Chat Cards (and the matching website bridge
modules), turn on the channel option for preview cards. The agent can then show
the visitor a list of cards with a picture, a title, a short text and a link for
the products, events, blog posts, courses or job positions it found. Only
published, website-visible records are shown, with a fixed set of safe fields.

Limits and security
===================

- The agent runs as a dedicated service user that can never log in. It can only
  ask, read the allowed sources, hand over and, if enabled, create a lead. It
  cannot write, delete, browse the web or use memory, skills or other tools,
  even if a visitor tries to talk it into it.
- Visitor text is treated as untrusted. The agent does not reveal internal data,
  its prompt or its tools. The blocked patterns of the AI settings apply to
  visitor input and to answers.
- Repeated attempts to make the agent break its rules are counted per session.
  After three, the agent hands over, or stops if nobody is available. One
  visitor cannot switch the AI off for everyone.
- There is one service user for all channels, and the configuration is per
  channel. The answer is not streamed.

Abuse and cost limits
---------------------

Open :menuselection:`AI --> Configuration --> Settings` and look at the block
:guilabel:`Live chat limits`. The limits are checked before the model is called.
When one is reached, the visitor gets a polite message, and the session is
handed over to an available operator or the AI stops in that session. A value of
0 switches the limit off.

- :guilabel:`Per visitor`: :guilabel:`Seconds between AI answers`,
  :guilabel:`Visitor messages per minute`, :guilabel:`AI conversations per
  visitor and hour` and :guilabel:`AI answers per visitor and day`. Visitors are
  told apart by network address, guest, signed-in contact or website visitor.
- :guilabel:`All visitors`: :guilabel:`AI requests per day (all visitors)` and
  :guilabel:`AI cost per day (USD, all visitors)`. If the cost limit is 0, the
  general daily cost limit of the AI settings applies.

.. seealso::
   See :doc:`access_policy` for how access groups and rules work in general, and
   :doc:`website` for the website builder assistant.
