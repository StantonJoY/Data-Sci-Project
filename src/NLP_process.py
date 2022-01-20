import spacy
from spacy.matcher import Matcher
from spacy.lang.en.stop_words import STOP_WORDS
import os
from pyecharts import options as opts
from pyecharts.charts import WordCloud
from pyecharts.globals import SymbolType

"""
@:param filePath 项目中的隐私政策路径
@:return  加了规则的nlp对象
"""


def getDoc_en(filePath):
    nlp = spacy.load('en_core_web_sm')
    doc = open(filePath).read()
    doc = nlp(doc)
    return doc


"""
@:param doc nlp文本
@:return 经过一系列规则筛选的关键词
"""


def getMatcher(doc):
    # 用spaCy词汇表初始化Matcher
    matcher = Matcher(doc.vocab)
    # 定义规则
    pattern_your = [{'TEXT': 'your'}, {'POS': 'ADJ', 'OP': '*'}, {'POS': 'NOUN', 'OP': '+'}]  # your address, phone
    pattern_including = [{'TEXT': {"IN": ["including", "include", "includes"]}}, {'POS': 'ADJ', 'OP': '*'},
                         {'POS': 'NOUN', 'OP': '+'},
                         {'TEXT': "and", 'OP': '*'}, {'POS': 'ADJ', 'OP': '*'},
                         {'POS': 'NOUN', 'OP': '+'}]  # including device, ip,
    pattern_info = [{'POS': 'ADJ', 'OP': '*'}, {'POS': 'NOUN', 'OP': '*'},
                    {'TEXT': {"IN": ["data", "information", "address"]}}]
    pattern_per = [{'TEXT': {"IN": ["personal", "private"]}}, {'POS': 'ADJ', 'OP': '*'},
                   {'POS': 'NOUN', 'OP': '*'}]
    # 添加规则
    matcher.add('rule_Your', None, pattern_your)
    matcher.add('rule_include', None, pattern_including)
    match_res = matcher(doc)

    # 提取匹配文本
    list = []
    for match_id, start, end in match_res:
        # 获得匹配的范围
        matched_span = doc[start:end]
        list.append(matched_span.text)
    return list


"""
@:param filePath 路径
@:param dataBase 隐私信息库
@:return （list） 包含的隐私信息
"""


def proc(filePath, dataBase):
    res = []
    nlp = spacy.load('en_core_web_lg')
    doc = open(filePath).read()
    doc = nlp(doc)

    # 基础操作：与数据库匹配
    for chunk in doc.noun_chunks:
        word1 = nlp(chunk.text)
        with open(dataBase)as db:
            line = db.readline()
            while line:
                word2 = nlp(line)
                similarity = word1.similarity(word2)
                if similarity > 0.85:
                    res.append(chunk.text)
                    break
                line = db.readline()
    return res


def crawlerProc():
    nlp = spacy.load('en_core_web_sm')
    stop_word = []
    with open('../stopwords.txt', encoding='utf-8')as f:
        line = f.readline()
        while line:
            stop_word.append(line)
            line = f.readline()
    i = 0
    while i <= 95:
        list = []
        print(i)
        i += 1
        try:
            path = r"../data/privacy policy/"
            doc = open(path + "%d" % i + ".txt", encoding='utf-8').read()
            doc = nlp(doc)
            with open(r"./db/" + "%d" % i + '.txt', mode='w', encoding='utf-8')as f:
                for chunk in doc.noun_chunks:
                    list.append(chunk.text)
                for word in list:
                    lexeme = nlp.vocab[word]
                    if lexeme.is_stop == False and word not in stop_word:
                        f.write(word + '\n')
        except:
            FileNotFoundError


def render_cloud():
    data = []
    with open("../data.txt", encoding='utf-8')as f:
        line1 = f.readline()
        line2 = f.readline()
        while line1:
            temp = [line1, line2]
            dup = tuple(temp)
            data.append(dup)
            line1 = f.readline()
            line2 = f.readline()
    c = (
        WordCloud()
            .add("", data, word_size_range=[20, 100], shape=SymbolType.DIAMOND)
            .set_global_opts(title_opts=opts.TitleOpts(title="WordCloud-shape-diamond"))
            .render("privacy policy.html")
    )


if __name__ == '__main__':
    crawlerProc()
