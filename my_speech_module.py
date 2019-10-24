
# coding: utf-8

# In[2]:



def speech_recognition(audio):
    
    
    
    # use the audio file as the audio source
    
    try:
        text = r.recognize_google(audio)
        print("You said : {}".format(text))
    except:
         print("Sorry could not recognize what you said")
       
    

