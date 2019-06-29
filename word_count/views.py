from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
	return render(request, 'home.html')

def count(request):
	full_text = request.GET['full_text']
	word_list = full_text.split()

	word_dict = {}
	for word in word_list:
		if word in word_dict:
			#Incremante
			word_dict[word] += 1
		else:
			#add the word
			word_dict[word] = 1

	sorted_words = sorted(word_dict.items(), key=operator.itemgetter(1), reverse=True)

	return render(request, 'count.html',{'full_text':full_text, 'count':len(word_list), 'sorted_words':sorted_words})

def about(request):
	return render(request, 'about.html')