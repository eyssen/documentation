==========================================
AI in Knowledge, Documents and cloud files
==========================================

Three small modules connect the AI to the places where your company keeps its
articles and files. They build on the knowledge sources described in
:doc:`knowledge_sources`, so the same indexing, citation and access rules apply,
and they install themselves when the required apps are present. AI Knowledge
needs the Knowledge app, AI Documents needs the Documents app and AI Cloud
Storage needs cloud storage.

.. important::
   The pgvector extension and an embedding model are required for all knowledge
   sources (see :doc:`knowledge_sources`).

Knowledge articles as sources
=============================

In :menuselection:`AI --> Knowledge --> Sources`, create a source and choose the
type :guilabel:`Knowledge articles`. Pick one or more :guilabel:`Knowledge
spaces` (every article of the space is used) and/or single :guilabel:`Articles`.
:guilabel:`Include sub-articles` is on by default. At least one space or article
is needed. Templates and articles in the trash are not indexed, and a source
covers at most 2000 articles by default.

- Each article is indexed together with its position in the space (space, parent
  articles, title), so a search finds it by context. A citation chip in an
  answer opens the article.
- When an article changes, only that article is indexed again, at the next
  indexing run (every 10 minutes) or when you click :guilabel:`Index now`.
  Moving an article takes its sub-articles along; deleting an article removes
  its excerpts at once.
- The Knowledge app's own sharing is respected for every question: a private,
  archived or trashed article is never cited to someone who may not see it, even
  before it is indexed again. Files embedded in an article are not indexed with
  it; add them as a file source if you need them.

Draft an article with AI
========================

In the article editor, the top bar shows :guilabel:`Draft with AI` when a main
AI model is configured, you are an AI user and the article is not locked or in
the trash. It saves the article and opens a dialog with three steps:

1. :guilabel:`Brief`: describe :guilabel:`What should the article cover?` (the
   title is the default). If knowledge sources are available to you, you can
   switch on :guilabel:`Use the knowledge sources` so that the AI draws on your
   company's own material. Click :guilabel:`Propose an outline`.
2. :guilabel:`Outline`: the AI proposes 3 to 8 sections as a list. Edit it
   freely, or click :guilabel:`New outline` to ask again. Then click
   :guilabel:`Write the article`.
3. :guilabel:`Preview`: read the finished article. Click :guilabel:`Insert into
   the article`, or :guilabel:`Write again` or go back. When the article already
   has text, choose :guilabel:`When accepting` between :guilabel:`Replace the
   current content` and :guilabel:`Add after the current content`.

The AI sees the title, the space, the current content and the names of the
parent and sibling articles that you may see, and the excerpts from the sources
when you chose them. It is told not to invent company facts and to put
placeholders in square brackets, so review and complete the draft. The text goes
into the article with your rights, is recorded in the AI change log and counts
as a normal edit in the article history.

AI cover
--------

When an image model is configured (see :doc:`models_and_providers`), a picture
button in the top bar (tooltip :guilabel:`Generate a cover image with AI`) opens
a dialog with an editable description of the cover (by default a calm, wide
banner for the title, without text). Click :guilabel:`Generate`, look at the
preview, and then :guilabel:`Use as cover`, try again or :guilabel:`Change the
description`. The cover appears above the article.

Document folders as sources
===========================

In :menuselection:`AI --> Knowledge --> Sources`, choose the type
:guilabel:`Document folders`, pick the folders and decide with
:guilabel:`Include sub-folders` whether the sub-folders count. Files attached to
fields and links are not used. A source covers at most 500 documents by default,
newest first, and the text of each file is read up to 25 MB. When a document is
attached to a business record, its excerpts also follow the record's access
rules.

New and changed documents are indexed again incrementally. At question time a
document is used only if you may read its folder and the document itself, with
the same visibility as in the Documents app. Users without the Documents app get
nothing from these sources.

AI filing of documents
======================

The AI can propose the right folder and tags for a document, either when you ask
or when a file is uploaded.

On request
----------

On a document form, click :guilabel:`Suggest a folder` (you need write access to
the document). The proposal is computed at once and shows the folder, the tags,
the confidence and the reason. Click :guilabel:`Apply` or :guilabel:`Dismiss`. A
pending proposal also appears as a banner on the document.

On upload
---------

Open a folder and look at the group :guilabel:`AI filing`. Choose
:guilabel:`Suggest a folder` so that every document uploaded into the folder
gets a proposal that the uploader confirms, or :guilabel:`File automatically` so
that proposals are applied at once when the AI is at least as sure as the
:guilabel:`Minimum confidence` (0.8 by default); the other proposals wait for
confirmation. The option :guilabel:`AI may file documents here` decides whether
other documents can be filed into this folder. Proposals are prepared about
every 10 minutes, in the name of the person who uploaded the file, with that
person's rights.

Open :menuselection:`Documents --> AI filing` to see the proposals (the filter
:guilabel:`To decide` is on by default), with the filters :guilabel:`Applied`,
:guilabel:`Failed` and :guilabel:`Applied automatically`. A failed proposal can
be retried with :guilabel:`Try again`. When a proposal is applied, the previous
folder and tags are kept on it, and a note in the document chatter says who
confirmed it, or that it was filed automatically.

.. note::
   The AI reads the first part of a document's text only when the AI read policy
   allows documents, or when the folder has AI filing turned on, and never when
   an explicit AI deny rule applies to you. Filing runs with the uploader's AI
   rights, so uploads made by technical users, such as the mail gateway, usually
   fail with a recorded error.

Files in cloud storage
======================

With AI Cloud Storage installed, files that are stored with the cloud storage
provider can be indexed like local files, wherever the knowledge sources read
attachments: file sources, record sources, document folders and AI filing. The
server downloads the file through the signed download link of the configured
provider.

- Only secure (https) links are followed and redirects are not. A file larger
  than 25 MB by default (100 MB at most) is skipped, and each file has a time
  budget, so a failed or too large download skips that file only.
- Cloud files are downloaded completely every time the source is indexed again;
  there is no local cache. If cloud storage is not configured, the source fails
  with a clear message.
