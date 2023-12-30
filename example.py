from exam_query import *
from exam_process import *

Uname = 'U20xxxxxx'
Upass = 'xxxxxxxx'

exam_list = get_exam_info(Uname,Upass)
exam_to_md(exam_list, 'exam.md')
exam_to_calendar(exam_list, 'exam.ics')
