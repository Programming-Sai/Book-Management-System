from tabulate import tabulate
import random 
import os




class Book:
     """
         This class represents a Book object.
     """
     def __init__(self, title, author, genre, description): 
        
          # Instance Attribute Initialisation 
                    
          self.title = title
          self.author = author
          self.genre = genre       
          self.description = description  
          self.ID = self.auto_generate_ID()
          
          
          
     def auto_generate_ID(self):
          """
               Generates a randomly unique ISBN for any book.
       
               Returns:
               string: The generated ISBN.
          """
          track = set()
          ISBN = 0          
          while ISBN not in track:
               ISBN = random.randint(1000000000000, 6000000000000)
               track.add(ISBN)                    
          id_num = str(ISBN)
          id = ''
          for i in range(len(id_num)):
               id += id_num[i]
               if i in [2, 3, 5, 11]:
                    id += '-'
          id = 'ISBN-13: ' + id
          return id
          
          

     

     










class Book_Management:
     """
          This class represents the system for all book operations.
     """
     def __init__(self):
          
          # Instance Attribute Initialisation 
          # for a list of Book instances 
          
          self.books =  self.get_book_list()



     def get_book_list(self):
          """
               Gets the list of book attributes from storage,
               then creates an instance of a Book Object,
               that is then added bro the list.
       
               Returns:
               list: A list containing all Book instances .
          """
          book_list = []
          books = []
          with open('Books.txt', 'r') as b:
               book_list = [book.strip() for book in b.readlines()]                    
          for book_info in book_list:
               book_info = book_info.split(',')
               book = Book(book_info[0], book_info[1], book_info[2], book_info[3])
               books.append(book)
          return books


          
     def add_book(self):
          """
               Adds a book to the list of books.
       
               Returns: None
          """
          title = input('What is the title of the Book '). title()
          author = input('Who is the author of this Book ').title()
          genre = input('What is the genre of this Book ').lower()
          
          description_option = input('Would You Like To Add A \nDescription For This Book? (Y/N) ').lower()
          
          if description_option == 'y':
               description = input('Synopsis: ')
          else:
               description = 'No description available'          
          with open('Books.txt', 'a') as b:
               b.write(f'{title},{author},{genre},{description}\n')          
          self.books =  self.get_book_list()



     def remove_book(self, del_book):
          """
               Removes any selected book from the list of books.
               
               Parameter
               del_book(class): the book to be deleted 

               Returns:
               string: This is a message that tells user the status
               of their delete operation.
          """
          return_message = ''
          for book in self.books:
               if book.ID == del_book.ID:                                   
                    with open('Books.txt', 'r') as b:
                         books = b.readlines()
                    books.remove(f'{del_book.title},{del_book.author},{del_book.genre},{del_book.description}\n')                   
                    with open('Books.txt', 'w') as b:
                         for book in books:
                              b.write(book)                    
                    return_message = 'Deleted Successfully'
               else:
                    return_message = f'Book {del_book.title} Not Found' 
          self.books =  self.get_book_list()
          return return_message
          
          
          
     def display_book_list(self, book_list):
          """
             Shows all books in a specified list
             
             Parameter
             book_list(list): the list in which books are, for display 
     
             Returns: None
          """
          header = ['No.', 'Title', 'Author', 'Genre']
          data = [(str(num)+'.', book.title, book.author) for num, book in enumerate(book_list, start = 1)]
          print(tabulate(data, header))




     def update_book_info(self, book):
          """
             Allows for updates to any book information 
             
             Parameter
             book(class): the book to be updated 
     
             Returns: None
          """
          update_title = input('What is the new title of the Book '). title()
          update_author = input('Who is the updated author of this Book ').title()
          update_genre = input('What is the updated genre of this Book ').lower()
          update_description = input('New Synopsis: ')
          
          old_info = f'{book.title},{book.author},{book.genre},{book.description}\n'
          new_info = f'{book.title if len(update_title) < 1 else update_title},{book.author if len(update_author) < 1 else update_author},{book.genre if len(update_genre) < 1 else update_genre},{book.description if len(update_description) < 1 else update_description}\n'
          
          with open('Books.txt', 'r') as b:
               all_books = b.readlines()
          all_books.remove(old_info)
          all_books.append(new_info)
                    
          with open('Books.txt', 'w') as b:
               for mbook in all_books:
                    b.write(mbook)
                    
          book.title = book.title if len(update_title) < 1 else update_title
          book.author = book.author if len(update_author) < 1 else update_author
          book.genre = book.genre if len(update_genre) < 1 else update_genre
          book.description = book.description if len(update_description) < 1 else update_description
                                       
          self.books =  self.get_book_list()



     def show_book_info(self, book):
          """
             Shows all book information
             
             Parameter
             book(class): the book whose information is needed
     
             Returns: None
          """
          print(f'\nTitle: {book.title}')
          print(f'Author: {book.author}')
          print(f'Genre: {book.genre}')
          print(f'ISBN: {book.ID}')
          print(f'Synopsis: {book.description}\n')
          
     
     
     def search(self, search_list, target):
          """
             Shows all books in a specified list
             
             Parameter
             search_list(list): the list in which books are, for search
             target(str): this is the input based on which the search is carried out 
     
             Returns: 
             list: the list of books that is covered by the target
          """
          return [item for item in search_list if target in item.title or target in item.author or target in item.genre or target in item.description]


             
     def clear_book_list(self):
          """
             Clears all books from the list
             
             Parameter: None
             
             Returns: None
          """
          with open('Books.txt', 'w') as b:
               b.write('')
          self.books =  self.get_book_list()
     












