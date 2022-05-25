import re

class TuringMachine:
    def __init__(self, text_file) -> None:
        self.Sigma = set()
        self.States = set()
        self.AlphabetSymbols = set()
        self.Transitions = {}
        self.StartingState = []
        self.FinalStates = []
        with open(text_file) as inFILE:
            while True:
                line = inFILE.readline().rstrip()
                if line == "":
                    break
                if line == "Sigma:":
                    line = inFILE.readline().rstrip()
                    while line != "End":
                        self.Sigma.add(line)
                        line = inFILE.readline().rstrip()
                if line == "States:":
                    line = inFILE.readline().rstrip()
                    while line != "End":
                        line = line.split(", ")
                        if len(line) > 1:
                            if line[1] == "S":
                                self.StartingState.append(line[0])
                            if line[1] == "A":
                                self.FinalStates.append(line[0])
                        self.States.add(line[0])
                        line = inFILE.readline().rstrip()
                if line == "Alphabet Symbols:":
                    line = inFILE.readline().rstrip()
                    while line != "End":
                        self.AlphabetSymbols.add(line)
                        line = inFILE.readline().rstrip()
                if line == "Transitions:":
                    line = inFILE.readline().rstrip()
                    pattern = re.compile(r" |, |->")
                    while line != "End":
                        line = pattern.split(line)
                        if line[0] not in self.Transitions:
                            self.Transitions[line[0]] = {}
                        self.Transitions[line[0]][line[1]] = [line[2], line[3], line[4]]
                        line = inFILE.readline().rstrip()
    

    def Validate(self) -> bool:
        if len(self.StartingState) > 1:
            return 0
        if len(self.FinalStates) > 1:
            return 0
        for x in self.Sigma:
            if x not in self.AlphabetSymbols:
                return 0
        for key in self.Transitions.keys():
            if key not in self.States:
                return 0
            for symbol, values in self.Transitions[key].items():
                if symbol not in self.AlphabetSymbols:
                    return 0
                if values[0] not in self.AlphabetSymbols:
                    return 0
                if values[1] != 'R' and values[1] != "L":
                    return 0
                if values[2] not in self.States:
                    return 0
        return 1


    def Run(self, input_string) ->bool:
        input_string = input_string + '_'
        input_string = list(input_string)
        current_state = self.StartingState[0]
        pos = 0
        while current_state != self.FinalStates[0]:
            current_symbol = input_string[pos]
            if current_symbol not in self.Transitions[current_state]:
                return 0
            input_string[pos] = self.Transitions[current_state][current_symbol][0] 
            if self.Transitions[current_state][current_symbol][1] == 'R':
                pos += 1
            if self.Transitions[current_state][current_symbol][1] == 'L':
                pos -= 1
            current_state = self.Transitions[current_state][current_symbol][2]
        return 1        


if __name__ == '__main__':
    Turing_Machine = TuringMachine("tm_config_file")
    if Turing_Machine.Validate():
        print("The given input for the Turing Machine is valid")
    else:
        print("The given input for the Turing Machine is not valid")
