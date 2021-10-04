"""         RESUME WEBPAGE BUILDER TEST FILE         """
"""
CIT 591 - week 4 assignment - Make a Website
Name: SINA ALIPOUR-NAZARI
PennID: 20359038

STATEMENT OF WORK:
- I used no resources, except for lecture materials and Python documentations.
- No people helped me (including TAs/Instructor).
- I completed this work alone without help.
"""
import unittest

from make_website import *

class MakeWebsite_Test(unittest.TestCase):

    # inputs a sample resume txt that fits our resume txt template
    global lst
    lst = ['Student Name',
           'email@email.com',
           'courses :!!@@ course1, course2, course3, course4',
           'Projects',
           'project1',
           'project2',
           'project3',
           '----------']


    def test_read_student_info(self):
        # tested against 3 accompanying test files: simplelines.txt, simplelinesb.txt, hardlines.txt

        # testing with numbers
        simple_lines = ['1\n', '2\n', '3']
        self.assertEqual(read_student_info('simplelines.txt'), simple_lines)

        # testing with letters
        simple_linesb = ['a\n', 'b\n', 'c']
        self.assertEqual(read_student_info('simplelinesb.txt'), simple_linesb)

        # edge
        hard_lines = ['a_\n', 'b+\n', 'c*\n', '@\n', '\n']
        self.assertEqual(read_student_info('hardlines.txt'), hard_lines)

    def test_read_html_template(self):
        # tested against 3 accompanying test files: simplelines.txt, simplelinesb.txt, hardlines.txt

        # testing with numbers
        simple_lines = ['1', '2', '3']
        self.assertEqual(read_html_template('simplelines.txt'), simple_lines)

        # testing with letters
        simple_linesb = ['a', 'b', 'c']
        self.assertEqual(read_html_template('simplelinesb.txt'), simple_linesb)

        # edge
        hard_lines = ['a_', 'b+', 'c*', '@', '']
        self.assertEqual(read_html_template('hardlines.txt'), hard_lines)


    def test_detect_name(self):
        lst = ['Student Name',
               'email@email.com',
               'courses :!!@@ course1, course2, course3, course4',
               'Projects',
               'project1',
               'project2',
               'project3',
               '----------']
        # checks to make sure first list element (line) is extracted
        # typical cases
        self.assertEqual(detect_name(['A', 'B', 'C']), 'A')
        self.assertEqual(detect_name(['B', 'A', 'C']), 'B')
        self.assertEqual(detect_name(lst), 'Student Name')

        # edge cases
        self.assertEqual(detect_name(['A ', 'B', 'C']), 'A')
        self.assertEqual(detect_name([' A', 'B', 'C']), 'A')
        self.assertEqual(detect_name(['\nA', 'B', 'C']), 'A')
        self.assertEqual(detect_name(['A\n', 'B', 'C']), 'A')

        # checks to make sure first line i is capitalized
        # typical cases
        self.assertRaises(RuntimeError, detect_name, ['1a', '2b', '3c'])
        self.assertRaises(RuntimeError, detect_name, ['1', '2', '3'])
        self.assertRaises(RuntimeError, detect_name, ['a', 'b', 'c'])
        self.assertRaises(RuntimeError, detect_name, ['aA', 'bB', 'cC'])

        # edge cases
        self.assertRaises(RuntimeError, detect_name, [' a', ' b', ' c'])
        self.assertRaises(RuntimeError, detect_name, [' 1', ' 2', ' 3'])
        self.assertRaises(RuntimeError, detect_name, [' !', ' @', ' #'])

    def test_detect_email(self):

        # checks condition 1: email found?
        # typical cases
        self.assertEqual(detect_email(['Name Line', 'email@email.com', 'not email']), 'email@email.com')
        self.assertEqual(detect_email(['Name Line', 'not email', 'email@email.com']), 'email@email.com')
        self.assertEqual(detect_email(['Name Line', 'not email', 'not email']), '')

        # edge cases
        self.assertEqual(detect_email(['Name Line', 'projects', 'email@email.com']), 'email@email.com')
        self.assertEqual(detect_email(['Name Line', 'projects', '----------', 'email@email.com']), 'email@email.com')
        self.assertEqual(detect_email(['Name Line', 'courses', 'email@email.com']), 'email@email.com')

        # checks condition 2: .com or .edu suffix?
        # typical cases
        self.assertEqual(detect_email(['Name Line', 'email@email.com']), 'email@email.com')
        self.assertEqual(detect_email(['Name Line', 'email@email.edu']), 'email@email.edu')
        self.assertEqual(detect_email(['Name Line', 'email@email.net']), '')

        # edge cases
        self.assertEqual(detect_email(['Name Line', 'email@department.company.net']), '')
        self.assertEqual(detect_email(['Name Line', 'email@department.company.com']), 'email@department.company.com')
        self.assertEqual(detect_email(['Name Line', 'email@department.company.com.us']), '')


        # checks condition 3: char after @ is lowercase integer
        # typical cases
        self.assertEqual(detect_email(['Name Line', 'email@email.com']), 'email@email.com')
        self.assertEqual(detect_email(['Name Line', 'email@Email.com']), '')
        self.assertEqual(detect_email(['Name Line', 'Email@email.com']), 'Email@email.com')

        # edge cases
        self.assertEqual(detect_email(['Name Line', 'Email@ email.com']), '')
        self.assertEqual(detect_email(['Name Line', 'Email@>mail.com']), '')

        # checks condition 4: no digits in email
        # typical cases
        self.assertEqual(detect_email(['Name Line', '1@2.com']), '')
        self.assertEqual(detect_email(['Name Line', 'email@1mail.com']), '')
        self.assertEqual(detect_email(['Name Line', '1mail@email.com']), '')
        self.assertEqual(detect_email(['Name Line', 'm1ail@e2mail.com']), '')
        self.assertEqual(detect_email(['Name Line', '1mail@e2mail.com']), '')

        # edge cases
        self.assertEqual(detect_email(['Name Line', 'e-mail@e-mail.com']), 'e-mail@e-mail.com')
        self.assertEqual(detect_email(['Name Line', 'fname.lname@e-mail.com']), 'fname.lname@e-mail.com')

    def test_detect_courses(self):
        # checks to see if line 3 of resume (the courses line) generates a lst of courses
        self.assertEqual(detect_courses(lst[1:]), ['course1', 'course2', 'course3', 'course4'])

        # lowercase: courses
        course_lst0 = ['Student Name Line', 'courses: course1, course2, course3, course4']
        self.assertEqual(detect_courses(course_lst0), ['course1', 'course2', 'course3', 'course4'])

        # mixed-case: Courses
        course_lst1 = ['Student Name Line', 'Courses: course1, course2, course3, course4']
        self.assertEqual(detect_courses(course_lst1), ['course1', 'course2', 'course3', 'course4'])

        # uppercase COURSES
        course_lst1 = ['Student Name Line', 'COURSES: course1, course2, course3, course4']
        self.assertEqual(detect_courses(course_lst1), ['course1', 'course2', 'course3', 'course4'])

        # edge: bad formatting of separation between "courses" and list of courses
        course_lst2a = ['Student Name Line', 'Courses : course1, course2, course3, course4']
        self.assertEqual(detect_courses(course_lst2a), ['course1', 'course2', 'course3', 'course4'])

        # edge: very bad formatting of separation between "courses" and list of courses
        course_lst2b = ['Student Name Line', 'Courses {}@ course1, course2, course3, course4']
        self.assertEqual(detect_courses(course_lst2b), ['course1', 'course2', 'course3', 'course4'])

        # edge: very bad formatting of separation between "courses" and list of courses
        course_lst2c = ['Student Name Line', 'Courses !! course1, course2, course3, course4']
        self.assertEqual(detect_courses(course_lst2c), ['course1', 'course2', 'course3', 'course4'])

        # poor spacing between commas between courses - extra space
        course_lst4 = ['Student Name Line', 'Courses : course1 , course2 , course3 , course4 ']
        self.assertEqual(detect_courses(course_lst4), ['course1', 'course2', 'course3', 'course4'])

        # poor spacing between commas between courses - no space
        course_lst5 = ['Student Name Line', 'Courses : course1,course2,course3,course4']
        self.assertEqual(detect_courses(course_lst5), ['course1', 'course2', 'course3', 'course4'])

    def test_detect_projects(self):
        # test successful

        # simple resume format
        self.assertEqual(detect_projects(['name', 'projects', 'p1', 'p2', '-----------']), ('p1', 'p2'))

        # resume on top (lst1)
        self.assertEqual(detect_projects(lst[1:]), ('project1', 'project2', 'project3'))

        # capital P in Projects
        self.assertEqual(detect_projects(['Student Name Line', 'Projects', 'project1', 'project2', '----------']), ('project1', 'project2'))

        # capital PROJECTS
        self.assertEqual(detect_projects(['Student Name Line', 'PROJECTS', 'project1', 'project2', '----------']), ('project1', 'project2'))

        # space between PROJECTS
        self.assertEqual(detect_projects(['Student Name Line', 'PROJECTS', '', '', 'project1', '', 'project2', '', '----------']), ('project1', 'project2'))

    def read_html_template(self):
        # contains opening a file and saving to a variable... does not return anything
        pass

    def test_remove_bottom_end_tags(self):
        bottom_tags = ['html_line_minus2',
                       'html_line_minus1',
                       '</body>',
                       '</html>',   # -> file ends here
                       '',
                       '']

        self.assertEqual(remove_bottom_end_tags(bottom_tags), ['html_line_minus2', 'html_line_minus1'])

    def test_add_bottom_end_tags(self):

        bottom_tags2 = ['html_line_minus2',
                       'html_line_minus1']

        self.assertEqual(add_bottom_end_tags(bottom_tags2), ['html_line_minus2',
                                                               'html_line_minus1',
                                                               '</div>',
                                                               '</body>',
                                                               '</html>'])   # -> file ends here

    def test_add_pagewrap(self):
        top_tags = ['tagline1',
                    'tagline2']

        self.assertEqual(add_pagewrap(top_tags), ['tagline1',
                                                  'tagline2',
                                                  '<div id="page-wrap">'])

    def test_surround_block(self):

        # test surrounding html
        self.assertEqual(surround_block('h1', 'Eagles'), "<h1>Eagles</h1>")

        # test surrounding html
        self.assertEqual(surround_block('p', 'Lorem ipsum dolor sit amet, consectetur ' +
                                        'adipiscing elit. Sed ac felis sit amet ante porta ' +
                                        'hendrerit at at urna. Donec in vehicula ex. Aenean ' +
                                        'scelerisque accumsan augue, vitae cursus sapien venenatis ' +
                                        'ac. Quisque dui tellus, rutrum hendrerit nisl vitae, ' +
                                        'pretium mollis lorem. Pellentesque eget quam a justo ' +
                                        'egestas vehicula in eu justo. Nulla cursus, metus vitae ' +
                                        'tincidunt luctus, turpis lectus bibendum purus, eget ' +
                                        'consequat est lacus ac nibh. In interdum metus vel est ' +
                                        'posuere aliquet. Maecenas et euismod arcu, eu auctor ' +
                                        'libero. Phasellus lectus magna, auctor ac auctor in, ' +
                                        'suscipit id turpis. Maecenas dignissim enim ac justo ' +
                                        'tincidunt viverra. Sed interdum molestie tincidunt. Etiam ' +
                                        'vitae justo tincidunt, blandit augue id, volutpat ligula. ' +
                                        'Aenean ut aliquet mi. Suspendisse consequat blandit posuere.'),
                                        '<p>Lorem ipsum dolor sit amet, consectetur ' +
                                        'adipiscing elit. Sed ac felis sit amet ante porta ' +
                                        'hendrerit at at urna. Donec in vehicula ex. Aenean ' +
                                        'scelerisque accumsan augue, vitae cursus sapien venenatis ' +
                                        'ac. Quisque dui tellus, rutrum hendrerit nisl vitae, ' +
                                        'pretium mollis lorem. Pellentesque eget quam a justo ' +
                                        'egestas vehicula in eu justo. Nulla cursus, metus vitae ' +
                                        'tincidunt luctus, turpis lectus bibendum purus, eget ' +
                                        'consequat est lacus ac nibh. In interdum metus vel est ' +
                                        'posuere aliquet. Maecenas et euismod arcu, eu auctor ' +
                                        'libero. Phasellus lectus magna, auctor ac auctor in, ' +
                                        'suscipit id turpis. Maecenas dignissim enim ac justo ' +
                                        'tincidunt viverra. Sed interdum molestie tincidunt. Etiam ' +
                                        'vitae justo tincidunt, blandit augue id, volutpat ligula. ' +
                                        'Aenean ut aliquet mi. Suspendisse consequat blandit posuere.</p>')

    def test_create_email_link(self):

        # test created email
        self.assertEqual(
            create_email_link('lbrandon@wharton.upenn.edu'),
            '<a href="mailto:lbrandon@wharton.upenn.edu">lbrandon[aT]wharton.upenn.edu</a>')

        # test created email
        self.assertEqual(
            create_email_link('lbrandon.at.wharton.upenn.edu'),
            '<a href="mailto:lbrandon.at.wharton.upenn.edu">lbrandon.at.wharton.upenn.edu</a>')

    def test_add_s_info(self):

        s_info_output = ['html_header_l1',
                         'html_header_l2',
                         '<div>',
                         '<h1>student_name</h1>',
                         '<p>Email: <a href="mailto:student@email.com">student[aT]email.com</a></p>',
                         '</div>']

        # simple test
        self.assertEqual(add_s_info('student_name',
                                    'student@email.com',
                                    ['html_header_l1',
                                     'html_header_l2']), s_info_output)

    def test_add_s_projects(self):

        # 2 projects listed, no lead html
        html_input = []
        s_p_input1 = ['project1', 'project2']
        s_p_output1 = ['<div>',
                          '<h2>Projects</h2>',
                          '<ul>',
                          '<li>project1</li>',
                          '<li>project2</li>',
                          '</ul>',
                          '</div>']

        self.assertEqual(add_s_projects(s_p_input1, html_input), s_p_output1)

        # 1b - 2 lines of leading html before section, input same as before
        html_input_b = ['leading_html_l1', 'leading_html_l2']
        s_p_output1b = ['leading_html_l1',
                          'leading_html_l2',
                          '<div>',
                          '<h2>Projects</h2>',
                          '<ul>',
                          '<li>project1</li>',
                          '<li>project2</li>',
                          '</ul>',
                          '</div>']

        self.assertEqual(add_s_projects(s_p_input1, html_input_b), s_p_output1b)

        # 3 projects listed
        html_input2 = []
        s_p_input2 = ['project1', 'project2', 'project3']
        s_p_output2 = ['<div>',
                          '<h2>Projects</h2>',
                          '<ul>',
                          '<li>project1</li>',
                          '<li>project2</li>',
                          '<li>project3</li>',
                          '</ul>',
                          '</div>']

        self.assertEqual(add_s_projects(s_p_input2, html_input2), s_p_output2)

        # edge - no projects listed
        html_input3 = []
        s_p_input3 = []
        s_p_output3 = ['<div>',
                          '<h2>Projects</h2>',
                          '<ul>',
                          '</ul>',
                          '</div>']

        self.assertEqual(add_s_projects(s_p_input3, html_input3), s_p_output3)

        # edge - no projects listed, leading html
        html_input3b = ['leading_html_l1', 'leading_html_l2']
        s_p_input3b = []
        s_p_output3b = ['leading_html_l1',
                        'leading_html_l2',
                        '<div>',
                        '<h2>Projects</h2>',
                        '<ul>',
                        '</ul>',
                        '</div>']

        self.assertEqual(add_s_projects(s_p_input3b, html_input3b), s_p_output3b)

    def test_add_s_courses(self):
        html_input = ['leading_html_l1', 'leading_html_l2']
        s_course_input = ['Algorithms', 'Race car training']
        s_course_output = ['leading_html_l1',
                           'leading_html_l2',
                           '<div>',
                           '<h3>Courses</h3>',
                           '<span>Algorithms, Race car training</span>',
                           '</div>']

        self.assertEqual(add_s_courses(s_course_input, html_input), s_course_output)

        html_input = []
        s_course_input = ['Algorithms', 'Race car training']
        s_course_output = ['<div>',
                           '<h3>Courses</h3>',
                           '<span>Algorithms, Race car training</span>',
                           '</div>']

        self.assertEqual(add_s_courses(s_course_input, html_input), s_course_output)

        html_input = []
        s_course_input = []
        s_course_output = ['<div>',
                           '<h3>Courses</h3>',
                           '<span></span>',
                           '</div>']

        self.assertEqual(add_s_courses(s_course_input, html_input), s_course_output)

        html_input = ['leading_html_l1', 'leading_html_l2']
        s_course_input = []
        s_course_output = ['leading_html_l1',
                           'leading_html_l2',
                           '<div>',
                           '<h3>Courses</h3>',
                           '<span></span>',
                           '</div>']

        self.assertEqual(add_s_courses(s_course_input, html_input), s_course_output)

    def test_main(self):
        pass

if __name__ == '__main__':
    unittest.main()
