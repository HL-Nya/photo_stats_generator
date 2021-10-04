import exifread
import os
import sys

def photo_stats(root_dir, file_formats):
	count = 0
	result_dict = {
					"EXIF LensModel":{}, 
					"Image Model": {},
					"Image Make": {},
					"Image Software": {},
					"EXIF ExposureTime":{},
					"EXIF FNumber":{},
					"EXIF ISOSpeedRatings":{},
					"EXIF FocalLength":{},
					"EXIF LensModel":{}
					}
	for root, subdirs, files in os.walk(root_dir):
		for file in files:
			count += 1
			print(count)
			if any(x in file for x in file_formats):
				f = open(f'{root}\\{file}', 'rb')
				tags = exifread.process_file(f)
				for tag in tags.keys():

					if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote'):
						print(tag)
						print(tags[tag])
						if tag in result_dict.keys():

							if str(tags[tag]) in result_dict[tag].keys():
								result_dict[tag][str(tags[tag])] += 1
							else:
								if tag in ["EXIF ISOSpeedRatings"]:
									result_dict[tag][int(str(tags[tag]))] = 1
								else:
									result_dict[tag][str(tags[tag])] = 1
				f.close()

	print(result_dict)
	print("\n\n\n\n")

	for tag in result_dict.keys():
		print(f"Stats for {tag}")
		total = 0

		for key in result_dict[tag]:
			total += result_dict[tag][key]
		for key in sorted(result_dict[tag].items(), key=lambda x: x[1], reverse=True):
			print(f"\t{key[0]}\n\t\t\tcount: {result_dict[tag][key[0]]}\tPercentage: {str(round(result_dict[tag][key[0]]/total*100,2))}%")






if __name__ == '__main__':
	# add photo format you want to scan
	file_formats = [".ARW", ".JPG", ".PNG", ".jpg", ".png"]
	# replace your photo dir here
	root_dir = "E:\\photos\\"

	photo_stats(root_dir, file_formats)
