=================================
Configure ICE servers with Twilio
=================================

Odoo Discuss uses WebRTC API and peer-to-peer connections for voice and video calls. If one of the
call attendees is behind a symmetric NAT, you need to configure an ICE server to establish a
connection to the call attendee. To set up an ICE server, first, create a Twilio account for video
calls, and then, connect that Twilio account to Odoo.

Create a Twilio account
=======================

First, go to `Twilio <https://www.twilio.com>`_ and click :guilabel:`Sign up` to create a new
Twilio account. Next, enter your name and email address, create a password, and accept Twilio's
terms of service. Then, click :guilabel:`Start your free trial`. Verify your email address with
Twilio, as per their instructions.

Next, enter your phone number into Twilio. Then, Twilio will send you an SMS text message
containing a verification code. Enter the verification code into Twilio to verify your phone
number.

After that, Twilio redirects to a welcome page. Use the following list to answer Twilio's
questions:

- For :guilabel:`Which Twilio product are you here to use?`, select :guilabel:`Video`.
- For :guilabel:`What do you plan to build with Twilio?`, select :guilabel:`Other`.
- For :guilabel:`How do you want to build with Twilio?`, select :guilabel:`With no code at all`.
- For :guilabel:`What is your goal today?`, select :guilabel:`3rd party integrations`.

.. screenshot:: productivity-ice-servers-twilio-welcome
   :menu: (Twilio console) ‣ Sign up
   :shows: The Twilio welcome page with the billing country selector and the "Get Started with Twilio" button.
   :data: Use a throw-away Twilio account.
   :module: mail
   :notes: English UI, light theme, 1440px width.

If necessary, change the billing country. Finally, click :guilabel:`Get Started with Twilio`.

Locate the Twilio Account SID and Auth Token
============================================

To locate the Account SID and Auth Token, go to the Twilio account dashboard. Then, click
:guilabel:`Develop` on the sidebar. In the :guilabel:`Account Info` section, locate the
:guilabel:`Account SID` and the :guilabel:`Auth Token`. Both of these are needed to connect Twilio
to Odoo.

.. screenshot:: productivity-ice-servers-twilio-credentials
   :menu: (Twilio console) ‣ Account Info
   :shows: The Account Info section of the Twilio console showing the Account SID and the Auth Token.
   :highlight: The Account SID and Auth Token (red frame).
   :data: Use throw-away credentials.
   :module: mail
   :notes: English UI, light theme, 1440px width.

Connect Twilio to Odoo
======================

Open the Odoo database and go to :menuselection:`Settings --> General Settings --> Discuss`. Check
the box next to :guilabel:`Use Twilio ICE servers` and enter the Twilio account's
:guilabel:`Account SID` and :guilabel:`Auth Token`. Finally, click :guilabel:`Save` to apply these
changes.

.. screenshot:: productivity-ice-servers-odoo-settings
   :menu: Settings ‣ General Settings ‣ Discuss
   :shows: The Discuss section of the General Settings with the "Use Twilio ICE servers" option enabled and the Account SID and Auth Token fields.
   :highlight: The "Use Twilio ICE servers" setting (red frame).
   :data: Use throw-away credentials.
   :module: mail
   :notes: English UI, light theme, 1440px width.

Define a list of custom ICE servers
===================================

This step is not required for the Twilio configuration. However, if Twilio is not configured or is
not working at any given moment, Odoo will fall back on the custom ICE servers list. The user must
define the list of custom ICE servers.

In :menuselection:`Settings --> General Settings --> Discuss`, click the :guilabel:`ICE Servers`
button under :guilabel:`Custom ICE server list`.

.. screenshot:: productivity-ice-servers-button
   :menu: Settings ‣ General Settings ‣ Discuss
   :shows: The Discuss section of the General Settings with the "ICE Servers" button.
   :highlight: The "ICE Servers" button (red frame).
   :module: mail
   :notes: English UI, light theme, 1440px width.

Odoo will redirect to the :guilabel:`ICE servers` page. Here you can define your own list of ICE
servers.

.. screenshot:: productivity-ice-servers-list
   :menu: Settings ‣ General Settings ‣ Discuss ‣ ICE Servers
   :shows: The ICE servers list with two custom server lines (URI, username, password).
   :data: Use throw-away server data.
   :module: mail
   :notes: English UI, light theme, 1440px width.

.. note::
   For on-premise instances of Odoo, the package `python3-gevent` is necessary for the Discuss
   module to run calls/video calls on Ubuntu (Linux) servers.
