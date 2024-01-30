# -*- coding: utf-8 -*-
"""
@author: PC
Update Time: 2024-11-24
"""
from Depend.News import News
from Depend.ArgumentParser import AP

class Entry:
    def __init__(self):
        self.type = None
        self.pathname = None

    def main(self):
        ap = AP(self)
        ap.config_once()
        news = News(self)
        news.main()

if __name__ == '__main__':
    entry = Entry()
    entry.main()