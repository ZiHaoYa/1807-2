class dog:
	__instance = None
	def __new__(cls):
		if cls.__instance == None:
			cls.__instance = super().__new__(cls)
			return cls.__instance

		else:
			return cls.__instance
a = dog()
print(id(a))

	
a1 = dog()
print(id(a1))
