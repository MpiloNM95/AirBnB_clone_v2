#!/usr/bin/python3
"""
Command interpreter for AirBnB project

"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.city import City

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    class_types = ['Basemodel', 'User', 'Amenity', 'Place', 'Review', 'State', 'City']
    intro = ' Welcome to AirBnB CLI!\n Type "?" or "help" to list commands \n Type "quit" or "x" or "q" to exit the CLI'

    def do_quit(self, input):
        '''Exit the command interpreter. Shorthand type x or q'''
        print('Goodbye from the AirBnB CLI');
        return True

    def emptyline(self):
        '''This method is called when an empty line + ENTER is pressed, to prevent execution of previous commands'''
        pass

    def default(self, input):
        '''This method is called when an unknown command is sent'''
        if input == 'x' or input == 'q':
            return self.do_quit(input)
        else:
            print('"{}" : Unknown command. Type "help" or "?" for more information'.format(input))


    def do_EOF(self, line):
         '''Exit the command interpreter.'''
         print('Goodbye from the AirBnB CLI')
         return True

    
    def do_create(self, arg):
        '''Creates a new instance of BaseModel'''
        args = arg.split()

        if len(args) < 1:
            print('** class name missing **')
        elif args[0] not in HBNBCommand.class_types:
            print("** class doesn't exist **")
        else:
            for key in HBNBCommand.class_types:
                if key == args[0]:
                    new_obj = eval("{}()".format(args[0]))
            new_obj.save()
            print(new_obj.id)
            
    def do_show(self, arg):
        '''Prints the string representation of
        an instance based on the class name
        '''
        args = arg.split()
        if len(args) < 1:
            print*('** Missing class name **')
        elif args[0] not in HBNBCommand.class_types:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print('** instance id missing **')
        else:
            arg_id = '{}.{}'.format(args[0], args[1])
            all_objects = storage.all()
            if arg_id in all_objects:
                print(all_objects[arg_id])
            else:
                print('** no instance found **')
            

    def do_update(self, arg):
        '''Updates an instance based on the class name
        and id by adding or updating an attribute
        
        Args:
            line(args): receives the commands:
            <class name> <id> <attribute name> "<attribute value>"
            Example: 'update User 1234-1234-1234 my_name "Jon"'
        '''
    
        args = arg.split()
        all_objects = storage.all()

        if len(args) == 0:
            print('**Missing class name**')
        elif args[0] not in HBNBCommand.class_types:
            print("** class doesn't exist**")
        elif len(args) < 2:
            print('** instance id missing **')
        else:
            key = args[0] + '.' + args[1]
            if key in all_objects:
                if len(args) < 3:
                    print('** attribute name missing **')
                elif len(args) < 4:
                    print('** value missing **')
                else:
                    obj_dict = all_objects[key].to_dict()
                    my_obj = all_objects[key]
                    if args[2] in obj_dict:
                        cast = type(my_obj.args[3])
                        cast(args[3])
                    setattr(my_obj, args[2], args[3])
                    my_obj.save()
            else:
                print('** no instance found **')

    def do_destroy(self, args):
        '''Deletes an instance based on the class name and id'''
        args = args.split()
        all_objects = storage.all()

        if len(args) < 1:
            print('** Missing class name **')
        elif args[0] not in HBNBCommand.class_types:
            print("** classs doesn't exist**")
        elif len(args) < 2:
            print('** instance id missing **')
        else:
            key = args[0] + '.' + args[1]
            if key in all_objects:
                del all_objects[key]
                storage.save()
            else:
                print('** no instance found **')
                
    def do_all(self, arg):
        '''
        Prints all representation of all instances
        based on the class name
        '''
        list_instan = []
        args = arg.split()
        all_objects = storage.all()
        if len(args) == 0:
            for key in all_objects:
                list_instan.append(all_objects[key].__str__())
            print(list_instan)
        else:
            if args[0] in HBNBCommand.class_types:
                for key in all_objects:
                    if args[0] in key:
                        list_instan.append(all_objects[key].__str__())
                        print(list_instan)
            else:
                print("** class doesn't exist**") 

    def do_User(self, arg):
        '''Pass'''

        CMD_MATCH = {
            '.all()': self.do_all,
            # 'count()': self.__count,
            '.show()': self.do_show,
            '.destroy()': self.do_destroy,
            '.update()': self.do_update,
            '.create()': self.do_create
        }

        if '(' and ')' in arg:
            for key, value in CMD_MATCH.items():
                if key == arg:
                    value('User')    

    def do_Amenity(self, arg):
        '''Pass'''

        CMD_MATCH = {
            '.all()': self.do_all,
            # 'count()': self.__count,
            '.show()': self.do_show,
            '.destroy()': self.do_destroy,
            '.update()': self.do_update,
            '.create()': self.do_create
        }

        if '(' and ')' in arg:
            for key, value in CMD_MATCH.items():
                if key == arg:
                    value('Amenity')    

    def do_City(self, arg):
        '''Pass'''

        CMD_MATCH = {
            '.all()': self.do_all,
            # 'count()': self.__count,
            '.show()': self.do_show,
            '.destroy()': self.do_destroy,
            '.update()': self.do_update,
            '.create()': self.do_create
        }

        if '(' and ')' in arg:
            for key, value in CMD_MATCH.items():
                if key == arg:
                    value('City')    

    def do_Place(self, arg):
        '''Pass'''

        CMD_MATCH = {
            '.all()': self.do_all,
            # 'count()': self.__count,
            '.show()': self.do_show,
            '.destroy()': self.do_destroy,
            '.update()': self.do_update,
            '.create()': self.do_create
        }

        if '(' and ')' in arg:
            for key, value in CMD_MATCH.items():
                if key == arg:
                    value('Place')    
    
    def do_Review(self, arg):
        '''Pass'''

        CMD_MATCH = {
            '.all()': self.do_all,
            # 'count()': self.__count,
            '.show()': self.do_show,
            '.destroy()': self.do_destroy,
            '.update()': self.do_update,
            '.create()': self.do_create
        }

        if '(' and ')' in arg:
            for key, value in CMD_MATCH.items():
                if key == arg:
                    value('Review')    

    def do_State(self, arg):
        '''Pass'''

        CMD_MATCH = {
            '.all()': self.do_all,
            # 'count()': self.__count,
            '.show()': self.do_show,
            '.destroy()': self.do_destroy,
            '.update()': self.do_update,
            '.create()': self.do_create
        }

        if '(' and ')' in arg:
            for key, value in CMD_MATCH.items():
                if key == arg:
                    value('State')    

    def do_BaseModel(self, arg):
        '''Pass'''

        CMD_MATCH = {
            '.all()': self.do_all,
            # 'count()': self.__count,
            '.show()': self.do_show,
            '.destroy()': self.do_destroy,
            '.update()': self.do_update,
            '.create()': self.do_create
        }

        if '(' and ')' in arg:
            for key, value in CMD_MATCH.items():
                if key == arg:
                    value('BaseModel')    

    def do__count(self, cls, arg):
        new_arg = arg.split('.')
        if new_arg == 'count()':
            cls.count()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
