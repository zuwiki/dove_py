def PrintOutput(message):
    '''
    Simply prints the output
    '''

    print message

class Logger(object):
    '''
    Takes log messages and calls the output member on them
    '''

    def __init__(self, output=PrintOutput):
        self.output = output

        self("Started Logger module.")

    def __call__(self, message):
        self.output(message)
