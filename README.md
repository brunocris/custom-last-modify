# Change last modification in file
This script is used to manipulate and update an attribute of the properties of a file in system.  
This attribute indicates the last change made to the queried file.

**Google Photos**, for example, is a application that uses the "Modified" attribute value to sort the photo files that do not have EXIF tags.

Click here and see the [sample](https://gitlab.com/bruno.criscuolo/python-utilities/tree/master/custom-last-modify/sample).

##### NOTE:
This sample uses image files in `.jpg` format,
available in the `'img'` folder, whose names follow
the regular expression:
	
    <PREFIX>_<YEAR><MONTH><DAY>_<HOUR><MINUTE><SECOND>.jpg

In this case `<PREFIX>` = IMG, because file is a image.

If you run this script for another use case, please check the standard expression of your files.

When running the script, the file name string is used to construct the date ante time that make up the last modified attribute.

### Running the sample script

The name of pictures samples is:

- IMG_20190423_204516.jpg
- IMG_20190423_204817.jpg
- IMG_20190423_205008.jpg
- IMG_20190423_205317.jpg

Each filename follows the regular expression presented above.  
To run the script, you need to rename the `.jpg` images by putting the dates you want, according to the regular expression. Then do:

	pyhton custom-last-modify.py

After renaming files, according to the prescribed format, you observe the match between the "modified in" property and the name entered in the file.  

In Google Photos, you realize that images are sorted by date according to the file name.  
The pictures were renamed as follows:

- IMG_20190423_204516.jpg -> *IMG_20151201_103244.jpg*
- IMG_20190423_204817.jpg -> *IMG_20151109_120923.jpg*
- IMG_20190423_205008.jpg -> *IMG_20140305_131753.jpg*
- IMG_20190423_205317.jpg -> *IMG_20170730_175602.jpg*

**Result in Google Photos is:**

![Google Photos Result](https://docs.google.com/drawings/d/e/2PACX-1vT2x-iv_DpJM9P6gv0GAYQXtb6F9s0mtIPat3x9tMvqPzCVKjy_rDPEDcWC7B6R6EwcQRv5oXGusJV9/pub?w=960&h=260)

![Google Photos Result Details](https://docs.google.com/drawings/d/e/2PACX-1vRQ8Qhuk8oDKDPIEJZcwMzUoAvjJqIZGSwKzpIpkZQhabb9NCty669jQ442a9W-hyOgW2bl0yrYBMZt/pub?w=961&h=486)