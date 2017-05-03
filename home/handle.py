from models import *
from django.db.models import Max, Count


class Elem():
    def __init__(self):
        self.question_id = 0
        self.question_title = ''
        self.date_publish = ''
        self.focus_num = 0
        self.simple_desc = None


def getSequence(length, divide):
    seq = []
    while (length > divide):
        seq.append(divide)
        length = length - divide
    seq.append(length)

    start = 0
    result = []
    for s in seq:
        end = start + s
        tup = (start, end)
        start = end
        result.append(tup)
    return result


def getIndexPage(query):
    content = []
    for question in query:
        elem = Elem()
        elem.question_id = question.id
        elem.question_title = question.title
        elem.date_publish = question.date_publish
        elem.focus_num = question.focus_num
        article = question.article.annotate(Max('thumbsup'))[0]
        elem.article = article
        dr = re.compile(r'<[^>]+>', re.S)
        dd = dr.sub('', article.content)
        elem.simple_desc = dd
        content.append(elem)
    return content


def showPage(query, result, pagenum):
    start = result[pagenum][0]
    end = result[pagenum][1]
    query = query[start:end]
    index_content = getIndexPage(query)
    return index_content


class MostReply:
    def __init__(self):
        self.id = 0
        self.count = 0
        self.title = ''


def getMostReply(query):
    MostReply_list = []
    for q in query:
        reply = MostReply()
        reply.count = q['count']
        reply.title = unicode(q['title'])
        reply.id = q['id']
        MostReply_list.append(reply)

    return MostReply_list
    # for reply in reply_list:
    #     print reply.count, reply.title, reply.id
