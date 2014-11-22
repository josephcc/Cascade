
def template(name):
    return open('templates/%s.html' % name).read()

def render(name, args):
    return template(name) % args

def dataset(qid):
    return open('dataset/%s.tsv' % qid)

Q = {
        102: 'How do I unclog my bathrub?'
}
def question(qid):
    return Q[qid]

def batches(iterable, n = 1):
   l = len(iterable)
   for ndx in range(0, l, n):
       yield iterable[ndx:min(ndx+n, l)]
