from scipy.io import wavfile
import urllib.request
import numpy as np
import matplotlib.pyplot as plt
import wave
import matplotlib.pylab

# # 网络数据读取与保存
# with urllib.request.urlopen('http://www.nch.com.au/acm/11k16bitpcm.wav') as response:
#    data = response.read()
# print(type(response))
# with open('english.wav','wb') as wavf:
#     wavf.write(data)

# print(help(wavfile.read))

# # 从wav格式的文件中读取出相应的采样率、数据等信息
samplerate, data = wavfile.read("english.wav")
print('samplerate',samplerate)
print('data',data)

#绘制出原始音频文件的波形图。
plt.subplot(2,1,1)
plt.title('Original')
plt.plot(data)


wavefile1 = wave.open("english.wav",'r')
params = wavefile1.getparams()
print(params)

data_arr = np.array(data)
print(type(data_arr))
low = 0.2
low_data_arr=data_arr*low
low_data_arr=low_data_arr.astype(np.int16)
print(low_data_arr)

#绘制出新音频文件的波形图。
plt.subplot(2,1,2)
plt.title('Quiet')
plt.plot(low_data_arr)
plt.show()

# samplerate = 44100
wavfile.write("silent.wav",samplerate,low_data_arr)

result = matplotlib.pylab.specgram(low_data_arr, NFFT=1024, Fs = samplerate, noverlap=900)
#y:音频信号
#NFFT：每个进行快速傅里叶变换的数据块大小，一般取2的幂次
#Fs:采样率
#noverlap：数据块之间重叠数据点的个数

matplotlib.pylab.show()