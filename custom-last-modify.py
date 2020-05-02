# -*- coding: utf-8 -*-
import os
import time
import datetime

# Enter the path of your target directory,
# where you want to change "Modified" tag attribute.
path = '/path/to/my/target/directory'
# Returns a list containing all the files in the given directory.
files = os.listdir(path)

for file_name in files:
	# Get only the filename, without its extension.
	text = os.path.splitext(file_name)[0]
	# Split text content about date attribute.
	date_block = text.split('_')[1]
	# Split text content about time attribute.
	time_block = text.split('_')[2]

	# The characters are grouped in
	# year, month, day for the date context and
	# hour, minute, second for the time context.
	# The 'datetime' module requires variables to be of 'integer' type.
	year = date_block[0:4]
	year = int(year)
	month = date_block[4:6]
	month = int(month)
	day = date_block[6:8]
	day = int(day)

	hour = time_block[0:2]
	hour = int(hour)
	minute = time_block[2:4]
	minute = int(minute)
	second = time_block[4:7]
	second = int(second)

	# Concatenates path of the target directory with
	# name of the file that will have the updated "Modified" tag.
	modFile = os.path.join(path, file_name)

	# Combination the date and time attributes.
	date = datetime.datetime(year=year, month=month, day=day, hour=hour, minute=minute, second=second)
	modTime = time.mktime(date.timetuple())

	# Applying changes on the file.
	os.utime(modFile, (modTime, modTime))