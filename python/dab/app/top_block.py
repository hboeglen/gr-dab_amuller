#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Top Block
# GNU Radio version: 3.10.4.0

from packaging.version import Version as StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import blocks
from gnuradio import dab
from gnuradio import digital
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio.qtgui import Range, GrRangeWidget
from PyQt5 import QtCore
import gnuradio.dab.app.adjust_gui_helpers



from gnuradio import qtgui

class top_block(gr.top_block, Qt.QWidget):

    def __init__(self, frequency_id_default=18, from_file=None, from_file_repeat=False, gain_bb_default=10, gain_if_default=10, gain_rf_default=33, ppm_default=0, server="tcp://127.0.0.1:10444", server_control="tcp://127.0.0.1:10445", zeromq=False):
        gr.top_block.__init__(self, "Top Block", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "top_block")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Parameters
        ##################################################
        self.frequency_id_default = frequency_id_default
        self.from_file = from_file
        self.from_file_repeat = from_file_repeat
        self.gain_bb_default = gain_bb_default
        self.gain_if_default = gain_if_default
        self.gain_rf_default = gain_rf_default
        self.ppm_default = ppm_default
        self.server = server
        self.server_control = server_control
        self.zeromq = zeromq

        ##################################################
        # Variables
        ##################################################
        self.frequency_id = frequency_id = frequency_id_default
        self.variable_qtgui_push_button_0 = variable_qtgui_push_button_0 = 0
        self.samp_rate = samp_rate = 2048000
        self.ppm = ppm = ppm_default
        self.gain_slider = gain_slider = gain_rf_default
        self.gain_if = gain_if = gain_if_default
        self.gain_bb = gain_bb = gain_bb_default
        self.frequency = frequency = gnuradio.dab.app.adjust_gui_helpers.id_to_frequency(frequency_id)

        ##################################################
        # Blocks
        ##################################################
        self._ppm_range = Range(-1000, 1000, 1, ppm_default, 200)
        self._ppm_win = GrRangeWidget(self._ppm_range, self.set_ppm, "'ppm'", "counter_slider", float, QtCore.Qt.Horizontal, "value")

        self.top_grid_layout.addWidget(self._ppm_win, 0, 0, 1, 1)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._gain_slider_range = Range(0, 100, 1, gain_rf_default, 200)
        self._gain_slider_win = GrRangeWidget(self._gain_slider_range, self.set_gain_slider, "Gain RF", "counter_slider", float, QtCore.Qt.Horizontal, "value")

        self.top_grid_layout.addWidget(self._gain_slider_win, 1, 0, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._gain_if_range = Range(0, 100, 1, gain_if_default, 200)
        self._gain_if_win = GrRangeWidget(self._gain_if_range, self.set_gain_if, "Gain IF", "counter_slider", float, QtCore.Qt.Horizontal, "value")

        self.top_grid_layout.addWidget(self._gain_if_win, 2, 0, 1, 1)
        for r in range(2, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._gain_bb_range = Range(0, 100, 1, gain_bb_default, 200)
        self._gain_bb_win = GrRangeWidget(self._gain_bb_range, self.set_gain_bb, "Gain BB", "counter_slider", float, QtCore.Qt.Horizontal, "value")

        self.top_grid_layout.addWidget(self._gain_bb_win, 3, 0, 1, 1)
        for r in range(3, 4):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        _variable_qtgui_push_button_0_push_button = Qt.QPushButton('Save adjustments to configuration file')
        _variable_qtgui_push_button_0_push_button = Qt.QPushButton('Save adjustments to configuration file')
        self._variable_qtgui_push_button_0_choices = {'Pressed': 1, 'Released': 0}
        _variable_qtgui_push_button_0_push_button.pressed.connect(lambda: self.set_variable_qtgui_push_button_0(self._variable_qtgui_push_button_0_choices['Pressed']))
        _variable_qtgui_push_button_0_push_button.released.connect(lambda: self.set_variable_qtgui_push_button_0(self._variable_qtgui_push_button_0_choices['Released']))
        self.top_grid_layout.addWidget(_variable_qtgui_push_button_0_push_button, 6, 0, 1, 1)
        for r in range(6, 7):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            frequency, #fc
            samp_rate, #bw
            "", #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis((-140), 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)
        self.qtgui_freq_sink_x_0.set_fft_window_normalized(False)



        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.qwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_freq_sink_x_0_win, 0, 1, 5, 1)
        for r in range(0, 5):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.qtgui_const_sink_x_1 = qtgui.const_sink_c(
            1024, #size
            "", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_const_sink_x_1.set_update_time(0.10)
        self.qtgui_const_sink_x_1.set_y_axis((-2), 2)
        self.qtgui_const_sink_x_1.set_x_axis((-2), 2)
        self.qtgui_const_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_1.enable_autoscale(False)
        self.qtgui_const_sink_x_1.enable_grid(False)
        self.qtgui_const_sink_x_1.enable_axis_labels(True)


        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
            "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_1.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_1.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_1.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_1_win = sip.wrapinstance(self.qtgui_const_sink_x_1.qwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_const_sink_x_1_win, 5, 1, 5, 1)
        for r in range(5, 10):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(1, 2):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._frequency_id_range = Range(0, (gnuradio.dab.app.adjust_gui_helpers.get_number_of_channels()-1), 1, frequency_id_default, 200)
        self._frequency_id_win = GrRangeWidget(self._frequency_id_range, self.set_frequency_id, "Frequency", "counter_slider", int, QtCore.Qt.Horizontal, "value")

        self.top_grid_layout.addWidget(self._frequency_id_win, 4, 0, 1, 1)
        for r in range(4, 5):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.digital_mpsk_snr_est_cc_0 = digital.mpsk_snr_est_cc(0, 10000, 0.001)
        self.dab_osmo_or_zmq_source_0 = dab.osmo_or_zmq_source(frequency, gain_slider, gain_if, gain_bb, zeromq, server, server_control, samp_rate=samp_rate, from_file=from_file, from_file_repeat=from_file_repeat)
        self.dab_ofdm_demod_0 = dab.ofdm_demod(
                  dab.parameters.dab_parameters(
                    mode=1,
                    sample_rate=samp_rate,
                    verbose=False
                  ),
                  dab.parameters.receiver_parameters(
                    mode=1,
                    softbits=True,
                    input_fft_filter=True,
                    autocorrect_sample_rate=False,
                    sample_rate_correction_factor=1+float(ppm)*1e-6,
                    always_include_resample=True,
                    verbose=False,
                    correct_ffe=True,
                    equalize_magnitude=True
                  )
                )

        self.blocks_vector_to_stream_0 = blocks.vector_to_stream(gr.sizeof_gr_complex*1, 1536)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_vector_to_stream_0, 0), (self.digital_mpsk_snr_est_cc_0, 0))
        self.connect((self.dab_ofdm_demod_0, 0), (self.blocks_vector_to_stream_0, 0))
        self.connect((self.dab_osmo_or_zmq_source_0, 0), (self.dab_ofdm_demod_0, 0))
        self.connect((self.dab_osmo_or_zmq_source_0, 0), (self.qtgui_freq_sink_x_0, 0))
        self.connect((self.digital_mpsk_snr_est_cc_0, 0), (self.qtgui_const_sink_x_1, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_frequency_id_default(self):
        return self.frequency_id_default

    def set_frequency_id_default(self, frequency_id_default):
        self.frequency_id_default = frequency_id_default
        self.set_frequency_id(self.frequency_id_default)

    def get_from_file(self):
        return self.from_file

    def set_from_file(self, from_file):
        self.from_file = from_file

    def get_from_file_repeat(self):
        return self.from_file_repeat

    def set_from_file_repeat(self, from_file_repeat):
        self.from_file_repeat = from_file_repeat

    def get_gain_bb_default(self):
        return self.gain_bb_default

    def set_gain_bb_default(self, gain_bb_default):
        self.gain_bb_default = gain_bb_default
        self.set_gain_bb(self.gain_bb_default)

    def get_gain_if_default(self):
        return self.gain_if_default

    def set_gain_if_default(self, gain_if_default):
        self.gain_if_default = gain_if_default
        self.set_gain_if(self.gain_if_default)

    def get_gain_rf_default(self):
        return self.gain_rf_default

    def set_gain_rf_default(self, gain_rf_default):
        self.gain_rf_default = gain_rf_default
        self.set_gain_slider(self.gain_rf_default)

    def get_ppm_default(self):
        return self.ppm_default

    def set_ppm_default(self, ppm_default):
        self.ppm_default = ppm_default
        self.set_ppm(self.ppm_default)

    def get_server(self):
        return self.server

    def set_server(self, server):
        self.server = server

    def get_server_control(self):
        return self.server_control

    def set_server_control(self, server_control):
        self.server_control = server_control

    def get_zeromq(self):
        return self.zeromq

    def set_zeromq(self, zeromq):
        self.zeromq = zeromq

    def get_frequency_id(self):
        return self.frequency_id

    def set_frequency_id(self, frequency_id):
        self.frequency_id = frequency_id
        self.set_frequency(gnuradio.dab.app.adjust_gui_helpers.id_to_frequency(self.frequency_id))

    def get_variable_qtgui_push_button_0(self):
        return self.variable_qtgui_push_button_0

    def set_variable_qtgui_push_button_0(self, variable_qtgui_push_button_0):
        self.variable_qtgui_push_button_0 = variable_qtgui_push_button_0

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_freq_sink_x_0.set_frequency_range(self.frequency, self.samp_rate)

    def get_ppm(self):
        return self.ppm

    def set_ppm(self, ppm):
        self.ppm = ppm
        self.dab_ofdm_demod_0.resample.set_resamp_ratio(1+float(self.ppm)*1e-6)

    def get_gain_slider(self):
        return self.gain_slider

    def set_gain_slider(self, gain_slider):
        self.gain_slider = gain_slider
        self.dab_osmo_or_zmq_source_0.set_rf_gain(self.gain_slider)

    def get_gain_if(self):
        return self.gain_if

    def set_gain_if(self, gain_if):
        self.gain_if = gain_if
        self.dab_osmo_or_zmq_source_0.set_if_gain(self.gain_if)

    def get_gain_bb(self):
        return self.gain_bb

    def set_gain_bb(self, gain_bb):
        self.gain_bb = gain_bb
        self.dab_osmo_or_zmq_source_0.set_bb_gain(self.gain_bb)

    def get_frequency(self):
        return self.frequency

    def set_frequency(self, frequency):
        self.frequency = frequency
        self.dab_osmo_or_zmq_source_0.set_frequency(self.frequency)
        self.qtgui_freq_sink_x_0.set_frequency_range(self.frequency, self.samp_rate)



def argument_parser():
    parser = ArgumentParser()
    return parser


def main(top_block_cls=top_block, options=None):
    if options is None:
        options = argument_parser().parse_args()

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
