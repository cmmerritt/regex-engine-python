def heading(string, markdown=1):
    if markdown <= 1:
        return "#" + ' ' + string
    elif 1 < markdown < 6:
        return "#" * markdown + ' ' + string
    else:
        return "#" * 6 + ' ' + string
