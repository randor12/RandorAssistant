"""
:author: Ryan Nicholas
:date: April 15, 2020
:description: Attempt at creating a smart assistant
"""

from AudioListener import AudioListener as al


def main():
    """
    Main code here
    :return: None
    """
    try:
        mic = al()
        mic.backgroundListener()
    except KeyboardInterrupt:
        print("Exited program")
    # # check if the person is talking to the smart assistant
    # if text is not None and 'hey randor' in text.lower():
    #     speak = Speaker()
    #     speak.respond('Go ahead Ryan')
    #     # initialize recording sound for a command
    #     print("State Command: ")
    #     command = mic.startMicrophone()
    #     response = cmd(command)
    #     # respond to the command
    #     response.result()
    # if text is not None and 'exit' in text.lower():
    #     break


if __name__ == '__main__':
    """
    Main of the code
    """
    main()
