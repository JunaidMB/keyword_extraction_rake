import yake
from yake.highlight import TextHighlighter

# Load in final sermon as text
text = "O People, lend me an attentive ear, for I know not whether after this year, I shall ever be amongst you again. Therefore listen to what I am saying to you very carefully and take these words to those who could not be present here today.\
O people, just as you regard this month, this day, this city as Sacred, so regard the life and property of every Muslim as a sacred trust. Return the goods entrusted to you to their rightful owners. Hurt no one so that no one may hurt you. Remember that you will indeed meet your Lord, and that He will indeed reckon your deeds. Allah has forbidden you to take usury (interest), therefore all interest obligation shall henceforth be waived. Your capital, however, is yours to keep. You will neither inflict nor suffer any inequity. Allah has Judged that there shall be no interest and that all the interest due to Abbas ibn Abd Al-Muttalib (Prophet’s uncle) shall henceforth be waived…\
Beware of Satan, for the safety of your religion. He has lost all hope that he will ever be able to lead you astray in big things, so beware of following him in small things.\
O people, it is true that you have certain rights with regard to your women, but they also have rights over you. Remember that you have taken them as your wives only under Allah’s trust and with His permission. If they abide by your right then to them belongs the right to be fed and clothed in kindness. Do treat your women well and be kind to them for they are your partners and committed helpers. And it is your right that they do not make friends with any one of whom you do not approve, as well as never to be unchaste.\
O people, listen to me in earnest, worship Allah, say your five daily prayers (Salah), fast during the month of Ramadan, and give your wealth in Zakat. Perform Hajj if you can afford to.\
All mankind is from Adam and Eve, an Arab has no superiority over a non-Arab nor a non-Arab has any superiority over an Arab; also a white has no superiority over black nor a black has any superiority over white except bypiety (taqwa) and good action. Learn that every Muslim is a brother to every Muslim and that the Muslims constitute one brotherhood. Nothing shall be legitimate to a Muslim which belongs to a fellow Muslim unless it was given freely and willingly. Do not, therefore, do injustice to yourselves.\
Remember, one day you will appear before Allah and answer your deeds. So beware, do not stray from the path of righteousness after I am gone.\
O people, no prophet or apostle will come after me and no new faith will be born.\
Reason well, therefore, O people, and understand words which I convey to you. I leave behind me two things, the Qu'ran and my example, the Sunnah and if you follow these you will never go astray.\
All those who listen to me shall pass on my words to others and those to others again; and may the last ones understand my words better than those who listen to me directly. Be my witness, O Allah, that I have conveyed your message to your people."

print(text)

# Default keywords extractor
kw_extractor = yake.KeywordExtractor()
keywords = kw_extractor.extract_keywords(text)

## The lower score the better
for kw in keywords:
    print(kw)

# Specific parameters
## Load stopwords as a list
gist_file = open("gist_stopwords.txt", "r")
try:
    content = gist_file.read()
    stopwords = content.split(",")
    stopwords=[i.replace('"',"").strip() for i in stopwords]
finally:
    gist_file.close()

# Specify parameters
language = "en"
max_ngram_size = 2
deduplication_thresold = 0.9
deduplication_algo = 'seqm'
windowSize = 1
numOfKeywords = 20

# Apply keyword extractor with specific parameters
custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_thresold, dedupFunc=deduplication_algo, windowsSize=windowSize, top=numOfKeywords, features=None, stopwords=stopwords)
keywords = custom_kw_extractor.extract_keywords(text)

for kw in keywords:
    print(kw)

# Highlight keywords within text
th = TextHighlighter(max_ngram_size = 3, highlight_pre = "<strong style='color:red'>", highlight_post= "</strong>")
highlighted_text = th.highlight(text, keywords)

# Write to HTML file
file = open("text.html","w")
file.write(highlighted_text)
file.close()



