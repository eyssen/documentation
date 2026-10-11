==========
Website AI
==========

The module AI Website adds three things to the eYssen website builder: a page
generator, builder tools for the AI panel and brand kits. All of them are for
website designers, and the AI never writes raw HTML or scripts: it only chooses
and fills your website's own building blocks.

Page generator
==============

The generator turns a short brief into a complete page. You can start it in two
places:

- In the website editor, click :guilabel:`New` and choose :guilabel:`Page with
  AI`.
- In the backend, open :menuselection:`Website --> Site --> Create a page with
  AI`.

Fill in the brief:

- :guilabel:`Page name`, :guilabel:`What is the page for?` and, optionally, the
  :guilabel:`Audience`.
- :guilabel:`Sections to include`: the sections you want, in order, one per
  line.
- :guilabel:`Tone` (:guilabel:`Professional`, :guilabel:`Friendly`,
  :guilabel:`Enthusiastic`, :guilabel:`Formal`, :guilabel:`Playful` or
  :guilabel:`Short and to the point`) and :guilabel:`Language`, chosen among the
  installed languages.
- :guilabel:`Add to the menu` adds a menu item for the new page.
  :guilabel:`Search pictures on Unsplash` appears only when an Unsplash key is
  configured; without it the blocks keep their default pictures, which you can
  replace in the editor.

Click :guilabel:`Generate page`. The page is created unpublished and opens in
the editor, so you can review and adjust it before publishing. Clicking the
button is the confirmation, so no extra approval card appears.

.. note::
   The generator can use twelve common building blocks: cover, title, text, text
   with image, image with text, picture, three columns, features, numbers, call
   to action, FAQ and contact information. Blocks added by a theme are not
   offered, but a theme's own version of a listed block is used. The contact
   block takes the e-mail address, phone number and address from your company.
   Texts are plain text and the AI is told not to invent prices, figures, quotes
   or names, so always review the page.

Builder tools in the AI panel
=============================

Website designers who have the :guilabel:`Customize UI & schema` capability can
also ask the AI panel (see :doc:`panel`) to work on the website. That capability
is off by default and for administrators only (see :doc:`feature_access`). The
shipped agent :guilabel:`Website builder` is set up for this: it first looks at
the existing pages and menus, proposes changes and never says that something is
done before you confirm it.

The tools can:

- list the usable blocks, pages, menu items and brand kits;
- create a new unpublished page from a plan of blocks, optionally with a menu
  item;
- insert one block at the start, at the end or at a given position of a page;
- add, rename and reorder menu items;
- replace or append a block of custom CSS managed by the AI;
- apply a saved brand kit, or colours and fonts you give.

Confirmation cards
------------------

Website changes are public, so they are always proposed first: the panel shows a
card that you confirm or cancel (see :doc:`panel`). Only the :guilabel:`Apply
without asking` write mode applies them straight away; the mixed mode still
asks. The card lists everything that will change: every block with its title,
texts, buttons and their targets, the replaced links, a note when a block goes
onto an already published page and, for CSS changes, the complete CSS. Links to
other websites are marked as external. The change is checked again when you
confirm.

Links and CSS rules
-------------------

- Links. The builder links only to pages and anchors that exist on this website,
  to its own absolute addresses, to e-mail addresses and to phone numbers. A
  made-up path or a link to another website is replaced and listed on the card;
  a menu item that points to another website is refused. An administrator can
  lift this with :guilabel:`AI may add links to other websites` in the block
  :guilabel:`Website builder` of :menuselection:`AI --> Configuration -->
  Settings`. Such links are then still marked on the card.
- Custom CSS. The AI may only write plain CSS between its own markers in the
  website's custom stylesheet; your own rules outside the markers are kept.
  Imports, scripts, Sass features, unknown functions and addresses outside this
  site are refused, and the website styles must still compile, otherwise the
  change is rolled back.

If a turn has no builder tools (the capability is missing or you are not a
website designer), the assistant explains the manual way instead: Menu Editor,
Pages, edit mode and theme settings.

Brand kits
==========

A brand kit keeps your brand colours, fonts and logo together. Open
:menuselection:`Website --> Configuration --> Brand kits`, click New and fill in
a name, optionally a website (leave it empty to use the kit on any website), the
five colours (:guilabel:`Primary colour`, :guilabel:`Secondary colour`,
:guilabel:`Accent colour`, :guilabel:`Light colour`, :guilabel:`Dark colour`) as
``#RRGGBB`` values, the :guilabel:`Text font` and :guilabel:`Headings font`, and
the logo. Empty values are left unchanged.

Click :guilabel:`Apply to the website` to set the colour palette, the fonts and
the logo of the website theme in one step, exactly as the Theme tab of the
editor would. A font that the website does not ship is loaded from Google Fonts.
The AI panel can do the same with the tool for brand kits.

Who can use it
==============

- The page generator and the brand kits need the website designer access right.
  Builder tools in the AI panel need the website designer right and the
  customize capability.
- Public visitors, portal users and the live chat agent never see the builder
  tools.
- If an AI access rule denies the website models, the builder is blocked as well
  (see :doc:`access_policy`).

.. seealso::
   The preview cards that the live chat agent can show to visitors are described
   in :doc:`livechat`.
