=================
Knowledge sources
=================

Knowledge sources let the assistant answer from your own material: handbooks,
price lists, web pages, a record and its attachments. The text is cut into
pieces, turned into vectors by an embedding model and stored in PostgreSQL. When
someone asks a question, the most similar pieces are found, the answer is
written from them, and numbered citations show where each fact comes from.

Requirements
============

- The module AI Knowledge Sources (RAG) must be installed.
- The PostgreSQL server that Odoo connects to must provide the pgvector
  extension (``vector``). Installing the module runs ``CREATE EXTENSION IF NOT
  EXISTS vector``; if the extension is not available on that server, the
  installation stops with a clear message. Install pgvector on the database
  server itself, not on the Odoo server, and make sure the database user is
  allowed to create the extension.
- With Docker, the extension has to be in the image of the database container
  (for example an image built for PostgreSQL with pgvector), not in the Odoo
  container. If you use a managed PostgreSQL service, enable pgvector there.
- An embedding model from a provider that offers one (OpenAI, Google Gemini or
  OpenRouter). Choose it under :menuselection:`AI --> Configuration -->
  Settings` in :guilabel:`Embedding model`. Changing it queues all sources for
  re-indexing, because vectors from different models are never compared.

Add a source
============

Open :menuselection:`AI --> Knowledge --> Sources` and create a source. Choose
its :guilabel:`Type`:

- :guilabel:`Files`: upload PDFs, office documents, OpenDocument files or plain
  text.
- :guilabel:`Web page`: an ``https://`` address. Tick :guilabel:`Crawl` to
  follow links to other pages of the same site, up to :guilabel:`Crawl Depth`
  link hops and :guilabel:`Max pages` pages. The crawler respects the site's
  ``robots.txt`` (it identifies itself as ``eYssenAIBot``), stays on the same
  host, reads static HTML only (no JavaScript) and never fetches private network
  addresses.
- :guilabel:`Record`: any record of the database; tick :guilabel:`Include
  Attachments` to index its attachments too. Stored text fields are indexed,
  except fields the assistant may never read (passwords, tokens and the like).
- :guilabel:`Folder`: groups other sources in a tree; place a source in a folder
  with the :guilabel:`Folder` field. Re-indexing a folder queues everything
  inside.

Knowledge articles, document folders and cloud-stored files are added as further
source types by the Knowledge and Documents bridges (see
:doc:`knowledge_documents`).

Who can use a source
====================

- :guilabel:`Available to the assistant` makes the source searchable from the
  everyday assistant. An agent searches its own sources instead, set in the
  :guilabel:`Knowledge` tab of the agent form, plus the global ones when
  :guilabel:`Also use global sources` is on.
- :guilabel:`Allowed groups` and the company restrict who may read the source.
  Folders restrict everything inside them as well.
- Whatever the source says, a person only gets excerpts from records and
  attachments they could open in Odoo themselves, and only for models the AI
  access rules allow. A private or archived record is never cited.

Indexing
========

A new or changed source gets the status :guilabel:`Pending`. A scheduled action
(:guilabel:`AI: Index knowledge sources`, every 10 minutes) processes pending
sources. :guilabel:`Index now` processes one at once and :guilabel:`Re-index`
queues it again. The status moves through :guilabel:`Processing` to
:guilabel:`Indexed`; if something goes wrong the status is :guilabel:`Failed`
and the error is shown on the form. The :guilabel:`Chunks` button shows how many
pieces were stored.

Tuning is in the block :guilabel:`Knowledge sources` of the AI settings:
:guilabel:`Chunk size (characters)` and :guilabel:`Chunk overlap (characters)`
(1500 and 200 by default), :guilabel:`Excerpts per search` (6),
:guilabel:`Embedding dimensions` (0 means the model's own size; OpenAI
text-embedding-3 models can return shorter vectors), :guilabel:`Texts per
embedding request`, :guilabel:`Embedding requests per minute` (indexing pauses
when reached) and :guilabel:`Max pages per crawl`. Embedding calls are logged
and priced like any other model call.

Use: citations and sources only
===============================

When an embedding model is set and at least one indexed source is in scope, the
assistant can search the sources. Its answer cites facts as numbered references,
and clickable chips under the answer show the sources: a web page opens its
address, a file downloads, a record opens its form.

In the :guilabel:`Conversation options` of the AI panel, :guilabel:`Answer from
sources only` appears when sources are available. With it on, the assistant must
search the sources and says plainly that it did not find the answer when the
excerpts do not contain it.

.. note::
   Text found in sources is treated as material, not as instructions: a web page
   cannot tell the assistant to do something.

Similar tasks
=============

With an embedding model set, projects can find tasks that resemble the one you
are looking at. In the project form, in the AI block, turn on :guilabel:`Similar
tasks enabled`, and optionally set the :guilabel:`Similarity threshold` (0 to 1,
default 0.75) and the :guilabel:`Time window (days)` (0 means no limit). Task
text (name, description and recent messages) is embedded in the background every
15 minutes.

The task form then shows a :guilabel:`Similar tasks` smart button with the
count, for example "5, 2 closed". It opens the matches sorted by similarity. The
counts are computed when you open the form. Triage and the ticket quick prompts
use the same feature (see :doc:`project_sla`).

Limits
======

- Token counts shown for chunks are estimates (characters divided by four);
  billing uses the provider's own counts in the AI log.
- Vectors of more than 2000 dimensions are searched exactly (without an index),
  which is slower on large collections. Pick a shorter vector size if you can.
- Web pages are read as static HTML; content built by JavaScript is not seen.
- When access is very selective on a very large collection, a search can return
  fewer excerpts than requested.
