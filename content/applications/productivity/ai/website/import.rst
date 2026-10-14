================
Import a website
================

The module **AI Website Import** (``ai_website_import``) copies an existing website into Odoo from
its address. It reads the pages of the site, rebuilds each page from your website's own building
blocks and shows everything for review before anything is created. It does not copy the HTML of the
other site: texts, pictures, links, lists, cards, questions and forms are taken over and put into
Odoo blocks, so the result can be edited in the website editor like any other page.

You describe what you want in your own words, for example "Copy it exactly" or "Copy it and change
the colours to blue". What the instructions leave open and matters is asked as a question with
choices.

.. note::
   Blog posts and products of the imported site are handled by two bridge modules that install
   themselves with the Blog and eCommerce apps (see :doc:`import_shop`).

Who can use it
==============

Only administrators who are also website designers can import a website (the import downloads
content from the internet). A chat model is recommended: without one, the pages are laid out by
rules and the texts are kept as they are (see :ref:`ai/website/import/without-ai`).

Start an import
===============

You can start an import in three ways:

- Open :menuselection:`Website --> Configuration --> Import a website`. The list shows the earlier
  imports; click :guilabel:`New`.
- In the website editor, click :guilabel:`New` and choose :guilabel:`Import website`. The import
  targets the website you are on.
- Ask the AI panel, for example "Copy the website https://www.example.com into a new website, with
  a blue colour scheme" (see :ref:`ai/website/import/chat`).

In the form, fill in:

- :guilabel:`Website address`: the address of the site to import, for example
  ``https://www.example.com``. Only public internet addresses are accepted.
- :guilabel:`Import`: :guilabel:`Into an existing website` (then choose the :guilabel:`Target
  website`) or :guilabel:`Into a new website` (then give the :guilabel:`New website name`).
- On the :guilabel:`Instructions` tab, your wishes in plain words (see below).

Then click :guilabel:`Start`.

Instructions in plain words
===========================

Write what you want as you would tell a colleague. Some examples:

- "Copy https://www.example.com exactly." The texts are kept word for word and the layout follows
  the source.
- "Copy it and suggest SEO improvements." The review lists SEO suggestions per page, which you tick.
- "Copy it and change the colours to blue." The design takes a blue colour scheme instead of the
  source's colours.
- "Copy only /about and /services, and publish the pages."
- "Copy it into a new website and translate it to Spanish."

The AI turns the instructions into the options below the text, which you can also set by hand
before starting:

- :guilabel:`Use AI`: lay out the pages with the AI (on when a chat model is configured).
- :guilabel:`Fidelity`: :guilabel:`Copy exactly` or :guilabel:`Improve the texts`.
- :guilabel:`SEO`: :guilabel:`Keep as it is` or :guilabel:`Suggest improvements`.
- :guilabel:`Design wish`: for example "blue colour scheme".
- :guilabel:`Translate to`: a language to translate the texts into.
- :guilabel:`Max Pages`: the number of pages to read (50 by default).
- :guilabel:`Scope`: :guilabel:`Every page` or :guilabel:`Only listed pages`, with the
  :guilabel:`Pages to import`, one path per line (for example ``/about``).
- :guilabel:`Publish the pages`: off by default, so the pages are created unpublished.
- :guilabel:`Menu`: :guilabel:`Add next to the current menu` or :guilabel:`Replace the menu`.
- :guilabel:`Replace the homepage` (existing website only) and :guilabel:`Rebuild the footer`.
- :guilabel:`Content changes`: other wishes, one per line.

What you state clearly in the instructions is never asked again.

Questions
=========

When something important is open, the import asks before it goes on. The questions appear on the
:guilabel:`Questions` tab, each with choices and often a field for another answer. Examples:

- "Create a new website or import into My Website?"
- "Replace the current menu of My Website or add the imported pages next to it?"
- "Replace the homepage of My Website with the imported homepage?"
- "Apply the colours and fonts of the imported site to My Website?"
- "Primary colour: keep #1a5f2a or use #1f4fbf / #2563eb / #1d4ed8?"
- "Rebuild the footer of My Website from the footer of the imported site?"
- questions about the languages, the blog posts, the products and their currency.

Some questions come before the site is read, because they change what is read; others come after
the analysis. Answer them and click :guilabel:`Continue`, or click :guilabel:`Use the suggested
answers` to take the pre-selected choices.

Reading the site
================

After :guilabel:`Start`, the form shows a progress bar with :guilabel:`Pages found`,
:guilabel:`Pages read`, :guilabel:`Pages ready` and :guilabel:`Pictures`. The work continues while
the form is open and, in the background, every minute, so you can close the form and come back
later. :guilabel:`Cancel import` stops it.

The import reads the site politely and safely:

- only pages of the same site (with and without ``www.``), starting with its sitemap, then
  following links up to four levels deep;
- the site's ``robots.txt`` is respected (the import identifies itself as ``eYssenImport``); a site
  that protects its ``robots.txt`` is not read;
- at most two requests per second, 15 seconds and 5 MB per page, HTML pages only;
- at most 300 pictures per import and 30 per page; further pictures keep the block's default
  picture.

The import recognises common platforms (WordPress, WooCommerce, Shopify, PrestaShop, Wix,
Squarespace, Webflow) and, on WordPress, also reads the public list of pages. Everything that
happens is written on the :guilabel:`Log` tab.

Languages
---------

A multilingual source (language versions such as ``/es/…``, language links or language switchers)
is imported in its main language, the language of its homepage. The import asks which other
languages to import as translations of the same pages. Those translations are written with the
page, its SEO texts and the menu items; the texts are matched by structure, and the AI translates
only what cannot be matched. Languages that are not active yet are activated and added to the
website during the import.

