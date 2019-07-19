def read_file(filename):
	lines = []
	with open(filename, 'r', encoding = 'utf-8') as f:
		for line in f:
			lines.append(line.strip())
	return lines

def convert(lines):
	markma_word_count = 0
	markma_sticker_count = 0
	markma_image_count = 0
	tiffany_word_count = 0
	tiffany_sticker_count = 0
	tiffany_image_count = 0
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Mark':
			if s[3] == '貼圖':
				markma_sticker_count += 1
			elif s[3] == '圖片':
				markma_image_count += 1
			else:
				for msg in s[3:]:
					markma_word_count += len(msg)
		elif name == 'Tiffany':
			if s[3] == '貼圖':
				tiffany_sticker_count += 1
			elif s[3] == '圖片':
				tiffany_image_count += 1
			else:	
				for msg in s[3:]:
					tiffany_word_count += len(msg)
	print('Mark word count =', markma_word_count, 'sticker count =', markma_sticker_count, 'image count =', markma_image_count)
	print('Tiffany word count =', tiffany_word_count, 'sticker count =', tiffany_sticker_count, 'image count =', tiffany_image_count)

def creat_file(convert_line):
	with open('output.txt', 'w') as f:
		for line in convert_line:
			f.write(line)

def main():
	lines = read_file('[LINE]Tiffany.txt')
	convert_line = convert(lines)
	#print(convert(lines))
	#creat_file(convert_line)
main()