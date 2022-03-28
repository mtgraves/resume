import yaml
import os
import templates.altacv as t_1
import templates.maxgcv as t_2

class Resume:
    '''Class representation of your resume object

    :param fpath_base: filename (without extension) you for .tex and .pdf output of your resume
    :param resume_info_path: full filepath to the yaml file containing your resume information
    :param resume_template: name of the resume template you wish to use.  Current options include:
        - altacv
        - maxgcv
    '''

    def __init__(self, fpath_base, resume_info_path, resume_template):
        '''Constructor Method
        '''

        # check input and raise useful errors if any "bad" input was passed
        allowed_templates = ['altacv', 'maxgcv'] 
        if resume_template not in allowed_templates:
            raise RuntimeError('resume_template must be from ['.join(allowed_templates)+']')

        if not os.path.exists(resume_info_path):
            raise RuntimeError('Cannot locate your yaml config at: '+str(resume_info_path))
        
        # load user resume info/configuration
        with open(resume_info_path, 'r') as config_f:
            self.resume_info_md = yaml.safe_load(config_f)

        # we hold the resume information in markdown and tex format so that each can be written out
        self.resume_info_tex = self.resume_info_md.copy()
        self.fpath_tex = os.path.join('out', fpath_base + '.tex')
        self.resume_template = resume_template
        self.resume_str = self.build_resume()


    def build_resume(self):
        '''build resume raw string from template, inserting resume information
        provided by the user.
        '''
        self.convert_resume_info_to_tex(
            md_val=self.resume_info_md,
            tex_val = self.resume_info_tex,
        )

        if self.resume_template == 'altacv':
            resume_str = t_1.resume(self.resume_info_tex)
        elif self.resume_template == 'maxgcv':
            resume_str = t_2.resume(self.resume_info_tex)

        return resume_str 


    def convert_resume_info_to_tex(self, md_val, tex_val):
        '''recursively converts an entire resume info dictionary from markdown style to LaTeX style
        '''
        for md_i_key, md_i_val in md_val.items():
            if type(tex_val[md_i_key]) == dict:
                self.convert_resume_info_to_tex(
                    md_val=md_i_val, 
                    tex_val=tex_val[md_i_key]
                )
            elif type(tex_val[md_i_key]) == str:
                tex_val[md_i_key] = self.convert_md_str_to_tex(md_val[md_i_key])


    def convert_md_str_to_tex(self, markdown_string):
        '''converts individual markdown style strings to LaTeX formatting including:
        - backticks to colorbox (for code highlighting)
        - ampersand
        - tilde to sim
        '''
        tex_string = r''
        found_backtick_start = False
        found_italics_start = False
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
            if str_ch == '*':
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
            else:
                tex_string += str_ch

        return tex_string
    

    def write_tex(self):
        '''write user resume out to LaTeX (.tex) format
        '''
        with open(self.fpath_tex, 'wt') as f:
            f.write(self.resume_str)


    def write_pdf(self):
        '''write user resume out to pdf format
        '''
        os.system('pdflatex '+str(self.fpath_tex)+' -output-directory out')


def main():

    fpath_base = 'MaxGraves_resume_test'
    resume_info_path = './resume_contents.yml'
    #resume_template = 'maxgcv'
    resume_template = 'altacv'

    my_resume = Resume(
        fpath_base = fpath_base,
        resume_info_path = resume_info_path,
        resume_template = resume_template,
    )

    my_resume.write_tex()
    my_resume.write_pdf()

if __name__=='__main__':
    main()