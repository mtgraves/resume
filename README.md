# Resume Builder

This allows you to build a resume using `LaTeX`, from a `yaml` file.

## Why?

This can allow us to try out multiple different styles/layouts for a resume while inserting content that might be job-specific into each template.

I always end up with dozens of resumes cluttering up my filesystems whenever it's time to apply for jobs.  Then I end up inevitably trying out multiple different styles each time.  So for `N` drafts of a resume (content) then `M` different styles you end up with `N x M` permutations of files and it's super unorganized and janky.

## How to use

an example use case is as follows.

1. create a file called `test.py` inside of the root project directory with the following contents:

```python
from src.resumebuilder import Resume

def main():

    fpath_base = 'my_resume_test'
    resume_info_path = './resume_contents.yml'
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
```

2. create a yaml config file inside of the root project directory called 'resume_contents.yml' with the following contents:

```yaml
applicant_info:
  name: 'Carl Junior'
  email: 'carljunior@things.com'
  phone: '999-999-9999'
  location: 'City, State'
  title: 'Burger King'
  objective: 'Currently looking to make some greasy software'


strengths:
  software_development:
    s_1: 
      skill: 'Things'
      rating: 4
    s_2: 
      skill: 'Stuff'
      rating: 4
  programming:
    s_1: 
      skill: 'Python'
      rating: 5
    s_2: 
      skill: 'Rust'
      rating: 3
  other:
    s_4: 
      skill: 'Chillin'
      rating: 5


education:
  e_1:
    school: 'School of Hard Knocks'
    degree: 'M.S. Computer Science'
    year_graduated: '2010'
    highlights:
      h_1: 'Thesis: [An awesome thesis](https://www.google.com)'
      h_2: 'did some amazing stuff'
  e_2:
    school: 'School of Hard Knocks'
    degree: 'B.S. Computer Science'
    year_graduated: '2008'
    highlights:
      h_1: ' Triple major, graduated Cum Laude'

experience:
  e_1:
    title: 'Senior Software Engineer'
    company: 'Amazing Company'
    tenure_start: '2015'
    tenure_end: 'current'
    highlights:
      h_1: 'built things'
      h_2: 'built stuff'
      h_3: 'made the company some dough'

  e_2:
    title: 'Software Engineer'
    company: 'Company with less amazingness'
    tenure_start: '2010'
    tenure_end: '2015'
    highlights:
      h_1: 'did a couple of things'
```
