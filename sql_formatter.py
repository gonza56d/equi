"""Format SQL files.

gonzalomanuel.garcia@equifax.com / gonzalo.garcia01@globant.com"""

from colorama import Fore
from sys import argv


class CommandException(Exception):
    
    def __init__(self, message) -> None:
        super().__init__(Fore.RED + '\n\nError de comando: ' + message)


def is_a_command(line: str) -> bool:
    return line.lstrip().startswith('impala') or line.lstrip().startswith('spark2')


def format(file: str) -> str:
    """Format SQL files by upper-casing everything except by impala/spark
    commands and SQL variables/parameters.
    
    Parameters
    ----------
    file : str - Name of the file to look for and format.
    
    Return
    ------
    str - Formatted text of the file found."""

    formatted_text = ''

    with open(file, 'r') as sql_file:

        for line in sql_file:
            _new_line = line

            if not is_a_command(line):

                splitted = line.split('${')

                for word in splitted:
                    word_to_upper = ''

                    try:  # replace text next to the '}' character, or everything if '}' is not present.
                        bracket_index = word.index('}')
                        word_to_upper = word[bracket_index:]
                    except ValueError:
                        word_to_upper = word

                    _new_line = _new_line.replace(word_to_upper, word_to_upper.upper())

                formatted_text += _new_line

            else:
                formatted_text += line

    return formatted_text


if __name__ == '__main__':
    file_name = ''
    try:
        file_name = argv[1]
        formatted_text = format(file_name)
        with open(f"{file_name.replace('.sql', '')}_formatted.sql", 'w') as formatted_sql:
            formatted_sql.write(formatted_text)
    except IndexError:
        raise CommandException('Debe indicar el archivo SQL a formatear.\n'
            + 'Ejemplo: sql_formatter.py my_query.sql')
    except FileNotFoundError:
        raise CommandException(f'No se pudo encontrar el archivo "{file_name}".')
    