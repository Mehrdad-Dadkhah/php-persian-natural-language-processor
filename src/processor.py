#!/usr/bin/python
# -*- coding: utf8 -*-

from __future__ import unicode_literals
from hazm import *
import json, sys, os

def normilizeText(txt):
	normalizer = Normalizer()

	return normalizer.normalize(txt)

def sentTokenizeText(txt):
	normalText = normilizeText(txt)
	
	return {
		'main': sent_tokenize(txt),
		'normalized': sent_tokenize(normalText)
	}

def wordTokenizeText(txt):
	normalText = normilizeText(txt)
	
	return {
		'main': word_tokenize(txt),
		'normalized': word_tokenize(normalText)
	}

def postTagText(txt):
	fileDir = os.path.abspath(os.path.dirname(__file__))
	filefullPath = os.path.join(fileDir, 'resources/postagger.model')

	normalText = normilizeText(txt)
	
	tagger = POSTagger(model=filefullPath)

	return {
		'main': tagger.tag(word_tokenize(txt)),
		'normalized': tagger.tag(word_tokenize(normalText))
	}

def chunksText(txt):
	fileDir = os.path.abspath(os.path.dirname(__file__))
	filefullPath = os.path.join(fileDir, 'resources/chunker.model')

	chunker = Chunker(model=filefullPath)
	
	tags = postTagText(txt)

	return {
		'main': chunker.parse(tags['main']),
		'normalized': chunker.parse(tags['normalized'])
	}

def getChunksGroup(txt):
	chunks = chunksText(txt)

	return {
		'main': tree2brackets(chunks['main']),
		'normalized': tree2brackets(chunks['normalized'])
	}

def stemText(txt):
	stemmer = Stemmer()
	tags = postTagText(txt)

	data = {
		'main': {
			'V': [],
			'ADV': [],
			'N': [],
			'Ne': []
		},
		'normalized': {
			'V': [],
			'ADV': [],
			'N': [],
			'Ne': []
		}
	}

	for tag in tags['main']:
		if tag[1] in ('N', 'Ne', 'V', 'ADV'):
			data['main'][tag[1]].append(stemmer.stem(tag[0]))

	for tag in tags['main']:
		if tag[1] in ('N', 'Ne', 'V', 'ADV'):
			data['normalized'][tag[1]].append(stemmer.stem(tag[0]))

	return data

def lemmatizeText(txt):
	lemmatizer = Lemmatizer()
	tags = postTagText(txt)

	data = {
		'main': {
			'V': [],
			'ADV': [],
			'N': [],
			'Ne': []
		},
		'normalized': {
			'V': [],
			'ADV': [],
			'N': [],
			'Ne': []
		}
	}

	for tag in tags['main']:
		if tag[1] in ('N', 'Ne', 'V', 'ADV'):
			data['main'][tag[1]].append(lemmatizer.lemmatize(tag[0]))

	for tag in tags['main']:
		if tag[1] in ('N', 'Ne', 'V', 'ADV'):
			data['normalized'][tag[1]].append(lemmatizer.lemmatize(tag[0]))
			
	return data

def allNLP(txt):
	return {
		'normalized': normilizeText(txt),
		'sentTokenize': sentTokenizeText(txt),
		'wordTokenize': wordTokenizeText(txt),
		'postTags': postTagText(txt),
		'chunksGroup': getChunksGroup(txt),
		'stem': stemText(txt),
		'lemmatized': lemmatizeText(txt),
	}

functionName = sys.argv[1]
text = json.loads(sys.argv[2])

callCommand = functionName + '("' + text + '")'
result = eval(callCommand)

print json.dumps(result)