import nltk
from nltk.corpus import conll2000
from django.core.management.base import BaseCommand, CommandError
import re


class Command(BaseCommand):
    text = '''
    Workers arrange EVMs in a strong room in Bengaluru after Karnataka Assembly elections.Karnataka election result 2023 will be declared on Saturday, 
    May 13, three days after the voting to elect the 224 members of the state Assembly. Karnataka recorded a voting percentage of 73.19 - its highest 
    ever - in Wednesdays polling. The state witnessed a fierce fight between the ruling Bharatiya Janata Party BJP and the Congress, with both the 
    parties claiming they will cross the magic figure and form the government on their own. Janata Dal Secular, which has previously formed the 
    government in Karnataka, has also expressed confidence about its electoral fortunes. JDS leader HD Kumaraswamy asserted on Wednesday that his 
    party will be King and not just the King maker.Karnataka Assembly election 2023 were held almost a year before the 2024 general elections. All 
    the parties would want to emerge victorious in this electoral battle.Exit polls released after the polling on Wednesday evening indicated a close 
    contest between the Congress and the BJP in the Karnataka Assembly elections. Most pollsters have given Congress a slight advantage in the race.
    Answer: The Karnataka election result coverage and counting will begin at 8am on Saturday, May 13, 2023.Answer: The detailed coverage and overall 
    results of Karnataka Assembly election 2023 can be checked live on ndtv.com. You may also watch the live stream of the election coverage on NDTV 
    24x7 and NDTV India.The one-stop shop for results from each constituency and the fate of individual candidates is here.Answer: The state has 224 
    Assembly seats and the fate of all the contestants will be decided on Saturday. The counting will be held in 36 centres across Karnataka, and poll 
    officials expect a clear picture about the outcome is likely to emerge by mid-day.Answer: The two main parties that have contested the elections 
    are BJP which is in power and Congress. The ruling BJP is looking to break a 38-year-old poll jinx where people have never voted the incumbent 
    party to power, while the Congress is hoping for a morale booster victory to give it a much-needed elbow room and momentum to position itself as 
    the main opposition player in the 2024 Lok Sabha elections.The Aam Aadmi Party AAP, which is in power in Delhi and Punjab, has also fielded its 
    candidates. Also there were some smaller parties in the fray in a few constituencies.Answer: The BJP had then emerged as the single largest party 
    by winning 104 seats, followed by Congress with 80 seats and JDS 37. There was also one independent member, while the Bahujan Samaj Party BSP and 
    Karnataka Pragnyavantha Janatha Party KPJP got one legislator each elected.In the 2018 elections, the Congress garnered a vote-share of 38.04 per 
    cent, followed by the BJP 36.22 per cent and the JDS 18.36 per cent.Track Latest News and Karnataka Elections 2023  Coverage Live on NDTV.com and 
    get news updates from India and around the world.
    ''';

    def handle(self, *args, **options):
        nltk.download('punkt')
        nltk.download('averaged_perceptron_tagger')
        nltk.download('brown')
        nltk.download('conll2000')
        nltk.download('treebank')
        nltk.download('maxent_ne_chunker')
        nltk.download('words')
        nltk.download('ieer')
        sentences = nltk.sent_tokenize(self.text)
        sentences = [nltk.word_tokenize(sent) for sent in sentences]
        # tokenize
        # print(sentences)
        sentences = [nltk.pos_tag(sent) for sent in sentences]
        # pos tag
        # print(sentences)
        
        # noun phrase chunking
        grammar = "NP: {<DT>?<JJ>*<NN>}"
        cp = nltk.RegexpParser(grammar)
        result = cp.parse(sentences[0])
        # print(result)
        
        # cp = nltk.RegexpParser('CHUNK: {<V.*> <TO> <V.*>}')
        # brown = nltk.corpus.brown
        # for sent in brown.tagged_sents():
        #     tree = cp.parse(sent)
        #     for subtree in tree.subtrees():
        #         if subtree.label() == 'CHUNK': print(subtree)
        
        # chinking done
        grammar = r"""
        NP:
            {<.*>+}
            }<VBD|IN>+{
        """
        
        cp = nltk.RegexpParser(grammar)
        print(cp.parse(sentences[0]))
        
        # Representing chunks: Tags and Trees
        # print(nltk.chunk.conllstr2tree(self.text, chunk_types=['NP']).draw())
        
        print(conll2000.chunked_sents('train.txt')[99])
        
        # cp = nltk.RegexpParser("")
        # test_sents = conll2000.chunked_sents('test.txt', chunk_types=['NP'])
        # print(cp.evaluate(test_sents))
        
        # grammar = r"NP: {<[CDJNP].*>+}"
        # cp = nltk.RegexpParser(grammar)
        # print(cp.evaluate(test_sents))
        
        # chunker = ConsecutiveNPChunker(train_sents)
        # print(chunker.evaluate(test_sents))
        
        # t= nltk.Tree('(S (NP Alice) (VP chased (NP the rabbit)))')
        # self.traverse(t)
        sent = nltk.corpus.treebank.tagged_sents()[22]
        print(nltk.ne_chunk(sent, binary=True))
        
        # relation extraction
        # here we can have our docs
        IN = re.compile(r'.*\bin\b(?!\b.+ing)')
        for doc in nltk.corpus.ieer.parsed_docs('NYT_19980315'):
            for rel in nltk.sem.extract_rels('ORG', 'LOC', doc, corpus='ieer', pattern=IN):
                print(nltk.sem.rtuple(rel))
                
        vnv = """
         (
         is/V|    # 3rd sing present and
         was/V|   # past forms of the verb zijn ('be')
         werd/V|  # and also present
         wordt/V  # past of worden ('become)
         )
         .*       # followed by anything
         van/Prep # followed by van ('of')
         """
        # VAN = re.compile(vnv, re.VERBOSE)
        # for doc in conll2000.chunked_sents('ned.train'):
        #     for rel in nltk.sem.extract_rels('PER', 'ORG', doc, corpus='conll2000', pattern=VAN):
        #         print(nltk.sem.clause(rel, relsym="VAN"))
        
    def npchunk_features(sentence, i, history):
        word, pos = sentence[i]
        return {"pos": pos}
    
    #tree traversal
    def traverse(self,t):
        try:
            t.label()
        except AttributeError:
            print(t, end=" ")
        else:
            print('(', t.label(), end=' ')
            for child in t:
                self.traverse(child)
                print(')', end=" ")
                
        
        
