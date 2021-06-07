
#Author: Seongmin Bak
#Date: 04-22-2021

import sys, os, signal, subprocess
import numpy as np
import time


from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QThread, QSettings
from PyQt5.QtWidgets import QMessageBox, QFileDialog


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('tes_main.ui', self)
        #self.initParams()
        # stage positioning control
        self.Btn_left.clicked.connect(self.stage_left)
        self.Btn_right.clicked.connect(self.stage_right)
        self.Btn_up.clicked.connect(self.stage_up)
        self.Btn_down.clicked.connect(self.stage_down)
        self.Btn_zoomin.clicked.connect(self.zoom_in)
        self.Btn_zoomout.clicked.connect(self.zoom_out)
        self.Btn_YAG.clicked.connect(self.YAG)
        self.Btn_FL.clicked.connect(self.FL)

        # data acquisition control
        self.Btn_StartScan_single_Efly.clicked.connect(self.start_Efly)
        self.show()


  
     # Make plots update live while scans run.
    # from bluesky.utils import install_kicker
     #install_kicker()
     #import matplotlib
     #matplotlib.use('Qt5Agg')
     #import matplotlib.pyplot as plt


    def stage_up(self):
        #PV name: XF:08BMES-OP{SM:1-Ax:X}Mtr.TWv
        y_step = self.spinBox_y_step.value()
        self.RE(bps.mvr(self.sample_stage.y, y_step))
        self.show_image()

    def stage_down(self):
        y_step = self.spinBox_y_step.value()
        self.RE(bps.mvr(self.sample_stage.y, -y_step))
        self.show_image()

    def stage_right(self):
        x_step = self.spinBox_x_step.value()
        self.RE(bps.mvr(self.sample_stage.x, x_step))
        self.show_image()

    def stage_left(self):
        x_step = self.spinBox_x_step.value()
        self.RE(bps.mvr(self.sample_stage.x, -x_step))
        self.show_image()

    def zoom_in(self):
        z_step = self.spinBox_z_step.value()
        self.RE(bps.mvr(self.sample_stage.z, z_step))
        self.show_image()

    def zoom_out(self):
        z_step = self.spinBox_z_step.value()
        self.RE(bps.mvr(self.sample_stage.z, -z_step))
        self.show_image()

    def YAG(self):
        self.RE(bps.mv(x,y,z))
        self.show_image()
    def FL(self):
        self.RE(bps.mv(x,y,z))
        self.show_image()


    def start_Efly(self):
        RE.E_fly ("copy the command for E_fly scan from profile")

    def abort_scan(self):
        signal.signal(signal.SIGINT, signal.SIG_DFL)
        RE.abort()

    def progressBar(self):
        value = np.round(self.progressValue)
        if not math.isnan(value):
            self.progressBar.setValue(int(value))

    #scan status update
    def update_re_state(self):
        palette = self.label_RE_state.palette()
        if (self.RE.state == 'idle'):
            palette.setColor(self.label_RE_state.foregroundRole(), QtGui.QColor(193, 140, 15))
        elif (self.RE.state == 'running'):
            palette.setColor(self.label_RE_state.foregroundRole(), QtGui.QColor(0, 165, 0))
        elif (self.RE.state == 'paused'):
            palette.setColor(self.label_RE_state.foregroundRole(), QtGui.QColor(255, 0, 0))
        elif (self.RE.state == 'abort'):
            palette.setColor(self.label_RE_state.foregroundRole(), QtGui.QColor(255, 0, 0))
        self.label_RE_state.setPalette(palette)
        self.label_RE_state.setText(self.RE.state)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ui()
    window.show()
    sys.exit(app.exec_())