class Book_Interface:
     """
         This class represents the Command-Line Interface for the book management system.
     """
     def __init__(self):
          
          # Instance Attribute Initialisation
          # of the Book_Management Class

          self.books = Book_Management()
          
          
          
     def select(self, option_list):
          """
             Allows for selection based on the list of options to select from
             
             Parameter
             option_list(list): the list of options for selection 
     
             Returns: 
             list item: the selection made by the user
          """
          selection = 0
          while selection < 1 or selection > len(option_list): 
               try:           
                    selection = int(input('Enter The Number Associated with your choice > '))
               except ValueError:
                    continue 
          return option_list[selection - 1]
          


     def view_books(self, mode = None):
          """
             Menu that show all book operations,
             displays books and allows for navigation
             between each operation This method makes use of recursion).
             
             Parameter
             mode(None): serves as a placeholder for the list of 
             specific items based on which navigation can occur
     
             Returns: None
          """
          if mode == None:
               mode = self.books.books          
          print()
          self.books.display_book_list(mode)
          print('\n1. Add Book\n2. Remove Book\n3. Search For Book\n4. Update Book Details\n5. Show Book Details\n6. Clear Book List\n7. Exit\n')
          choice = self.select([1, 2, 3, 4, 5, 6, 7])
          if choice == 1:
               self.books.add_book()
          elif choice == 2:
               print('Which Book Do You Want To Delete ', end = '')               
               
               del_book = self.select(mode)
               print('Are You Sure?\n1. Y\n2. N')
               inner_choice = self.select(['Y', 'N'])
               if inner_choice == 'Y':                   
                    print(self.books.remove_book(del_book))
               
          elif choice == 3:
               target = input('Type Your Search ')
               search_result = self.books.search(mode, target)
               if len(search_result) == 0:
                    print('Search Not Found')
               else:
                    self.view_books(mode = search_result)
          elif choice == 4:
               print('Which Book Do You Want To Update', end = '')
               possible_updatee = self.select(mode)
               print('Are You Sure?\n1. Y\n2. N')
               inner_choice = self.select(['Y', 'N'])
               if inner_choice == 'Y':          
                    self.books.update_book_info(possible_updatee)
                    
          elif choice == 5:
               print('Which Book\'s Info do you want to see')
               self.books.show_book_info(self.select(mode))
               
          elif choice == 6:
               print('Are You Sure?\n1. Y\n2. N')
               inner_choice = self.select(['Y', 'N'])
               if inner_choice == 'Y':
                    self.books.clear_book_list()
                    
                                      
          elif choice == 7:
               print('Are You Sure?\n1. Y\n2. N')
               inner_choice = self.select(['Y', 'N'])
               if inner_choice == 'Y':          
                    raise SystemExit

          input('\nPress Any key To Continue ')
          self.view_books()
          





     def home(self):
          """
             Displays the home screen for the user
             and serves as the base for all navigation 
             
             Parameter: None
             
             Returns: None
          """
          print(('\033[1m\033[3m   Book Management System   \033[0m \n').center(50))
          print('\n\n1. View Books\n2. Exit\n')
          choice = self.select([1, 2])
          if choice == 1:
               self.view_books()
          else:
               return 
          
          
          
          
          
          
          
          
          
          
          



if __name__ == '__main__':
     
     book_management_system = Book_Interface()
     book_management_system.home()
     