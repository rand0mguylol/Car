from format_file_list import format_file_list

def get_id_info(filename, id_list):
  target_list = []
  file_list = format_file_list(filename)
  target_list.append(file_list[0]) # Append header
  for row in file_list:
      if row[0] in id_list:
        target_list.append(row)
  
  return target_list
    