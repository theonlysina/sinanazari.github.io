"""
CIT 591 - week 4 assignment - Make a Website
Name: SINA ALIPOUR-NAZARI
PennID: 20359038

STATEMENT OF WORK:
- I used no resources, except for lecture materials and Python documentations.
- No people helped me (including TAs/Instructor).
- I completed this work alone without help.
"""

"""              INTRODUCTION: RESUME WEBPAGE BUILDER

This program will take a resume in a simplistic text file and convert it into an HTML fil."
This program is tested on a sample student resume that is somewhat unstructured, but will have the following commonalities:

Functions by
1) reading the file into memory,
2) parsing each section of the file to extract the relevant information, and
3) writing the final HTML-formatted information to a new file.

Follows these rules:
● Every resume will have a name, which will be written at the top. The top line in the text
file will contain just the name.
● There will be a line in the file, which contains an email address. It will be a single line
with just the email address and nothing else.
● Every resume will have a list of projects. Projects are listed line by line below a heading
called “Projects”. The list of projects ends with a single line that looks like ‘----------’ . That is, it will have
at least 10 minus signs.
● Every single resume will just have this comma separated list of courses
with the word “Courses” being there in front of them. 

"""


def read_student_info(resume_txt_file):
    """
This function reads the resume file and stores it in the program’s memory as a str.
Does not manipulate anything from the file.
    """

    # sets variable resume_txt
    resume_txt = []

    # opens resume.txt in reading mode (and closes afterward) and names it stream
    with open(resume_txt_file, 'r') as stream:
        # adds each line of resume.txt as a string element in the list resume_txt
        resume_txt = stream.readlines()
        
        # debugging
        # print(type(stream))
        # print(stream)
        # print(resume_txt)

    return resume_txt


def detect_name(resume_txt):
    """
Detecting the Name
● Extracts the first line of resume (student name).
● Removes leading or trailing whitespace.
● Raises a RuntimeError if the first character in the name string is not an uppercase letter (capital ’A’ through ’Z’)
and the program will crash and informs the users that the first line has to be a name with proper capitalization.
● Returns student name
    """
    # extracts the first line of resume txt file as and strips whitespace from ends --> assigns it to string student_name
    student_name = resume_txt[0]

    if student_name != "":      # makes sure student name line is not removed
        student_name = student_name.strip() # strips whitespace from name

        # raises a Runtime Error if the first letter of student name is not uppercase.
        if student_name[0].isupper() != True:
            raise RuntimeError("The first line of resume has to be the first line has to be a name with proper capitalization.")


    # debugging
    # print(student_name)

    # returns student name
    return student_name


