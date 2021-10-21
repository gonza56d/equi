"""Format SQL files."""

from sys import argv


class CommandException(Exception):
    pass


def format(file: str) -> None:
    formatted_text = ''
    with open(file, 'r') as sql_file:
        for line in sql_file:
            if not line.startswith('impala'):
                for word in line.split():
                    if '${' not in word:
                        pass

            else:
                formatted_text = formatted_text.join(line)



        formatted_text = ''.join(
            [line.upper() if is_safe(line) else line for line in sql_file]
        )
        print(line)


if __name__ == '__main__':
    try:
        format(argv[1])
    except IndexError:
        raise CommandException('\n\nDebe indicar el archivo SQL a formatear.\n'
            + 'Ejemplo: sql_formatter.py my_query.sql')
    