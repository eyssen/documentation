==========
Website AI
==========

The module **AI Website Builder** (``ai_website``) adds AI to the eYssen website builder. It creates
new pages from a short brief, edits the pages and the footer you already have, styles blocks with
the editor's own options, writes SEO texts and translations, and keeps a history in which every AI
change can be undone. The module **AI Website Import** (``ai_website_import``) copies an existing
website from its address. Everything is for website designers.

.. important::
   The AI never writes HTML or scripts. It only chooses your website's own building blocks and
   gives the texts, links, pictures and options to put in them; the server builds the markup and
   checks every change again before it is saved.

What you can do
===============

- **Create a page** from a brief with the page generator (below).
- **Edit existing pages and the footer**: change texts, links and pictures, remove, move or
  duplicate blocks and items, add blocks and set block options such as colours and spacing (see
  :doc:`website/edit_pages`).
- **Use AI inside the website editor**: select a block, ask, then accept or reject the proposal
  (see :doc:`website/editor`).
- **Undo any AI change** in one click, also days later (see :doc:`website/history`).
- **Improve SEO**: titles, descriptions, keywords and the sharing picture, an SEO audit, structured
  data and ``/llms.txt`` (see :doc:`website/seo`).
- **Translate pages** into the other languages of the website (see :doc:`website/translation`).
- **Import a website** from its address, with blog posts and products (see :doc:`website/import`
  and :doc:`website/import_shop`).
- **Apply a brand kit** with your colours, fonts and logo (below).

Administrators find the rights, settings and the visual check in :doc:`website/setup`.

Page generator
==============

The generator turns a short brief into a complete page. You can start it in two places:

- In the website editor, click :guilabel:`New` and choose :guilabel:`Page with AI`.
- In the backend, open :menuselection:`Website --> Site --> Create a page with AI`.

Fill in the brief:

- :guilabel:`Page name`, :guilabel:`What is the page for?` and, optionally, the
  :guilabel:`Audience`.
- :guilabel:`Sections to include`: the sections you want, in order, one per line.
- :guilabel:`Tone` (:guilabel:`Professional`, :guilabel:`Friendly`, :guilabel:`Enthusiastic`,
  :guilabel:`Formal`, :guilabel:`Playful` or :guilabel:`Short and to the point`) and
  :guilabel:`Language`, chosen among the installed languages.
- :guilabel:`Add to the menu` adds a menu item for the new page. :guilabel:`Search pictures on
  Unsplash` appears only when an Unsplash key is configured; without it the blocks keep their
  default pictures, which you can replace in the editor.

Click :guilabel:`Generate page`. The page is created unpublished and opens in the editor, so you can
review and adjust it before publishing. Clicking the button is the confirmation, so no extra
approval card appears. The new page is listed in :doc:`the AI changes <website/history>`, where you
can undo it.

.. note::
   A page has at most twelve blocks, chosen from the catalogue of building blocks described in
   :ref:`ai/website/catalogue`. The contact block takes the e-mail address, phone number and address
   from your company. Texts are plain text and the AI is told not to invent prices, figures, quotes
   or names, so always review the page.

Brand kits
==========

A brand kit keeps your brand colours, fonts and logo together. Open :menuselection:`Website -->
Configuration --> Brand kits`, click New and fill in a name, optionally a website (leave it empty to
use the kit on any website), the five colours (:guilabel:`Primary colour`, :guilabel:`Secondary
colour`, :guilabel:`Accent colour`, :guilabel:`Light colour`, :guilabel:`Dark colour`) as
``#RRGGBB`` values, the :guilabel:`Text font` and :guilabel:`Headings font`, and the logo. Empty
values are left unchanged.

Click :guilabel:`Apply to the website` to set the colour palette, the fonts and the logo of the
website theme in one step, exactly as the Theme tab of the editor would. A font that the website
does not ship is loaded from Google Fonts. The AI panel can do the same with the tool for brand
kits; a brand kit applied by the AI is recorded in :doc:`the AI changes <website/history>` and can
be undone there.

Who can use it
==============

- The brand kits and the SEO audit need the website designer access right. The page generator and
  the SEO and translation buttons also need the :guilabel:`Ask (Q&A)` capability.
- Changes made by the AI panel and by the AI in the website editor, and undoing them, need the
  website designer right and the :guilabel:`Customize UI & schema` capability.
- Importing a website needs the website designer right and the Settings administrator right.
- Public visitors, portal users and the live chat agent never see these tools.
- If an AI access rule denies the website models, the builder is blocked as well (see
  :doc:`access_policy`).

See :doc:`website/setup` for the details.

.. seealso::
   The preview cards that the live chat agent can show to visitors are described in
   :doc:`livechat`.

.. toctree::
   :titlesonly:

   website/edit_pages
   website/editor
   website/history
   website/seo
   website/translation
   website/import
   website/import_shop
   website/setup
