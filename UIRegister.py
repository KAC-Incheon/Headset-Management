from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5 import *

from DBConnect import DB

import pymysql
############################ 등록창 ################################################
class Ui_Resigster(QDialog):

    def __init__(self):  # 클래스 생성 시  자동 실행되는 함수
        super().__init__()
        self.db = DB()
        print(self.db)
        self.setupUi(self)
        self.show()


    def setupUi(self, Dialog):

        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)  ### QDialog 윈도창에 물음표 제거
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(464, 440)
        self.label_1 = QtWidgets.QLabel(Dialog)
        self.label_1.setGeometry(QtCore.QRect(140, 10, 181, 41))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_1.setFont(font)
        self.label_1.setTextFormat(QtCore.Qt.RichText)
        self.label_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_1.setObjectName("label_1")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(120, 140, 210, 41))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.textEdit_4 = QtWidgets.QTextEdit(self.horizontalLayoutWidget_4)
        self.textEdit_4.setObjectName("textEdit_4")
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setBold(False)
        font.setPointSize(10)
        self.textEdit_4.setFont(font)
        self.horizontalLayout_4.addWidget(self.textEdit_4)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(50, 290, 361, 102))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 40, 152, 40))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setBold(False)
        self.label.setFont(font)
        self.horizontalLayout.addWidget(self.label)
        self.textBrowser = QtWidgets.QTextBrowser(self.horizontalLayoutWidget)
        self.textBrowser.setObjectName("textBrowser")
        self.horizontalLayout.addWidget(self.textBrowser)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(180, 40, 142, 40))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setBold(False)
        self.label_3.setFont(font)
        self.horizontalLayout_2.addWidget(self.label_3)
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.horizontalLayoutWidget_2)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.horizontalLayout_2.addWidget(self.textBrowser_2)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(120, 70, 60, 54))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(220, 80, 110, 41))
        self.comboBox.setObjectName("comboBox")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(226, 210, 101, 41))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")

        self.pushButton_4.setStyleSheet("QPushButton"
                                        "{"
                                        "border-style:solid;"
                                        "border-width: 2px;"
                                        "border-color: #9DCFFF;"
                                        "border-radius: 3px;"
                                        "}""QPushButton::hover"
                                        "{"
                                        "border-style:solid;"
                                        "border-width: 1px;"
                                        "color:white;"
                                        "background-color: #9DCFFF;"
                                        "border-radius: 3px;"
                                        "}"
                                        )

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.pushButton_4.clicked.connect(Dialog.new)

        self.comboBox.addItem("HW251")
        self.comboBox.addItem("H171")
        self.comboBox.currentIndexChanged.connect(self.combo_change)

        self.textBrowser.setText(str(self.db.execute_one("SELECT * from stock WHERE model_name = 'HW251';")[1]))


        self.textBrowser_2.setText(str(self.db.execute_one("SELECT * from stock WHERE model_name = 'H171';")[1]))
        print("is register start")


    def new(self):
        print("등록 클릭")

        ment = self.Question_event()  ### yes or no

        if ment:
            try:
                ####사용자 입력값 받아오기
                global user, h_user
                user = [1, 2, 3, 4, 5, 6, 7, 8, ]
                h_user = [1, 2]

                user[0] = ''  ###상태
                user[1] = ''  ###state_date
                user[2] = ''  ###give_memo
                user[3] = ''  ###return_memo
                user[4] = ''  ###recieve_person
                user[5] = ''  ###return_person
                user[6] = ''  ###check_person
                user[7] = ''  ###bigo

                h_user[0] = self.textEdit_4.toPlainText()  # 일련번호
                h_user[1] = self.combo_change()  ###모델명 콤보박스 현재 데이터

                ###헤드셋에 추가
                self.db.excute(f"INSERT INTO headset VALUES (%s,%s,%s);", (h_user[0], h_user[1],'1'))

                ###빈 이력 생성
                # sql = "INSERT INTO history VALUES (NULL,'{1[0]}','{0[0]}',NULL,'{0[2]}','{0[3]}','{0[4]}','{0[5]}','{0[6]}','{0[7]}');".format(user,h_user)
                # cur.execute(sql)
                # print(sql)

                self.db.excute(f"UPDATE stock SET amount = amount-1 WHERE model_name = '{h_user[1]}';")

                ######재고 수량 다시 세기
                self.textBrowser.setText(str(self.db.execute_one("SELECT * from stock WHERE model_name = 'HW251';")[1]))

                self.textBrowser_2.setText(str(self.db.execute_one("SELECT * from stock WHERE model_name = 'H171';")[1]))

                QMessageBox.about(self, '알림', '등록 완료')

            except pymysql.err.IntegrityError as e:
                print('에러')
                print(e)
                QMessageBox.warning(self, '경고', '중복되는 일련번호가 있습니다.')


        elif not ment:
            pass

    def Question_event(self):

        ment_1 = self.combo_change()
        ment_2 = self.textEdit_4.toPlainText()
        ment = '모델명 : {} , 일련번호 : {} 을 등록하시겠습니까?'.format(ment_1, ment_2)
        buttonReply = QMessageBox.question(self, '알림', ment, QMessageBox.Yes | QMessageBox.No)

        if buttonReply == QMessageBox.Yes:
            print('Yes clicked.')
            return True
        elif buttonReply == QMessageBox.No:
            print('No clicked.')
            return False

    def combo_change(self):  ###모델명

        combo = self.comboBox.currentText()
        return combo

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "신규 등록"))
        self.label_1.setText(_translate("Dialog", "신규 등록"))
        self.label_4.setText(_translate("Dialog", "일련번호   "))
        self.groupBox.setTitle(_translate("Dialog", "현재 재고수량"))
        self.label.setText(_translate("Dialog", "HW251"))
        self.label_3.setText(_translate("Dialog", "H171"))
        self.label_2.setText(_translate("Dialog", "모델명  "))
        self.pushButton_4.setText(_translate("Dialog", "등록"))
