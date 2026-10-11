============
Consent mode
============

*Google Consent Mode v2* tells the Google tags what the visitor allowed, so that they adapt their
behavior. It is required for the audiences and measurement of Google Ads in the European Economic
Area. The Google app sends the seven consent signals of Consent Mode v2 and updates them when the
visitor makes a choice in the :doc:`cookies bar or consent platform
</applications/websites/website/tracking/cookie_consent>`:

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Signal
     - Granted when the visitor accepts…
   * - `ad_storage`, `ad_user_data`, `ad_personalization`
     - the **marketing** cookies
   * - `analytics_storage`
     - the **analytics** cookies
   * - `functionality_storage`, `personalization_storage`
     - the **functional** cookies
   * - `security_storage`
     - always granted (necessary cookies)

Before the visitor chooses, the signals have the *default* values of the :ref:`regional defaults
<google/consent/defaults>`. A returning visitor's choice is applied **before** the first page view
is sent, so that it is not counted as a cookieless ping.

.. _google/consent/mode:

Advanced or basic mode
======================

In the :guilabel:`Consent Mode` block of :menuselection:`Google --> Configuration --> Settings`, the
:guilabel:`Consent Mode v2` setting offers two modes:

:guilabel:`Advanced: load the tags at once, cookieless pings until consent`
   The Google tags load on the first page with every signal denied. Until the visitor consents,
   Google receives cookieless pings without cookies or identifiers, which it uses to **model**
   conversions. This is the recommended mode: the landing page, the referrer, and the campaign of the
   first visit are not lost.

:guilabel:`Basic: load the tags only after consent`
   No Google script is loaded before the visitor accepts analytics or marketing cookies. There is
   no modeling, and the first page of the visit is lost for Google Analytics.

:guilabel:`Wait for Update (ms)` (`500` by default) is the time the tags wait for an answer of an
external consent platform before sending the first hits. Increase it if your platform answers slowly.

.. important::
   Whatever the mode, a Google tag is never given more than the visitor allowed: the tags and
   the consent signals are updated at each choice.

Privacy options
===============

In the :guilabel:`Privacy Options` setting:

- :guilabel:`Redact Ads Data` (enabled by default): when advertising storage is denied, ad click
  identifiers are removed from the requests sent to Google.
- :guilabel:`URL Passthrough`: when storage is denied, the ad click and session identifiers are
  passed in the links of the website instead of cookies, so that the conversions of a visit that
  spans several pages can still be attributed. The identifiers appear in the address of the pages.

.. _google/consent/defaults:

Default consent per region
==========================

Click :guilabel:`Default Consent per Region` in the :guilabel:`Consent Mode v2` setting, or go to
:menuselection:`Google --> Configuration --> Consent Defaults`. Each line defines the state of the
seven signals before the visitor chooses:

.. list-table::
   :header-rows: 1
   :widths: 25 75

   * - Field
     - Description
   * - :guilabel:`Name`
     - A label for the line.
   * - :guilabel:`Website`
     - Leave empty to apply the line to every website.
   * - :guilabel:`Regions`
     - ISO 3166-1 country codes and ISO 3166-2 subdivisions, separated by commas, for example
       `ES, HU, US-CA`. Leave empty for **all the other regions**.
   * - :guilabel:`Ad Storage`, :guilabel:`Ad User Data`, :guilabel:`Ad Personalization`,
       :guilabel:`Analytics Storage`, :guilabel:`Functionality Storage`, :guilabel:`Personalization
       Storage`, :guilabel:`Security Storage`
     - :guilabel:`Granted` or :guilabel:`Denied`.

The default line :guilabel:`Denied until the visitor consents` (without region) is provided: it denies
everything except the security storage. Google applies the **most specific** line: a subdivision
(`US-CA`) before a country (`ES`) before the line without region. Lines of a given website come
before the lines shared by all websites.

.. screenshot:: google-consent-defaults
   :menu: Google ‣ Configuration ‣ Consent Defaults
   :shows: The editable list of consent defaults: the default line without region and a line for
      `US` with some signals granted, the signal columns showing Granted/Denied.
   :highlight: The Regions column (red frame).
   :data: Lines "Denied until the visitor consents" (no region) and "United States" (region US).
   :notes: English UI, light theme, 1440px width.

.. tip::
   Keep all the signals denied for the European Economic Area, the United Kingdom, and Switzerland.
   A more permissive default for other regions, such as `US`, is a legal choice that you make.

.. seealso::
   - :doc:`/applications/websites/website/tracking/cookie_consent`
   - `Google documentation on consent mode <https://support.google.com/tagmanager/answer/13695607>`_
