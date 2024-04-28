class BudgetCategory:
    def __init__(self, category_name, budget):
        self.__category_name = category_name
        self.__budget = budget
        self.__expenses = 0
        
    def get_category_name(self):
        return self.__category_name
    
    def set_category_name(self, new_category):
        self.__category_name = new_category
        
    def get_budget(self):
        return self.__budget
    
    def set_budget(self, new_budget):
        self.__budget = new_budget
    
    def add_expense(self, amount):
        if amount > 0:
            self.__expenses += amount
            print(f"Expense of {amount} added to {self.__category_name} category.")
        else:
            print("Invalid expense amount. Expense should be greater than zero.")
    
    def display_category_summary(self):
        print(f"Category: {self.__category_name}")
        print(f"Budget: {self.__budget}")
        print(f"Total Expenses: {self.__expenses}")
        print(f"Remaining Budget: {self.__budget - self.__expenses}")
    
    
food_category = BudgetCategory("Food", 500)
food_category.add_expense(100)
food_category.display_category_summary()
