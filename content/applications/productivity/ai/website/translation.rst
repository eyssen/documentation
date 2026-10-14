=======================
Translate pages with AI
=======================

The AI translates website pages from the website's default language into its other languages. For
the languages of a website and the manual translate mode, see
:doc:`/applications/websites/website/configuration/translate`.

Translate one or several pages
==============================

#. Open a page in :menuselection:`Website --> Site --> Pages` and click :guilabel:`Translate with
   AI`, or select up to 20 pages of one website in the list and choose :guilabel:`Translate with AI`
   in the :guilabel:`Actions` menu.
#. Tick the :guilabel:`Languages` to translate into. Only the languages of the website other than
   its default language are offered; if the website has only one language, the dialog says so.
#. Leave :guilabel:`Translate again what is already translated` off to keep the existing
   translations and translate only what is missing. Turn it on to replace them.
#. Click :guilabel:`Translate`. A message shows how many texts were translated per language.

Review the result in the website editor's translate mode. You can also translate the page you are
editing from the AI dialog of the editor (see :doc:`editor`), or ask the AI panel, for example
"Translate the About us page into Spanish".

What is translated
==================

- the texts of the page, including buttons, picture texts and the texts of the blocks;
- the SEO title, description and keywords of the page;
- the menu items that link to the page.

Formatting inside a text (bold, links…) is kept exactly: the AI may not add, remove or change tags
or their attributes, and a translation that does not keep them is refused and asked again once.
Text that only looks like code, such as "<b>" written on a page about HTML, stays plain text.

Every translated page is recorded in the AI changes and can be undone (see :doc:`history`).
