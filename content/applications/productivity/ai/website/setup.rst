=========================
Requirements and settings
=========================

This page is for administrators: what the website AI needs, who may use which part, the settings and
system parameters, and how the module keeps the website and the server safe.

Requirements
============

- The modules **AI Website Builder** (``ai_website``, it needs AI, Website and the Unsplash image
  library) and, for imports, **AI Website Import** (``ai_website_import``). The import bridges for
  the Blog and eCommerce apps install themselves.
- A chat model (see :doc:`../models_and_providers`). Generated pictures also need an image model,
  and stock photos need an Unsplash key in the website settings.
- For the visual check and the page comparison of the import: Chromium or Google Chrome on the Odoo
  server (see :ref:`ai/website/visual-check`).

Who can use what
================

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Feature
     - Needs
   * - Page generator, :guilabel:`Optimize SEO with AI`, :guilabel:`Translate with AI`
     - Website designer, :guilabel:`Ask (Q&A)` capability
   * - Brand kits, SEO audit
     - Website designer
   * - AI panel and AI in the website editor, undo of AI changes
     - Website designer, :guilabel:`Customize UI & schema` capability
   * - Website import (form and AI panel)
     - Website designer and Settings administrator; in the AI panel also the
       :guilabel:`Customize UI & schema` capability

Capabilities are set in :menuselection:`AI --> Configuration --> Behavior --> Capabilities` (see
:doc:`../feature_access`). AI access rules apply on top (see :doc:`../access_policy`), and every
change is written to the AI logs (see :doc:`../monitoring`).

Settings
========

In :menuselection:`AI --> Configuration --> Settings`, block :guilabel:`Website builder`:

- :guilabel:`AI may add links to other websites`: off by default. When off, the buttons and menu
  items the AI creates may only link to this website, e-mail addresses and phone numbers.
- :guilabel:`Let the AI use all building blocks`: on by default, for the selected website. When off,
  the AI uses only the curated blocks (see :ref:`ai/website/catalogue`).

In :menuselection:`Website --> Configuration --> Settings`, block :guilabel:`SEO`:
:guilabel:`Structured data` and :guilabel:`Publish /llms.txt` (see :doc:`seo`).

System parameters
-----------------

These optional parameters are set in :menuselection:`Settings --> Technical --> Parameters -->
System Parameters` (developer mode):

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Parameter
     - Use
   * - ``ai_website.chrome_path``
     - Path or command name of the browser for the visual check. Empty: the server looks for
       Chromium or Chrome itself. ``disabled`` switches the visual check off.
   * - ``ai_website.screenshot_base_url``
     - The address at which the server's browser reaches Odoo, for example an internal address in
       Kubernetes. Empty: ``web.base.url``.
   * - ``ai_website.ca_bundle``
     - Path of a file of certificate authorities used to check HTTPS certificates when pictures and
       pages are downloaded, for example behind a proxy that inspects TLS. Certificates are always
       checked.
   * - ``ai_website_import.max_pages``
     - The highest number of pages an import may read (default 50, at most 300).
   * - ``ai_website_import.request_interval``
     - Seconds between two requests to the imported site (default 0.5).
   * - ``ai_website_import.compare_pages``
     - Pages compared per click on :guilabel:`Compare pages` (default 3, at most 20).

Two scheduled actions belong to the modules: :guilabel:`AI website: drop AI change history older
than 90 days` (daily) and :guilabel:`AI website import: continue running imports` (every minute).

.. _ai/website/visual-check:

Visual check
============

When a browser is available, the AI can take a screenshot of a page, as a visitor sees it, to check
its work after large changes: on a desktop (1366 pixels wide) or a mobile (390 pixels) screen, the
whole page or one block, at most two per answer. The picture is stored with the AI conversation and
sent to the model. The import uses the same browser to compare the source and the imported pages.

- An unpublished page is shown to the browser with a short-lived code (two minutes) that is valid
  for that page only. No session is opened and nothing is saved.
- The browser opens the page on the server's own address, never on the website's domain. It may only
  reach that address; pictures, fonts and style sheets of other sites are downloaded by the server's
  safe download and handed to it, and everything else (other documents, scripts of other sites,
  connections) is blocked.
- Run Odoo as an ordinary user, not as root: as root, Chromium cannot use its own sandbox, and a
  warning is written to the log.

If no browser is found, the AI simply does not offer the visual check.

Security in plain words
=======================

- **The AI writes data, not code.** It gives texts, links, pictures and options; the server builds
  the blocks from the website's own templates and stores texts as plain text. JavaScript is never
  accepted, and custom CSS is checked and compiled before it is saved.
- **Your rights, never more.** Every change runs with your own access rights, goes through the AI
  access rules and is logged. Website changes are proposals that you confirm, unless you chose the
  :guilabel:`Apply without asking` write mode.
- **Everything can be undone.** Each change keeps the earlier state, and an undo that would
  overwrite later work by hand is refused unless you choose :guilabel:`Undo anyway`.
- **Downloads are fenced.** Pictures and imported pages are downloaded by the server only from
  public internet addresses (never internal ones), over the usual web ports, with limits on size,
  time and redirects; the result is stored, never linked.
- **Imported content is untrusted.** Texts read from another site are only data: they are cleaned,
  scripts, frames and foreign forms are dropped, and the AI is told that they are not instructions.
  Once such content is part of an AI conversation turn, every change in that turn waits for your
  confirmation.
- **Only for the right people.** Visitors, portal users and the live chat agent never get these
  tools; imports are for administrators.
