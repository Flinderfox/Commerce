from django import template
from django.utils import timezone

register = template.Library()


# Filter search : searches a list for a key
@register.filter(name='search')
def search(value, id):
    """
    Parameters
    ----------
    value : list
        A list with key values
    id : int
        The key we are searching
    
    Returns
    ------
    boolean
        True if the key is found, False otherwise.
    """
    for v in value:
        if v.id == id:
            return True
    return False

# Filter time_left : string representation of the auction’s time left
@register.filter(name="time_left")
def time_left(value):
    """
    Parameters
    ----------
    value : DateTime
        The deadline
    
    Returns
    ------
    string
        Remaining time in minutes and seconds
    """    
    t = value - timezone.now()
    days, seconds = t.days, t.seconds
    hours = days * 24 + seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    st = str(minutes) + "m " + str(seconds) + "s"
    return st

# Filter current_price : the current price of the auction item based on the number of bids
@register.filter(name="current_price")
def current_price(value):
    """
    Parameters
    ----------
    value : IntegerField
        Number of Bids.
    
    Returns
    ------
    string
        Current value with two decimals.
    """
    current_cost = 0.20 + (value.number_of_bids * 0.20)
    current_cost = "%0.2f" % current_cost
    return current_cost