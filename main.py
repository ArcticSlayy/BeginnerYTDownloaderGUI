from pytube import YouTube
from pytube.cli import on_progress
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
import time
import os
import sys

class MainUI(QMainWindow):
    def __init__(self):
        super(MainUI, self).__init__()
        loadUi("tutorial.ui",self)

        self.video_button.clicked.connect(self.doActionVideo)
        self.audio_button.clicked.connect(self.doActionAudio)
    

    def doActionVideo(self):
        #Change where you want the download path here, you can make it a direct url just by entering the 
        #desired output path as a string. E.g 'USERNAME\Desktop\YoutubeDownloader'
        Download_Path = os.environ['USERPROFILE']+"\\Desktop"

        try:
            url = str(self.url_text.toPlainText())
        except Exception as ex:
            print(f"Error due to {ex}")

        yt = YouTube(url, on_progress_callback=on_progress)

        self.status_label.setText(f'Your YouTube video\'s title is: {yt.title}')

        time.sleep(0.2)

        # setting for loop to set value of progress bar
        for i in range(101):
  
            # slowing down the loop
            time.sleep(0.04)
  
            # setting value to progress bar
            self.progressBar.setValue(i)
        
        self.status_label.setText("Your video download is complete")

        video = yt.streams.get_highest_resolution()
        video.download(output_path=Download_Path)

    def doActionAudio(self):
        Download_Path = os.environ['USERPROFILE']+"\\Desktop"

        try:
            url = str(self.url_text.toPlainText())
        except Exception as ex:
            print(f"Error due to {ex}")

        yt = YouTube(url, on_progress_callback=on_progress)


        self.status_label.setText(f'Your YouTube video\'s title is: {yt.title}')
        # setting for loop to set value of progress bar
        for i in range(101):
  
            # slowing down the loop
            time.sleep(0.04)
  
            # setting value to progress bar
            self.progressBar.setValue(i)

        self.status_label.setText("Your audio download is complete")
        audio = yt.streams.filter(type="audio").first()
        audio.download(output_path=Download_Path)

    #just for testing
    #def clicked(self):
    #    print("You pressed a button")

    

if __name__=="__main__":
    app = QApplication(sys.argv)
    ui =  MainUI()
    ui.show()
    app.exec_()
