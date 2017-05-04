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


class CommentView:
    def __init__(self):
        self.user = None
        self.content = ''
        self.date_publish = None
        self.thumbsup = 0


class ArticleView:
    def __init__(self):
        self.id = 0
        self.content = ''
        self.user = None
        self.date_publish = None
        self.thumbsup = 0
        self.comments = []
        self.comments_length=0

# Create your tests here.
class Ques_Article:
    def __init__(self):
        self.qid = 0
        self.tags = []
        self.queston_decs = ''
        self.queston_title = ''
        self.articles = []
        self.article_count = 0


def getArticleCommet(qid):
    question = Question.objects.get(id=qid)
    ques_art = Ques_Article()
    ques_art.qid = question.id
    ques_art.tags = question.tag.all()
    ques_art.queston_title = question.title
    ques_art.queston_decs = question.desc
    # ques_art.articles=question.article.all()
    count = Question.objects.filter(id=qid).annotate(count=Count('article')).values('count')[0]
    ques_art.article_count = count['count']

    ques_art.articles = []

    articles = question.article.all()
    for art in articles:
        arti_view = ArticleView()
        arti_view.id = art.id

        # dr = re.compile(r'<[^>]+>', re.S)
        # dd = dr.sub('', art.content)
        # arti_view.content = dd

        arti_view.content = art.content
        arti_view.date_publish = art.date_publish
        arti_view.thumbsup = art.thumbsup
        arti_view.user = art.user

        arti_view.comments = []

        for com in art.comment.all():
            # print unicode(c.content)
            com_view = CommentView()
            com_view.user = com.user
            com_view.content = com.content
            com_view.date_publish = com.date_publish
            com_view.thumbsup = com.thumbsup
            arti_view.comments.append(com_view)
        arti_view.comments_length=len(arti_view.comments)
        ques_art.articles.append(arti_view)
    return ques_art