def detect_email(resume_txt):
    """
This function detects the student's email.
● Identifies email by looking for a line that has the ‘@’ character.
● Removes leading or trailing whitespace from the email string.
● If the email is not a professional email (denoted by criteria below), returns a runtime error telling student to use a professional email address..
    - the last four characters of the email are either ‘.com’ or ’.edu’ .
    - the email string begins with a lowercase English character between the ‘@’
and the ending ( ’.com’ or the ’.edu’ )
    - there are no digits or numbers in the email address.

For example::
lbrandon@wharton.upenn.edu is a valid email
lbrandon@wharton2.upenn.com is not a valid email
lbrandon2@wharton.upenn.com is also not a valid email

● returns student email address
● If an e-mail string is not found, returns an empty string.

    """
    # by default, assumes email address not found
    email_found = False
    student_email = ""

    # for each line of resume after first line *student name)
    for line in resume_txt[1:]:

        # first, removes each line's leading and trailing whitespace and saves
        line_content = line.strip()

        # debugging
        # print("line_content:", line_content)
        # print("stripped line type:", type(line_content))
        # print("student email function iterating through this line:", line)

        # still, for each line...
        # checks to see if requirements for correct email are met
        if "@" in line_content:  # condition 1: looks for an atsign to detect the email address
            # print(True)
            index_of_atsign = line_content.index("@")  # if first condition met, finds the line index of line that has atsign

            # indicates email address found
            email_found = True

            # and then checks for second condition
            if (line_content[-4:] == ".com") or (line_content[-4:] == ".edu"):  # condition 2: looks to make sure email's domain suffix is either ".com" or ".edu"
                # print(True)
                # if second condition is met, checks for third condition
                if line_content[index_of_atsign + 1].isalpha() and (line_content[index_of_atsign + 1].islower()):  # condition 3: looks to make sure the letter after atsign is both alphabetical and lowercase
                    # print(True)
                    # if third condition is true, checks for fourth condition

                    # condition 4: checks to make sure no chatacter in the email address is a digit.

                    digit_found = False

                    # for loop looks to see if there is any digits in the email address
                    for char in line_content:
                      if char.isdigit() == True:
                          digit_found = True

                    # if there is a digit in the email address, condition 4 fails.
                    if digit_found == True:
                        print("Email Error 1: Please make sure not to include digits anywhere in the email address.")
                        # print(student_email)
                    # if condition 4 is met (i.e. all conditions are met), stores the stripped version of line containing the atsign in str student_email
                    elif digit_found == False:
                        print("Valid email found.")
                        student_email = line_content
                        # breaks the for loop to stop searching for the next atsign
                        break
        # if any of the conditions are not met, writes on screen to inform user (of the first condition that failed) and assigns blank to student_email
                else:
                    print("Email Error 2: Please make sure the email provider's website starts with a lowercase letter.")
            else:
                print("Email Error 3: Please provide a '.com' or '.edu' email address.")   
        else:
            if email_found == True:
                print("Email Error 4: Please provide an email address with an @ sign")
            else:
                continue

    # informs user if no email address with an @ sign was
    if email_found == False:
        print("No email address with @ sign found")
    
    # debugging
    # print("student email:", student_email)

    # returns extracted student email
    return student_email


def detect_courses(resume_txt):
    """
This function detects the courses completed by student.
● Finds the word courses “Courses” in the file and extracts the line that contains that word.
● Makes sure to extract the correct courses.
● any random punctuation after the word “Courses” and before the first actual course needs to be ignored, assuming every course begins with a letter of the English alphabet.
● Removes any whitespace leading or trailing the word “Courses”, the random punctuation, or individual courses in the list.
    """

    # creates the output variable -- the list list for stripped list of courses
    student_courses_slst = []

    # assumes courses section is not found unless/until it is found --> for error reporting
    courses_found = False

    # looks through every line in resume text after first line (name line)
    for line in resume_txt[1:]:

        # strips each line's leading and trailing whitespace
        line = line.strip()
        # print(line)

        # makes an all-lowercase line for to compare with lowercase word "courses"
        line_lcase = line.lower()
        # print("lcase:", line_lcase)
        
        # looks for txt "courses" in lowercased line content
        if line_lcase.find("courses") != -1: # if found....
            courses_found = True
            courses_str_index = line_lcase.find("courses")  # get index of courses
            # print(courses_str_index)

            # in the same line, finds the index for first char after "courses"
            courses_str_end_index = courses_str_index + 7
            # print("courses_str_end_index: ", courses_str_end_index)

            # creates a starting point for searching for the first course
            course_search_start_index = courses_str_end_index + 1
            # print(course_search_start_index)

            # finds the index for first alphabetical character after "courses",
            for character in line_lcase[course_search_start_index:]:  # for every char after "courses"

                # checks to see if char is alphabetical
                if character.isalpha():  # if true...
                    line_lcase = line_lcase
                    first_course_index = line_lcase.index(character, course_search_start_index)  # saves char index

                    # debugging
                    # print("first_course_index", first_course_index)

                    # creates a string from that point onward
                    student_courses_str = line[first_course_index:]

                    # makes a list of courses, separated by commas, removes the title word "Courses"
                    student_courses_lst = student_courses_str.split(",")
                    # print('student_courses_lst', student_courses_lst)

                    # strips each course of whitespace by...
                    for course in student_courses_lst:  # iterating through each course in course list
                        course_stripped = course.strip()  # stripping leading and trailing whitespace
                        student_courses_slst.append(course_stripped)  # adding it to the list of whitestripped courses
                        # print("idl_course:" + course)

                    # debugging
                    # print("student courses:", student_courses_slst)
                    break
            break
        
    # if the courses section was never found...    
    if courses_found == False:
        # informs user course section not found
        print("courses section not found in text-based resume.")

    # returns the list of whitestrepped courses
    # print(student_courses_slst)
    return student_courses_slst

