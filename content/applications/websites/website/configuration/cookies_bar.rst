===========
Cookies bar
===========

**Cookies** are small text files sent to your device when you visit a website. They are processed
and stored by your browser and record visitor information like login details, preferences, and
browsing history. **Essential cookies** are necessary for the website to function, while
**optional cookies** are used to analyze behavior or display ads.

.. important::
   When the Google app or the Meta app is installed, the cookies bar is replaced by the **cookie
   consent banner** (:guilabel:`Accept all`, :guilabel:`Reject all`, :guilabel:`Customize`, consent
   categories, cookie list, and :guilabel:`Cookie settings` link) and its settings replace the
   :guilabel:`Cookies Bar` setting. See :doc:`/applications/websites/website/tracking/cookie_consent`.

Data protection laws require notifying visitors about data collection methods and purposes.
**Cookies bar** fulfill this obligation by informing visitors on their first visit and allowing them
to decide whether to store all or only essential cookies on their device.

.. note::
   - Cookies bars are required to obtain visitors' consent for optional cookies only. Consent is not
     required for essential cookies.

   - Odoo is compliant with `Google consent mode v2
     <https://support.google.com/tagmanager/answer/13695607>`_: the consent state is set to
     *denied* by default and updated to *granted* or *denied* according to the visitor's choice. In
     eYssen ERP, the :ref:`Google consent mode (advanced) <cookies-bar/consent-mode-advanced>`
     module also lets the Google tag load before the choice is made.

Configuration
=============

To add a cookies bar on your website, go to :menuselection:`Website --> Configuration -->
Settings` and enable :guilabel:`Cookies Bar` in the :guilabel:`Privacy` section. This activates
:guilabel:`Block tracking 3rd-party services` by default, including social media, video hosting
platforms, and Google services. Click :guilabel:`Add domains to the block list` to include other
external websites. These services remain blocked on your website until visitors accept optional
cookies.

.. note::
   Using third-party cookies without a cookies bar does not prevent them from being triggered. Only
   the presence of a cookie bar **and** the visitor’s refusal ensure that these cookies are blocked.

.. _cookies-bar/consent-mode-advanced:

Google consent mode (advanced)
==============================

With the cookies bar enabled, the standard behavior is to block the Google tag (`gtag.js`) until the
visitor accepts optional cookies, because `googletagmanager.com` and `google-analytics.com` are on
the block list of third-party services. As a result, the tag only loads on the **next** page after
the visitor accepted. Google Analytics 4 then loses the landing page, the `gclid` parameter of
Google Ads and the referrer of the first page, and the visit is reported as *Direct*.

The *Website: Google consent mode (advanced)* module (`eyssen_website_consent_mode`) fixes this by
removing these two domains, and only these two, from the block list.

.. rubric:: Set it up

#. Install the module from :menuselection:`Apps` (search for `eyssen_website_consent_mode`). It has
   no setting and no menu.
#. Go to :menuselection:`Website --> Configuration --> Settings`, enable :guilabel:`Cookies Bar`
   in the :guilabel:`Privacy` section, and enable :guilabel:`Google Analytics` in the
   :guilabel:`SEO` section with your :guilabel:`Measurement ID`
   (see :ref:`Google Analytics <analytics/google-analytics>`).
#. Click :guilabel:`Save`.

.. important::
   The module removes the two Google domains from the block list of every website that has a
   Google Analytics :guilabel:`Measurement ID`. It only has a visible effect when the cookies bar is
   enabled with :guilabel:`Block tracking 3rd-party services`, which is the default. Websites
   without a :guilabel:`Measurement ID` keep the standard behavior.

.. rubric:: How it behaves

- The Google tag loads on the first page, before the visitor answers the cookies bar. The consent
  default stays *denied* for analytics and advertising storage, so Google does not set analytics
  cookies until the visitor accepts.
- When the visitor accepts or refuses optional cookies, the cookies bar sends the consent update
  (*granted* or *denied*) on the **same page**, without a reload.
- The landing page, the `gclid` and the referrer of the first page reach Google Analytics 4.
- If you added `googletagmanager.com` or `google-analytics.com` yourself with :guilabel:`Add domains
  to the block list`, they stay blocked.

