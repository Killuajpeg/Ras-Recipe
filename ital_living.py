from neon_kitchen import ItalCooking

ital_cooking = ItalCooking()
Ital_living_open = True

while Ital_living_open:
    print ('\n\n***********************************')
    print ('***** WELCOME TO ITAL LIVING! *****')
    print ('***********************************')

    print ('1.) Create Recipe')
    print ('2.) Update Recipe')
    print ('3.) Ital Cookbook')
    print ('4.) Release Recipe')
    print ('5.) Ital Exit')

    choice = input ('Please Select: ')
    if choice == '1': #Create a new recipe
        recipe_name = input('\nEnter Recipe Name: ').upper()  #Record the recipes name
        recipe_ing = input('Enter Recipe Ingredients: ') #Record the recipes ingredients 
        recipe_ins = input('Enter Recipe Instructions: ') #Record the recipes instructions
        ital_cooking.add_recipe(recipe_name, recipe_ing, recipe_ins) #Add the recipe to the italcookbook

    elif choice == '2': #Update an existing recipe
        update = input('\nSelect an Update Type;\nName), Ingredients), Instructions), or All): ').lower() #Decide the type of update needed
        ital_cooking.update_recipe(update) #Perform the update
        
    elif choice == '3':
        ital_cooking.ital_cookbook() #Begin to browse the italcookbook
    
    elif choice == '4':
        print ('\nDanger Zone!')
        recipe_name = input ('Enter the Recipe Name you want to release: ').upper() #Ascertain the recipe of possible deletion
        decision = input ('Are you sure? (y/n): ').lower() #Confirm the deletion
        if decision == 'y':
            ital_cooking.release(recipe_name) #Release the recipe
        elif decision == 'n':
            pass
        else:
            print ('Error. Expecting The "Y" or "N" Characters.')
    
    elif choice == '5':
        print ('\nThank you! Enjoy!\n')
        exit()
    else:
        print ('Invalid Input. Please Type One of The Options Above.')
