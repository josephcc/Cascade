
def template(name):
    return open('templates/%s.html' % name).read()

def render(name, args):
    return template(name) % args

def dataset(qid):
    return open('dataset/%s.tsv' % qid)

Q = {
        96: 'What does a planet need to support life?',
        102: 'How do I unclog my bathtub?'
        115: 'How do I get my tomato plants to grow more tomatoes?',
        116: 'What are the best day trips possible from Barcelona, Spain?',
}
def question(qid):
    return Q[qid]

def batches(iterable, n = 1):
   l = len(iterable)
   for ndx in range(0, l, n):
       yield iterable[ndx:min(ndx+n, l)]
