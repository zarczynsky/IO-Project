import python_files

result2 = python_files.list_directory('.\\', 'py')

my_catalogs = []
for el in result2:
    my_catalogs.append(el.split('.')[0])


def how_many_lines(file):

    try:
        first = open('graf.txt', 'a')
        first.write("Number of lines in the file: \n")
        first.close()
        for el in file:
            with open(el, 'r') as f:
                lines = 0
                for line in f:
                    if line != '\n':
                        lines += 1

            with open('graf.txt', 'a') as fi:

                fi.write(el)
                fi.write(" ")
                fi.write(str(lines))
                fi.write("\n")
    except IndexError as m:
        print(m)
        print("Lack of file")


def file_connect(file):
    try:
        fi = open('graf.txt', 'a')
        fi.write("Connect file: \n")
        for first in file:
            zmienna_do_polaczen = []
            with open(first, 'r') as f:
                for line in f:
                    polaczenia = line.split()
                    if polaczenia and (polaczenia[0] == 'import'):
                        for plik in my_catalogs:
                            if polaczenia[1] == plik:
                                zmienna_do_polaczen.append(polaczenia[1])
            fi.write(first)
            fi.write(' ')
            fi.write(str(zmienna_do_polaczen))
            fi.write('\n')

        fi.close()

    except IndexError as m:
        print(m)
        print("Lack of file")

'''def file_connect_weight(file):
    try:
        fi = open('graf.txt', 'a')
        fi.write("Connect file\n")
        for first in file:
            zmienna_do_polaczen = []
            with open(first, 'r') as f:
                for line in f:
                    polaczenia = line.split()
                    if polaczenia and (polaczenia[0] == 'import'):
                        zmienna_do_polaczen.append(polaczenia[1])
            fi.write(first)
            fi.write(' ')
            fi.write(str(zmienna_do_polaczen))
            fi.write('\n')

        fi.close()

    except IndexError as m:
        print(m)
        print("Lack of file")'''
