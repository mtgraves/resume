import os

def cls_file_path():
    '''
    build a filepath for the alta cls file so that tex can find it.  It expects
    all filepaths to be in nix format (forward slashes).
    '''
    # ensure that the class file is able to be found
    alta_cls_file_og = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'altacv'
    )

    # latex will not take windows style path in for documentclass, so we
    # we convert if we detect a windows style filepath
    split_windows_path = alta_cls_file_og.split('\\')
    
    # ( this maybe could be improved with string replacement.. ) 
    # alta_cls_file = alta_cls_file_og.replace('\\', '/')
    if len(split_windows_path) > 1:
        alta_cls_file = ''
        for fpath_part_i, fpath_part in enumerate(split_windows_path):
            if fpath_part_i != len(split_windows_path)-1:
                alta_cls_file += str(fpath_part) + '/'
            else:
                alta_cls_file += str(fpath_part)
    else:
        alta_cls_file = alta_cls_file_og
    
    return alta_cls_file

def build_strength_group(strength_vals:dict, line_char_max:int):
    '''builds a strength group, ensuring
    that the tags are wrapped based on some (rudimentary)
    length limit to avoid horizontal overflow.
    '''
    resume_str = r''
    line_char_count = 0
    # iterate the kvps inside of this particular
    for exp_i_count, exp_i in enumerate(strength_vals.values()):
        line_char_count += len(exp_i['skill'])
        # if we are under the limit with our new tag, we add it
        # to the list and continue.
        if line_char_count < line_char_max:
            resume_str += r'\cvtag{'+str(exp_i['skill'])+r'}'
        # otherwise, we add a new line then add the tag,
        # then reset the line character count to that of the current
        # tags length.
        else:
            # we do not add a line break for the first element
            if exp_i_count != 0:
                resume_str += r'\\'
            resume_str += r'\cvtag{'+str(exp_i['skill'])+r'}'
            line_char_count = len(exp_i['skill'])

    # ensure we have a line break between strength types
    resume_str += r'\\'

    return resume_str

def build_strengths(resume_info, show_skill_ratings):
    '''returns tex for the skills section
    '''
    
    resume_str = r''
    if show_skill_ratings:
        resume_str += r'''
            \skillsection{Software Development}
            \vspace{0.5em}
            '''
        for exp_i_count, exp_i in enumerate(resume_info['strengths']['software_development'].values()):
            resume_str += r'\skill{'+str(exp_i['skill'])+r'}{'+str(exp_i['rating'])+r'}'

        resume_str += r'''
            \vspace{1.0em}
            \skillsection{Programming Languages}
            \vspace{0.5em}
            '''
        for exp_i_count, exp_i in enumerate(resume_info['strengths']['programming'].values()):
            resume_str += r'\skill{'+str(exp_i['skill'])+r'}{'+str(exp_i['rating'])+r'}'
        resume_str += r'''
            \vspace{1.0em}
            \skillsection{Other}
            \vspace{0.5em}
            '''
        for exp_i_count, exp_i in enumerate(resume_info['strengths']['other'].values()):
            resume_str += r'\skill{'+str(exp_i['skill'])+r'}{'+str(exp_i['rating'])+r'}'
    else:
        resume_str += r'''
        \cvsection{Strengths}
            '''
        line_char_max = 20
        for strength_key in resume_info['strengths'].keys():
            resume_str += build_strength_group(resume_info['strengths'][strength_key], line_char_max)
    
    return resume_str


