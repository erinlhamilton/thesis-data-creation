client-vs-server data creation
==============================

This is the code and data used to create the final SQLite database for client-vs-server. It took several steps to get the final datasets, starting from a shapefile format and ending as well-known text blobs in a SQLite database. 
<br>
These steps used a combination of ArcGIS, QGIS, Python, JAVA, and SQL.

<h3>Step One</h3>
Original geographic datasets were obtained from LA County GIS (http://egis3.lacounty.gov/dataportal/):
<ul>
<li><b>Points</b> - 2012 LA County Address Points: http://egis3.lacounty.gov/dataportal/wp-content/uploads/2012/06/lacounty_address_points.zip</li>
<li><b>Polygons</b> - 2008 LA County Building Footprints: http://egis3.lacounty.gov/dataportal/wp-content/uploads/2012/11/lariac_buildings_2008.zip</li>
<li><b>Polylines</b> - 2010 LA County Tiger Roads: http://egis3.lacounty.gov/dataportal/wp-content/uploads/2011/04/tigerroads.zip</li>
</ul>
<h3>Step Two</h3>
<p>Separate data were needed for the different geoprocesses. Buffer tested with points, lines, and polygons. The same points used for buffer were tested with Voronoi triangulation. Union required a new set of test data, in this case two sets of polygon datasets that overlapped.</p>
<b>For Buffer and Voronoi Triangulation Data</b>
<p>QGIS was used to convert LA County shapefiles to well-known text format. The Vector ->Research Tools ->Random Selection tool was then used to randomly select n number of
features from each datatype because the size in megabytes are all roughly the same (~20MB):</p>
<b>Datatypes and number of features selected:</b>
<ul>
<li><b>Points:</b> 500,000</li>
<li><b>Polylines:</b> 150,000</li>
<li><b>Polygons:</b> 45,000</li>
</ul>


<b>For Union Data Data</b>
<p>ArcGIS was used to select out a smaller subsection of the original buildings polygon shapefile. A new shapefile was created from this along with a duplicate of this new shapefile.
The duplicate shapefile was then offset using ArcGIS by a fraction of a decimal degree, so that there was overlap between every polygon in the two shapefiles, but they weren't identical in coordinates. QGIS was then used to
convert the shapefiles to well-known text.</p>

<h3>Step Three</h3>
<b>(Code above)</b> 
<p>Python was used to create points, lines, and polygons WKT for the buffer and Voronoi tests. The python script started with the original large WKT files created using QGIS in a
previous step. It first iterated through the points WKT and determined sizes (in KB), based on an array of vertice sizes, and then randomly selected features from the lines and polygon
files equivalent in sizes (in kb) to create outputs of each vertice size.</p>

<h3>Step Four</h3>
<b>(Code above)</b> 
<p>Python was used to accomplish a similar task as the previous step. This time the starting files were points along with the two duplicate polygon files created from previous steps.
This time the random seed of the code was set to be the same for each creation so that the same features from each polygon file were randomly selected. Polygon WKT of increasing size (in vertices) were created.</p>

<h3>Step Five</h3>
<b>(Code above)</b>  
<p>Java JDBC and SQL were used to create the SQLite database and db tables for the final database.</p>
<b>Tables Created:</b>
<ul>
<li>Points: for the wkt points used for buffer and voronoi triangulation.</li>
<li>Polygons: for the wkt polygons used for buffer.</li>
<li>Lines: for the wkt lines used for buffer.</li>
<li>PolygonA: for first set of wkt polygons used for union.</li>
<li>PolygonB: for second set of wkt polygons used for union.</li>
<li>Metadata: for information on specific test.</li>
<li>Results: for all of the timing results of the tests.</li>
<li>Network: for the network badnwidth and latency tests.</li>
</ul>

<h3>Step Six</h3>
<b>(Code above)</b> 
<p>Java JDBC and SQL were used to populate the SQLite database with WKT in the blob format, pulling in wkt data created in previous steps from file.</p>


