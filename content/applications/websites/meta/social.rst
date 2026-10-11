======================================
Facebook and Instagram inbox and posts
======================================

The **Meta Social** feature brings the conversations of your Facebook pages and Instagram professional
accounts into **Discuss**, and lets you publish posts on them from Odoo. Your team answers the
customers who write on Messenger or Instagram without leaving Odoo, and plans the posts of all the
accounts in one place.

.. important::
   This feature is not installed automatically. Install *Meta Social: Facebook & Instagram Inbox
   and Posts* from :menuselection:`Apps`. It needs the :doc:`Meta connection <connection>` and the
   :ref:`Meta webhooks <meta/webhooks>`, with the app secret.

Load the accounts
=================

#. In :menuselection:`Meta --> Configuration --> Settings`, in the :guilabel:`Pages and Instagram
   Accounts` setting, click :guilabel:`Load Accounts`. Odoo reads the Facebook pages that the
   Meta connection manages, and the Instagram professional accounts linked to these pages.
#. Click :guilabel:`Accounts` (or open :menuselection:`Meta --> Configuration --> Facebook & Instagram
   Accounts`) to see them. The number of accounts is displayed next to the buttons.

.. screenshot:: meta-social-accounts
   :menu: Meta ‣ Configuration ‣ Facebook & Instagram Accounts
   :shows: The list of the Facebook and Instagram accounts with the Load Accounts and Subscribe to
      Messages buttons and the Inbox and Publishing toggles.
   :highlight: The Inbox and Publishing toggle columns (red frame).
   :data: One Facebook page and its Instagram account.
   :notes: English UI, light theme, 1440px width.

For each account, switch on what you need:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Setting
     - Description
   * - :guilabel:`Inbox`
     - Receive the messages of the account in Discuss and answer them from Odoo. Select the
       :guilabel:`Responsible Users`: they are the members of the conversations. At least one is
       required. Click :guilabel:`Subscribe to Messages` so that Meta sends the messages to your
       database.
   * - :guilabel:`Human Agent Tag`
     - Allows to answer up to seven days after the last message of the customer. Enable it only if
       your Meta app is approved for this feature.
   * - :guilabel:`Publishing`
     - Publish posts from Odoo on this account.
   * - :guilabel:`Website`
     - The website whose address is used for the public image links sent to Instagram.

Inbox
=====

Everybody who writes to your page or to your Instagram account becomes a **contact** of
:menuselection:`Meta --> Contacts`, with their name and picture when they allow it, and has **one
conversation** in Discuss with the responsible users.

- Texts, images, videos, audio, files, stickers, reactions, buttons, and shared posts are posted in
  the conversation.
- Write your answer in the conversation: Odoo sends it to Messenger or Instagram (texts and images).
- Meta only allows to answer **within 24 hours** after the last message of the customer (seven days
  with the human agent tag). After this window, the answer stays in the conversation but is not
  delivered, and the error is displayed.
- Open a contact to see its messages, their direction, and the delivery errors, or click
  :guilabel:`Open Conversation`.

.. screenshot:: meta-social-conversation
   :menu: Discuss ‣ (a Messenger conversation)
   :shows: A Discuss conversation with an Instagram contact: the message of the customer with an
      image and the reply of an agent.
   :highlight: The conversation header with the name of the contact (red frame).
   :data: Fictitious customer and messages.
   :notes: English UI, light theme, 1440px width.

Publish posts
=============

Go to :menuselection:`Meta --> Posts` (kanban, list, and calendar views), and click :guilabel:`New`:

#. Write the message, add a :guilabel:`Link` (Instagram does not make links clickable), and up to
   **10 images**. Instagram needs at least one image; several images make a carousel.
#. Select the :guilabel:`Accounts`: one or several pages and Instagram accounts that have
   :guilabel:`Publishing` enabled.
#. Click :guilabel:`Publish Now`, or choose a :guilabel:`Scheduled Date` and click
   :guilabel:`Schedule`. A scheduled action publishes the scheduled posts every 15 minutes.

The :guilabel:`Results` tab lists, for each account, the status, the ID, the link of the published
post, and the error if any. If some accounts failed, fix the problem and click :guilabel:`Retry
Failed Accounts`. Click :guilabel:`Back to Draft` to modify a scheduled post.

The statuses of a post are :guilabel:`Draft`, :guilabel:`Scheduled`, :guilabel:`Posting`,
:guilabel:`Posted`, and :guilabel:`Error`.

.. note::
   The messages and the posts are not related to the cookie consent: they are the communication between
   your company and the people who contacted you. The data of the contacts (names, user names, messages)
   are stored in Odoo; mention it in your privacy policy.

.. seealso::
   - :doc:`connection`
   - :doc:`whatsapp`
