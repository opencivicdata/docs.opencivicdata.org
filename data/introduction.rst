Adopting the OCD Specification
==============================

.. warning::
    Parts of Open Civic Data underwent a large refactor as of mid-2014, some information on this
    page may be out of date.   We're working on updating this documentation as soon as possible.

    We'll remove these messages from pages as they're updated and vetted.

If you're a city or vendor looking to adopt the OCD specification, this section serves as an implementation guide, including working examples from the OCD API. When you've implemented any one of the OCD elements, please `contact us <mailto:opencivicdata@sunlightfoundation.com>`_ so we can begin collecting your data into Open Civic Data. 

To begin, you'll want to find the :doc:`division id <division>` for your locality.

Finding Your Division ID
------------------------

If you're within the United States (or a selection of other countries), your geographic division should already be included in the database. To look up your division id, `visit the Open Civic Data editor and lookup tool <http://editor.opencivicdata.org/geo/select/>`_. Start by typing in your state, and then locality name. 

For instance, by typing in 'OH' for Ohio and then 'Cleveland' for the City of Cleveland, the division id displayed should look like this:

    ocd-division/country:us/state:oh/place:cleveland

This data is pulled from the US Census and should include every geographic division listed in the Census. If your division is too new to be in the Census or you otherwise need to add it, please take a look at `the OCD repository for the division ids on Github <https://github.com/opencivicdata/ocd-division-ids>`_. If you're outside the United States, chances are your division has not been added yet. You can clone the aforementioned repository to see if your division exists. If it does not, review the :doc:`requirements for new ids <../ocdids>` and then send an email to our `google group <https://groups.google.com/forum/#!forum/open-civic-data>`_. New ids for divisions and jurisdictions are created and agreed upon by consensus via the mailing list, to prevent collisions. 


Finding or Creating Organizations
-------------------------------------
Now that you've found your geopolitical division, you need to find (or create) your :doc:`organization<organization>`. To see if your organization already exists, you can use the same `editor and lookup tool <http://editor.opencivicdata.org/geo/select/>`_ that you used to look up the division. Following the example above, if you click on the division id for Cleveland, you should see a list of all the organizations inside that division. 

If you see your organization, or a parent of your organization, take note of the organization id and the jurisdiction id. If not, you'll need to create these. Jurisdiction ids are used to help identify top level parents, such as a city council or state legislature. These bodies usually have multiple children, and sometimes multiple levels of children, such as committees or the upper and lower chambers of a state legislature. The jurisdiction id helps to identify the top level governing body for all of the organizations underneath it. You can read more about creating a jurisdiction and organization ids :ref:`here<jurisdiction-ids>`. 

For example, here's how the data looks for the Ohio state senate. The division id references the state of Ohio, and the jurisdiction id references the overall Ohio state legislature (including the house and senate). The organization id for the Ohio state senate is `ocd-organization/b87d2136-3b43-11e3-9ac3-1231391cd4ec`. ::

    {
        division_id: "ocd-division/country:us/state:oh",
        classification: "legislature",
        founding_date: null,
        chamber: "upper",
        identifiers: [
            
        ],
        posts: [
            {
                role: "member",
                label: "Member",
                num_seats: 1,
                id: "1"
            },
            {
                role: "member",
                label: "Member",
                num_seats: 1,
                id: "10"
            },
            {
                role: "member",
                label: "Member",
                num_seats: 1,
                id: "11"
            }
            ...
        ],
        other_names: [
            
        ],
        contact_details: [
            
        ],
        id: "ocd-organization/b87d2136-3b43-11e3-9ac3-1231391cd4ec",
        links: [
            
        ],
        name: "Ohio General Assembly, Senate",
        dissolution_date: null,
        sources: [
            {
                url: "http://www.legislature.state.oh.us/",
                note: null
            }
        ],
        memberships: [
            ...
        ],
        parent_id: null,
        extras: {
            
        },
        abbreviation: "oh",
        jurisdiction_id: "ocd-jurisdiction/country:us/state:oh/legislature"
    }



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

In person objects, the only absolutely required field is the name attribute. If the type (person, in this case) cannot be inferred from the endpoint, then a type attribute with the value "person" is also necessary. The more information you add, the better. Person objects can also be linked to organizations. For instance, in the OCD API, each organization object has a 'memberships' attribute, which is an array of people holding office. Here's an example of the memberships from the organization object displayed above: ::


    memberships: [
            {
                person: {
                    contact_details: [
                        
                    ],
                    birth_date: null,
                    biography: null,
                    chamber: "upper",
                    identifiers: [
                        
                    ],
                    name: "Nina Turner",
                    image: "http://www.ohiosenate.gov/senate/Assets/Headshots/Small/25.jpg",
                    updated_at: "2014-04-16T00:18:58.287",
                    other_names: [
                        
                    ],
                    death_date: null,
                    id: "ocd-person/ba595e34-3b43-11e3-9ac3-1231391cd4ec",
                    links: [
                        {
                            url: "http://www.ohiosenate.gov/senate/turner",
                            note: "Homepage"
                        }
                    ],
                    summary: null,
                    district: "25",
                    extras: {
                        first_name: "Nina",
                        last_name: "Turner",
                        +biography: "Representing Ohio’s 25",
                        office_phone: "(614) 466-4583"
                    },
                    gender: null,
                    sources: [
                        {
                            url: "http://www.ohiosenate.gov/senate/members/senate-directory"
                        }
                    ],
                    created_at: "2011-02-22T21:25:58.284"
                },
                contact_details: [
                    {
                        value: "Senate Building 1 Capitol Square, 2nd Floor Columbus, OH 43215",
                        note: "Capitol Office",
                        type: "address"
                    },
                    {
                        value: "614-466-4583",
                        note: "Capitol Office",
                        type: "phone"
                    }
                ],
                end_date: null,
                sources: [
                    
                ],
                role: null,
                chamber: "upper",
                organization_id: "ocd-organization/b87d2136-3b43-11e3-9ac3-1231391cd4ec",
                post_id: "25",
                extras: {
                    term: "2013-2014"
                },
                start_date: "2013",
                unmatched_legislator: null,
                person_id: "ocd-person/ba595e34-3b43-11e3-9ac3-1231391cd4ec"
            },
            
            ...
        ]


The object includes lots of information about the legislature seat generally, and then contains a person attribute that contains information about the legislator filling this seat specifically. The generic information about the seat is important because it can exist and describe the seat even if it isn't presently occupied. 



And More!
---------

These are the basics of what any API or data store that adopts the OCD standard should contain. You can read more about other objects, like :doc:`events <event>`, :doc:`bills <bill>` and :doc:`votes <vote>` on their respective pages. OCD is a new effort and improvements to the standard are being made all the time. If you have suggestions, questions, or want to participate in shaping the OCD standard, please `join our google group <https://groups.google.com/forum/#!forum/open-civic-data>`_.

