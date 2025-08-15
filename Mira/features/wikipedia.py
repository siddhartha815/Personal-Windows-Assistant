import wikipedia
import sys, codecs

# Wikipedia problem solution
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())

def wikipedia_info(topic):
    # sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())
    try:
        wiki_result = wikipedia.summary(topic, sentences=3)

        return wiki_result
    except Exception as e:
        print(e)
        return False