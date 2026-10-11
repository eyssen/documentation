==============
Cookie consent
==============

Google and Meta may only measure a visitor or show personalized ads to a visitor who agreed. The
tracking base therefore extends the :doc:`cookies bar </applications/websites/website/configuration/cookies_bar>`
of the website with **consent categories**, remembers the version of your cookie policy, logs every
choice as proof of consent, and can hand the consent over to an **external consent management
platform** (CMP) instead.

Every tracking feature checks the consent of the visitor before it loads a script or sends an event.

.. important::
   The consent is only requested if the :guilabel:`Cookies Bar` is enabled in the Website settings
   (or if an external consent platform is used). **Without a cookies bar, the website considers that
   consent is handled elsewhere, and all categories are treated as granted.**

.. _tracking/consent/categories:

Consent categories
==================

Visitors can accept or refuse the cookies by category:

.. list-table::
   :header-rows: 1
   :widths: 20 45 35

   * - Category
     - Used for
     - Effect on the Google signals
   * - Necessary
     - Session, cart, language, and the cookie choice itself. Always on; visitors cannot disable it.
     - Security storage is always granted.
   * - Functional
     - Embedded content such as videos and maps, and remembered preferences.
     - Functionality storage and personalization storage.
   * - Analytics
     - Visit statistics: Google Analytics, Search Console links, GA4 Measurement Protocol.
     - Analytics storage.
   * - Marketing
     - Advertising: Google Ads, Meta Pixel, Conversions API, remarketing, Customer Match.
     - Ad storage, ad user data, and ad personalization.

No tracking script of an unaccepted category is loaded, and no server event of an unaccepted category
is sent.

Configure the cookies bar
=========================

Go to :menuselection:`Website --> Configuration --> Settings`. In the privacy section, enable
:guilabel:`Cookies Bar`. Right below it, the :guilabel:`Consent Categories` setting groups the options
of this page:

.. screenshot:: tracking-consent-settings
   :menu: Website ‣ Configuration ‣ Settings
   :shows: The privacy section of the Website settings: the Cookies Bar setting enabled and, right
      below it, the Consent Categories setting with Consent Source, Consent Categories, Cookie
      Policy Version, and Log Consents, and the Consent Log link.
   :highlight: The Consent Categories setting block (red frame).
   :data: Demo website "My Website", cookies bar enabled.
   :notes: English UI, light theme, 1440px width, crop to the privacy section.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Field
     - Description
   * - :guilabel:`Consent Source`
     - :guilabel:`Website cookies bar` (default): visitors choose in the cookies bar of the website.
       :guilabel:`External consent platform (CMP)`: the cookies bar is replaced by a consent
       platform such as Cookiebot, which provides the consent state to the trackers. See
       :ref:`tracking/consent/cmp`.
   * - :guilabel:`Consent Categories`
     - Shows a :guilabel:`Customize` button in the cookies bar so that visitors can choose the
       functional, analytics, and marketing cookies one by one. Only available with the website
       cookies bar. If disabled, the bar offers the standard choice between all optional cookies
       and essential cookies only.
   * - :guilabel:`Cookie Policy Version`
     - A short text, `1` by default. **Change it each time your cookie policy changes:** the
       visitors who consented to an older version are asked again and nothing is granted until they
       answer.
   * - :guilabel:`Log Consents`
     - Keeps a record of every choice (categories, policy version, date) as proof of consent. Enabled
       by default. See :ref:`tracking/consent/log`.

.. _tracking/consent/customize:

The Customize panel
-------------------

With :guilabel:`Consent Categories` enabled, the cookies bar shows a :guilabel:`Customize` button
next to the usual buttons. It opens a panel with one switch per category: :guilabel:`Necessary`
(always on), :guilabel:`Functional`, :guilabel:`Analytics`, and :guilabel:`Marketing`. A visitor
chooses the categories and clicks :guilabel:`Save my choices`. The choice is stored in the cookie of
the cookies bar, together with the policy version.

.. screenshot:: tracking-consent-customize-panel
   :menu: (Website frontend) ‣ Cookies bar
   :shows: The cookies bar of the website with the Customize panel open: four switches (Necessary
      on and locked, Functional, Analytics, Marketing) each with a one-line description, and the
      Save my choices button.
   :highlight: The Customize panel (red frame).
   :data: Demo website with the default cookies bar text.
   :notes: English UI, light theme, 1440px width, crop to the bottom of the page.

A visitor who clicks the standard buttons instead gets the matching shortcut: accepting all optional
cookies grants every category, and keeping only the essential cookies refuses functional, analytics,
and marketing.

