prices = {
	"Strawberries" : "$1.50",
	"Banana" : "$0.50",
	"Mango" : "$2.50",
	"Blueberries" : "$1.00",
	"Raspberries" : "$1.00",
	"Apple" : "$1.75",
	"Pineapple" : "$3.50"
}

class Smoothie:
	
	def __init__(self, ingredients):
		self.ingredients = ingredients

	def get_cost(self):
		return "${:.2f}".format(sum([float(prices[self.ingredients[i]].replace("$", "")) for  i in range(len(self.ingredients))]))

	def get_price(self):
		calc_cost = [float(prices[self.ingredients[i]].replace("$", "")) for  i in range(len(self.ingredients))]
		return "${:.2f}".format((sum(calc_cost)*1.5+sum(calc_cost)))

	def get_name(self):
		if len(self.ingredients) <= 1:
			if self.ingredients[0].endswith('ies'):
				self.ingredients[0] = self.ingredients[0][:-3] + "y"
			return " ".join(sorted(self.ingredients)) + " Smoothie"
		else:
			for i in range(len(self.ingredients)):
				if self.ingredients[i].endswith('ies'):
					self.ingredients[i] = self.ingredients[i][:-3] + "y"
			return " ".join(sorted(self.ingredients)) + " Fusion"





s1 = Smoothie(["Banana"])
s2 = Smoothie(["Raspberries", "Strawberries", "Blueberries"])
s3 = Smoothie(["Mango", "Apple", "Pineapple"])
s4 = Smoothie(["Pineapple", "Strawberries", "Blueberries", "Mango"])
s5 = Smoothie(["Blueberries"])

print(s5.ingredients)
print(s5.get_cost())
print(s5.get_price())
print(s5.get_name())
