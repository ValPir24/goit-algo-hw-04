def total_salary(path):
    total = 0
    average = 0
    try: # Error handling
        with open(path, mode = "r", encoding = 'utf-8') as file: # Opening file in read mode 
            for count, line in enumerate(file.readlines()): # Loop by rows and counting
                _,a = line.split(",") # Splitting each row by "," symbol
                total+=int(a) # Salaries sum
            average = total // (count + 1) # Salaries average
            return (total, average)
            # The task is done, function returns tuple of total and average salary from defined document
    except FileNotFoundError: # File not found error
        return ("The file is not found")
    except (UnboundLocalError, ValueError): # File content errors
        return ("The file has invalid content")

# Debugging
total, average = total_salary(r"C:\Users\Valentyn\Desktop\File.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")