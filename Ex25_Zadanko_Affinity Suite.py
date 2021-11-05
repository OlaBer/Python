indicators = {'Pure Tone Bracketing': {'result':'FailedResult', 'description':'Pure Tone Bracketing Insert right 1000 Hz: Insufficient number of presentations', 'comment':''},
              'Transducer used': {'result':'AcceptedResult', 'description':'Transducers used according to standard', 'comment':''},
              'Frequencies Required': {'result':'FailedResult', 'description':'The following mandatory frequencies are not tested: For Phone/Insert Right HL: 125Hz 250Hz 500Hz 750Hz 1500Hz 2000Hz 3000Hz 4000Hz 6000Hz 8000Hz 9000Hz 10000Hz 11200Hz 12500Hz 14000Hz 16000Hz 18000Hz 20000Hz For Phone/Insert Left HL: 125Hz 250Hz 500Hz 750Hz 1000Hz 1500Hz 2000Hz 3000Hz 4000Hz 6000Hz 8000Hz 9000Hz 10000Hz 11200Hz 12500Hz 14000Hz 16000Hz 18000Hz 20000Hz For Bone Right HL: 250Hz 500Hz 750Hz 1000Hz 1500Hz 2000Hz 3000Hz 4000Hz 6000Hz 8000Hz For Bone Left HL: 250Hz 500Hz 750Hz 1000Hz 1500Hz 2000Hz 3000Hz 4000Hz 6000Hz 8000Hz For Free Field 1 HL: 125Hz 250Hz 500Hz 750Hz 1000Hz 1500Hz 2000Hz 3000Hz 4000Hz 6000Hz 8000Hz For Free Field 2 HL: 125Hz 250Hz 500Hz 750Hz 1000Hz 1500Hz 2000Hz 3000Hz 4000Hz 6000Hz 8000Hz For Air Conduction Right UCL: 125Hz 250Hz 500Hz 750Hz 1000Hz 1500Hz 2000Hz 3000Hz 4000Hz 6000Hz 8000Hz 9000Hz 10000Hz 11200Hz 12500Hz 14000Hz 16000Hz 18000Hz 20000Hz For Air Conduction Left UCL: 125Hz 250Hz 500Hz 750Hz 1000Hz 1500Hz 2000Hz 3000Hz 4000Hz 6000Hz 8000Hz 9000Hz 10000Hz 11200Hz 12500Hz 14000Hz 16000Hz 18000Hz 20000Hz ', 'comment':''},
              'Interoctave frequencies': {'result':'AcceptedResult', 'description':'Neccessary Interoctave frequencies are tested', 'comment':''},
              'Bone needed on second ear': {'result':'NeedsAttentionResult', 'description':'Bone needed on second ear: No Bone data', 'comment':''},
              'Speech Input Indicator': {'result':'InsufficientDataResult', 'description':'Speech Input, no thresholds stored yet', 'comment':''},
              'PTA SRT Agreement': {'result':'InsufficientDataResult', 'description':'Right ear: PTA missing, Left ear: PTA missing', 'comment':''},
              'Excessive use of DNT, CNT and NR - Tone': {'result':'AcceptedResult', 'description':'Excessive use of DNT, CNT and NR - Tone', 'comment':''},
              'Excessive use of DNT, CNT and NR - Speech': {'result':'InsufficientDataResult', 'description':'Excessive use of DNT, CNT and NR - Speech', 'comment':''},
              'Effective Masking Air Conduction': {'result':'InsufficientDataResult', 'description':'No masking has been performed for Air Conduction', 'comment':''},
              'Effective Masking Bone Conduction': {'result':'InsufficientDataResult', 'description':'No masking has been performed for Bone Conduction', 'comment':''},
              'Effective Masking Speech': {'result':'InsufficientDataResult', 'description':'No masking has been performed for Speech test', 'comment':''},
              'Test required': {'result':'FailedResult', 'description':'The following tests are missing: Speech test, Weber test, SISI test, QuickSIN test, Tone Decay test, ANL test, SIN test, SIQ test', 'comment':''}
              }
def get_qa_result(dct):

    dct = {}
    
    for keys in indicators:
        pass
        print(keys)
        for values in indicators[keys]:
            pass
        print(values, ":", indicators[keys][values])
    return indicators

#print(get_qa_result(indicators))
get_qa_result(dct)

#if 'FailedResult' or 'NeedsAttentionResult' in indicators:
 #   print(...)
