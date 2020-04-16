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
    mic = al()
    text = mic.startMicrophone()
    # check if the person is talking to the smart assistant
    if text.lower() == 'hey randor':
        # initialize recording sound for a command
        command = mic.startMicrophone()
        response = cmd(command)
        # respond to the command
        response.result()


if __name__ == '__main__':
    """
    Main of the code
    """
    main()
