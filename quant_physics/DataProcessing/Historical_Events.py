def create_event(name, start_date, end_date):
    '''
    List of Historical Events which would be nice to have on command

    Inputs:
    * name (string) - Name of the event
    * start_date 
    * end_date
    '''
    dictionary_of_event = dict(name = name,
                               start_date = start_date,
                               end_date = end_date)

    return dictionary_of_event