def resume(
    resume_info,
    background_color='E2E2E2',
    primary_font_color='666666',
    show_skill_ratings=True,
):
    '''
    build out the tex file from a resume info object for altacv format
    '''
    
    alta_cls_file = cls_file_path()
    
    resume_str = r'''
%%%%%%%%%%%%%%%%%
% This is an sample CV template created using altacv.cls
% (v1.3, 10 May 2020) written by LianTze Lim (liantze@gmail.com). Now compiles with pdfLaTeX, XeLaTeX and LuaLaTeX.
% This fork/modified version has been made by Nicolás Omar González Passerino (nicolas.passerino@gmail.com, 15 Oct 2020)
%
%% It may be distributed and/or modified under the
%% conditions of the LaTeX Project Public License, either version 1.3
%% of this license or (at your option) any later version.
%% The latest version of this license is in
%%    http://www.latex-project.org/lppl.txt
%% and version 1.3 or later is part of all distributions of LaTeX
%% version 2003/12/01 or later.
%%%%%%%%%%%%%%%%

%% If you need to pass whatever options to xcolor
\PassOptionsToPackage{dvipsnames}{xcolor}

%% If you are using \orcid or academicons
%% icons, make sure you have the academicons
%% option here, and compile with XeLaTeX
%% or LuaLaTeX.
% \documentclass[10pt,a4paper,academicons]{'''+str(alta_cls_file)+r'''}

%% Use the "normalphoto" option if you want a normal photo instead of cropped to a circle
% \documentclass[10pt,a4paper,normalphoto]{altacv}

%% Fork: CV dark mode toggle enabler to use a inverted color palette.
%% Use the "darkmode" option if you want a color palette used to 
% \documentclass[10pt,a4paper,darkmode]{altacv}
\documentclass[10pt,letterpaper,ragged2e,withhyper]{'''+str(alta_cls_file)+r'''}

%% AltaCV uses the fontawesome5 and academicons fonts
%% and packages.
%% See http://texdoc.net/pkg/fontawesome5 and http://texdoc.net/pkg/academicons for full list of symbols. You MUST compile with XeLaTeX or LuaLaTeX if you want to use academicons.

% Change the page layout if you need to
\geometry{left=1.2cm,right=1.2cm,top=1cm,bottom=1cm,columnsep=0.75cm}

% The paracol package lets you typeset columns of text in parallel
\usepackage{paracol}

% Change the font if you want to, depending on whether
% you're using pdflatex or xelatex/lualatex
\ifxetexorluatex
  % If using xelatex or lualatex:
  \setmainfont{Roboto Slab}
  \setsansfont{Lato}
  \renewcommand{\familydefault}{\sfdefault}
\else
  % If using pdflatex:
  \usepackage[rm]{roboto}
  \usepackage[defaultsans]{lato}
  % \usepackage{sourcesanspro}
  \renewcommand{\familydefault}{\sfdefault}
\fi

% Fork: Change the color codes to test your personal variant on any mode
\ifdarkmode%
  \definecolor{PrimaryColor}{HTML}{0F52D9}
  \definecolor{SecondaryColor}{HTML}{3F7FFF}
  \definecolor{ThirdColor}{HTML}{F3890B}
  \definecolor{BodyColor}{HTML}{ABABAB}
  \definecolor{EmphasisColor}{HTML}{ABA2A2}
  \definecolor{BackgroundColor}{HTML}{242424}
\else%
  \definecolor{PrimaryColor}{HTML}{001F5A}
  \definecolor{SecondaryColor}{HTML}{0039AC}
  \definecolor{ThirdColor}{HTML}{F3890B}
  \definecolor{BodyColor}{HTML}{'''+str(primary_font_color)+r'''}
  \definecolor{EmphasisColor}{HTML}{2E2E2E}
  \definecolor{BackgroundColor}{HTML}{'''+str(background_color)+r'''}
\fi%

\colorlet{name}{PrimaryColor}
\colorlet{tagline}{PrimaryColor}
\colorlet{heading}{PrimaryColor}
\colorlet{headingrule}{ThirdColor}
\colorlet{subheading}{SecondaryColor}
\colorlet{accent}{SecondaryColor}
\colorlet{emphasis}{EmphasisColor}
\colorlet{body}{BodyColor}
\pagecolor{BackgroundColor}

% Change some fonts, if necessary
\renewcommand{\namefont}{\Huge\rmfamily\bfseries}
\renewcommand{\personalinfofont}{\small\bfseries}
\renewcommand{\cvsectionfont}{\LARGE\rmfamily\bfseries}
\renewcommand{\cvsubsectionfont}{\large\bfseries}

% Change the bullets for itemize and rating marker
% for \cvskill if you want to
\renewcommand{\itemmarker}{{\small\textbullet}}
\renewcommand{\ratingmarker}{\faCircle}

%% sample.bib contains your publications
%% \addbibresource{sample.bib}

\begin{document}
    \name{'''+str(resume_info['applicant_info']['name'])+r'''}
    \tagline{'''+str(resume_info['applicant_info']['title'])+r'''}
    
    \personalinfo{
        \email{'''+str(resume_info['applicant_info']['email'])+r'''}\smallskip
        \phone{'''+str(resume_info['applicant_info']['phone'])+r'''}
        \location{'''+str(resume_info['applicant_info']['location'])+r'''}\\
        % \linkedin{johnDoe}
        %\github{johnDoe}
        %\dev{johnDoe}
        %\homepage{nicolasomar.me}
        %\medium{nicolasomar}
        %% You MUST add the academicons option to \documentclass, then compile with LuaLaTeX or XeLaTeX, if you want to use \orcid or other academicons commands.
        % \orcid{0000-0000-0000-0000}
        %% You can add your own arbtrary detail with
        %% \printinfo{symbol}{detail}[optional hyperlink prefix]
        % \printinfo{\faPaw}{Hey ho!}[https://example.com/]
        %% Or you can declare your own field with
        %% \NewInfoFiled{fieldname}{symbol}[optional hyperlink prefix] and use it:
        % \NewInfoField{gitlab}{\faGitlab}[https://gitlab.com/]
        % \gitlab{your_id}
    }
    
    \makecvheader
    %% Depending on your tastes, you may want to make fonts of itemize environments slightly smaller
    % \AtBeginEnvironment{itemize}{\small}
    
    %% Set the left/right column width ratio to 6:4.
    \columnratio{0.25}

    % Start a 2-column paracol. Both the left and right columns will automatically
    % break across pages if things get too long.
    \begin{paracol}{2}

        % ------ CONTACT -----
        %\cvsection{Contact}
        %    \personalinfo{
        %        \email{'''+str(resume_info['applicant_info']['email'])+r'''}\smallskip\\
        %        \phone{'''+str(resume_info['applicant_info']['phone'])+r'''\\}
        %        \location{'''+str(resume_info['applicant_info']['location'])+r'''}\\
        %    }
        % ----- CONTACT -----

        % ----- ABOUT ME -----
        \cvsection{Objective}
            \begin{quote}\small
            '''+str(resume_info['applicant_info']['objective'])+r'''
            \end{quote}
        % ----- ABOUT ME -----

        \vspace{1.0em}

        % ----- STRENGTHS -----
        '''
    resume_str += build_strengths(resume_info, show_skill_ratings)
    resume_str += r'''

        % use ONLY \newpage if you want to force a page break for
        % ONLY the current column
        \newpage
        
        %% Switch to the right column. This will now automatically move to the second
        %% page if the content is too long.
        \switchcolumn
        
        % ----- EXPERIENCE -----
        \cvsection{Experience}
'''
    for exp_i_count, exp_i in enumerate(resume_info['experience'].values()):
        resume_str += r'\cvevent{'+exp_i['title']+r'}{| '+fr"{exp_i['company']}"+r'}{'+exp_i['tenure_start']+r' - '+exp_i['tenure_end']+r'}{}'
        resume_str += r'''
        '''
        if 'highlights' in exp_i:
            resume_str += r'\begin{itemize}'
            for highlight_i in exp_i['highlights'].values():
                resume_str += r'\item '+highlight_i+r'\\'
            resume_str += r'\end{itemize}'
        
        if exp_i_count < len(resume_info['experience'].values())-1:
            resume_str += r'\divider\\'
    resume_str += r'''    
        % ----- EXPERIENCE -----
        % ----- EDUCATION -----
        \cvsection{Education}
'''
    for exp_i_count, exp_i in enumerate(resume_info['education'].values()):
        resume_str += r'\cvevent{'+exp_i['degree']+r'}{| '+exp_i['school']+r'}{'+exp_i['year_graduated']+r'}{}'
        resume_str += r'''
        '''
        if 'highlights' in exp_i:
            resume_str += r'\begin{itemize}'
            for highlight_i in exp_i['highlights'].values():
                resume_str += r'\item '+highlight_i+r'\\'
            resume_str += r'\end{itemize}'
        
        if exp_i_count < len(resume_info['education'].values())-1:
            resume_str += r'\divider\\'
    resume_str += r'''
        % ----- EDUCATION -----
        \end{paracol}
        \newpage
        % ----- PUBLICATIONS -----
        \cvsection{Publications}
'''
    for exp_i_count, exp_i in enumerate(resume_info['publications'].values()):
        resume_str += r'\cveventtwo{'+exp_i['journal']+r'}{| '+exp_i['title']+r' |}{ '+str(exp_i['year'])+r'}{}'
        resume_str += r'''
        '''
        resume_str += r'\begin{itemize}[label = {}]'
        resume_str += r'\item '+str(exp_i['authors'])+r' | DOI: '+str(exp_i['doi'])+r' | '+str(exp_i['status'])+r'\\'
        resume_str += r'\end{itemize}'

        if exp_i_count < len(resume_info['publications'].values())-1:
            resume_str += r'\divider\\'
    resume_str += r'''
        % ----- PUBLICATIONS -----
        % ----- HONORS/AWARDS -----
        \cvsection{Honors/Awards}
'''
    for exp_i_count, exp_i in enumerate(resume_info['honors'].values()):
        resume_str += r'\cveventtwo{'+exp_i['org']+r'}{| '+exp_i['title']+r' |}{ '+str(exp_i['year'])+r'}{}'
    resume_str += r'''
        % ----- HONORS/AWARDS -----

        % ----- PROJECTS -----
        %\cvsection{Projects}
        %    \cvevent{Project 1 }{\cvrepo{| \faGithub}{https://github.com/user/repo}\cvrepo{| \faGlobe}{https://repo-demo.com/}}{Mm YYYY -- Mm YYYY}{}
        %    \begin{itemize}
        %        \item Item 1
        %        \item Item 2
        %    \end{itemize}
        %    \divider
        %    
        %    \cvevent{Project 1 }{\cvrepo{| \faGitlab}{https://gitlab.com/user/repo}\cvrepo{| \faGlobe}{https://repo-demo.com/}}{Mm YYYY -- Mm YYYY}{}
        %    \begin{itemize}
        %        \item Item 1
        %        \item Item 2
        %    \end{itemize}
        % ----- PROJECTS -----
    %\end{paracol}
\end{document}
'''
    return resume_str