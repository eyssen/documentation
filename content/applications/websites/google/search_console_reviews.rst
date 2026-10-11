===================================
Search Console and Business Profile
===================================

Two Google products can be read in Odoo, next to your website statistics: the performance of your
pages in Google Search, and the reviews of your business on Google Maps. Both require a
:doc:`Google connection <connection>`.

.. _google/search-console:

Search Console statistics
=========================

Odoo imports the daily clicks, impressions, click-through rate, and average position of your pages
from Google Search Console, and lets you analyze them in graphs, pivot tables, and lists.

Set it up
---------

#. Add and verify your website in `Google Search Console <https://search.google.com/search-console>`_
   (see :doc:`/applications/websites/website/configuration/google_search_console`).
#. In :menuselection:`Google --> Configuration --> Settings`, in the :guilabel:`Google APIs` block,
   enable :guilabel:`Search Console` and fill in:

   .. list-table::
      :header-rows: 1
      :widths: 30 70

      * - Field
        - Description
      * - :guilabel:`Property`
        - The property as written in Search Console: `sc-domain:example.com` for a domain
          property, or `https://www.example.com/` for a URL-prefix property.
      * - :guilabel:`Statistics by Query`
        - Also stores the search queries. This creates many more lines.
      * - :guilabel:`Initial History (days)`
        - The number of days fetched at the first synchronization (`90` by default). Google keeps
          16 months.

#. Click :guilabel:`Synchronise Now` to import the data at once. Afterwards, a scheduled action
   updates the statistics every day.
#. Click :guilabel:`Submit Sitemap` to send the sitemap of the website to Google.

Read the statistics
-------------------

Go to :menuselection:`Google --> Reporting --> Search Console`. The default view is a graph of the
clicks per day over the last 28 days. Switch to the pivot view (pages by month) or to the list, use
the filters :guilabel:`Last 7 Days` and :guilabel:`Last 28 Days`, search by :guilabel:`Page` or
:guilabel:`Query`, and group by page, query, website, or day.

.. screenshot:: google-search-console-graph
   :menu: Google ‣ Reporting ‣ Search Console
   :shows: The Search Console graph view: a line of clicks per day over 28 days, with the Last 28
      Days filter, and the view switcher (graph, pivot, list).
   :data: Demo statistics of a website with several pages.
   :notes: English UI, light theme, 1440px width.

.. _google/business-profile:

Business Profile reviews
========================

Odoo synchronizes the Google reviews of your business location every hour. You can read them,
reply to them from Odoo, and assign a to-do to the person who must answer the bad ones.

Set it up
---------

In the :guilabel:`Google APIs` block of the settings, enable :guilabel:`Business Profile Reviews`.
Click :guilabel:`Select Location`: the locations managed by the connected Google account are
listed, and you click :guilabel:`Select` on the one of this website. Then:

- :guilabel:`Alert at Rating`: a to-do is scheduled for each new review with this rating or lower
  (`2` by default; `0` for no alert).
- :guilabel:`Alert Responsible`: the user who receives the to-do.

Click :guilabel:`Synchronise Now` to fetch the reviews immediately.

Answer the reviews
------------------

Go to :menuselection:`Google --> Reporting --> Reviews`. Each review shows the reviewer, the stars,
the comment, and the date; the reviews that you answered are greyed out. Use the filters
:guilabel:`Not Replied` and :guilabel:`Low Ratings`, group by :guilabel:`Rating`,
:guilabel:`Website`, or :guilabel:`Month`, and open the graph view to see the distribution of the
ratings.

Open a review and click :guilabel:`Reply`, write your answer, and confirm: the **public reply** is
published under the review on Google. :guilabel:`Edit Reply` changes it later. The activities and
the chatter of the review keep the internal follow-up.

.. screenshot:: google-reviews-form
   :menu: Google ‣ Reporting ‣ Reviews ‣ (a review)
   :shows: A Google review form with the reviewer name, the star rating, the comment, the Reply
      button in the header, and the chatter with a scheduled activity.
   :highlight: The Reply button (red frame).
   :data: A 2-star review with a comment.
   :notes: English UI, light theme, 1440px width. Use a demo reviewer name.

.. warning::
   The reply is public and visible to everybody on Google. Follow your communication policy.
