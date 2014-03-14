Adopting the OCD Specification
==============================

If you're a city or vendor looking to adopt the OCD specification, this section serves as a guide for implementing each type of object, including working examples from the OCD API. When you've implemented any one of the OCD elements, please `contact us <mailto:opencivicdata@sunlightfoundation.com>`_ so we can begin collecting your data into Open Civic Data. 

To begin, you'll want to find the :doc:`division id <division>` for your locality.

Finding Your Division
---------------------

If you're within the United States (or a selection of other countries), your geographic division should already be included in the database. To look up your division id, `visit the Open Civic Data editor and lookup tool <http://editor.opencivicdata.org/geo/select/>`_. Start by typing in your state, and then locality name. 

For instance, by typing in 'OH' for Ohio and then 'Cleveland' for the City of Cleveland, the division id displayed should look like this:

    ocd-division/country:us/state:oh/place:cleveland

This data is pulled from the US Census and should include every geographic division listed in the Census. If your division is too new to be in the Census or you otherwise need to add it, please take a look at `the OCD repository for the division ids on Github <https://github.com/opencivicdata/ocd-division-ids>`_. If you're outside the United States, chances are your division has not been added yet. You can clone the aforementioned repository to see if your division exists. If it does not, review the :doc:`requirements for new ids<ocdids>` and then send an email to our `google group <https://groups.google.com/forum/#!forum/open-civic-data>`_. New ids for divisions and jurisdictions are created and agreed upon by consensus via the mailing list, to prevent collisions. 


Finding or Creating Your Organization
-------------------------------------
Now that you've found your geopolitical division, you need to find (or create) your :doc:`organization<organization>`. To see if your organization already exists, you can use the same `editor and lookup tool <http://editor.opencivicdata.org/geo/select/>`_ that you used to look up the division. Following the example above, if you click on the division id for Cleveland, you should see a list of all the organizations inside that division. 

If you see your organization, or a parent of your organization, take note of the organization id and the jurisdiction id. If not, you'll need to create these. Jurisdiction ids are used to help identify top level parents, such as a city council or state legislature. These bodies usually have multiple children, and sometimes multiple levels of children, such as committees and subcommittees. The jurisdiction id helps to identify the top level governing body for all of the organizations underneath it. You can read more about creating a jurisdiction id :ref:`here<jurisdiction-ids>`. 





Publishing Your Local Representatives
-------------------------------------

Representatives can be expressed using the :doc:`Person Object <person>` format. You can read more about the explicit elements on the :doc:`person page <person>` but for a quick start, here's an example in JSON: ::

    {
        "_type": "person", 
        "contact_details": [
            {
                "note": "", 
                "type": "email", 
                "value": "roswellmayor@roswell-nm.gov"
            }, 
            {
                "note": "", 
                "type": "voice", 
                "value": "575-637-6202"
            }
        ], 
        "name": "Del Jurney", 
        "links": [], 
        "gender": "m", 
        "image": "http://www.roswell-nm.gov/images/library/Image/del-jurney.jpg, 
        "other_names": [], 
        "sources": [
            {
                "url": "http://www.roswell-nm.gov/staticpages/index.php/city-mayor, 
                "note": ""
            }
        ], 
        "extras": {}, 
        "_id": "ocd-person/bff59848-b1c4-11e2-b819-12313d2facc4", 
        "biography": "Roswell City Mayor Del Jurney. The Mayor is elected at-large and represents all neighborhood wards within the City."
    }

In person objects, the only required fields are the _type and name attributes. 