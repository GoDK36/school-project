import os, re

inDir = r"D:\GOD's folder\자료\대학교\언어학\프로그래밍 연습\과제\과제3"
outDir = r"D:\GOD's folder\자료\대학교\언어학\프로그래밍 연습\과제\과제3\작성중"

with open(os.path.join(inDir, 'WRAY00001.sjml'), 'r', encoding='utf8') as inF:
    txt = inF.read()

author = re.findall('<author>(.*?)</author>', txt)[0]
for atc_attr, atc_only in re.findall('(<text.*?>)(.*?)</text>', txt, re.S):
    id_ = re.findall('id="(.*?)"', atc_attr)[0]
    date = re.findall('date="(.*?)"', atc_attr)[0]
    subclass = re.findall('subclass="(.*?)"', atc_attr)[0]
    body1 = re.sub(re.compile(r'^\s+',re.M),'  ', atc_only)
    body2 = re.sub('</byline>\n','</byline>',body1)
    output = f"""<header>
  <author>{author}</author>
  <date>{date}</date>
  <subclass>{subclass}</subclass>
</header>
<body>
{body2}
</body>
"""
    fn = id_+'.xml'
    with open(os.path.join(outDir, fn), 'w', encoding='utf8') as outF:
        outF.write(output)