# class UnigramChunker(nltk.ChunkParserI):
#     def __init__(self, train_sents):
#         train_data = [[(t,c) for w,t,c in nltk.chunk.tree2conlltags(sent)]
#                       for sent in train_sents]
#         self.tagger = nltk.UnigramTagger(train_data) [2]

#     def parse(self, sentence):
#         pos_tags = [pos for (word,pos) in sentence]
#         tagged_pos_tags = self.tagger.tag(pos_tags)
#         chunktags = [chunktag for (pos, chunktag) in tagged_pos_tags]
#         conlltags = [(word, pos, chunktag) for ((word,pos),chunktag)
#                      in zip(sentence, chunktags)]
#         return nltk.chunk.conlltags2tree(conlltags)
    
    
# class ConsecutiveNPChunkTagger(nltk.TaggerI):

#     def __init__(self, train_sents):
#         train_set = []
#         for tagged_sent in train_sents:
#             untagged_sent = nltk.tag.untag(tagged_sent)
#             history = []
#             for i, (word, tag) in enumerate(tagged_sent):
#                 featureset = npchunk_features(untagged_sent, i, history) [2]
#                 train_set.append( (featureset, tag) )
#                 history.append(tag)
#         self.classifier = nltk.MaxentClassifier.train([3]
#             train_set, algorithm='megam', trace=0)

#     def tag(self, sentence):
#         history = []
#         for i, word in enumerate(sentence):
#             featureset = npchunk_features(sentence, i, history)
#             tag = self.classifier.classify(featureset)
#             history.append(tag)
#         return zip(sentence, history)

# class ConsecutiveNPChunker(nltk.ChunkParserI):
#     def __init__(self, train_sents):
#         tagged_sents = [[((w,t),c) for (w,t,c) in
#                          nltk.chunk.tree2conlltags(sent)]
#                         for sent in train_sents]
#         self.tagger = ConsecutiveNPChunkTagger(tagged_sents)

#     def parse(self, sentence):
#         tagged_sents = self.tagger.tag(sentence)
#         conlltags = [(w,t,c) for ((w,t),c) in tagged_sents]
#         return nltk.chunk.conlltags2tree(conlltags)