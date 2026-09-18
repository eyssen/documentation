=============
Store locator
=============

The *Website Store Locator* module (`website_store_locator`) publishes the company's physical stores
on a public page at `/stores`, with their address, contact details, opening hours and a short
description. The page is crawlable, so the stores can be found through search engines as well.

Configuration
=============

A store is an ordinary warehouse marked as a store. Go to :menuselection:`Inventory -->
Configuration --> Warehouses`, open the warehouse, and set:

- :guilabel:`Physical Store`: makes this warehouse appear on the store locator.
- :guilabel:`Visible on Website`: whether the store is actually published. A warehouse marked as a
  store is published automatically when it is created; existing warehouses stay unpublished until
  the checkbox is ticked, so that internal warehouses are never published by accident.
- :guilabel:`Website`: limits the store to one website when several websites are in use.
- :guilabel:`Store Image`: the photo shown on the store card.
- :guilabel:`Store Description`: a short translatable text shown on the card, for example the
  services offered at that location.
- :guilabel:`Opening Hours`: the working schedule describing when the store is open.

.. screenshot:: website-store_locator-warehouse-store
   :menu: Inventory ‣ Configuration ‣ Warehouses ‣ (warehouse)
   :shows: A warehouse form with the Physical Store and Visible on Website checkboxes enabled, the Store Image, the Store Description and the Opening Hours field.
   :highlight: The Physical Store and Visible on Website checkboxes (red frame).
   :data: Warehouse "Budapest store" with opening hours "Budapest store hours".
   :module: website_store_locator
   :notes: English UI, light theme, 1440px width.

The address and the phone number shown on the page come from the warehouse's address, so keep them
up to date on the warehouse itself.

.. _website/store_locator/opening-hours:

Opening hours
-------------

Opening hours are working schedules (:menuselection:`Settings --> Technical --> Working
Schedules`) marked with :guilabel:`Store Opening Hours`. Only schedules with that marker are offered
in the store's :guilabel:`Opening Hours` field, so the list is not cluttered with employee working
schedules.

Create one schedule per store — or one shared schedule for stores that open at the same times — and
enter the opening periods as its working hours. Exceptional closures (public holidays, stocktaking
days) are entered as time off on the schedule and are taken into account on the public page.

.. screenshot:: website-store_locator-opening-hours
   :menu: Settings ‣ Technical ‣ Working Schedules ‣ (schedule)
   :shows: A working schedule marked as Store Opening Hours, with its weekly opening periods and a time-off line for a public holiday.
   :highlight: The Store Opening Hours checkbox (red frame).
   :data: Schedule "Budapest store hours", open Monday to Saturday.
   :module: website_store_locator
   :notes: English UI, light theme, 1440px width.

The store locator page
======================

The published stores are listed at `/stores`, each as a card with its image, name, address, contact
details, description and opening hours. The page has an editable area above and below the list, so
an introduction, a map or a call-to-action block can be added with the :doc:`website editor
<web_design>`.

.. screenshot:: website-store_locator-page
   :menu: (website) ‣ /stores
   :shows: The public store locator page with the store cards, each showing the store image, name, address, opening hours and description.
   :highlight: One store card (red frame).
   :data: Three published stores.
   :module: website_store_locator
   :notes: English UI, light theme, 1440px width.

.. note::
   When :doc:`Click & Collect <../ecommerce/shipping>` is also in use, the same opening hours are
   shown on the store locator page and in the Click & Collect step of the checkout: both read the
   same field. Install the *Website Store Locator / Click & Collect bridge* module
   (`website_store_locator_collect`) to remove the duplicated :guilabel:`Opening Hours` field that
   would otherwise appear twice on the warehouse form.