.. note::
   This is Google's *advanced* consent mode: while consent is denied, Google may receive cookieless
   pings from the visitor's browser. Check that this fits your data protection requirements and
   mention it in your :ref:`cookies policy <cookies-bar/policy>`.

.. rubric:: Check that it works

Open your website in a private browsing window and open the developer tools of your browser
(:kbd:`F12`), :guilabel:`Network` tab.

#. Reload the page, without answering the cookies bar. A request to `googletagmanager.com/gtag/js`
   must appear on this first page. Without the module, the script is rendered with the address
   `about:blank` and no request is made.
#. Click :guilabel:`I agree` or :guilabel:`Only essentials` in the cookies bar. In the browser
   console, the `dataLayer` object receives a `consent` `update` entry (*granted* or *denied*) on
   the same page, without a reload.

.. note::
   The module has no effect on other trackers: the other third-party services of the block list
   (social networks, video platforms, Google Maps, etc.) are still blocked until the visitor
   accepts optional cookies.

.. _cookies-bar/policy:

Cookies policy
==============

When you enable the cookies bar for your website, Odoo creates the **Cookie Policy** page
(`/cookie-policy`) containing a list of cookies set by default, with their purpose and examples.

.. spoiler:: Click here to preview the list of default cookies

   .. list-table::
      :header-rows: 1
      :stub-columns: 1

      * - Category
        - Role
        - Name
      * - Essential - Session & Security
        - Authenticate visitors, protect visitor data and allow the website to deliver the services
          visitors expects, such as maintaining the content of their cart, or allowing file uploads.
          The website will not work properly without these cookies.
        - session_id (Odoo)
      * - Essential - Preferences
        - Remember information about the preferred look or behavior of the website, such as the
          preferred language or region. The website will continue to function without these cookies,
          but the visitor’s experience may be affected.
        - frontend_lang (Odoo)
      * - Optional - Interaction History
        - Collect information about your interactions with the website, the pages you've seen, and
          any specific marketing campaign that brought you to the website. The website will work
          without these cookies, but some features or services may not perform optimally.
        - im_livechat_previous_operator (Odoo),
          utm_campaign (Odoo),
          utm_source (Odoo),
          utm_medium (Odoo)
      * - Optional - Advertising & Marketing
        - Make advertising more engaging to visitors and more valuable to publishers and advertisers,
          such as providing more relevant ads when you visit other websites that display ads or to
          improve reporting on ad campaign performance. Note that some third-party services may
          install additional cookies on your browser in order to identify you.
        - __gads (Google),
          __gac (Google)
      * - Optional - Analytics
        - Understand how visitors engage with the website, via Google Analytics. The website will
          still work without these cookies.
        - _ga (Google),
          _gat (Google),
          _gid (Google),
          _gac_* (Google)

.. note::
   It is not possible to let visitors customize or select which optional cookies they want to allow.

.. tip::
   You could add a link to this page in your website's footer, for example.

.. _cookies-bar/edit-policy-page:

Edit the Cookies policy page
----------------------------

To access it, click the :guilabel:`Cookie Policy` hyperlink in the cookies bar or open the page from
:menuselection:`Website --> Site --> Pages`.

To adapt the content of the page according to your needs, click the :guilabel:`Edit` button.

.. note::
   You have to list every cookie you added yourself on the `/cookie-policy` page including their
   name, role, category and duration.

.. tip::
   To check the duration of cookies, use your browser’s developer tools.

.. seealso::
   :doc:`Pages <../structure/pages>`

.. _cookies-bar/customization:

Customization
=============

To adapt the display of the cookies bar on your website, click :guilabel:`Edit` on the website
editor, go to the :guilabel:`Invisible Elements` section at the bottom of the panel, and click
:guilabel:`Cookies Bar`. You can modify the :guilabel:`Layout` and :guilabel:`Size` of the
cookies bar, and enable :guilabel:`Backdrop` to gray out the page in the background when the cookies
bar is displayed on the screen.

Click anywhere in the building block to further customize the appearance of the cookies bar using
:guilabel:`Block`, :guilabel:`Column` and/or :guilabel:`Inline Text` customization options.

To edit the contents of the cookies bar (i.e., the consent message), click directly in the building
block.
