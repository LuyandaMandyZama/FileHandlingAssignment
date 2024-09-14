

file = open("test.txt", "w")



file.path = 'my_file.txt'

print("File path:", file.path)
      
  
try:
      with open(file.path, 'r') as file:
          contents = file.read()
          print("Contents:", contents)
except Exception as error:
     print("Error:", error)
     
     
try:
    with open(file.path, 'a') as file:
        file.write("\nFirst Line")
        file.write("\nSecond Line")
        file.write("\nThird Line")
        print("Content Appended Successfully!")
        
except FileNotFoundError:
    print("Error: file not found:( Please check File Path.") 
    
except PermissionError:
    print("Error: Permission Denied! Ensure you have Write Access.")
    
               
except Exception as error:
    print("Unexpected Error Occurred:", str(error))   
    
finally:
    print("File Operation Complete!")         