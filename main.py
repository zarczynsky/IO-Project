import functions
import python_files


result = python_files.list_directory('.\\', 'py')

functions.how_many_lines(result)
functions.file_connect(result)

