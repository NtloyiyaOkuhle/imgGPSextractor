# imgGPSextractor

This code extracts GPS metadata from an image file and generates a KML file with the GPS coordinates. The KML file can be opened with Google Earth or other mapping software to view the location on a map. Additionally, the code prints out the GPS coordinates and URLs for Google Maps and OpenStreetMap.

To use the code, you first need to make sure you have Python and the necessary packages installed. You will need to install the argparse and simplekml packages, which you can do using pip. You will also need to install the PIL package (Python Imaging Library).

Once you have the necessary packages installed, you can run the code by typing "python" followed by the name of the file and the path to the image you want to extract GPS metadata from. For example,the file is named "imgpsextractor.py" and if the image is located in the same directory as the script, you can run the code with the following command:


python imgpsextractor.py image.jpg

The code will extract the GPS metadata from the image and generate a KML file with the same name as the image, but with the ".kml" extension. It will also print out the GPS coordinates and URLs for Google Maps and OpenStreetMap.

Note that not all images will have GPS metadata, so the code will print out an error message if no metadata is found in the image.
