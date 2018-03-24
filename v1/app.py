import cmd
import os

from docopt import DocoptExit, docopt
from termcolor import colored


# Creating the classes Book, User, and Admin

class Book(cmd.Cmd):

    def argument_parser(fn):
        '''
        input fn -> function
        return -> a fuction that can parse commandline args using docopt.

        This function re-used as-is(without alteration) from the TDD intro class
        '''
        def get_args(self, args):
            try:
                print(type(args))
                opt = docopt(fn.__doc__, args)
                return fn(self, opt)
            except DocoptExit as e:
                print(e, "Malformed Command")
        return get_args

    def default(self, args):
        invalid_command = args.split(' ')[0]
        print(invalid_command, 'Command Does Not exist')

    @argument_parser
    def do_add_book(self, book_information):
        """
            book_information(dict): User book_information

            Usage:
                add_book <title> <author> <publisher> <copies>
        """
        #TODO
        pass

    @argument_parser
    def do_borrow_book(self, book_information):
        """
            book_information(dict): User book_information

            Usage:
                borrow_book <title> <author> <publisher> <copies>
        """
        #TODO
        pass

    @argument_parser
    def do_delete_book(self, book_information):
        """
            book_information(dict): User book_information

            Usage:
                delete_book <title> <author> <publisher> <copies>
        """
        #TODO
        pass

    @argument_parser
    def do_update_book(self, book_information):
        """
            book_information(dict): User book_information

            Usage:
                update_book <title> <author> <publisher> <copies>
        """
        #TODO
        pass

if __name__ == '__main__':
    app = Book()
    app.cmdloop()
