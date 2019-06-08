# coding=utf-8

import json
import os
import jieba
import re
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator

filepath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

bookmark_path = os.path.join(filepath, 'Bookmarks')
fontpath = os.path.join(filepath, 'font', 'sarasa-ui-sc-regular.ttf')


def export_bookmark(node):
    """提取 Bookmarks 文件中的每个书签项目"""
    if 'url' in node:
        yield dict(name=node['name'], url=node['url'])
    elif 'children' in node:
        for n in node['children']:
            yield from export_bookmark(n)
    else:
        yield 'nothing'


def jieba_custom():
    custom_word_list = ['树莓派', '公众号', '哔哩哔哩', '百度网盘', '红黑联盟', '吾爱破解', '以太坊', '前后端',
                        '中州韻輸入法引擎', '再创世纪']
    for i in custom_word_list:
        jieba.add_word(i)


def cut_json(data):
    jieba_custom()
    filter_str = r'\s+|–|-|_|\||\.|,|，|、|—|:|：|\/|的|）|（|\(|\)|和|吧|&|!|【|】|\？|\'|゜|\[|\]|与|让|用|·|•|»|=|\+|~|在|不|《|》|你|！|之|及|是|\?|上|下|到|。|\…|「|」|“|”|#|『|』|๑'
    space_regex = re.compile(filter_str)
    for bookmark in data:
        name = space_regex.sub(r'', bookmark['name'])
        yield from jieba.cut(name, cut_all=False)


def gen_wordcloud(contents):

    bookmark_cloud = WordCloud(font_path=fontpath,
                               background_color="white",
                               max_words=2000,
                               #    mask=back_coloring,  # 设置背景图片
                               max_font_size=100,
                               random_state=42,
                               width=1000, height=860, margin=2,
                               )

    bookmark_cloud.generate_from_frequencies(contents)

    plt.figure()
    plt.imshow(bookmark_cloud)
    plt.axis("off")
    plt.show()


def main():
    # 提取书签
    with open(bookmark_path, 'r', encoding='utf-8') as f:
        contents = json.load(f)

    bookmark_bar = list(export_bookmark(contents['roots']['bookmark_bar']))
    bookmark_bar.extend(list(export_bookmark(contents['roots']['other'])))

    # jieba 分词统计
    res = cut_json(bookmark_bar)

    # 取出 top 300
    # top = 300
    # jieba_dict = dict(Counter(list(res)).most_common(top))
    jieba_dict = dict(Counter(list(res)))
    gen_wordcloud(jieba_dict)


if __name__ == "__main__":
    main()
