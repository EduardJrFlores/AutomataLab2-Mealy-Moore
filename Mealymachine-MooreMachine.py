class MealyMachine:
    def __init__(self):
        self.state = 'A'
        self.output = []
    
    def reset(self):
        self.state = 'A'
        self.output = []
    
    def process(self, input_str):
        self.reset()
        for ch in input_str:
            if self.state == 'A':
                if ch == '0':
                    self.state = 'B'
                    self.output.append('b')
                else:
                    self.state = 'A'
                    self.output.append('b')
            elif self.state == 'B':
                if ch == '0':
                    self.state = 'B'
                    self.output.append('b')
                else:
                    self.state = 'C'
                    self.output.append('a')
            elif self.state == 'C':
                if ch == '0':
                    self.state = 'B'
                    self.output.append('b')
                else:
                    self.state = 'A'
                    self.output.append('b')
        return ''.join(self.output)

class MooreMachine1:
    def __init__(self):
        self.state = 'A'
        self.state_output = {
            'A': '0',
            'B': '0',
            'C': '1'
        }

    def reset(self):
        self.state = 'A'

    def process(self, input_str):
        self.reset()
        output = [self.state_output[self.state]] 
        for ch in input_str:
            if self.state == 'A':
                if ch == '0':
                    self.state = 'C'
                elif ch == '1':
                    self.state = 'B'
            elif self.state == 'B':
                if ch == '0':
                    self.state = 'C'
                elif ch == '1':
                    self.state = 'B'
            elif self.state == 'C':
                if ch == '0':
                    self.state = 'C'
                elif ch == '1':
                    self.state = 'B'
            output.append(self.state_output[self.state]) 
        return ''.join(output)
    
class MooreMachine2:
    def __init__(self):
        self.state = 'A'
        self.state_output = {
            'A': '0',
            'B': '1',
            'C': '0'
        }

    def reset(self):
        self.state = 'A'

    def process(self, input_str):
        self.reset()
        output = [self.state_output[self.state]] 
        for ch in input_str:
            if self.state == 'A':
                if ch == '0':
                    self.state = 'A'
                elif ch == '1':
                    self.state = 'B'
            elif self.state == 'B':
                if ch == '0':
                    self.state = 'B'
                elif ch == '1':
                    self.state = 'C'
            elif self.state == 'C':
                if ch == '0':
                    self.state = 'B'
                elif ch == '1':
                    self.state = 'C'
            output.append(self.state_output[self.state]) 
        return ''.join(output)

def main():
    while True:
        print("\nChoose the machine you want to use:")
        print("-------------------------------")
        print("1: Mealy Machine")
        print("2: Moore Machine (1's complement)")
        print("3: Moore Machine (2's complement)")
        print("-------------------------------")
        machine_type = input("Enter 1, 2 or 3: ").strip()
        if machine_type == '1':
            machine = MealyMachine()
        elif machine_type == '2':
            machine = MooreMachine1()
        elif machine_type == '3':
            machine = MooreMachine2()
        else:
            print("Invalid input. Please enter 1, 2 or 3.")
            continue

        input_str = input("Enter a binary string (sequence of 0s and 1s): ").strip()
        if not set(input_str).issubset({'0', '1'}):
            print("Invalid input. Please enter only 0s and 1s!")
            continue

        result = machine.process(input_str)
        print("Output:", result)
        cont = input("Do you want to run another input string? (y/n): ").lower().strip()
        if cont != 'y':
            print("Exiting program. Goodbye!")
            break

if __name__ == "__main__":
    main()