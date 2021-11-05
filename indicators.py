class Indicator:
    title = None
    result = None
    description = None
    comment = None
    def __init__(self, title, result, description, comment):
        self.title = title
        self.result = result
        self.description = description
        self.comment = comment

    def __str__(self):
        return "Title: " + self.title + "\nResult: " + self.result + "\nDescription: " + self.description + "\nComment: " + self.comment + "\n\n"

titles = ["Pure Tone Bracketing", "Transducer used", "Frequencies Required", "Interoctave frequencies", "Bone needed on second ear"]
results = ["FailedResult", "AcceptedResult", "NeedsAttentionResult", "InsufficientDataResult", "AcceptedResult"]
descriptions = ["Pure Tone Bracketing\r\nPhone right 500 Hz: Insufficient number of presentations\r\nPhone right 1000 Hz: Insufficient number of presentations\r\nPhone right 2000 Hz: Insufficient number of presentations\r\nPhone right 3000 Hz: Insufficient number of presentations\r\nPhone right 6000 Hz: Insufficient number of presentations\r\nPhone right 8000 Hz: Insufficient number of presentations\r\n",
                "Transducers used according to standard",
                "The following mandatory frequencies are not tested:\r\n\r\nFor Phone/Insert Right HL: 125Hz 250Hz 750Hz 1500Hz 4000Hz 8000Hz 9000Hz 10000Hz 11200Hz 12500Hz 14000Hz 16000Hz 18000Hz 20000Hz \r\n\r\nFor Phone/Insert Left HL: 125Hz 250Hz 500Hz 750Hz 1000Hz 1500Hz 2000Hz 3000Hz 4000Hz 6000Hz 8000Hz 9000Hz 10000Hz 11200Hz 12500Hz 14000Hz 16000Hz 18000Hz 20000Hz \r\n\r\nFor Bone Right HL: 250Hz 500Hz 750Hz 1500Hz 4000Hz \r\n\r\nFor Bone Left HL: 250Hz 500Hz 750Hz 1000Hz 1500Hz 2000Hz 3000Hz 4000Hz 6000Hz 8000Hz \r\n\r\nFor Free Field 1 HL: 125Hz 250Hz 500Hz 750Hz 1000Hz 1500Hz 2000Hz 3000Hz 4000Hz 6000Hz 8000Hz \r\n\r\nFor Free Field 2 HL: 125Hz 250Hz 500Hz 750Hz 1000Hz 1500Hz 2000Hz 3000Hz 4000Hz 6000Hz 8000Hz \r\n\r\nFor Air Conduction Right UCL: 125Hz 250Hz 500Hz 750Hz 1000Hz 1500Hz 2000Hz 3000Hz 4000Hz 6000Hz 8000Hz 9000Hz 10000Hz 11200Hz 12500Hz 14000Hz 16000Hz 18000Hz 20000Hz \r\n\r\nFor Air Conduction Left UCL: 125Hz 250Hz 500Hz 750Hz 1000Hz 1500Hz 2000Hz 3000Hz 4000Hz 6000Hz 8000Hz 9000Hz 10000Hz 11200Hz 12500Hz 14000Hz 16000Hz 18000Hz 20000Hz",
                "Neccessary Interoctave frequencies are tested",
                "No AC thresholds for Inserts, Phones or Free Field at all, or AC thresholds are missing for one or more frequencies with BC thresholds"]
comments = ["Failed as expected", "Passed as expected", "Attention!", "Double check it", "Passed, it wass NOT expected"]
qa_panel = []
qa_panel_childs = 5 # czyste założenie, w TestComplete używa się różnych metod i atrybutów jak ChildCount czy wItemCount
for i in range(qa_panel_childs):
    qa_panel.append(Indicator(titles[i], results[i], descriptions[i], comments[i]))
   # print(qa_panel[i])


def get_qa_result(dct):
    qa_result = {}

    for keys in titles:
        qa_result[self.title[i]] = [self.qa_panel[i]]
        
        print(keys)
        for values in indicators[keys]:
            pass
        print(values, ":", indicators[keys][values])
    return qa_result
    

    # Kolejne kroki

print(get_qa_result(qa_result))

# Wywołanie funkcji
# Wypisać nazwę oraz opis wszystkich wskaźników, które zostały oznaczone jako 'FailedResult' bądź 'NeedsAttentionResult'
