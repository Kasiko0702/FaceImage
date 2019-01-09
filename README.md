# FaceImage
Development based on Raspberry Pi with OpenCV by Python
此專案是利用PiCamera 抓去影像.並用OpenCV擷取出人臉的影像. 送至Line ChatBot. 但由於Line API所傳送的影像只能位於網路上. 故使用Paspberry Pi 自己搭建Http Server (故用 Python -m http.server). 並用ngrok 將http server 轉址到Line 可以存取的網址
