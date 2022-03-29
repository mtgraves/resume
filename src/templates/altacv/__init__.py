import os
def resume(resume_info):
    '''
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
  \definecolor{BodyColor}{HTML}{666666}
  \definecolor{EmphasisColor}{HTML}{2E2E2E}
  \definecolor{BackgroundColor}{HTML}{E2E2E2}
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
            \begin{quote}
            '''+str(resume_info['applicant_info']['objective'])+r'''
            \end{quote}
        % ----- ABOUT ME -----

        \vspace{1.0em}

        % ----- STRENGTHS -----
        \cvsection{Strengths}
        
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
    resume_str += r'''


        %\skill{Python}{5}
        %\skill{Bash}{4}
        %\skill{C++}{2}
        %\skill{Apple Script}{3}
        %\skill{HTML/CSS}{3}
        %\skill{LaTeX}{4}
        
        %\vspace{0.5em}
        %\skillsection{Operating Systems}
        %\skill{Linux}{4}
        %\skill{MacOS}{5}
        %\skill{Windows}{3}
        
        % ----- STRENGTHS -----
        
        % ----- LEARNING -----
        %\cvsection{Learning}
        %    \cvtag{Uno}
        %    \cvtag{Dos}
        %    \cvtag{Tres}
        %    \cvtag{Cuatro}
        %    \cvtag{Cinco}
        %    \cvtag{Seis}
        %    \cvtag{Siete}
        %    \cvtag{Ocho}
        %    \cvtag{Nueve}
        %    \cvtag{Diez}
        %    \medskip
        %    
        %    \cvtag{Rojo}
        %    \cvtag{Amarillo}
        %    \cvtag{Azul}
        %    \cvtag{Verde}
        %    \cvtag{Violeta}
        %    \cvtag{Naranja}
        %    \cvtag{Marron}
        %    \cvtag{Blanco}
        %    \cvtag{Gris}
        %    \cvtag{Negro}
        % ----- LEARNING -----
        
        % ----- LANGUAGES -----
        %\cvsection{Languages}
        %    \cvlang{Lang 1}{Native}\\
        %    \divider
        %    
        %    \cvlang{Lang 2}{Basic / A2}
        %    %% Yeah I didn't spend too much time making all the
        %    %% spacing consistent... sorry. Use \smallskip, \medskip,
        %    %% \bigskip, \vpsace etc to make ajustments.
        %    \smallskip
        % ----- LANGUAGES -----
            
        % ----- REFERENCES -----
        %\cvsection{References}
        %    \cvref{Ref 1}{ref-1}
        %    \divider
        %    
        %    \cvref{Ref 2}{ref-2}
        %    \divider
        %    
        %    \cvref{Ref 3}{ref-3}
        %    \smallskip
        % ----- REFERENCES -----
        
        % ----- MOST PROUD -----
        % \cvsection{Most Proud of}
        
        % \cvachievement{\faTrophy}{Fantastic Achievement}{and some details about it}\\
        % \divider
        % \cvachievement{\faHeartbeat}{Another achievement}{more details about it of course}\\
        % \divider
        % \cvachievement{\faHeartbeat}{Another achievement}{more details about it of course}
        % ----- MOST PROUD -----
        
        % \cvsection{A Day of My Life}
        
        % Adapted from @Jake's answer from http://tex.stackexchange.com/a/82729/226
        % \wheelchart{outer radius}{inner radius}{
        % comma-separated list of value/text width/color/detail}
        % \wheelchart{1.5cm}{0.5cm}{%
        %   6/8em/accent!30/{Sleep,\\beautiful sleep},
        %   3/8em/accent!40/Hopeful novelist by night,
        %   8/8em/accent!60/Daytime job,
        %   2/10em/accent/Sports and relaxation,
        %   5/6em/accent!20/Spending time with family
        % }
        
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
            resume_str += r'\divider'
    resume_str += r'''    
        % ----- EXPERIENCE -----
        % ----- EDUCATION -----
        \cvsection{Education}'''
    for exp_i_count, exp_i in enumerate(resume_info['education'].values()):
        resume_str += r'\cvevent{'+exp_i['degree']+r'}{| '+exp_i['school']+r'}{'+exp_i['year_graduated']+r'}{}'
        resume_str += r'''
        '''
        if 'highlights' in exp_i:
            resume_str += r'\begin{itemize}'
            for highlight_i in exp_i['highlights'].values():
                resume_str += r'\item '+highlight_i+r'\\'
            resume_str += r'\end{itemize}'
        
        if exp_i_count < len(resume_info['experience'].values())-1:
            resume_str += r'\divider'

    resume_str += r'''% ----- EDUCATION -----
        
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
    \end{paracol}
\end{document}
'''
    return resume_str