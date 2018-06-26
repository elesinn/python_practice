import cmd
from math import sqrt, floor
 
class robot(cmd.Cmd):
    position = [0, 0]

    def do_left(self, arg):
        self.position[0] -= float(arg) 

    def do_right(self, arg):
        self.position[0] += float(arg)

    def do_forward(self, arg):
        self.position[1] += float(arg)

    def do_backward(self, arg):
        self.position[1] -= float(arg)
               
    def do_distance(self, arg):
        print int(floor(sqrt(pow(self.position[0], 2) + pow(self.position[1], 2))))

if __name__ == "__main__":
    robot().cmdloop()