.. note::
   Visitors can change their mind at any time: the cookies bar is shown again when the visitor
   removes the cookie of the website in the browser, or when you change the :guilabel:`Cookie
   Policy Version`.

.. _tracking/consent/cmp:

External consent platform (CMP)
===============================

If you already use a consent management platform, let it collect the consent and hand the result to
Odoo. Set :guilabel:`Consent Source` to :guilabel:`External consent platform (CMP)`: the cookies bar
of the website is hidden, and the following fields appear.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Field
     - Description
   * - :guilabel:`Consent Platform`
     - :guilabel:`Cookiebot`, :guilabel:`Usercentrics`, :guilabel:`Complianz`, or
       :guilabel:`Custom (JavaScript event)`.
   * - :guilabel:`CMP Script`
     - The script tag(s) of the platform, copied from its administration. They are inserted at the
       top of the head of every page. Leave it empty if the platform is loaded another way, for
       example through Google Tag Manager.

Odoo reads the choice of the visitor from the platform and maps its categories to the four
categories above (for example, the *Preferences* category of Cookiebot to :guilabel:`Functional`,
*Statistics* to :guilabel:`Analytics`, and *Marketing* to :guilabel:`Marketing`). Each time the
visitor changes the choice, the tracking tags are updated.

.. rubric:: Custom platform

Choose :guilabel:`Custom (JavaScript event)` if your platform is not in the list. From your consent
tool, dispatch this browser event whenever the visitor makes or changes a choice:

.. code-block:: javascript

   window.dispatchEvent(new CustomEvent("website_tracking_consent", {
       detail: {functional: true, analytics: true, marketing: false}
   }));

.. tip::
   With a consent platform, the Google tags load at once with all the signals denied (in the default
   *Advanced* :doc:`consent mode </applications/websites/google/consent_mode>`), and the platform's
   choice updates them. Set :guilabel:`Wait for Update (ms)` in the Google settings if your platform
   needs a moment to answer.

.. _tracking/consent/log:

Consent log
===========

Go to :menuselection:`Website --> Configuration --> Tracking & Consent --> Consent Log` (or click
:guilabel:`Consent Log` in the Website settings). Every choice made in the cookies bar or in the
consent platform is a line, which cannot be edited:

- :guilabel:`Date`, :guilabel:`Website` (with several websites), and the :guilabel:`Consent ID`, a
  random identifier stored in the visitor's consent cookie.
- :guilabel:`Source`: :guilabel:`Cookies bar` or :guilabel:`Consent platform`.
- :guilabel:`Functional`, :guilabel:`Analytics`, :guilabel:`Marketing`: what the visitor accepted.
- :guilabel:`Policy Version`, the :guilabel:`Page` where the choice was made, the truncated IP
  address (the last part is removed), and the contact if the visitor was logged in.

Use the filters :guilabel:`Marketing Granted`, :guilabel:`Analytics Granted`, and :guilabel:`All
Refused`, and group the lines by :guilabel:`Policy Version` or :guilabel:`Day`. To answer a data
subject's request, search by :guilabel:`Consent ID` or contact.

Consent log lines are deleted automatically after 36 months. A choice that is identical to the
previous choice of the same visitor session is not logged again.

.. _tracking/consent/retention:

Retention and debug settings
============================

The :guilabel:`Tracking` block of :menuselection:`Website --> Configuration --> Settings` contains the
:guilabel:`Tracking Debug Mode` setting and the retention options:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Field
     - Description
   * - :guilabel:`Tracking Debug Mode`
     - Logs every tracking event and the data sent to each provider in the **browser console**, and
       in the server log. Disable it in production.
   * - :guilabel:`Customer Name Order`
     - How the name of a customer is split into first and last name when sent to the advertising
       platforms: :guilabel:`First name, Last name` or :guilabel:`Last name, First name` (useful
       for Hungarian names, for instance).
   * - :guilabel:`Keep Sent Events (days)`
     - Sent, failed, and discarded :doc:`server events <server_events>` are deleted after this
       delay. `30` days by default. Events that are still waiting to be sent are never deleted.
   * - :guilabel:`Keep Visitor Identifiers (days)`
     - The IP address, the browser data, and the ad click identifiers stored on orders and leads
       are cleared after this delay. `90` days by default, which is the longest period during
       which the ad platforms accept an offline conversion for a click.

A scheduled action runs every day to apply these delays.

.. seealso::
   - :doc:`privacy`
   - :doc:`/applications/websites/website/configuration/cookies_bar`
   - :doc:`/applications/websites/google/consent_mode`
