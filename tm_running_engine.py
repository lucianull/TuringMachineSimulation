from tm_validation_engine import TuringMachine


if __name__ == '__main__':
    Turing_Machine = TuringMachine("tm_config_file.txt")
    input_string = input("Introduceti input-ul pentru Turing Machine: ")
    if Turing_Machine.Run(input_string):
        print("Accepted")
    else:
        print("Rejected")