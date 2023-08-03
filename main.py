from chat_parameters.interaction import chat_conversation
from chat_parameters.mapping import mapping as mapping_func


def main():
    chat_conversation.greeting()
    while True:
        data = input(f'Arpan: ')
        mapping_func(data)
    

if __name__ == "__main__":
    main()