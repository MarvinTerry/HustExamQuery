# HustExamQuery

A project for Husters, helping you get exam schedule.

*powered by [HustAuth](https://github.com/MarvinTerry/HustAuth).*

## Requirements

1. Python packages

    ```
    requests
    requests_hustauth
    ics
    datetime
    ```

2. Tesseract-OCR back-end *(essential, dependency of [HustAuth](https://github.com/MarvinTerry/HustAuth))*

    ```
    sudo apt install tesseract-ocr
    ```
    P.S. For Windows users [download binary here](https://digi.bib.uni-mannheim.de/tesseract/) (5.0.0+)
    
## Usage

example:

```python
from exam_query import *
from exam_process import *

Uname = 'U20xxxxxx'
Upass = 'xxxxxxxx'

exam_list = get_exam_info(Uname,Upass)
exam_to_md(exam_list, 'exam.md')
exam_to_calendar(exam_list, 'exam.ics')
```

explanation:

- ```Uname```&```Upass```: hust account u/p
- ```get_exam_info```: fetch exam list from web
- ```exam_to_md```: save the table as md
- ```exam_to_calendar```: save as calendar format


## Demo

<img src="https://github.com/MarvinTerry/HustExamQuery/assets/58030272/72290d94-222a-493b-a85d-843ffc7f7a32" alt="Image" style="width:300px">
<img src="https://github.com/MarvinTerry/HustExamQuery/assets/58030272/71ed9569-a8c0-41c9-9876-e804a1c158f4" alt="Image" style="width:200px">




