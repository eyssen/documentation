============
Translations
============

Your website is displayed in the language that matches your visitor’s browser. If the browser’s
language has not been installed and added to your website, the content is shown in the
:ref:`default language <translate/default-language>`. When additional languages are installed, users
can choose their preferred language using the :ref:`language selector <translate/language-selector>`.

The :ref:`Translate <translate/translate>` feature on your website allows automatic translation of
standard terms and provides a tool for manual content translation.

Install languages
=================

To allow translation of your website, you must first :doc:`install <../../../general/users/language>`
the required languages and add them to your website. To do so, go to :menuselection:`Website -->
Configuration --> Settings` and click :icon:`fa-arrow-right` :guilabel:`Install languages` in the
:guilabel:`Website Info` section. In the dialog box that opens, select the :guilabel:`Languages` you
want from the dropdown menu, tick the required :guilabel:`Websites to translate`, and
click :guilabel:`Add`.

To edit your website's languages, go to :menuselection:`Website -–> Configuration -–> Settings` and
add/remove the required languages in/from the :guilabel:`Languages` field in the
:guilabel:`Website info` section.

.. tip::
   Alternatively, once the languages have been installed, you can add them from the :ref:`language
   selector <translate/language-selector>`. You might then need to refresh your page to see the new
   language.

.. _translate/default-language:

Default language
----------------

When multiple languages are available on your website, you can set a default language to be used if
the visitor’s browser language is not available. To do so, go to :menuselection:`Website –->
Configuration -–> Settings`, and select a language in the :guilabel:`Default` field.

.. note::
   This field is only visible if multiple languages have been installed and added to your website.

.. _translate/language-selector:

Language selector
=================

Your website’s visitors can switch languages using the language selector, available by default in
the :guilabel:`Copyright` section at the bottom of the page. To edit the language selector menu:

#. Go to your website and click :guilabel:`Edit`;
#. Click the language selector available in the :guilabel:`Copyright` block and go to the
   :guilabel:`Copyright` section of the website builder;
#. Set the :guilabel:`Language Selector` field to either :guilabel:`Dropdown` or :guilabel:`Inline`.
   Click :guilabel:`None` if you do not want to display the  :guilabel:`Language selector`;

     .. screenshot:: website-translate-language-selector
        :menu: (website)
        :shows: The website header with the language selector drop-down menu open, listing the installed website languages.
        :highlight: The language selector (red frame).
        :data: Languages English and Hungarian installed.
        :module: website
        :notes: English UI, light theme, 1440px width.

#. Click :guilabel:`Save`.

.. tip::
  You can also add the :guilabel:`Language Selector` to the :guilabel:`Header` of your page. To do
  so, click the :guilabel:`Header` block and go to the :guilabel:`Navbar` section to edit the
  :guilabel:`Language Selector`.

.. _translate/translate:

Translate your website
======================

Select your desired language from the language selector to see your content in another language.
Then, click the :guilabel:`Translate` button in the top-right corner to manually activate the
translation mode so that you can translate what has not been translated automatically by Odoo.

Translated text strings are highlighted in green; text strings that were not translated
automatically are highlighted in yellow.

.. screenshot:: website-translate-translated-text
   :menu: (website) ‣ Edit ‣ Translate
   :shows: The website editor in translation mode, where the translatable texts are highlighted and the second language is selected in the top bar.
   :highlight: A highlighted translatable text block (red frame).
   :data: Translating a page into Hungarian.
   :module: website
   :notes: English UI, light theme, 1440px width.

In this mode, you can only translate text. To change the page's structure, you must edit the master
page, i.e., the page in the original language of the database. Any changes made to the master page
are automatically applied to all translated versions.

To replace the original text with the translation, click the block, edit its contents, and
:guilabel:`Save`.

.. note::
  When a website supports multiple languages, the core URL structure remains consistent across
  languages, while specific elements like product names or categories are translated. For example,
  `https://www.mywebsite.com/shop/product/my-product-1` is the English version of a product page,
  while `https://www.mywebsite.com/fr/shop/product/mon-produit-1` is the French version of the same
  page. The structure (/shop/product/) stays unchanged, but the translated elements (e.g., product
  name) adapt to the selected language.

