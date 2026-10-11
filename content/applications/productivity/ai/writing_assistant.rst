=================
Writing assistant
=================

The writing assistant helps you write texts where you already work: in any
rich-text field, in the chatter of a record and in the image dialog of the
editor. It only produces text or a picture for you to review. Nothing is posted,
sent or saved until you do it yourself.

It needs a chat model (and, for pictures, an image model) set under
:menuselection:`AI --> Configuration --> Settings`, and your user must be in the
:guilabel:`AI: User` group. Every request counts against your rate limit and is
written to the AI log.

AI writer in the editor
=======================

1. In any rich-text field (a description, a note, an email body), type ``/`` and
   choose :guilabel:`AI writer` under the AI tools. You can also select some
   text and click the :guilabel:`AI` button in the toolbar.
2. In the dialog :guilabel:`Generate text with AI`, say what you want: write a
   paragraph, rewrite the selection in a friendlier tone, shorten it, expand it,
   fix the grammar or translate it. The dialog keeps the conversation, so you
   can refine the result with follow-up messages.
3. Click :guilabel:`Insert` on the answer you like. It replaces the selection or
   goes at the cursor. If you do not like it, close the dialog: the document is
   unchanged.

To translate selected text quickly, use the :guilabel:`Translate with AI`
language selector in the toolbar.

.. note::
   The same dialog is used in the email marketing editor (see
   :doc:`app_integrations`), where it is also called :guilabel:`AI writer`.

Draft with AI in the chatter
============================

On a saved record, the message composer of the chatter shows a :guilabel:`Draft
with AI` button (a magic wand next to the attachment button). Use it for both a
reply to followers (:guilabel:`Send message`) and an internal note. The
assistant reads the record and its recent messages and writes a draft into the
box. If you had already typed something, it takes your text into account.

The draft is only placed in the box. Edit it and send it the usual way. The
button is not offered in Discuss channels or while you are editing an existing
message.

AI images in the media dialog
=============================

When an image model is configured, the editor's media dialog (the picture
button, or the ``/image`` command) gets an :guilabel:`AI image` tab. Describe
the picture in :guilabel:`Describe the image`, choose :guilabel:`Landscape`,
:guilabel:`Square` or :guilabel:`Portrait`, and click :guilabel:`Generate`. When
the preview looks right, add it like any uploaded picture. It is stored as a
normal attachment.

Good to know
============

- Review before you use: the model can be wrong, and the text it writes is yours
  once you insert or send it.
- The assistant only sees what you may see. The chatter draft reads the record
  and its thread with your own rights; if an administrator denied the AI access
  to that model, the draft is written from the conversation alone.
- Prompts are sent to your AI provider. Do not paste secrets or data you may not
  share with it.
