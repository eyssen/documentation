==============
Cookie consent
==============

Google and Meta may only measure a visitor or show personalized ads to a visitor who agreed. The
tracking base therefore replaces the cookies bar of the website with a **consent banner** in the
form visitors know from most websites: :guilabel:`Accept all`, :guilabel:`Reject all`, and
:guilabel:`Customize` on the first screen, a preferences dialog with one switch per category and the
list of the cookies, and a :guilabel:`Cookie settings` link to change or withdraw the choice at any
time. It remembers the version of your cookie policy, logs every choice as proof of consent, and can
hand the consent over to an **external consent management platform** (CMP) instead.

Every tracking feature checks the consent of the visitor before it loads a script or sends an event.

.. important::
   The consent is only requested if :guilabel:`Cookie Consent` is enabled in the Website settings.
   **Without it, the website considers that consent is handled elsewhere, and all categories are
   treated as granted.**

.. _tracking/consent/categories:

Consent categories
==================

Visitors accept or refuse the cookies by category:

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
     - Embedded content such as videos and maps, the live chat, the campaign cookies (UTM) and
       features that remember choices, such as recently viewed products.
     - Functionality storage and personalization storage.
   * - Analytics
     - Visit statistics: Google Analytics, Search Console links, GA4 Measurement Protocol.
     - Analytics storage.
   * - Marketing
     - Advertising: Google Ads, Meta Pixel, Conversions API, remarketing, Customer Match.
     - Ad storage, ad user data, and ad personalization.

No tracking script of an unaccepted category is loaded, and no server event of an unaccepted category
is sent. The optional cookies of the website itself (embedded content, campaign and live chat cookies)
follow the :guilabel:`Functional` category.

.. _tracking/consent/settings:

Configure the consent banner
============================

Go to :menuselection:`Website --> Configuration --> Settings` and enable :guilabel:`Cookie Consent`
in the :guilabel:`Privacy` section. This setting replaces the standard :guilabel:`Cookies Bar` setting
of the website, which is no longer shown.

.. screenshot:: tracking-consent-settings
   :menu: Website ‣ Configuration ‣ Settings
   :shows: The privacy section of the Website settings: the Cookie Consent setting enabled, with
      Consent Source, Banner Layout, Banner Title, Banner Text, Cookie Policy Page, Floating
      Settings Button, Ask Again After (months), Cookie Policy Version, Log Consents and Block
      Third-Party Content, and the Cookie List, Consent Log, Blocked Third-Party Domains and Recreate
      Cookie Policy Page links.
   :highlight: The Cookie Consent setting block (red frame).
   :data: Demo website "My Website", Cookie Consent enabled.
   :notes: English UI, light theme, 1440px width, crop to the privacy section.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Field
     - Description
   * - :guilabel:`Consent Source`
     - :guilabel:`Consent banner of this website` (default): visitors choose in the banner of the
       website. :guilabel:`External consent platform (CMP)`: the banner is replaced by a consent
       platform such as Cookiebot, which provides the consent state to the trackers. See
       :ref:`tracking/consent/cmp`.
   * - :guilabel:`Banner Layout`
     - :guilabel:`Bar at the bottom` (default), :guilabel:`Box, bottom left`, :guilabel:`Box, bottom
       right`, or :guilabel:`Popup in the center` (the page is dimmed until the visitor chooses).
       On the cookie policy page, the popup is shown as a bar so that the policy stays readable.
   * - :guilabel:`Banner Title`, :guilabel:`Banner Text`
     - Your own title and text. Leave them empty to use the default ones (*We value your privacy*
       and a short explanation), which are translated into the languages of the website. Your own
       texts can be translated with the translation button of the fields.
   * - :guilabel:`Cookie Policy Page`
     - The page linked from the banner and the dialog. Leave it empty to use `/cookie-policy`.
   * - :guilabel:`Floating Settings Button`
     - Once the visitor has chosen, a small round cookie button stays in the bottom left corner of
       the page. It opens the preferences dialog. Enabled by default. A :guilabel:`Cookie settings`
       link is added to the footer in any case.
   * - :guilabel:`Ask Again After (months)`
     - How long the choice of a visitor is kept. `12` months by default; after this delay the
       banner is shown again.
   * - :guilabel:`Cookie Policy Version`
     - A short text, `1` by default. **Change it each time your cookie policy changes:** the
       visitors who consented to another version are asked again and nothing is granted until they
       answer.
   * - :guilabel:`Log Consents`
     - Keeps a record of every choice (categories, policy version, date) as proof of consent. Enabled
       by default. See :ref:`tracking/consent/log`.
   * - :guilabel:`Block Third-Party Content`
     - Keeps embedded videos, maps, and other third-party content blocked until the visitor accepts
       the functional cookies. In their place, visitors see a notice; clicking it opens the
       preferences dialog. Click :guilabel:`Blocked Third-Party Domains` to add domains to the list.

The links below the fields open the :ref:`cookie list <tracking/consent/cookie_list>`, the
:ref:`consent log <tracking/consent/log>`, the list of blocked domains, and recreate the
:ref:`cookie policy page <tracking/consent/policy_page>`.

.. tip::
   The banner uses the fonts and colors of your theme; its buttons take the text color of the banner,
   so they always stand out. Edit its texts in the settings, not in the website editor.

.. _tracking/consent/banner:

What visitors see
=================

The banner
----------

A visitor who has not chosen yet sees the banner with three buttons of the same size:
:guilabel:`Customize`, :guilabel:`Reject all`, and :guilabel:`Accept all`, and a link to the cookie
policy. Rejecting is as easy as accepting, as the European data protection authorities require.

- :guilabel:`Accept all` grants every category.
- :guilabel:`Reject all` keeps the necessary cookies only.
- :guilabel:`Customize` opens the preferences dialog.

