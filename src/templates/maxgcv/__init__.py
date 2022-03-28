
def resume(resume_info):
    '''returns resume string in maxgcv format
    '''

    resume_str = r'''\documentclass[10pt,letterpaper]{report}
\usepackage[latin2]{inputenc}
\usepackage{amsmath}
\usepackage{amsfonts}
\usepackage{amssymb}
\usepackage{hyperref}
\usepackage[pdftex]{graphicx}
\usepackage{fancyhdr}
\usepackage[margin=1in, tmargin=0.5in]{geometry}
\usepackage{tikz}
\usetikzlibrary{arrows}
\pagestyle{fancy}
\author{Max Graves}
\title{Curriculum Vitae}

\usepackage{scrextend}
\usepackage{comment}

%======================================================
% Fancy rule
%======================================================
\newcommand{\myrule} [3] []{
    \begin{center}
        \begin{tikzpicture}
            \draw[#2-#3, ultra thick, #1] (0,0) to (1.0\linewidth,0);
        \end{tikzpicture}
    \end{center}
}

\begin{document}
%=======================================================
% Create footer
%=======================================================
\renewcommand{\headrulewidth}{0mm}
\cfoot{}
\fancyfoot[C]{\footnotesize{\textit{
'''    
    resume_str += resume_info['applicant_info']['name']
    resume_str += r'''    
} - \thepage}}

%=======================================================
% SET HANGING INDENT
%=======================================================
\leftskip 0.4in
\parindent -0.4in

%=======================================================
% HEADING
%=======================================================
\begin{center}
\textbf{'''
    resume_str += resume_info['applicant_info']['name']
    resume_str += r'''} 
\end{center}

\vspace{-10pt}
\href{mailto:
'''
    resume_str += resume_info['applicant_info']['email']
    resume_str += r'}{'+resume_info['applicant_info']['email']+r'}'
    if 'phone' in resume_info['applicant_info']:
        resume_str += r'\hfill'
        resume_str +=  resume_info['applicant_info']['phone']
    resume_str += r'''
\vspace{-20pt}
\myrule[double]{}{}

%\end{center}

%=======================================================
% EXPERIENCE
%=======================================================
\textbf{EXPERIENCE}\\'''
    for exp_i in resume_info['experience'].values():
        resume_str += r'\textbf{'+exp_i['title']+r'} ('+exp_i['tenure_start']+r' - '+exp_i['tenure_end']+r')\\'
        resume_str += r'\textit{'+fr"{exp_i['company']}"+r'}'
        resume_str += r'''
        '''
        if 'highlights' in exp_i:
            resume_str += r'\begin{itemize}\itemsep0em'
            for highlight_i in exp_i['highlights'].values():
                resume_str += r'\item '+highlight_i+r''
            resume_str += r'\end{itemize}'
    resume_str += r'''
\textbf{Engineering Laboratory Manager} (Sep. 2014 - Present)\\
\textit{University of Vermont - School of Engineering  (Burlington, VT)}\\
-- Supported all electrical, mechanical, and civil/environmental engineering teaching laboratories.\\
-- Served as primary technician for electrical and mechanical laboratory equipment.\\
-- Primary resource for laboratory instrumentation, safety, and field work/field equipment.\\
-- Collaborated directly with equipment vendors to maintain and upgrade test equipment.\\
-- Performed safety inspections for Fabrication Lab.\\
-- Developed and deployed a new inventory system for School of Engineering lab equipment.\\
-- Designed website to serve as central repository for teaching laboratory documentation.\\
-- Supervised engineering undergraduate students working on various projects.\\
-- Coordinated and assisted with science/engineering outreach programs.\\\\
\textbf{Jr. Systems Administrator} (Jul. 2014 - Sep. 2014)\\
\textit{Logic Supply  (South Burlington, VT)} \\
-- Linux and Windows server administration.\\
%-- Wrote Python code to monitor, compare, and present data for company website load times to/from Netherlands and US web servers over a period of time.\\
-- Worked alongside and directly supported development, marketing, and sales teams.\\
-- Developed code to monitor and optimize performance of live company web servers.\\
-- General network administration tasks. \\\\
\textbf{Research Assistant} (Summer 2012 , Summer 2013)\\
\textit{University of Vermont - Physics Department  (Burlington, VT)} \\
-- Graduate research in computational condensed matter physics.\\\\
\textbf{Teaching Assistant} (Jan. 2012 - Jul. 2014)\\
\textit{University of Vermont - Physics Department  (Burlington, VT)} \\
-- Taught mechanics, circuits, optics, electricity and magnetism lab courses.\\\\
\textbf{Physical Science Tutor} (Sep. 2009 - Dec. 2011)\\
\textit{UNC Greensboro Learning Assistance Center  (Greensboro, NC)} \\ 
-- Tutored approximately 10 students per semester in general chemistry 1,2 and general physics 1,2.\\\\
\textbf{Contracted Employee} (Dec. 2010 - Jan. 2011)\\
\textbf{Summer Student} (June 2010 - Aug. 2010)\\
\textit{GlaxoSmithKline  (RTP, NC)}\\
-- Performed data-entry tasks for pharmaceutical development-information systems group. \\
-- Job shadowing for R{\&}D, scale-up, and manufacturing of pharmaceuticals.\\ %This included learning the basics of using and maintaining UV-Vis spectrophotometers, mass spectrometers, and various specialized experimental equipment.\\
%\textbf{Olive Garden}  - \textit{Server} (Burlington NC, USA)\\
%(May 2009 - June 2010)\\


%=======================================================
%  EDUCATION SECTION
%=======================================================
\textbf{EDUCATION}\\
\textbf{M.S. Materials Science} -- Oct. 2014 \\
University of Vermont (Burlington, VT)\\
GPA: 3.92\\
THESIS:  \textit{Quantum Monte Carlo Study of Enhanced Proximity Effects in Superfluid Helium}\\
Computational Condensed Matter Physics Research:
\vspace{5pt}
\begin{addmargin}[20pt]{0pt}
\leftskip 0.4in
\parindent -0.4in
\begin{itemize}
\itemsep0em 
\item Worked closely with team of developers to implement path integral quantum Monte Carlo algorithm using Singleton design pattern in C++.
\item Wrote and maintained repository of Python scripts to perform data analysis/presentation, automated job submission/retrieval to/from supercomputing center, and 3D visualization of materials.
%\item Determined how to checkpoint Torque job arrays and wrote documentation for Vermont Advanced Compute Core.
\item Wrote Torque job array checkpoint documentation for Vermont Advanced Computing Core.
\item Provided explanation for anomalously large proximity effects in experimental superfluid systems using large scale quantum Monte Carlo simulations.\\ %using Python and POVray.\\
\end{itemize}
\end{addmargin}
%Relevant Coursework:
%$\cdot$
%
\textbf{B.S. Interdisciplinary Mathematics / B.A. Chemistry / B.A. Physics} -- Dec. 2011\\
University of North Carolina at Greensboro (Greensboro, NC)\\
GPA: 3.50 -- (Math/Science GPA: 3.68)\\
Molecular Reaction Dynamics Research:
\vspace{5pt}
\begin{addmargin}[20pt]{0pt}
\leftskip 0.4in
\parindent -0.4in
\begin{itemize}
\itemsep0em 
\item Lead computational chemist in microwave spectroscopy research group.
\item Wrote code to help design an apparatus that slows and traps polar neutral molecules.
% account for quantum mechanical effects in a classical electrodynamics software package (SIMION) to help design an apparatus that slows and traps polar neutral molecules.
\item Assisted with the design and operation of an instrument built for probing molecular reaction dynamics via pure rotational spectroscopy.\\
\end{itemize}
\end{addmargin}  


%=======================================================
%  TECHNICAL SKILLS
%=======================================================
\textbf{TECHNICAL SKILLS}\\
\textbf{Languages:}  Python, C++, Java, HTML, CSS3, \LaTeX , Lua.\\
\textbf{Software:} Bash, GNU toolchain, Git, Subversion, PBS Torque, Matlab, Mathematica, vi/vim, Eclipse, Inkscape, GIMP, POVray, Abaqus FEA, MS Office Suite. \\
\textbf{Operating Systems:}  Linux (various distributions), MS Windows.\\




%=======================================================
% Honors and Awards
%=======================================================
\textbf{HONORS AND AWARDS}
\begin{addmargin}[20pt]{0pt}
\leftskip 0.4in
\parindent -0.4in
\begin{itemize}
\itemsep0em 
\item Graduate Student Teaching Assistant of the Year -- (Apr. 2014)
\item Outstanding Physics Teaching Assistant Award -- (Apr. 2014)
\item UVM Student Scholars Poster Competition Finalist -- (Oct. 2012)
\item NSF S.T.A.M.P.S. Scholarship -- (Jan. 2011 - Dec. 2011)
\item Turrentine Scholarship, UNCG -- (Aug. 2011 - Dec. 2011)
\item Bielhauer UNCG Mathematics Dept. Scholarship -- (Jan. 2010 - Dec. 2011)
\item GlaxoSmithKline undergraduate scholarship -- (Aug. 2006 - May 2010)
\end{itemize}
\end{addmargin}


\end{document}

'

'''
    return resume_str