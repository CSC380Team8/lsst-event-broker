"""
This class will get the time value and error observation from each transient
and store that data into each specific transient. Afterwards this data can be used
to classify the data based on this information.
"""

class Oberservation(object):

    time = None
    light = None
    error = None

    def __init__(self, time, light_value, error):
        """
        this method is to be called on by the event broker when it wants
        to geneerate a transients time, light-value and error, it will return
        a tuple.
        """

        self.time = time
        self.light = light_value
        self.error = error
