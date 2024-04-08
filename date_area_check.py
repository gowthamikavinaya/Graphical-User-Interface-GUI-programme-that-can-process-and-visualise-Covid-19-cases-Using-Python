from . import stop_search

def check(start, end, area,):
    start_year = start.year
    end_year = end.year
    errors = ""
    if start_year != 2020 or end_year != 2020:
        errors+=("Year should be 2020")
    if not area:
        errors+=("\nArea must be specified")
    return errors


'''Stop and Search checks'''

def sns_check(year, month, area):
    errors = []
    if year not in stop_search.selected_years:
        errors.append("Year is incorrect")
    elif month not in stop_search.months:
        errors.append("MOnth is incorrect")
    elif area not in stop_search.force_list:
        errors.append("Area is incorrect")
    
    return errors
