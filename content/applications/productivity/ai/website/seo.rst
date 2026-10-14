=================================
SEO, structured data and llms.txt
=================================

The AI writes SEO titles, descriptions and keywords from the content of your pages. An SEO audit
finds what is missing, and two website settings publish data for search engines and AI assistants.
For the SEO features of the website itself, see :doc:`/applications/websites/website/structure/seo`.

Optimize SEO with AI
====================

#. Open a page in :menuselection:`Website --> Site --> Pages` and click :guilabel:`Optimize SEO
   with AI`. To do several pages at once (at most 20), select them in the list and choose
   :guilabel:`Optimize SEO with AI` in the :guilabel:`Actions` menu.
#. The AI reads the visible headings and paragraphs of each page and suggests a title (50 to 60
   characters, at most 70), a description (120 to 160 characters, at most 170), up to ten keywords
   taken from the content and, when the page has pictures, one of them as the sharing picture.
#. Review the suggestions in the dialog. The current values are shown next to the new ones, with the
   length of the new title and description. Edit what you want, and untick :guilabel:`Apply` on the
   pages to keep as they are. Tick :guilabel:`Use as sharing picture` (off by default) to make the
   suggested picture the page's social sharing picture.
#. Click :guilabel:`Apply`.

The new values are recorded in the AI changes and can be undone (see :doc:`history`). In the AI
panel or the editor dialog you can ask for the same, for example "Improve the SEO of this page".

SEO audit
=========

Open :menuselection:`Website --> Site --> SEO audit`. The audit checks the pages of the website
without AI and lists its findings as errors, warnings and hints:

- missing, duplicate, too short or too long titles and descriptions;
- pages without a main heading (H1) or with several;
- pictures without alternative text;
- thin pages (fewer than 150 words);
- broken internal links;
- unpublished pages in the menu.

The :guilabel:`Open the page` button of a line opens the page. :guilabel:`Check again` runs the
audit again after your changes. :guilabel:`Improve titles and descriptions with AI` opens the SEO
dialog above for the pages with title or description findings.

Structured data
===============

With :guilabel:`Structured data` on (:menuselection:`Website --> Configuration --> Settings`, block
:guilabel:`SEO`), every page carries structured data (JSON-LD) for search engines:

- your organisation: name, address of the website, logo, social network links and contact data;
- a local business, when the company has an address;
- the website itself;
- the questions and answers of the visible FAQ blocks of the page. Hidden blocks are left out, so
  the structured data only states what a visitor can read.

No AI is involved: the data comes from your company, your website and the page. The setting is on
for new installations and off for databases upgraded to this version.

llms.txt
========

With :guilabel:`Publish /llms.txt` on (same place), the website answers at ``/llms.txt`` with a
short text file for AI assistants and search tools: the website name, the description of the
homepage and the list of published pages, each with its title and description. Only pages that
everybody may see and that search engines may index are listed. The setting is off by default.
