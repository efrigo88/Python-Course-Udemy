import shelve

# example dictionary
# books = {'recepies': {'blt': ['bacon', 'lettuce', 'tomato', 'bread'],
#                       'beans on toast': ['beans', 'bread'],
#                       'scrambled eggs': ['eggs', 'butter', 'milk'],
#                       'soup': ['tin of soup'],
#                       'pasta': ['pasta', 'cheese']
#                       },
#          'maintenance': {'stuck': ['oil'],
#                          'loose': ['gaffer tape']
#                          }
#         }

# print(books['recepies']['soup'])
# print(books['recepies']['scrambled eggs'])
# print(books['maintenance']['loose'])

# to convert it to a shelve

books = shelve.open('book')
books['recepies'] = {'blt': ['bacon', 'lettuce', 'tomato', 'bread'],
                     'beans on toast': ['beans', 'bread'],
                     'scrambled eggs': ['eggs', 'butter', 'milk'],
                     'soup': ['tin of soup'],
                     'pasta': ['pasta', 'cheese']
                      }
books['maintenance'] = {'stuck': ['oil'],
                        'loose': ['gaffer tape']
                       }


print(books['recepies']['beans on toast'])



books.close()