from ics import Calendar, Event
from datetime import datetime, timedelta

def exam_to_calendar(exam_list:list, ics_file_path:str) -> None:
    # map time to iso_format
    time_map = {
        "上午":"T083000+08",
        "下午":"T143000+08",
        "晚上":"T190000+08"
    }    

    cal = Calendar()

    for exam in exam_list:
        # eg:'2023-10-29 晚上' -> isoformat '2023-10-29T183000+08'
        begin_time = exam["KSRQ"][:-3] + time_map[exam["KSRQ"][-2:]]

        event = Event()
        event.name = exam["KCMC"] + "考试"
        event.begin = datetime.fromisoformat(begin_time)  
        event.end = event.begin + timedelta(hours=2.5)  
        event.location = exam["JSMC"]

        cal.events.add(event)

    with open(ics_file_path, "w", encoding='utf-8') as f:
            f.writelines(cal)
            
    print("华科考试日历已输出至 " + ics_file_path)
    


def exam_to_md(exam_list:list,md_file_path:str) -> None:
    eg = exam_list[0]
    xqmc = eg["XQMC"]
    sfid = eg["SFID"]
    xm = eg["XM"]

    md = "# 华中科技大学{}考试列表\n\n".format(xqmc)
    md += "{}({})\n\n".format(xm, sfid)
    
    md += "|课程|考试时间|考试地点|\n"
    md += "|:---:|:---:|:---:|\n"

    for exam in exam_list:
        md += "|" + exam["KCMC"] + "|" + exam["KSRQ"] + "|" + exam["JSMC"] + "|\n"

    md += '<p align="right">生成时间：{}</p>'.format(datetime.now().date().isoformat())

    with open(md_file_path, "w", encoding='utf-8') as f:
        f.writelines(md)
    print("华科考试列表已输出至 " + md_file_path)
