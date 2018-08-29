class cat():
	def __init__(self):
		pass

	def execute(self, cls):
		print(cls.options, cls.data)
		fileCat = cls.data[0]
		try:
			f = open(fileCat, 'r')
			case_insensetive = '-i' in cls.options
			
			if case_insensetive:
				line_processor = lambda l: l.lower()
			else:
				line_processor = lambda l: l

			for line in f:
					print(line_processor(line))

		except:
			print("Please Specify the correct input file")