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

def main():
    machine = MealyMachine()
    while True:
        input_str = input("Enter a binary string (sequence of 0s and 1s): ")
        result = machine.process(input_str)
        print("Output:", result)
        cont = input("Do you want to input another binary string? (y/n): ").lower()
        if cont != 'y':
            print("Exiting program. Goodbye!")
            break

if __name__ == "__main__":
    main()