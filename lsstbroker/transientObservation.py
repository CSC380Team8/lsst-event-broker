"""

This class will get the time value and color observation from each transient
and store that data into each specific transient. Afterwards this data can be used
to classify the data based on this information.

"""


class transientOberservation(object):


    def __init__(time, light_value, color) : # init the time light value and color
    """
    
    this method is to be called on by the event broker when it wants
    to geneerate a transients time, light-value and color, it will return
    a tuple.

    """

    # implement the methods to get this data
