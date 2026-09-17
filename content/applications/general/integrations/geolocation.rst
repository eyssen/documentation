===========
Geolocation
===========

The *Geo Localization* feature computes the geographic coordinates (latitude and longitude) of
contacts from their address.

.. screenshot:: general-geolocation-partner-tab
   :menu: Contacts ‣ (a contact) ‣ Partner Assignment tab
   :shows: The Geolocation group of a contact with the latitude/longitude values, the "Geo Location" date and the "Compute based on address" button.
   :highlight: The "Compute based on address" button.
   :data: Demo contact with a full address.
   :module: base_geolocalize
   :notes: English UI, crop to the tab.

To use the feature, open the :guilabel:`Settings` app, and, under the :guilabel:`Integrations`,
section, activate :guilabel:`Geo Localization`. Then, choose between using the OpenStreetMap or
Google Places API.

Once the feature is enabled, open a contact, go to the :guilabel:`Partner Assignment` tab, and click
:guilabel:`Compute based on address` to compute the contact's coordinates. The coordinates can be
used by other apps and modules, e.g., to display contacts on a map.

**OpenStreetMap**

OpenStreetMap is a free, open geographic database updated and maintained by volunteers. To use it,
select :guilabel:`Open Street Map`.

  .. important::
     OpenStreetMap might not always be accurate. You can `join the OpenStreetMap community
     <https://www.openstreetmap.org/fixthemap>`_ to fix any issues encountered.

**Google Places API map**

The Google Places API map provides detailed info on places, businesses, and points of interest. It
supports location-based features like search, navigation, and recommendations.

.. important::
   Using the Google Places API could require `payment to Google
   <https://mapsplatform.google.com/pricing/>`_.

To use it, select :guilabel:`Google Place Map` and enter your :ref:`API Key
<address_autocomplete/generate_api_key>`.

.. screenshot:: general-geolocation-google-key
   :menu: Settings ‣ General Settings ‣ Integrations
   :shows: The "Geo Localization" setting with "Google Place Map" selected and the API Key field.
   :highlight: The API Key field.
   :module: base_geolocalize
   :notes: English UI, crop to the setting; blur the key.

.. seealso::
   :doc:`/applications/websites/website/configuration/address_autocomplete`
