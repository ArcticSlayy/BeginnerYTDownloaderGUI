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
        self.remove_button.clicked.connect(self.removeIt)

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
            #had to remove pipes and odd characters
            file_name = yt.title.replace('|', '') + '.mp4'
            downloaded_file = os.path.join(self.download_path, file_name)

            if os.path.exists(downloaded_file):
                skipped = True
                skipped_file = downloaded_file
            else:
                self.status_label.setText(f'Downloading {yt.title}...')
                video.download(output_path=self.download_path)
                self.status_label.setText(f'Your video download is complete for {yt.title}')

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

            audio = yt.streams.yt.streams.filter(type="audio").first()
            #had to remove pipes and odd characters
            file_name = yt.title.replace('|', '') + '.mp4'
            downloaded_file = os.path.join(self.download_path, file_name)

            if os.path.exists(downloaded_file):
                skipped = True
                skipped_file = downloaded_file
            else:
                self.status_label.setText(f'Downloading {yt.title}...')
                audio.download(output_path=self.download_path)
                self.status_label.setText(f'Your audio download is complete for {yt.title}')

        if skipped:
            self.status_label.setText(f"Some audio downloads were skipped because the files already existed. \n File skipped: {skipped_file}")
        else:
            self.status_label.setText("All audio downloads are complete")

    def addIt(self):
        #Gets the url from the text
        url = self.url_text.toPlainText()
        if url:
            if "youtube.com" not in url:
                self.status_label.setText("Invalid URL, please ensure you're copying the https://www.youtube.com/ link")
                return
            self.url_list.addItem(url)
            self.download_list.append(url)

            self.url_text.setPlainText("")
        else:
            self.status_label.setText("Text is blank, please enter your URL into the top bar.")
    def removeIt(self):
            item_tbd = self.url_list.currentRow()
            self.url_list.takeItem(item_tbd)
            #Was just debugging to see if the index was right
            deleting_item = self.download_list[item_tbd]
            self.status_label.setText(f"Successfully removed {str(self.download_list[item_tbd])} from your URL list.")


if __name__=="__main__":
    app = QApplication(sys.argv)
    ui =  MainUI()
    ui.show()
    app.exec_()