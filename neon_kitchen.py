import sqlite3


class ItalCooking:

    def __init__(self): #At the moment of this class being initiated:
        self.conn = sqlite3.connect('recipe.db') #Connect to the recipe database
        self.cursor = self.conn.cursor() #Connect & simplify my connection to the cursor
        self.create_table() #Create a table to store the recorded recipes

    def create_table(self): 
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS Italfood (
                Name TEXT PRIMARY KEY,
                Ingredients TEXT,
                Instructions TEXT
                )                    
        ''')
        self.conn.commit()


    def add_recipe(self, recipe_name, recipe_ing, recipe_ins): #Pass the recipes attributes in the parameter
        self.cursor.execute('''INSERT OR IGNORE INTO Italfood (Name, Ingredients, Instructions) VALUES (?, ?, ?)''',
                            (recipe_name, recipe_ing, recipe_ins,)) 
        self.conn.commit() #Commit operations after inserting the recipe attributes into the Italfood table


    def update_recipe(self, update): #Depending on the 'type' of update the user selects:

        if update == 'name': #Update only the Name of a specfic recipe
            recipe_name = input('\nEnter Recipe Name You Would Like to Change: ').upper()
            new_recipe_name = input('Enter Recipe Name Update: ').upper()
            self.cursor.execute('''UPDATE Italfood SET Name = ? WHERE Name = ? ''', (new_recipe_name, recipe_name,))
            self.conn.commit()
            print(f'\nThe Recipe "{recipe_name}" Has Succesfully Been Updated to {new_recipe_name}!')
        
        elif update == 'ingredients': #Update only the Ingredients of a specific recipe
            recipe_name = input('\nEnter Recipe Name You Would Like to Change: ').upper()
            new_ingredients = input('Enter New Ingredients: ')
            self.cursor.execute('''UPDATE Italfood SET Ingredients = ? WHERE Name = ? ''', (new_ingredients, recipe_name,))
            self.conn.commit()
            print(f'\nThe Recipe "{recipe_name}" Has the New Ingredients: {new_ingredients}')
        
        elif update == 'instructions': #Update only the Instructions of a specific recipe
            recipe_name = input('\nEnter Recipe Name You Would Like to Change: ').upper()
            new_instructions = input('Enter New Instructions: ')
            self.cursor.execute('''UPDATE Italfood SET Instructions = ? WHERE Name = ? ''', (new_instructions, recipe_name,))
            self.conn.commit()
            print(f'\nThe Recipe "{recipe_name}" Has the New Instructions: {new_instructions}')
                                
        elif update == 'all': #Update a specifc recipe completely
            recipe_name = input('\nEnter Recipe Name You Would Like to Change: ').upper()
            new_recipe_name = input('Enter New Recipe Name: ').upper()
            new_recipe_ing = input('Enter New Ingredient Names: ')
            new_recipe_ins = input('Enter New Recipe Instructions: ')
            self.cursor.execute('''UPDATE Italfood SET Name = ?, Ingredients = ?, Instructions = ? WHERE Name = ? ''', (new_recipe_name, new_recipe_ing, new_recipe_ins, recipe_name,))
            self.conn.commit()
            print(f'\nThe Recipe "{recipe_name}" Has Been Renewed to:\n*{new_recipe_name}\n*{new_recipe_ing}\n*{new_recipe_ins}')    

        else:
            print('Invalid Input. Expected one of the Following Four Options.')


    def ital_cookbook(self): #Browse the Ital_Cookbook
        print ('\n1.) Select a Recipe') #Browse for a specifc recipe
        print ('2.) Browse by Ingredients') #Browse for specific ingredients
        print ('3.) View Ital Cookbook') #Browse the entire ItalCookbook
        choice = input ('Please Select Cookbook Usage: ')

        if choice == '1': #Search for and return the recipe if it exists
            recipe_query = input ('\nThe Name of the Recipe You Would Like to Query: ').upper()
            self.cursor.execute('''SELECT * FROM Italfood WHERE Name = ?''', (recipe_query,))
            view_recipe = self.cursor.fetchone()
            for food in view_recipe:
                print (f'\n- {food}')

        elif choice == '2': #Search for and return the ingredietns if they exist
            recipe_queries = input ('\nThe Ingredient(s) You Would Like to Query: ')
            self.cursor.execute('''SELECT * FROM Italfood WHERE Ingredients LIKE ?''', (f'%{recipe_queries}%',))
            view_ingredients = self.cursor.fetchall()
            for food in view_ingredients:
                print ('')
                print (f'- {food[0]}: {food[1]}; {food[2]}')
            

        elif choice == '3': #Reveal and return all available recipes
            self.cursor.execute('''SELECT * FROM Italfood''')
            view_recipes = self.cursor.fetchall()
            for food in view_recipes:
                print ('')
                print (f'- {food[0]}: {food[1]}; {food[2]}')
        else:
            print ('Invalid Input. Please Select one of the Numbers Above.')
            ItalCooking.ital_cookbook(self)


    def release(self, recipe_name): #Release the requested recipe.
        self.cursor.execute('''DELETE FROM Italfood WHERE Name = ?''', (recipe_name,))
        self.conn.commit()
        print (f'{recipe_name} succesfully deleted!')


    def leave_kitchen(self): #Exit the kitchen!
        self.conn.close()