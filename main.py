# -*- coding:utf-8 -*-
# Author：余时锐
# Date: 2016-08-21
# Message：余时锐随机字符串v9.0

import random

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

# 导入正则
import re

# 导入ui文件
from Ui_main import Ui_MainWindow

# 图片
import image_rc

# 暗黑主题
import qdarkstyle



class Yu(QMainWindow, Ui_MainWindow):
    # 构造函数
    def __init__(self, parent=None):
        # 调用父类构造函数
        super(QMainWindow, self).__init__(parent)
        self.setupUi(self)

        # 经典暗黑主题
        qApp.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

        # 窗口置顶
        self.setWindowFlags(Qt.WindowStaysOnTopHint)

        # 图标
        self.setWindowIcon(QIcon(':/yu/yu.ico'))

        # 标题
        self.setWindowTitle('余时锐随机字符串v9.0')

        # 置顶复选框变化槽函数
        self.cb_zhiding.stateChanged.connect(self.zhiding)

        # 按钮槽函数
        self.pb_wanneng.clicked.connect(lambda: self.cao(self.pb_wanneng))
        self.pb_tongyong.clicked.connect(lambda: self.cao(self.pb_tongyong))
        self.pb_tesu.clicked.connect(lambda: self.cao(self.pb_tesu))
        self.pb_10.clicked.connect(lambda: self.cao(self.pb_10))
        self.pb_20.clicked.connect(lambda: self.cao(self.pb_20))
        self.pb_50.clicked.connect(lambda: self.cao(self.pb_50))
        self.pb_100.clicked.connect(lambda: self.cao(self.pb_100))

        # 计数器值变化槽函数
        self.spinBox.valueChanged.connect(self.spChanged)

        # 文本域变化槽函数
        self.textEdit.textChanged.connect(self.textEditChanged)

    # 置顶
    def zhiding(self):
        if not self.cb_zhiding.isChecked():
            self.setWindowFlags(Qt.Widget)
            yu_pos = self.pos()
            self.move(yu_pos)
            self.show()
        else:
            self.setWindowFlags(Qt.WindowStaysOnTopHint)
            yu_pos = self.pos()
            self.move(yu_pos)
            self.show()

    # 判断字符
    def panduan(self):
        str = ''
        if self.cb_zhongwen.isChecked():
            str += ('的一是在不了有和人这中大为上个国我以要他'
                    + '时来用们生到作地于出就分对成会可主发年动'
                    + '同工也能下过子说产种面而方后多定行学法所'
                    + '民得经十三之进着等部度家电力里如水化高自'
                    + '二理起小物现实加量都两体制机当使点从业本'
                    + '去把性好应开它合还因由其些然前外天政四日'
                    + '那社义事平形相全表间样与关各重新线内数正'
                    + '心反你明看原又么利比或但质气第向道命此变'
                    + '条只没结解问意建月公无系军很情者最立代想'
                    + '已通并提直题党程展五果料象员革位入常文总'
                    + '次品式活设及管特件长求老头基资边流路级少'
                    + '图山统接知较将组见计别她手角期根论运农指'
                    + '几九区强放决西被干做必战先回则任取据处队'
                    + '南给色光门即保治北造百规热领七海口东导器'
                    + '压志世金增争济阶油思术极交受联什认六共权'
                    + '收证改清己美再采转更单风切打白教速花带安'
                    + '场身车例真务具万每目至达走积示议声报斗完'
                    + '类八离华名确才科张信马节话米整空元况今集'
                    + '温传土许步群广石记需段研界拉林律叫且究观'
                    + '越织装影算低持音众书布复容儿须际商非验连'
                    + '断深难近矿千周委素技备半办青省列习响约支'
                    + '般史感劳便团往酸历市克何除消构府称太准精'
                    + '值号率族维划选标写存候毛亲快效斯院查江型'
                    + '眼王按格养易置派层片始却专状育厂京识适属'
                    + '圆包火住调满县局照参红细引听该铁价严龙飞')
        if self.cb_zhongbiao.isChecked():
            str += '，。、；、/*-+~·=！@#￥%……&*（）{}|\\“”’‘：《》？'
        if self.cb_yingwen.isChecked():
            str += 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
        if self.cb_yingbiao.isChecked():
            str += ',./\\;\"\"!@#$%^&*()_+{}~[]|;:<>?/-'
        if self.cb_shuzi.isChecked():
            str += '0123456789'
        if len(str) < 5:
            str += ('测') * 100
        return str * 100

    # 按钮槽函数
    def cao(self, btn):
        # 字符类型
        str_obj = self.panduan()

        # 按钮文字
        btn_text = btn.text()

        # 10
        if btn_text == '10':
            yu_suijiZifu = self.yu_suijiStr(str_obj, (10 - 2)) + '十字'

        # 20
        if btn_text == '20':
            yu_suijiZifu = self.yu_suijiStr(str_obj, (20 - 3)) + '二十字'

        # 50
        if btn_text == '50':
            yu_suijiZifu = self.yu_suijiStr(str_obj, (50 - 3)) + '五十字'

        # 100
        if btn_text == '100':
            yu_suijiZifu = self.yu_suijiStr(str_obj, (100 - 3)) + '一百字'

        # 万能
        if btn_text == '万能':
            # 随机字符
            yu_suijiZifu = self.yu_suijiStr(str_obj, (14 - 3)) + '十四字'
            yu_suijiZifu += self.yu_suijiStr(str_obj, (18 - 3 - 14)) + '十八字'
            yu_suijiZifu += self.yu_suijiStr(str_obj, (25 - 3 - 18)) + '二五字'
            yu_suijiZifu += self.yu_suijiStr(str_obj, (30 - 3 - 25)) + '三十字'
            yu_suijiZifu += self.yu_suijiStr(str_obj, (36 - 3 - 30)) + '三六字'
            yu_suijiZifu += self.yu_suijiStr(str_obj, (50 - 3 - 36)) + '五十字'
            yu_suijiZifu += self.yu_suijiStr(str_obj, (75 - 3 - 50)) + '七五字'
            yu_suijiZifu += self.yu_suijiStr(str_obj, (100 - 3 - 75)) + '一百字'
            yu_suijiZifu += self.yu_suijiStr(str_obj, (120 - 3 - 100)) + '百二字'
            yu_suijiZifu += self.yu_suijiStr(str_obj, (150 - 3 - 120)) + '百五字'
            yu_suijiZifu += self.yu_suijiStr(str_obj, (200 - 3 - 150)) + '二百字'
            yu_suijiZifu += self.yu_suijiStr(str_obj, (300 - 3 - 200)) + '三百字'
            yu_suijiZifu += self.yu_suijiStr(str_obj, (500 - 3 - 300)) + '五百字'
            yu_suijiZifu += self.yu_suijiStr(str_obj, (1000 - 3 - 500)) + '一千字'
            yu_suijiZifu += self.yu_suijiStr(str_obj, (1100 - 3 - 1000)) + '千一字'
            yu_suijiZifu += self.yu_suijiStr(str_obj, (1200 - 3 - 1100)) + '千二字呢'

        # 通用
        if btn_text == '通用':
            # 随机字符
            yu_suijiZifu = '测' * (14 - 3) + '十四字'
            yu_suijiZifu += '测' * (18 - 3 - 14) + '十八字'
            yu_suijiZifu += '测' * (25 - 3 - 18) + '二五字'
            yu_suijiZifu += '测' * (30 - 3 - 25) + '三十字'
            yu_suijiZifu += '测' * (36 - 3 - 30) + '三六字'
            yu_suijiZifu += '测' * (50 - 3 - 36) + '五十字'
            yu_suijiZifu += '测' * (60 - 3 - 50) + '六十字'
            yu_suijiZifu += '测' * (75 - 3 - 60) + '七五字'
            yu_suijiZifu += '测' * (100 - 3 - 75) + '一百字'
            yu_suijiZifu += '测' * (120 - 3 - 100) + '百二字'
            yu_suijiZifu += '测' * (150 - 3 - 120) + '百五字'
            yu_suijiZifu += '测' * (200 - 3 - 150) + '二百字'
            yu_suijiZifu += '测' * (300 - 3 - 200) + '三百字'
            yu_suijiZifu += '测' * (500 - 3 - 300) + '五百字'
            yu_suijiZifu += '测' * (1000 - 3 - 500) + '一千字'
            yu_suijiZifu += '测' * (1100 - 3 - 1000) + '千一字'
            yu_suijiZifu += '测' * (1200 - 3 - 1100) + '千二字呢'

        # 特殊
        if btn_text == '特殊':
            yu_suijiZifu = '\\r前杠r后杠n啊\\n\n';
            yu_suijiZifu += '\n上下都空一行啊\n';
            yu_suijiZifu += '\n\t制个表啊';
            yu_suijiZifu += '\n\\t杠t啊\n';
            yu_suijiZifu += '''
综合\\^\\n\\r\\./../.\\..\\|\\t(.*?).*?\\??\\\$(.*)*.\$//.*?\\\$
中文，。、；、/*-+~·=！@#￥%……&*（）{}|\\“”’‘：《》？【】
英文,./\\;\"\"!@#\$%^&*()_+{}~[]|;:<>?/-
字母ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz
数字0123456789'''

        # 文本域设置字符
        self.textEdit.setText(yu_suijiZifu)

    # 随机字符串（随机型）
    def yu_suijiStr(self, zifu, num):
        l = random.sample(zifu, num)
        r = ''
        for i in l:
            r += i
        return r

    # 计数器变化槽函数
    def spChanged(self):
        # 字符类型
        str_obj = self.panduan()
        # 计数器数字
        num = self.spinBox.value()
        # 随机字符
        str = self.yu_suijiStr(str_obj, num)
        # 文本域设置字符
        self.textEdit.setText(str)
        # 光标移动到末尾
        self.moveGuangbiao()

    # 文本域变化槽函数
    def textEditChanged(self):
        # 获得文本域的值
        yu_str = self.textEdit.toPlainText()
        # 复制到剪贴板
        self.yu_CtrlC(yu_str)
        # 改变标题
        self.setWindowTitle('余时锐随机字符串v9.0，字符数 = ' + str(len(yu_str)))

    # 复制到剪贴板
    def yu_CtrlC(self, yu_text):
        clipboard = QApplication.clipboard()
        clipboard.setText(yu_text)

    # 光标移到末尾
    def moveGuangbiao(self):
        # ui->QTextEdit_rx->moveCursor(QTextCursor::End, QTextCursor::MoveAnchor);
        self.textEdit.moveCursor(QTextCursor.End, QTextCursor.MoveAnchor)
        # cursor = self.textEdit.textCursor()
        # cursor.movePosition(QtGui.QTextCursor.End)
        # self.textEdit.setTextCursor(cursor)

# 余时锐随机字符串v9.0
# pyinstaller -F -w -i yu.ico main.py
if __name__ == "__main__":
    app = QApplication(sys.argv)
    suijiStr = Yu()
    suijiStr.show()
    sys.exit(app.exec_())
