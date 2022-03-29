
def convert_md_str_to_tex(markdown_string):
    '''converts individual markdown style strings to LaTeX formatting including:
    - backticks to colorbox (for code highlighting)
    - ampersand
    - tilde to sim
    - dollar sign
    - hyperlinks
    - asterisk to italics

    :param markdown_string: string in markdown formatting
    '''
    tex_string = r''
    found_backtick_start = False
    found_italics_start = False

    # detect hyperlink
    # this is broken for the case of brackets being in the string
    # this could likely be done better with regex...
    if "](" in markdown_string:
        
        # we could first iterate the characters and see if []() come
        # in the correct order and are all there?
        brackets_found = []
        for str_ch_i, str_ch in enumerate(markdown_string):
            if str_ch in ['[', ']', '(', ')']:
                brackets_found.extend([
                    {
                        'char': str_ch,
                        'index': str_ch_i,
                    }
                ])

        # group them and check for correct ordering etc
        # ... this is where the multi-link logic should live

        # ...but for now we just handle the first one encountered in the string (jank)
        sq_open_index = markdown_string.find('[')
        sq_close_index = markdown_string.find(']')
        par_open_index = markdown_string.find('(')
        par_close_index = markdown_string.find(')')

        # add on beginning of markdown string (if not just a hyperlink)
        tex_string += markdown_string[:sq_open_index]


        tex_string += r'\href{'
        tex_string += markdown_string[par_open_index+1:par_close_index]
        tex_string += r'}'

        tex_string += r'{'
        tex_string += markdown_string[sq_open_index+1: sq_close_index]
        tex_string += r'}'

        # add on end of markdown string
        tex_string += markdown_string[par_close_index+1:]
        
    
    else:
        # deal with individual character conversions
        for str_ch in markdown_string:
            
            # backticks
            if str_ch == '`':
                if not found_backtick_start:
                    found_backtick_start = True
                    tex_string += r'\colorbox{lightgray}{'
                else:
                    found_backtick_start = False
                    tex_string += r'}'
            # italics
            elif str_ch == '*':
                if not found_italics_start:
                    found_italics_start = True
                    tex_string += r'\textit{'
                else:
                    found_italics_start = False
                    tex_string += r'}'
            # tilde (~)
            elif str_ch == '~':
                tex_string += r'$\sim$'
            # ampersand (&)
            elif str_ch == '&':
                tex_string += r'\&'
            # dollar sign ($)
            elif str_ch == '$':
                tex_string += r'\$'
            else:
                tex_string += str_ch

    return tex_string