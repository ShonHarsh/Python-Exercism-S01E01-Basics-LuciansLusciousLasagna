"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

# According to your cookbook, the Lasagna should be in the oven for 40 minutes.
EXPECTED_BAKE_TIME = 40
# Each layer of lasagna takes 2 minutes to prepeare
TIME_PER_LAYER = 2



def bake_time_remaining(elapsed_bake_time):
    """Calculate remaining bake time in minutes.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    """Calculates the preperation time in minutes.

    Parameters
    ----------
    number_of_layers : Int
        The number of layers to be added to the lasagna.

    Returns
    -------
    Int
        How many minutes needed to making the layers of lasagna.

    This function that takes the number of layers you want to add to the lasagna
    as an argument and returns how many minutes you would spend making them.
    Assume each layer takes 2 minutes to prepare.
    """

    return number_of_layers * TIME_PER_LAYER

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculates the total elapsed cooking time (prep + bake) in minutes.
    
    Parameters
    ----------
    number_of_layers : Int
        The number of layers added to the lasagna.
    elapsed_bake_time : Int
        The number of minutes the lasagna has been baking in the oven.

    Returns
    -------
    preparation_time_in_minutes : int
        The preperation time total in minutes.

    This function that has two parameters: number_of_layers (the number of layers
    added to the lasagna) and elapsed_bake_time (the number of minutes the lasagna
    has been baking in the oven). This function should return the total number of
    minutes you've been cooking, or the sum of your preparation time and the time
    the lasagna has already spent baking in the oven.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
