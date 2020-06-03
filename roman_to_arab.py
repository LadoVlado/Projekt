class Arab():

	def __init__(self, num):
		self.n = str(num)

	dict = {
		'1': 'I',
		'4': 'IV',
		'5': 'V',
		'9': 'IX',
		'10': 'X',
		'40': 'XL',
		'50': 'L',
		'90': 'XC',
		'100': 'C',
		'400': 'CD',
		'500': 'D',
		'900': 'CM',
		'1000': 'M'
	}
	@property
	def arab_to_roman(self):
		result = ''

		for index, digit in enumerate(list(self.n)):

			zeros = (len(list(self.n))-1-index)*'0'

			if int(digit) < 4:
				result += self.dict['1'+zeros]*int(digit)

			elif int(digit) >= 5 and int(digit) < 9:
				result += self.dict['5'+zeros] + self.dict['1'+ zeros]*(int(digit)-5)

			else:
				result += self.dict[digit+zeros]

			
		return result

	def __add__(self, other):
		return self.n + other.n

	def __sub__(self, other):
		return self.n - other.n


class Roman(Arab):

	def __init__(self, num):
		super().__init__(num)

	dict = {
		'I': 1,
		'V': 5,
		'X': 10,
		'L': 50,
		'C': 100,
		'D': 500,
		'M': 1000
	}
	@property
	def roman_to_arab(self):
		last, result = 0, 0

		for symbol in list(self.n)[::-1]:
			if last == 0:
				result += self.dict[symbol]

			elif last > self.dict[symbol]:
				result -= self.dict[symbol]

			else:
				result += self.dict[symbol]

			last = self.dict[symbol]
		return result

	def __add__(self, other):
		result = Arab(self.roman_to_arab+other.roman_to_arab)
		return result.arab_to_roman

	def __sub__(self, other):
		result = Arab(self.roman_to_arab-other.roman_to_arab)
		return result.arab_to_roman



number1 = Roman('DX')
number2 = Arab(125)

print(number1.roman_to_arab)
print(number2.arab_to_roman)