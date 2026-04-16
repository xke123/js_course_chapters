import re
import os
from datetime import timedelta

# 提取出的章节内容与起始时间戳
chapters = [
    {"title": "Intro", "start": "00:00:00"},
    {"title": "Lesson 1 - JavaScript Basics", "start": "00:02:01"},
    {"title": "Lesson 2 - Numbers and Math", "start": "00:14:48"},
    {"title": "Lesson 3 - Strings", "start": "00:43:26"},
    {"title": "Lesson 4 - HTML CSS Review", "start": "01:07:32"},
    {"title": "Lesson 5 - Variables", "start": "01:51:06"},
    {"title": "Lesson 6 - Booleans and If-Statements", "start": "02:32:55"},
    {"title": "Lesson 7 - Functions", "start": "03:34:12"},
    {"title": "Lesson 8 - Objects", "start": "04:15:45"},
    {"title": "Lesson 9 - DOM", "start": "05:25:46"},
    {"title": "Lesson 10 - HTML CSS JS Together", "start": "06:38:51"},
    {"title": "Lesson 11 - Arrays and Loops", "start": "07:42:28"},
    {"title": "Lesson 12 - Advanced Functions", "start": "09:28:26"},
    {"title": "Lesson 13 - Amazon Project and Git", "start": "10:58:57"},
    {"title": "Lesson 14 - Modules", "start": "12:28:00"},
    {"title": "Lesson 15 - External Libraries", "start": "13:56:33"},
    {"title": "Lesson 16 - Testing", "start": "15:34:37"},
    {"title": "Lesson 17 - Object-Oriented Programming", "start": "17:36:30"},
    {"title": "Lesson 18 - Backend Async Await", "start": "19:32:59"}
]

def parse_time(time_str):
    """高容错时间转换：兼容单数字、点号分隔符等非标准情况"""
    time_str = time_str.replace('.', ',') # 把句号纠正为逗号
    if ',' in time_str:
        t, ms = time_str.split(',')
        ms = ms.ljust(3, '0')[:3] # 确保毫秒是3位
        h, m, s = map(int, t.split(':'))
        return timedelta(hours=h, minutes=m, seconds=s, milliseconds=int(ms))
    else:
        h, m, s = map(int, time_str.split(':'))
        return timedelta(hours=h, minutes=m, seconds=s)

def format_time(td):
    if td.total_seconds() < 0:
        td = timedelta(0)
    
    total_seconds = int(td.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    milliseconds = int(td.microseconds / 1000)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d},{milliseconds:03d}"

def split_srt(input_srt, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for i in range(len(chapters)):
        chapters[i]['start_td'] = parse_time(chapters[i]['start'])
        if i < len(chapters) - 1:
            chapters[i]['end_td'] = parse_time(chapters[i+1]['start'])
        else:
            chapters[i]['end_td'] = timedelta(days=99)
        chapters[i]['subs'] = []

    try:
        with open(input_srt, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        with open(input_srt, 'r', encoding='utf-8-sig') as f:
            content = f.read()

    blocks = re.split(r'\n\s*\n', content.strip())
    
    last_processed_time = "未知"

    for block in blocks:
        lines = block.split('\n')
        if len(lines) >= 3:
            time_line = lines[1].strip()
            # 放宽正则：允许小时位为1-3位，分秒1-2位，兼容点号
            match = re.search(r'(\d{1,3}:\d{1,2}:\d{1,2}[,\.]\d{1,3})\s*-->\s*(\d{1,3}:\d{1,2}:\d{1,2}[,\.]\d{1,3})', time_line)
            
            if match:
                start_str, end_str = match.groups()
                start_td = parse_time(start_str)
                end_td = parse_time(end_str)
                last_processed_time = start_str # 记录追踪时间
                
                for chapter in chapters:
                    if chapter['start_td'] <= start_td < chapter['end_td']:
                        new_start = start_td - chapter['start_td']
                        new_end = end_td - chapter['start_td']
                        
                        chapter['subs'].append({
                            'time_line': f"{format_time(new_start)} --> {format_time(new_end)}",
                            'text': '\n'.join(lines[2:])
                        })
                        break

    for i, chapter in enumerate(chapters):
        if not chapter['subs']:
            continue
            
        safe_title = "".join(c for c in chapter['title'] if c.isalnum() or c in (' ', '-', '_')).rstrip()
        output_file = os.path.join(output_dir, f"{str(i).zfill(2)}_{safe_title}.srt")
        
        with open(output_file, 'w', encoding='utf-8') as f:
            for idx, sub in enumerate(chapter['subs'], start=1):
                f.write(f"{idx}\n")
                f.write(f"{sub['time_line']}\n")
                f.write(f"{sub['text']}\n\n")
                
        print(f"✅ 生成字幕: {output_file} (包含 {len(chapter['subs'])} 条对话)")
        
    print("-" * 40)
    print(f"🔍 诊断信息：脚本读到的最后一条有效字幕的时间是 -> [{last_processed_time}]")

if __name__ == "__main__":
    INPUT_SRT = "JavaScript Tutorial Full Course - Beginner to Pro.中文.srt"
    OUTPUT_DIRECTORY = "./js_course_chapters"
    
    print("开始处理字幕文件...")
    split_srt(INPUT_SRT, OUTPUT_DIRECTORY)
    print("✨ 处理结束！")