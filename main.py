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
            file_name = yt.title.replace('|', '') + '.mp4'
            downloaded_file = os.path.join(self.download_path, file_name)

            if os.path.exists(downloaded_file):
                skipped = True
                skipped_file = downloaded_file
            else:
                self.status_label.setText(f'Downloading {yt.title}...')
                video.download(output_path=self.download_path)
                self.status_label.setText(f'Your video download is complete for {yt.title}')

            # setting for loop to set value of progress bar
            # for i in range(101):
            # slowing down the loop
            # time.sleep(0.04)
            # setting value to progress bar
            # self.progressBar.setValue(i)

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
                    # s\lowing down the loop
                    #time.sleep(0.04)
                    # setting value to progress bar
                    #self.progressBar.setValue(i)

        if skipped:
            self.status_label.setText(f"Some audio downloads were skipped because the files already existed. \n File skipped: {skipped_file}")
        else:
            self.status_label.setText("All audio downloads are complete")
    def addIt(self):
        #Gets the url from the text
        url = self.url_text.toPlainText()
        
        #setting the pattern to understand a valid url
        url_pattern = re.compile(r'http(s)?://[a-zA-Z0-9./]+')

        if url:
            if not url_pattern.match(url):
                self.status_label.setText("Invalid URL, please ensure you're copying the https://www.youtube.com/ link")
                return
            self.url_list.addItem(url)
            self.download_list.append(url)

            self.url_text.setPlainText("")
        else:
            self.status_label.setText("Please enter text")

if __name__=="__main__":
    app = QApplication(sys.argv)
    ui =  MainUI()
    ui.show()
    app.exec_()