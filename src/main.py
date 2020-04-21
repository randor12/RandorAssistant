"""
:author: Ryan Nicholas
:date: April 15, 2020
:description: Attempt at creating a smart assistant
"""

from AudioListener import AudioListener as al
from commands import Commands as cmd


def main():
    """
    Main code here
    :return: None
    """
    while True:
        mic = al()
        text = mic.startMicrophone()
        # check if the person is talking to the smart assistant
        if text is not None and text.lower() == 'hey randor':
            # initialize recording sound for a command
            print("State Command: ")
            command = mic.startMicrophone()
            response = cmd(command)
            # respond to the command
            response.result()
        if text is not None and text.lower() == 'exit':
            break


if __name__ == '__main__':
    """
    Main of the code
    """
    main()
