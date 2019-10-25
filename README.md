# Aganitha.ai
I have uploaded three notebooks in the github

One notebook usues google API to convert speech to text(speech_recognition_Task)

The other  notebook is to make module in python(mymodule)

Third notebook is how to convert speech to text with feature extraction and building the model.(Speech_Recognition_Assingment)

The data has been taken from Kaggle for the third Notebook.



What is an Analog Signal?

An audio signal is a continuous representation of amplitude as it varies with time. The time can even be in picoseconds. 

Hence  an audio signal is an analog signal.
Analog signals are memory hogging since they have an infinite number of samples and processing them is highly computationally demanding.

Therefore, we need a technique to convert analog signals to digital signals so that we can work with them easily.

#  The features that have been extracted here are following:-
1.Time-domain:- The audio signal is represented by the amplitude as a function of time. It is a plot between amplitude and time. The features are the amplitudes which are recorded at different time intervals

2.Frequency domain:-In the frequency domain, the audio signal is represented by amplitude as a function of frequency. Simply put – it is a plot between frequency and amplitude. The features are the amplitudes recorded at different frequencies.


# Some more features that can be extracted:-

1.Silence Removal:-
For feature extraction we can use  VAD(Voice Activity Detection).Sometimes there is lot of silence in them .A decent VAD can reduce training size a lot, accelerating training speed significantly.

2.Resampling (Dimensionality reduction):-Another way to reduce the dimensionality of our data is to resample recordings.

3. We use  padding with 0 to make signals be equal length

4.Log spectrogram (or MFCC, or PLP)

5.Features normalization with mean and std

6.Stacking of a given number of frames to get temporal information


