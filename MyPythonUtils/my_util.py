import os

target_file = r"E:\BooksLearn\LeetCode\README.md"
dir = r"E:\BooksLearn\LeetCode"


def convert_gb2312_to_utf_8(file_path):
	print("convert_gb2312_to_utf_8 start")
	file_data = None
	try:
		with open(file_path, "r", encoding="GB2312") as f:
			file_data = f.read() # 读取以gb2312编码的字符串到str
	except UnicodeDecodeError:
		return
	with open(file_path, "w", encoding="utf-8") as f:
		f.write(file_data)      # 将str编码为utf-8
	print("convert_gb2312_to_utf_8 finish!")


def convert_gb2312_to_utf_8_dir(dir):
	for root, dirs, files in os.walk(dir):
		for name in files:
			if name.endswith(".md") or name.endswith(".cpp") or name.endswith(".h"):
				convert_gb2312_to_utf_8(os.path.join(root, name))


if __name__ == "__main__":
	convert_gb2312_to_utf_8_dir(dir)

