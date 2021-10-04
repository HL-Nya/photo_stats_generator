import exifread
import os
import sys

def photo_stats(root_dir, file_formats):
	count = 0
	result_dict = {
					"EXIF LensModel":{}, 
					"EXIF FocalLengthIn35mmFilm": {}, 
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
						if tag in result_dict.keys():
							if str(tags[tag]) in result_dict[tag].keys():
								result_dict[tag][str(tags[tag])] += 1
							else:
								if tag in ["EXIF ISOSpeedRatings", "EXIF FocalLengthIn35mmFilm"]:
									result_dict[tag][int(str(tags[tag]))] = 1
								else:
									result_dict[tag][str(tags[tag])] = 1
				f.close()

	print(result_dict)
	print("\n\n\n\n")

	for tag in result_dict.keys():
		print(f"Stats for {tag}")
		total = 0
		for key in sorted(result_dict[tag]):
			total += result_dict[tag][key]
		for key in sorted(result_dict[tag]):
			print(f"\t{key}\n\t\t\tcount: {result_dict[tag][key]}\tPercentage: {str(round(result_dict[tag][key]/total*100,2))}%")






if __name__ == '__main__':
	file_formats = [".ARW", ".JPG", ".PNG", ".jpg", ".png"]
	root_dir = "E:\\photos\\"

	# file_formats = [".ARW"]
	# root_dir = "E:\\photos\\A7 MK II\\2015年6月11日  星期四"

	photo_stats(root_dir, file_formats)