def detect_projects(resume_txt) -> object:
    """
This function detects and returns the projects done by the student.
● Looks for the word “Projects” in the file.
● Each subsequent line is a project until program hits a line that looks like ‘----------' (ten or more minus signs put together).
● If it detects a blank line between project descriptions, ignores that line.
● Removes any leading or trailing whitespace from any projects.
    """
    # sets variable list_count to count the lines with
    line_count = 0

    p_start = 0
    p_end = 0
    student_project_list = []

    # iterates through each line of resume after the fist line (student name)
    for line in resume_txt[1:]:  # for each line...
        line_count += 1  # counts the line
        line_content = line.strip()  # strips the line of leading and trailing whitespace

        if "projects" in line_content.lower():  # if lowercase "projects" is found in the lowercased version of the line
            # records the line count as index for projects
            p_index = line_count

            # debugging
            # print("project index:", p_index)
            # print("line:", line)
            # print("projects and below:", resume_txt[p_index:])

            # sets a variable to start looking for a list of individual projects -- in practice, moves to next line
            p_start = p_index + 1

            # print(p_start)
            # print(resume_txt[p_start])

            # resets the line count variable
            line_count = 0

            # looks through the line where the list of projects start to the end line in resume_txt
            for line in resume_txt[p_start:]:  #

                # counts the line
                line_count += 1
                # strips the line of leading and trailing whitespace
                line_content = line.strip()

                # print(line_content)

                # looks to see if it has reached the end of projects section of resume by looking for 10 minus signs
                if "----------" in line_content:  # if it finds the end of projects section
                    # indexes the last line where projects are listed
                    p_end = p_start + line_count - 1

                    # debugging
                    # print("p_end:", p_end)
                    # print("p_end_txt:", resume_txt[p_end])

                    # makes a list of student projects, sets to blank
                    student_project_list = []

                    # assigns each line between the start of projects and end of projects to a str variable in lst of projects
                    for line in resume_txt[p_start:p_end]:  # looks through each line from beginning to end of projects section
                        line = line.strip()  # strips leading and trailing whitespace in each line
                        if not (line == ""):  # if line is not empty
                            # adds the line to the list of projects
                            student_project_list.append(line)

                    # keep in mind, stripping of whitespace and checking to see if line is empty together mean that lines with line breaks are not included in list of projects.
                    # so there are no empty projects going into the list of projects

                    # debugging
                    # print("student project list:", student_project_list)

    # returns the student's list of projects as a tuple
    # print(tuple(student_project_list))
    return tuple(student_project_list)

def read_html_template(resume_template_file):
    """
    This function programmatically opens and reads the HTML template.
    Stores all lines of template as list template.
    Strips all line breaks (\n) at the end of each line.
    """

    # CREATE VARIABLE RESUME OUTPUT TO STORE HTML CODE
    resume_output = []

    # opens resume template html file
    with open(resume_template_file, "r") as fin:
        template = list(fin.readlines())

    # debugging
    # print("template:", template)

    # strips the trailing spaces from each of the lines in template
    for line in template:
        line = line.replace('\n', '')
        # and saves to the variable resume output
        resume_output.append(line)

    # debugging
    # print("resume output after read_html:", resume_output)

    # returns output code
    return resume_output

