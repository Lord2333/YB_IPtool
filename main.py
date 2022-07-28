from PyQt5 import QtWidgets
from PyQt5.Qt import QThread, QMutex, pyqtSignal
from PyQt5.QtWidgets import QDialog, QMessageBox, QInputDialog

import Function
import sys
import time
from home_page import Ui_MainWindow
from update import Ui_Dialog

Ver = 0.2
global App_id, Count, run_times

ThreadLock = QMutex()


class Thread_1(QThread):  # 线程1
	update_data = pyqtSignal(int, int)

	def __init__(self):
		super().__init__()

	def run(self):
		global App_id, Count, run_times
		run_times = int(int(run_times)/5+1)
		while run_times:
			run_times -= 1
			IPS = Function.Deal_IP()
			for ip in IPS:
				if Function.Run(App_id, ip):
					Count += 1
					self.update_data.emit(Count, run_times)
					time.sleep(0.2)


class MyUpdateWindow(QDialog, Ui_Dialog):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.Comfirm.clicked.connect(self.confirm_button_click)
		self.Ignore.clicked.connect(self.Ignore_button_click)

	def confirm_button_click(self):
		i = QMessageBox.information(self, "Tips", "已复制下载地址到剪切板，请打开浏览器下载！", QMessageBox.Yes, QMessageBox.Yes)
		return 1

	def Ignore_button_click(self):
		return 2


class MyGraphWindow(QtWidgets.QMainWindow, Ui_MainWindow):
	def __init__(self):
		super(MyGraphWindow, self).__init__()
		self.thread_1 = Thread_1()  # 创建线程
		self.setupUi(self)
		self.Check.clicked.connect(self.Check_IP)
		self.Submit.clicked.connect(self.Run)
		self.thread_1.update_data.connect(self.UP_data)

	def Check_IP(self):
		flag, data = Function.check_zm()
		if flag:
			self.Submit.setEnabled(True)
			self.textBrowser.setText('成功连接到芝麻代理！')
		else:
			self.textBrowser.setText(data + '\n芝麻代理官网：https://www.zmhttp.com/')

	def UP_data(self, cnt, run_time):
		self.textBrowser.setText('当前已请求数：' + str(cnt))
		if run_time == 0:
			self.Submit.setEnabled(True)
			self.textBrowser.setText('当前已请求数：' + str(cnt)+'\n已完成任务！')

	def Run(self):
		global App_id, Count, run_times
		Count = 0
		App_id = self.lineEdit.text()
		run_times, ok = QInputDialog.getText(self, '请输入请求次数！', '请求次数：')
		if ok and App_id != '':
			self.Check.setEnabled(False)
			self.Submit.setEnabled(False)
			self.textBrowser.setText(
				'请求地址：https://q.yiban.cn/app/index/appid/' + App_id + '\n请求数：' + run_times + '   任务即将启动...')
			time.sleep(2)
			self.thread_1.start()  # 开始线程
		else:
			self.textBrowser.setText('请设置请求数或轻应用ID！')


if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	MyUpdate = MyUpdateWindow()
	MyMain = MyGraphWindow()
	Info = Function.Check_update(Ver)
	if Info:
		MyUpdate.show()
		MyUpdate.Check_info.setText(Info)
		if MyUpdate.exec_() == 1:
			clipboard = app.clipboard()
			clipboard.setText('https://ur.daj8.ml/IP_Update')
		else:
			MyMain.show()
	else:
		MyMain.show()
	sys.exit(app.exec_())
