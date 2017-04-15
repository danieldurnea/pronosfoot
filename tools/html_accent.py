#encoding:latin-1
"""
HTML FRENCH ACCENT MODULE
"""
import copy

def accent_to_html_code(str):
    """
    converts most common accented letter
    from french into corresponding html code
    """
    newstr = copy.copy(str)
    newstr = newstr.replace('�','&ucirc;')
    newstr = newstr.replace('�','&ecirc;')
    newstr = newstr.replace('�','&eacute;')
    newstr = newstr.replace('�','&egrave;')
    newstr = newstr.replace('�','&agrave;')

    newstr = newstr.replace('\xfb','&ucirc;')
    newstr = newstr.replace('\xea','&ecirc;')
    newstr = newstr.replace('\xe9','&eacute;')
    newstr = newstr.replace('\xe8','&egrave;')
    newstr = newstr.replace('\xe0','&agrave;')

    return newstr

if __name__ == '__main__':
    mystr = '_�_�_�_�_�'
    print(accent_to_html_code(mystr))