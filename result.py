from nltk.corpus import wordnet
from textblob import TextBlob
from textblob import Word
def everything(ch):
	result=[[ch]]
	syns = wordnet.synsets(ch)
	if syns!=[]:
		k=[]
		for i in (syns[0].lemmas()):
			k.append(i.name())
		k=[]
		for i in syns:
			if i.definition() != []:
				k.append(i.definition())
		result.append(k)
		k=[]
		for i in syns:
			if i.examples() != []:
				for j in i.examples():
					k.append(j)
		result.append(k)
		synonimes=[]
		antonyms=[]
		for syn in syns:
			for l in syn.lemmas():
				synonimes.append(l.name())
				if l.antonyms():
					antonyms.append(l.antonyms()[0].name())
		
		synonimes=set(synonimes)
		antonyms=set(antonyms)
		k=[]
		for i in synonimes:
			try:
				if syns[0].wup_similarity(wordnet.synset(i+".n.01")) != None:
					k.append(i+" (NOUN)")
			except:
				pass
			try:
				if syns[0].wup_similarity(wordnet.synset(i+".v.01")) != None:
					k.append(i+" (VERB)")
			except:
				pass
			try:
				if syns[0].wup_similarity(wordnet.synset(i+".a.01")) != None:
					k.append(i+" (ADJECTIVE)")
			except:
				pass
			try:
				if syns[0].wup_similarity(wordnet.synset(i+".s.01")) != None:
					k.append(i+" (ADJECTIVE SATELLITE)")
			except:
				pass
			try:
				if syns[0].wup_similarity(wordnet.synset(i+".r.01")) != None:
					k.append(i+" (ADVERB)")
			except:
				pass
		result.append(k)
		k=[]
		for i in antonyms:
			try:
				if syns[0].wup_similarity(wordnet.synset(i+".n.01")) != None:
					k.append(i+" (NOUN)")
			except:
				pass
			try:
				if syns[0].wup_similarity(wordnet.synset(i+".v.01")) != None:
					k.append(i+" (VERB)")
			except:
				pass
			try:
				if syns[0].wup_similarity(wordnet.synset(i+".a.01")) != None:
					k.append(i+" (ADJECTIVE)")
			except:
				pass
			try:
				if syns[0].wup_similarity(wordnet.synset(i+".s.01")) != None:
					k.append(i+" (ADJECTIVE SATELLITE)")
			except:
				pass
			try:
				if syns[0].wup_similarity(wordnet.synset(i+".r.01")) != None:
					k.append(i+" (ADVERB)")
			except:
				pass
		result.append(k)
	return(result)
def main(a):
	w = Word(a)
	if w.spellcheck()==[(a,1.0)]:
		return(everything(a))
	else:
		return(w.spellcheck())
