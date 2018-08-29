

def coroutine(fn):
	def wrapper(*args, **kwargs):
		c = fn(*args, **kwargs)
		next(c)
		return c
	return wrapper

#
# if __name__ == '__main__':
#     import argparse
#     parser = argparse.ArgumentParser()
#     parser.add_argument('-i', action='store_true',
#                         dest='case_insensitive')
#     parser.add_argument('pattern', type=str)
#     parser.add_argument('infile', type=argparse.FileType('r'))
#     args = parser.parse_args()
#     cat(args.infile, args.case_insensitive,
#         grep(args.pattern, args.case_insensitive,
#              count(args.pattern)))


class grep():
	def __init__(self):
		pass

	def cat(self,f, case_insensitive, child):
		if case_insensitive:
			line_processor = lambda l: l.lower()
		else:
			line_processor = lambda l: l

		for line in f:
			child.send(line_processor(line))


	@coroutine
	def grep(self,substring, case_insensitive, child):
		if case_insensitive:
			substring = substring.lower()
		while True:
			text = (yield)
			child.send(text.count(substring))

	@coroutine
	def count(self,substring):
		n = 0
		try:
			while True:
				n += (yield)
		except GeneratorExit:
			print(substring,n)

	def execute(self, cls):

		case_insensetive = '-i' in cls.options
		pattern = cls.data[1]
		fileC = cls.data[0]
		try:
			f = open(fileC, 'r')
			self.cat(f, case_insensetive,
					 self.grep(pattern, case_insensetive, self.count(pattern)))

		except:
			self.cat(fileC, case_insensetive,
					 self.grep(pattern, case_insensetive, self.count(pattern)))

