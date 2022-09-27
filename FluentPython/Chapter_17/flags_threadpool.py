from concurrent import futures
from flags import save_flag, get_flag, show, main


MAX_WORKERS = 20


def download_one(cc):
	image = get_flag(cc)
	show(cc)
	save_flag(image, cc.lower() + ".gif")
	return cc


def download_many(cc_list):
	"""
	多线程并发
	"""
	workers = min(MAX_WORKERS, len(cc_list))

	with futures.ThreadPoolExecutor(workers) as executor:
		res = executor.map(download_one, sorted(cc_list))
	return len(list(res))


def download_many_process(cc_list):
	"""
	多进程并行
	"""
	with futures.ProcessPoolExecutor() as executor:
		res = executor.map(download_one, sorted(cc_list))
	return len(list(res))


def download_many_ac(cc_list):
	"""
	把 download_many 函数中的 executor.map 方法换成 executor.submit + futures.as_completed
	"""
	cc_list = cc_list[:5]
	with futures.ThreadPoolExecutor(max_workers=3) as executor:
		to_do = []
		for cc in sorted(cc_list):
			future = executor.submit(download_one, cc)
			to_do.append(future)
			print("Scheduled for {}: {}".format(cc, future))

		results = []
		for future in futures.as_completed(to_do):
			res = future.result()
			print("{} result: {!r}".format(future, res))
			results.append(res)

		return len(results)


if __name__ == "__main__":
	main(download_many_process)
