<<<<<<< HEAD
from pytube import YouTube
from pytube.cli import on_progress
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
import time
import os
import sys
import re

class MainUI(QMainWindow):
    def __init__(self):
        super(MainUI, self).__init__()
        loadUi("tutorial.ui",self)

        self.video_button.clicked.connect(self.doActionVideo)
        self.audio_button.clicked.connect(self.doActionAudio)
        self.add_button.clicked.connect(self.addIt)
        self.download_path = os.environ['USERPROFILE']+"\\Desktop"
        self.download_list = []

    def progress_func(self, stream, chunk, bytes_remaining):
        size = stream.filesize
        progress = (float(abs(bytes_remaining-size)/size))*float(100)
        self.progressBar.setValue(int(progress))



    def doActionVideo(self):
        if not self.download_list:
            self.status_label.setText("Please add a video URL to download")
            return

        skipped = False
        for url in self.download_list:
            yt = YouTube(url, on_progress_callback=self.progress_func)
            self.status_label.setText(f'Your YouTube video\'s title is: {yt.title} \n')

            video = yt.streams.get_highest_resolution()
            downloaded_file = os.path.join(self.download_path, yt.title) + '.mp4'

            if os.path.exists(downloaded_file):
                self.status_label.setText(f'Your file already exists at {downloaded_file}')
                skipped_file = downloaded_file
                skipped = True
            else:
                self.status_label.setText(f'Downloading {yt.title}...')
                video.download(output_path=self.download_path)
                self.status_label.setText(f'Your video download is complete for {yt.title}')

                # setting for loop to set value of progress bar
                #for i in range(101):
                    # slowing down the loop
                    #time.sleep(0.04)
                    # setting value to progress bar
                    #self.progressBar.setValue(i)

        if skipped:
            self.status_label.setText(f"Some video downloads were skipped because the files already existed. \n File skipped: {skipped_file}")
        else:
            self.status_label.setText("All video downloads are complete")

    def doActionAudio(self):
        if not self.download_list:
            self.status_label.setText("Please add a video URL to download")
            return

        skipped = False
        for url in self.download_list:
            yt = YouTube(url, on_progress_callback=self.progress_func)
            self.status_label.setText(f'Your YouTube video\'s title is: {yt.title} \n')

            audio = yt.streams.filter(type="audio").first()
            downloaded_file = os.path.join(self.download_path, yt.title) + '.mp4'

            if os.path.exists(downloaded_file):
                self.status_label.setText(f'Your file already exists at {downloaded_file}')
                skipped_file = downloaded_file
                skipped = True
            else:
                self.status_label.setText(f'Downloading {yt.title}...')
                audio.download(output_path=self.download_path)
                self.status_label.setText(f'Your video download is complete for {yt.title}')

                # setting for loop to set value of progress bar
                #for i in range(101):
                    # slowing down the loop
                    #time.sleep(0.04)
                    # setting value to progress bar
                    #self.progressBar.setValue(i)

        if skipped:
            self.status_label.setText(f"Some audio downloads were skipped because the files already existed. \n File skipped: {skipped_file}")
        else:
            self.status_label.setText("All audio downloads are complete")
        

if __name__=="__main__":
    app = QApplication(sys.argv)
    ui =  MainUI()
    ui.show()
    app.exec_()
=======
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
>>>>>>> 08b5ab6f4456bd65e983a13fc0e43e9282f2db31