Review
======

When the analysis is done, the import shows :guilabel:`Review`. Check the tabs before you import:

- :guilabel:`Pages`: every page found, with :guilabel:`Include`, its title, the source address, the
  :guilabel:`New address`, the status and the list of :guilabel:`Blocks` chosen for it. Untick the
  pages to leave out and change a new address if needed.
- :guilabel:`Design`: the colours and fonts found on the source, the five colours and two fonts that
  will be used, and :guilabel:`Apply colours and fonts`. A colour wish such as "blue" is turned into
  a palette whose text stays readable on the primary colour.
- :guilabel:`SEO`: the suggestions, each with a tick box (see below).
- :guilabel:`Menu and redirects`: the menu that will be created, the :guilabel:`Footer of the
  source` and the :guilabel:`Redirects (301)`.
- :guilabel:`Languages`: the languages of the source and what happens with them.
- :guilabel:`Compare`: screenshots of source pages next to the imported pages (see below).

SEO and internal links
----------------------

With :guilabel:`SEO` set to :guilabel:`Keep as it is`, titles, descriptions and headings are copied
as they are. With :guilabel:`Suggest improvements`, the import checks the source with rules and asks
the AI for better titles, descriptions, main headings, picture texts and keywords. It also suggests
internal links:

- a link to a page that no other page, menu or footer links to;
- a clear text instead of a vague link text such as "click here" or "read more";
- a new target for a link to a page that is not imported, when the website has a page at the same
  address;
- a link to the contact page on important pages (services, prices, about…).

Only the ticked suggestions are applied.

Addresses and redirects
-----------------------

Imported pages keep their original address when it is free on the website. Otherwise they get a new
address, and a permanent (301) redirect is created from the old address, so links and search
results keep working. On an existing website, the imported homepage becomes ``/home`` unless you
replace the homepage. The redirects are listed on the :guilabel:`Menu and redirects` tab.

Compare pages
-------------

When the visual check is available on the server (see :ref:`ai/website/visual-check`), click
:guilabel:`Compare pages` to take screenshots of the next pages (three at a time by default). On a
page line, :guilabel:`Compare` opens the source page and the imported page side by side;
:guilabel:`Take the pictures` takes them again and :guilabel:`List the differences with AI` asks the
AI for the visible differences. The source page is loaded without JavaScript, so pages that build
their content with scripts look emptier than in a browser.

Import and undo
===============

Click :guilabel:`Import` and confirm. The import creates everything on the target website at once:

- the pages, unpublished unless :guilabel:`Publish the pages` is on;
- the menu: added next to the current menu, or replacing it. A replaced menu is not deleted: its
  items are kept aside unchanged and come back if you undo the import;
- the homepage, only on a new website or when :guilabel:`Replace the homepage` is ticked;
- a brand kit "Imported from …" with the colours, fonts and logo of the review (see
  :doc:`../website`), applied to the website when :guilabel:`Apply colours and fonts` is on (always
  on a new website), and the social network links of the source;
- the footer, when :guilabel:`Rebuild the footer` is on (always on a new website);
- the translations, the blog posts and the products you chose, and the redirects.

The form then shows a summary and a link to the imported homepage. The import is listed in the AI
changes as :guilabel:`Website import` (see :doc:`history`).

To remove the import, click :guilabel:`Undo import` and confirm. Everything the import created is
deleted (pages, menu items, redirects, posts, products, pictures it downloaded, the brand kit, a new
website) and the homepage, menu, design and languages of the website are restored. A language the
import activated stays installed.

- If a later AI change touched the imported content, undo that change first (see :doc:`history`).
- If imported content was changed by hand since, the form shows :guilabel:`Changed since the
  import:` and only :guilabel:`Undo import anyway` is offered. It deletes the imported pages and
  records with your changes.

.. _ai/website/import/chat:

Import from the AI panel
========================

The AI panel can run the whole import in the conversation. Ask, for example, "Copy the website
https://www.example.com exactly" or "Copy https://www.example.com and suggest SEO improvements". The
assistant starts the import, asks the questions as choices, reports the progress and shows the
review. Creating the import on the website is a change you confirm on a card, like any other website
change (see :doc:`edit_pages`).

The assistant needs the :guilabel:`Customize UI & schema` capability, and you need the rights
described above. Texts read from the other site are treated as untrusted data: they are shown to the
AI marked as such, and once they are part of a conversation turn, every change in that turn waits
for your confirmation.

.. _ai/website/import/without-ai:

Limits and troubleshooting
==========================

- **Without an AI model**, the pages are laid out by rules (a cover for the first heading and
  picture, alternating text and pictures, cards for repeated items, FAQ, contact form, text blocks)
  and the texts are kept as they are. Improving or translating texts needs an AI model.
- **Pages built with JavaScript**: the import reads the HTML that the server sends. A site that
  only fills its pages with scripts gives little content.
- **Protected or private sites**: pages behind a login, sites that forbid reading in their
  ``robots.txt`` and internal addresses are not read.
- **What is not copied**: scripts, iframes (YouTube and Vimeo videos are rebuilt from their
  address), inline styles and forms that send their data elsewhere. A form of the source becomes the
  website's own contact form.
- **Errors**: when the import stops, the form shows the error and :guilabel:`Retry` continues where
  it stopped. Pages that could not be read are listed on the :guilabel:`Pages` tab with their error.
- **More pages**: the default limit of 50 pages can be raised to 300 by an administrator (see
  :doc:`setup`).
