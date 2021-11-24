def csv_read(directory,convert_list_of_lists=True):
  directory = directory + '.csv' if '.csv' not in directory else directory 

  with open(directory, 'r') as csvfile:
    lol = []
    l = csv.reader(csvfile)
    for row in l:
      lol.append(row)
      if convert_list_of_lists:
        array = list_of_list_to_dictionary(lol)
        return array
      else:
        return lol 