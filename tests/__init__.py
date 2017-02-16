import sys
import threading

from pyblish_qml import ipc

from PyQt5 import QtCore

self = sys.modules[__name__]

self.app = (
    QtCore.QCoreApplication.instance() or
    QtCore.QCoreApplication(sys.argv)
)

self.port = 50998
self.service = ipc.service.Service()
self.server = ipc.server._server(self.port, self.service)
self.thread = threading.Thread(target=self.server.serve_forever)
self.thread.daemon = True
self.thread.start()
