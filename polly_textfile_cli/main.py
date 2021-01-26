from boto3 import client
import boto3
from io import FileIO
from contextlib import closing
import argparse, os

def fileChunkList(filePath, limit):
	with open(filePath, 'r') as file:
		data = file.read().replace('\n','')
	#lines = [data[i:i+limit] for i in range(0, len(data), limit)]
	lines_in = data.split(" ")
	lines = constructSentences(lines_in,limit)
	return lines

def constructSentences(words,limit):
	ss = []
	s = []
	for w in words:
		if len(w) + len(" ".join(s)) <= limit:
			s.append(w)
		else:
			sentence = " ".join(s)
			ss.append(sentence)
			s = []
			s.append(w)
	return ss

def streamAudio(inString):
	polly = client("polly", "us-east-2")
	response = polly.synthesize_speech(
		Text=inString,
		OutputFormat="mp3",
		VoiceId="Matthew")
	return response

def createChunkAudio(id, linesList):
	parts = len(linesList)
	partsIdList = []
	for i in range(1, parts):
		resp = streamAudio(linesList[i-1])
		stream = resp['AudioStream']._raw_stream
		with FileIO("%s-part-%s.mp3" % (id,i), 'w') as file:
			for i in stream:
				file.write(i)
			partsIdList.append(file.name)	
	return partsIdList

def concatPartsAudio(pathList, id):
	print(pathList)
	cmdStr = "concat:"
	for p in pathList:
#		concat = os.system("ffmpeg -i '%s.mp3' -acodec copy '%s'" % (id,p))
		if pathList[-1] == p:
			cmdStr = cmdStr + "%s" % (p)
		else:
			cmdStr = cmdStr + "%s|" % (p)
	print(cmdStr)
	#concat = os.system("ffmpeg %s -filter_complex amerge -ac 2 -c:a libmp3lame -q:a 4 '%s.mp3'" % (cmdStr, id) )
	concat = os.system("ffmpeg -i '%s' -acodec copy '%s.mp3'" % (cmdStr, id))
	s = os.system("stat %s.mp3" % (id))
	return s

#if __name__ == '__main__':
def main():
	parser = argparse.ArgumentParser(description='Process some integers.')
	parser.add_argument('-p', '--path', action="store", default=False)
	parser.add_argument('-n', '--name', action="store", default=False)
	args = parser.parse_args()
	path = args.path
	name = args.name
	f = fileChunkList(path, 250)
	c = createChunkAudio(name, f)
	a = concatPartsAudio(c, name)
	print(a)
	return a
