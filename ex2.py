def get_cats_info(path):
    cats=[]
    try: # Error handling
        with open(path, mode = "r", encoding='utf-8') as file: # Opening file in read mode
            for line in file.readlines(): # Loop by rows
                id, name, age = line.split(",") # Splitting each row by "," symbol
                cat = {"id": id, "name" : name, "age" : age.strip()} # Dict init of cat properties
                cats.append(cat) # Adding dict of cat properties to tuple
            return cats
            # The task is done, function returns list of dictionaries with cats properties
    except FileNotFoundError: # File not found error
        return ("The file is not found")
    except (UnboundLocalError, ValueError): # File content errors
        return ("The file has invalid content")

# Debugging
cats_info = get_cats_info(r"C:\Users\Valentyn\Desktop\File1.txt")
print(cats_info)