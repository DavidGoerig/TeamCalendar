from datetime import datetime

"""
    Here define the main function for use them directly in the view
"""

def get_infos(request):
    date_actuelle = datetime.now()
    return {'date_actuelle': date_actuelle}