def remove_bottom_end_tags(resume_output):
    """
    This function removes the last 2 lines of HTML
    """
    # print("template before removing end tag:", resume_output)

    # sets line count to 0
    line_count = 0

    # iterates through all lines in resume output file
    for line in resume_output:
        # counts the line
        line_count += 1
        # finds body end tag and stores its line number
        if "</body>" in line:
            body_end_tag_line_index = line_count - 1

            # deletes html code starting from body end tag to the end of the file
            del resume_output[body_end_tag_line_index:]

    # print("template after removing end tags:", resume_output)
    # print(resume_output)
    
    # returns output code
    return resume_output

def add_bottom_end_tags(resume_output):
    """
    Adds the following three lines to the bottom of the HTML file:
    
        </div>
        </body>
        </html>
    """

    # creates a list of the last three lines of code to be added to the bottom of the html code
    end_tags = ["</div>", "</body>", "</html>"]

    # debugging
    # print("end list:", end_tags)
    
    # adds the resume html end tags to the end of html code
    resume_output.extend(end_tags)

    # returns output code
    return resume_output


def create_email_link(email_address):
    """
    Takes a string for a valid email address as an input
    Creates an email link from the given email address text.
    To reduce spam, displays the email address with an [aT] instead of an @.

        For example, create_email_link(‘tom@seas.upenn.edu’) would return:
        ’<a href="mailto:tom@seas.upenn.edu">tom[aT]seas.upenn.edu</a>’

    If the given email address does not contain @, uses the email address as is.

        For example, create_email_link(‘tom.at.seas.upenn.edu’) would return
        ‘<a href="mailto:tom.at.seas.upenn.edu">tom.at.seas.upenn.edu</a>'
    """

    # converts email address to spam-proof email address (if it contains an atsign)
    email_address_sp = email_address.replace("@", "[aT]")

    # makes an link (with a tag and href reference) to email address
    email_link = '<a href="mailto:{}">{}</a>'.format(email_address, email_address_sp)

    # print(email_link)

    # returns the email link
    return email_link    


def surround_block(tag, text):
    """
    surrounds the given text with the given HTML tag and returns the html tagged text.
    """

    # converts element into tagged text
    block = '<{}>{}</{}>'.format(tag, text, tag)

    # debugging
    # print("block:", block)

    # returns the block of code (i.e. tagged text)
    return block


def add_pagewrap(resume_output):
    """
    Adds a line of HTML code that denotes the start of page wrap
    """
    # adds the open tag of page-wrap to list of lines representing html output
    resume_output.extend(['<div id="page-wrap">'])

    # returns output code
    return resume_output


def add_s_info(student_name, student_email, resume_output):
    """
    adds HTML code representing a student intro section in HTML code, like below:

        <div>
        <h1>student_name</h1>
        <p>Email: <a href=”mailto:student_email”>student_email_sp</a></p>
        </div>
    """
    
    # create a list to represent the lines that make up the intro section
    html_intro_section = []

    # opens the section in a div
    html_intro_section.append('<div>')

    # adds student name to intro section in an <h1> tag
    html_intro_section.append(surround_block("h1", student_name))

    # creates an email link in variable email line
    email_link = create_email_link(student_email)
    
    # formats the email link in a <p> tag
    html_intro_section.append(surround_block("p", "Email: " + email_link))
    
    # closes the section div
    html_intro_section.append('</div>')

    # debugging
    # print("student_info: ", html_intro_section)

    # adds the intro section to the bottom line of html file
    resume_output.extend(html_intro_section)

    # returns output code
    return resume_output


