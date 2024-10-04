# coding:utf-8
from my_custom_package import todayDateFileName, strdate, createAndScrape, write_to_top_of_file

title = strdate
url = './' + todayDateFileName
description = 'Crypto Daily News Feed - ' + strdate
readme_new_top_line = (u"* [{title}]({url}):{description}\n".format(title=title, url=url, description=description))

def job():
    createAndScrape('Crypto Daily News Feed', todayDateFileName, '2023', strdate, isToday=True)
    write_to_top_of_file('README.md', readme_new_top_line)
    
if __name__ == '__main__':
    job()