.. tip::
  Once the desired language is installed, you can translate some items from the backend (e.g., the
  product's name in the product form). To do so, click the language code (e.g., :guilabel:`EN`) next
  to the text you want to translate and add the translation.

Content visibility by language
------------------------------

You can hide content (such as images or videos, for example) depending on the language. To do so:

#. Click :guilabel:`Edit` and select an element of your website;
#. Go to the :guilabel:`Text - Image` section and :guilabel:`Visibility`;
#. Click :guilabel:`No condition` and select :guilabel:`Conditionally` instead;
#. Go to :guilabel:`Languages` to configure the condition(s) to apply by selecting
   :guilabel:`Visible for` or :guilabel:`Hidden for`, and click :guilabel:`Choose a record` to
   decide which languages are impacted.

.. _website/translate/image-variants:

Language-specific images
------------------------

Images that contain text — banners, product sheets, infographics — usually need a different file per
language. The *Website Image Translation* module (`website_image_translation`) makes it possible to
attach a language variant to an image without touching the page itself: the page keeps pointing at
the original image, and the visitor is served the variant matching their language, falling back to
the original when no variant exists.

The variants are managed under :menuselection:`Website --> Configuration --> Image Language
Variants`, where each record links a :guilabel:`Source attachment` — the image used in the page — to
a :guilabel:`Language` and to the :guilabel:`Attachment` served for that language, optionally
limited to one :guilabel:`Website`.

.. screenshot:: website-translate-image-language-variants
   :menu: Website ‣ Configuration ‣ Image Language Variants
   :shows: The Image Language Variants list with the source attachment, the language, the variant attachment and the website columns.
   :highlight: The Language and variant attachment columns (red frame).
   :data: One banner image with a Hungarian and a German variant.
   :module: website_image_translation
   :notes: English UI, light theme, 1440px width.

This works for images placed with the website editor, for background images and for images from the
media library. Because the page HTML is unchanged, adding or removing a variant later does not
require editing the pages that use the image.

.. note::
   The menu is only visible to users in the *Editor and Designer* website group.

.. _website/translate/region-selector:

Region selector
---------------

On a webshop serving several countries, the language is only part of the choice: the country also
determines the prices, the currency and the taxes applied. The *Website Region Selector* module
(`website_region_selector`) replaces the plain language menu with a modal in which anonymous
visitors choose their :guilabel:`Language`, :guilabel:`Country` and :guilabel:`Currency`
(pricelist) in one step. The selected country also drives the fiscal position used for the cart, so
the prices shown include the right VAT.

Enable it per website in :menuselection:`Website --> Configuration --> Settings`:

- :guilabel:`Region Selector`: shows the selector on this website. Turn it off on websites that
  should not offer it, such as a B2B portal.
- :guilabel:`Replace the language menu`: replaces the native header language menu with the region
  selector button. The language stays selectable inside the modal, and the `hreflang` tags are kept
  for search engines.

.. screenshot:: website-translate-region-selector-settings
   :menu: Website ‣ Configuration ‣ Settings
   :shows: The Website settings page with the Region Selector and "Replace the language menu" options enabled.
   :highlight: The two region selector settings (red frame).
   :data: Website "My Website".
   :module: website_region_selector
   :notes: English UI, light theme, 1440px width, crop to the Website Info block.

Which countries are offered, and with which pricelists, is configured on the countries themselves
(:menuselection:`Settings --> Technical --> Countries`):

- :guilabel:`Available on the Website`: makes the country selectable in the region selector;
- :guilabel:`Website Pricelists`: the pricelists offered for this country. The first one, by
  pricelist sequence, is the default selection.

.. screenshot:: website-translate-region-selector-country
   :menu: Settings ‣ Technical ‣ Countries ‣ (country)
   :shows: A country form with "Available on the Website" enabled and two website pricelists selected.
   :highlight: The "Available on the Website" checkbox and the Website Pricelists field (red frame).
   :data: Country Hungary with the pricelists "Public (HUF)" and "Wholesale (EUR)".
   :module: website_region_selector
   :notes: English UI, light theme, 1440px width.

.. screenshot:: website-translate-region-selector-modal
   :menu: (website)
   :shows: The region selector modal opened on the website, with the language, country and currency choices and the confirmation button.
   :highlight: The country and currency choices (red frame).
   :data: Languages English and Hungarian, countries Hungary and Germany, two pricelists.
   :module: website_region_selector
   :notes: English UI, light theme, 1440px width.

.. note::
   - Logged-in users never see the selector: their language, pricelist and fiscal position come
     from their contact record.
   - With the **Theme Prime** theme, install the *Website Region Selector - Theme Prime* module
     (`website_region_selector_theme_prime`) as well, so that the selector button is rendered in
     that theme's header.
