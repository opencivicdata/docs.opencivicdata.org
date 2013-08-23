diff --git a/_includes/__init__.py b/_includes/__init__.py
index 3bc66f9..483c711 100644
--- a/_includes/__init__.py
+++ b/_includes/__init__.py
@@ -4,24 +4,23 @@ from .people import PersonScraper
 
 
 class Example(Jurisdiction):
-    jurisdiction_id = 'ocd-jurisdiction/country:us/state:ex/place:example'
+    jurisdiction_id = 'ocd-jurisdiction/country:us/state:nm/place:albequerque/council'
 
     def get_metadata(self):
         return {
-            'name': 'Example',
-            'legislature_name': 'Example Legislature',
-            'legislature_url': 'http://example.com',
+            'name': 'Albequerque City Council',
+            'legislature_name': 'Albequerque City Council',
+            'legislature_url': 'http://www.cabq.gov/council/',
             'terms': [{
-                'name': '2013-2014',
-                'sessions': ['2013'],
+                'name': '2013-2015',
                 'start_year': 2013,
-                'end_year': 2014
+                'end_year': 2015,
+                'sessions': ['2013'],
                 }],
             'provides': ['people'],
             'parties': [
-                {'name': 'Independent' },
-                {'name': 'Green' },
-                {'name': 'Bull-Moose'}
+                {'name': 'Democratic' },
+                {'name': 'Republican' },
                ],
             'session_details': {
                 '2013': {'_scraped_name': '2013'}