def add_s_projects(student_projects, resume_output):
    """
    adds the html code for the projects section of the resume output to be printed, like below:
        <div>
        <h2>Projects</h2>
        <ul>
        <li>built a robot</li>
        <li>fixed an ios app</li>
        </ul>
        </div>   
    """

    # starts a list of lines representing projects section in html code
    html_projects_section = []

    # adds a div opening to begin the projects section
    html_projects_section.append("<div>")

    # adds header of "Projects" to projects section
    html_projects_section.append(surround_block("h2", "Projects"))

    # print("projects type:", type(student_projects))
    # print("student projects:", student_projects)

    # adds a list tag beginning to start listing student projects
    html_projects_section.append("<ul>")

    # type(student_projects)

    # lists all student projects derived from the list of projects as html list bullets
    for project in student_projects:  # iterates through each project in list of projects
        # for each project...
        project_bullet = surround_block("li", project)  # makes a bullet list tag
        html_projects_section.append(project_bullet)  # adds a line with that project's bullet/list tag

    # adds a list end tag
    html_projects_section.append("</ul>")
    # adds a div end tag to lose the projects section of html code
    html_projects_section.append("</div>")
    
    # print("projects section html", html_projects_section)

    # adds projects section html code to resume output html
    resume_output.extend(html_projects_section)

    # returns output code
    return resume_output


def add_s_courses(student_courses, resume_output):
    """
    This function adds the html code for the courses section of the output html file.
    Takes as input a list of courses, and adds the html code for a courses section to an html file.
    Products an html like below:
    
        <div>
        <h3>Courses</h3>
        <span>Algorithms, Race car training</span>
        </div>
    """
    # creates a list to represent each line of the html code for courses section
    html_courses_section = []

    # opens the html section with a div tag
    html_courses_section.append("<div>")

    # adds a courses section with header3 format to html section
    html_courses_section.append(surround_block("h3", "Courses"))

    # makes a string of comma-separated (", ") student courses
    student_courses_str = ""  # creates a list of student courses, and assigns the first course
    for course in student_courses:  # goes second course to last course... for each course

        # debugging
        # print("idl" + course)

        # adds the student course to the string of courses
        student_courses_str += course

        # adds a comma after the course, unless it is the last course in the list
        if course is not student_courses[-1]:
            student_courses_str += ", "

    # print("student_courses_str:" + student_courses_str)

    # adds a line with str list of courses in span tag
    html_courses_section.append(surround_block("span", student_courses_str))

    # closes the courses section
    html_courses_section.append("</div>")
    # print("html courses section", html_courses_section)

    # adds the courses section to the html code to be printed
    resume_output.extend(html_courses_section)
    # print(resume_output)

    # returns output code
    return resume_output


def main():
    """The main function opens student txt file, detects key student resume info.
    Then writes key student info to an html template to create an html resume
    """

    # this part of the program opens student txt resume and detects key info

    # sets the name of resume txt file to be scanned for content
    resume_txt_file = "resume.txt"

    resume_txt = read_student_info(resume_txt_file)
    student_name = detect_name(resume_txt)
    student_email = detect_email(resume_txt)
    student_courses = detect_courses(resume_txt)
    student_projects = detect_projects(resume_txt)

    # this part of program prepares the code for html resume.

    # sets the location of the imput resume txt file to be reformatted by the program
    resume_template_file = "resume_template.html"

    # creates a resume template
    resume_output = read_html_template(resume_template_file)
    resume_output = remove_bottom_end_tags(resume_output)

    # adds page wrapper (open tag), student info, projects, courses, and bottom tags to the html code to-be-printed, in order mentioned
    resume_output = add_pagewrap(resume_output)
    resume_output = add_s_info(student_name, student_email, resume_output)
    resume_output = add_s_projects(student_projects, resume_output)
    resume_output = add_s_courses(student_courses, resume_output)
    resume_output = add_bottom_end_tags(resume_output)

    # print(resume_output)

    # this part of the program writes the resume output html code into resume.html

    # sets the resume.html file as output file
    fout = open("resume.html", "w")
    # writes the html code!
    fout.writelines(resume_output)
    # saves to file and closes the output file resume.html
    fout.close()


# runs the program
if __name__ == '__main__':
    main()
