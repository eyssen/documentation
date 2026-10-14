===================
AI changes and undo
===================

Every website change made by the AI is recorded with what the content looked like before, so it can
be undone in one click: new pages, page and footer edits, new blocks, menu changes, custom CSS,
brand kits applied by the AI, SEO texts, translations and website imports.

The list of changes
===================

Open :menuselection:`Website --> Configuration --> AI changes`. The list shows the
:guilabel:`Applied` changes by default, with the date, the :guilabel:`Kind of change` (for example
:guilabel:`Page edited`, :guilabel:`Footer edited`, :guilabel:`New page`, :guilabel:`SEO` or
:guilabel:`Translation`), a summary, the author and the status. Use the filters :guilabel:`Undone`
and :guilabel:`My changes`, or group by :guilabel:`Kind of change` or :guilabel:`Author`.

The history keeps 90 days: older changes are removed automatically and can no longer be undone.

Undo a change
=============

Click :guilabel:`Undo` on a line, or open the change and click :guilabel:`Undo`, then confirm. The
content touched by the change is put back as it was: the texts and blocks of the page, the menu
items, the CSS, the SEO fields and their translations. Pages and menu items the change created are
removed. The change gets the status :guilabel:`Undone`, with who undid it and when.

You can also undo from the website editor (see :doc:`editor`) or ask the AI panel, for example
"Undo my last website change". The AI then proposes the undo, which you confirm.

Undoing needs the same rights as the changes: the website designer right and the
:guilabel:`Customize UI & schema` capability.

When an undo is refused
-----------------------

- **A later AI change touched the same content.** Undo the later change first: always undo the
  newest change first. The message names the later changes.
- **The content was changed by hand since** (in the editor or by another tool). The form shows
  :guilabel:`Changed since this AI change:` with what changed. A normal undo would overwrite that
  work, so it is refused. If you really want the earlier state back, click :guilabel:`Undo anyway`
  and confirm: your later changes are lost, and pages or menu items created by the AI change are
  deleted even if they were edited since. The AI itself never forces an undo.

.. note::
   A website import is undone from the import itself, with :guilabel:`Undo import` (see
   :doc:`import`). It is listed here so that later changes can see it, but it has no
   :guilabel:`Undo` button.
