=============
Privacy notes
=============

This page summarizes what the Google and Meta apps send, to whom, and under which conditions. It
helps you complete your privacy policy and your records of processing. It is not legal advice:
check the requirements that apply to your company with your data protection officer.

Consent first
=============

- A tracking script (Google tag, Google Tag Manager, Meta Pixel) is loaded, and a server event
  is sent, only if the matching :doc:`consent category <cookie_consent>` is granted:
  **analytics** for Google Analytics events, **marketing** for Google Ads, the Meta Pixel, the
  Conversions API, remarketing, and Customer Match.
- Without a cookies bar and without an external consent platform, all categories are considered
  granted: enable one of them.
- The consent state is checked again on every page. Visitors who consented to an older
  :guilabel:`Cookie Policy Version` are asked again.
- No tracking is done in the website editor, in the translation mode, or for the website
  designers while they edit the website.
- With the Google :doc:`consent mode </applications/websites/google/consent_mode>` in
  *Advanced* mode, the Google tags load before the answer with every signal denied and send
  **cookieless pings**, which Google uses to model conversions. In *Basic* mode, nothing is loaded
  before consent. With :guilabel:`Load Before Consent`, the Meta Pixel does the same with its
  consent revoked: enable it only if your legal basis allows it.

What is sent
============

.. list-table::
   :header-rows: 1
   :widths: 24 76

   * - Data
     - Where it goes and how
   * - Page views, product views, cart, checkout steps
     - From the browser, to Google (gtag or the Google Tag Manager data layer) and to Meta (pixel),
       with the product identifier, name, price, and quantity.
   * - Purchases, refunds, leads, sign-ups
     - From the browser and/or from the server. The same :guilabel:`Event ID` is used on both sides
       so that the platform counts the event once.
   * - Customer data (email, phone, name, address)
     - Only for :guilabel:`Enhanced Conversions`, :guilabel:`Advanced Matching`, the Conversions
       API, Customer Match, and offline conversions. It is **normalized (trimmed, lowercased,
       phone numbers in international format) and hashed with SHA-256** before leaving the server;
       Odoo never sends the email address or the phone number in clear text. Enhanced conversions
       and advanced matching also require marketing consent.
   * - Customer identifier
     - The :guilabel:`GA4 User ID` is a keyed hash of the customer, never the email address. The
       Meta external identifier is hashed.
   * - Browser data
     - The Conversions API requires the **IP address and the user agent** of the visitor, and the
       Meta identifiers `fbp` and `fbc`: they are sent as they are, as Meta requires. The GA4 client
       and session identifiers and the Google click identifiers (`gclid`, `gbraid`, `wbraid`) are
       sent with the server events of Google.
   * - Customer lists
     - :guilabel:`Customer Match` sends hashed email addresses, phone numbers, and addresses of the
       contacts selected by the filter, and removes the contacts that leave it.
   * - Never sent
     - Passwords, payment card data, and bank details are not part of any event.

Data stored in Odoo
===================

- **Orders and leads** created from a tracked visit store the Google and Meta click identifiers, the
  GA4 client identifier, the IP address, the user agent, and the consent state at the time (in the
  :guilabel:`Ad Tracking` tab, visible in developer mode). They are needed for the offline
  conversions and are **cleared after** :guilabel:`Keep Visitor Identifiers (days)` (90 days by
  default). The consent snapshot is kept.
- **Server events** keep a copy of what was sent for :guilabel:`Keep Sent Events (days)` (30 days
  by default).
- The **consent log** keeps the choices for 36 months, with a truncated IP address (the last part
  is removed).

Special cases
=============

Store sales (point of sale)
   No cookie consent can be collected at the counter. Reporting store purchases to Google
   (Measurement Protocol) or Meta (Conversions API) is a separate setting for each provider and
   must have a legal basis that you determine. It only concerns customers recorded on the order
   with an email address or a phone number.

Lead Ads
   The person who fills in a Meta lead form gave the consent in the Meta form. The lead events
   are reported to Meta with the Meta lead ID without a cookie consent.

Customer Match
   The audience filter must only contain customers who agreed to receive marketing and
   personalized advertising. You confirm it with :guilabel:`Customers Consented`; the members are
   sent with the consent signals granted.

Limited Data Use
   For the US state privacy laws, :guilabel:`Limited Data Use` flags the Meta server events.

Google Tag Manager
   The tags that you create in a GTM container are under your responsibility: check what they send.

Third-party domains
   Scripts of Google and Meta that Odoo manages itself are removed from the blocked third-party
   list of the cookies bar, so that they are loaded after consent and not blanked. Other embedded
   services stay blocked until the visitor accepts the :guilabel:`Functional` cookies.

.. seealso::
   - :doc:`cookie_consent`
   - :doc:`/applications/websites/website/configuration/cookies_bar`