Until the visitor answers, nothing optional is used: continuing to browse or scrolling does not count
as consent.

.. screenshot:: tracking-consent-banner
   :menu: (Website frontend)
   :shows: The consent banner at the bottom of a website page: the title "We value your privacy", the
      short text with the Cookie policy link, and the Customize, Reject all and Accept all buttons.
   :highlight: The three buttons (red frame).
   :data: Demo website, Banner Layout "Bar at the bottom", default texts.
   :notes: English UI, light theme, 1440px width, crop to the bottom of the page.

.. _tracking/consent/customize:

The preferences dialog
----------------------

The dialog lists the categories: :guilabel:`Necessary` (always on), :guilabel:`Functional`,
:guilabel:`Analytics`, and :guilabel:`Marketing`, each with a switch, a short description and, when
the visitor unfolds it, the cookies of the category with their provider, duration, and purpose. The
visitor clicks :guilabel:`Save my choices`, or :guilabel:`Reject all` or :guilabel:`Accept all`.

.. screenshot:: tracking-consent-preferences
   :menu: (Website frontend) ‣ Customize
   :shows: The Cookie preferences dialog: the four categories with their switches (Necessary "Always
      on"), the Marketing category unfolded with its cookie table (Cookie, Provider, Duration,
      Purpose), and the Reject all, Save my choices and Accept all buttons.
   :highlight: The cookie table of the unfolded category (red frame).
   :data: Demo website with Google Analytics, Google Ads and the Meta Pixel enabled.
   :notes: English UI, light theme, 1440px width.

The choice is stored in the consent cookie of the website, with the policy version and the date.

Change or withdraw the choice
-----------------------------

Visitors can open the preferences dialog again at any time:

- with the floating cookie button in the bottom left corner (if :guilabel:`Floating Settings Button`
  is enabled);
- with the :guilabel:`Cookie policy · Cookie settings` links added to the copyright line of the
  footer;
- with the :guilabel:`Change my cookie settings` button of the cookie policy page;
- by clicking the notice shown in place of blocked embedded content.

When a visitor withdraws a category, the cookies of that category listed in the
:ref:`cookie list <tracking/consent/cookie_list>` are deleted from the browser, and the tracking tags
stop using them.

.. tip::
   To add your own link to the cookie settings, for example in a footer column or a menu, point it
   to `#cookie-settings`.

.. _tracking/consent/cookie_list:

Cookie list
===========

Go to :menuselection:`Website --> Configuration --> Tracking & Consent --> Cookies` (or click
:guilabel:`Cookie List` in the settings). The list feeds the preferences dialog and the cookie policy
page.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Field
     - Description
   * - :guilabel:`Cookie`
     - The name of the cookie. Use `*` for names that vary, for example `_ga_*`.
   * - :guilabel:`Provider`
     - Who sets the cookie: *This website* or a third party, such as *Google Analytics*.
   * - :guilabel:`Category`
     - :guilabel:`Necessary`, :guilabel:`Functional`, :guilabel:`Analytics`, or
       :guilabel:`Marketing`.
   * - :guilabel:`Duration`
     - How long the cookie is kept, for example *2 years*. The duration of the consent cookie follows
       :guilabel:`Ask Again After (months)`.
   * - :guilabel:`Purpose`
     - What the cookie is used for, in a sentence visitors understand.
   * - :guilabel:`Website`
     - Leave it empty to list the cookie on every website.

The cookies of the website and of the installed features are listed from the start: the session,
language and consent cookies, the campaign cookies, the live chat cookies (with a live chat channel
on the website), the recently viewed products (eCommerce), Google Analytics (`_ga`, `_ga_*`), Google
Ads (`_gcl_au`, `_gcl_aw`), and the Meta Pixel (`_fbp`, `_fbc`). A cookie of a feature is only shown
while the feature is enabled on the website; with Google Tag Manager, the Google Analytics and Google
Ads cookies are both listed.

Add the cookies of the other services you embed in your pages (a video platform, a chat, a booking
widget) with their category, so that visitors see them and they are deleted when the category is
withdrawn. All the texts can be translated.

.. _tracking/consent/policy_page:

Cookie policy page
==================

When you enable :guilabel:`Cookie Consent`, a **Cookie Policy** page is created at `/cookie-policy`.
Its first part explains what cookies are and how visitors choose; you can edit it in the website
editor like any page. Below it, the page lists the cookies of the website by category, from the
:ref:`cookie list <tracking/consent/cookie_list>`, and shows a :guilabel:`Change my cookie settings`
button. This part is always up to date and is not editable.

If the website already had a cookie policy page, click :guilabel:`Recreate Cookie Policy Page` in the
settings to replace it with the new one. The changes made to the old page are lost.

.. note::
   If your cookie policy lives on another page, set it in :guilabel:`Cookie Policy Page`.

.. _tracking/consent/cmp:

External consent platform (CMP)
===============================

If you already use a consent management platform, let it collect the consent and hand the result to
Odoo. Set :guilabel:`Consent Source` to :guilabel:`External consent platform (CMP)`: the consent
banner of the website is hidden, and the following fields appear.

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
visitor changes the choice, the tracking tags are updated, and embedded content follows the
functional choice.

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
:guilabel:`Consent Log` in the Website settings). Every choice made in the consent banner or in the
consent platform is a line, which cannot be edited:

- :guilabel:`Date`, :guilabel:`Website` (with several websites), and the :guilabel:`Consent ID`, a
  random identifier stored in the visitor's consent cookie.
- :guilabel:`Source`: :guilabel:`Consent banner` or :guilabel:`Consent platform`.
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
   - :doc:`/applications/websites/google/consent_mode`
