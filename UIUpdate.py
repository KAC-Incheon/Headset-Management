from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

import pymysql

############################ 수정창 ################################################
class Ui_Update(QDialog):

    def __init__(self):  # 클래스 생성 시  자동 실행되는 함수
        super().__init__()
        self.setupUi(self)
        self.show()

    def setupUi(self, UpdateUi):

        UpdateUi.setWindowModality(Qt.ApplicationModal)  ### 메인창 조작 불가
        self.setWindowFlag(Qt.WindowContextHelpButtonHint, False)  ### QDialog 윈도창에 물음표 제거

        UpdateUi.setObjectName("UpdateUi")
        UpdateUi.setFixedSize(1220, 440)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        UpdateUi.setFont(font)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(UpdateUi)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(260, 280, 221, 30))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.horizontalLayoutWidget_3)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.horizontalLayout_3.addWidget(self.textBrowser_2)
        self.textEdit_3 = QtWidgets.QTextEdit(self.horizontalLayoutWidget_3)
        self.textEdit_3.setObjectName("textEdit_3")
        self.horizontalLayout_3.addWidget(self.textEdit_3)

        self.textBrowser_3 = QtWidgets.QTextBrowser(UpdateUi)
        self.textBrowser_3.setGeometry(QtCore.QRect(520, 280, 97, 30))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textEdit_4 = QtWidgets.QTextEdit(UpdateUi)
        self.textEdit_4.setGeometry(QtCore.QRect(630, 280, 200, 30))
        self.textEdit_4.setObjectName("textEdit_4")

        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(UpdateUi)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(260, 360, 221, 30))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.horizontalLayoutWidget_5)
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.horizontalLayout_5.addWidget(self.textBrowser_4)
        self.textEdit_5 = QtWidgets.QTextEdit(self.horizontalLayoutWidget_5)
        self.textEdit_5.setObjectName("textEdit_5")
        self.horizontalLayout_5.addWidget(self.textEdit_5)
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(UpdateUi)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(580, 360, 170, 30))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        self.textEdit_6 = QtWidgets.QTextEdit(self.horizontalLayoutWidget_6)
        self.textEdit_6.setObjectName("textEdit_6")
        self.horizontalLayout_6.addWidget(self.textEdit_6)
        self.horizontalLayoutWidget_7 = QtWidgets.QWidget(UpdateUi)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(860, 280, 280, 30))
        self.horizontalLayoutWidget_7.setObjectName("horizontalLayoutWidget_7")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_7.addWidget(self.label_5)
        self.textEdit_7 = QtWidgets.QTextEdit(self.horizontalLayoutWidget_7)
        self.textEdit_7.setObjectName("textEdit_7")
        self.horizontalLayout_7.addWidget(self.textEdit_7)
        self.verticalLayoutWidget = QtWidgets.QWidget(UpdateUi)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(60, 19, 1100, 220))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(QtCore.Qt.RichText)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.tableWidget = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        self.tableWidget.setFont(font)
        self.verticalLayout.addWidget(self.tableWidget)
        self.label_6 = QtWidgets.QLabel(UpdateUi)
        self.label_6.setGeometry(QtCore.QRect(60, 270, 121, 54))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.comboBox = QtWidgets.QComboBox(UpdateUi)
        self.comboBox.setGeometry(QtCore.QRect(130, 280, 91, 30))
        self.comboBox.setObjectName("comboBox")
        self.label_7 = QtWidgets.QLabel(UpdateUi)
        self.label_7.setGeometry(QtCore.QRect(60, 350, 121, 54))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.comboBox_2 = QtWidgets.QComboBox(UpdateUi)
        self.comboBox_2.setGeometry(QtCore.QRect(130, 360, 91, 30))
        self.comboBox_2.setObjectName("comboBox_2")
        self.pushButton_2 = QtWidgets.QPushButton(UpdateUi)
        self.pushButton_2.setGeometry(QtCore.QRect(826, 360, 101, 41))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(UpdateUi)
        self.pushButton_3.setGeometry(QtCore.QRect(940, 360, 101, 41))
        self.pushButton_4 = QtWidgets.QPushButton(UpdateUi)
        self.pushButton_4.setGeometry(QtCore.QRect(1054, 360, 101, 41))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_4.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(UpdateUi)
        QtCore.QMetaObject.connectSlotsByName(UpdateUi)

        self.tableWidget.verticalHeader().sectionClicked.connect(self.header_click)  # 헤더 클릭
        self.pushButton_2.clicked.connect(UpdateUi.update)  #####수정 버튼 클릭 함수연결
        self.pushButton_3.clicked.connect(UpdateUi.insert)  #####이력등록 버튼 클릭 함수연결
        self.pushButton_4.clicked.connect(UpdateUi.remove)  #####이력삭제 버튼 클릭 함수연결

        self.pushButton_2.setStyleSheet("QPushButton"
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

        self.pushButton_3.setStyleSheet("QPushButton"
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

        # 선택값 초기화시켜야하는 경우
        self.tableWidget.horizontalHeader().sectionClicked.connect(self.headerclicked_event)
        self.tableWidget.cellClicked.connect(self.cellclicked_event)

        self.tableWidget.setCornerButtonEnabled(False)  # 왼쪽 상단 코너버튼 클릭 끄기

        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)  ###테이블 안에서 수정 금지

        #######메인창에서 선택한 데이터의 일련번호 기준 표출
        global selected_data

        print(selected_data)
        conn = pymysql.connect(host='127.0.0.1', user='headset', password='headset', port=3306,  # sql테이블 읽어오기
                               db='headset_db', charset='utf8')
        cur = conn.cursor()

        sql = "SELECT * FROM v_now WHERE serial_num = '{}' ORDER BY state_date DESC".format(selected_data[1])

        ####테이블 행열 지정

        print(sql)

        cur.execute(sql)

        allrows = cur.fetchall()
        self.tableWidget.setRowCount(len(allrows))  # 테이블 행 갯수 지정
        self.tableWidget.setColumnCount(11)  # 테이블 열 갯수 지정
        self.tableWidget.setHorizontalHeaderLabels(
            ['모델명', '일련번호', '상태', '일자', '지급내용', '인수자', '반납내용', '반납자', '확인자', '비고'])  # 헤드이름

        self.tableWidget.setStyleSheet("border-style:solid;"
                                       "border-width: 1px;"
                                       "border-color: #9DCFFF;"
                                       "border-radius: 3px;")

        ####테이블 데이터 표출
        cur.execute(sql)
        row = 0
        while True:
            sqlrow = cur.fetchone()
            if sqlrow == None:
                break
            for col in range(0, 11):  # 0~10열 출력
                self.tableWidget.setItem(row, col, QTableWidgetItem(str(sqlrow[col])))
                if str(sqlrow[col]) == "None":  # 일자 null값 공백으로 표출
                    self.tableWidget.setItem(row, col, QTableWidgetItem(""))
            row += 1
        self.tableWidget.setColumnHidden(10, True)  ####마지막 기록 순번 열 숨김

        ###콤보박스 리스트 추가
        conn = pymysql.connect(host='127.0.0.1', user='headset', password='headset', port=3306,  # sql테이블 읽어오기
                               db='headset_db', charset='utf8')
        cur = conn.cursor()

        sql = "SELECT DISTINCT model_name, IF (model_name = '', '', model_name) AS result \
               FROM headset WHERE NOT model_name = '{}' ORDER BY model_name DESC ;".format(selected_data[0])
        cur.execute(sql)

        self.comboBox.addItem(selected_data[0])  ###메인창에서 선택한 데이터를 콤보박스 첫행에 추가

        ###콤보박스 리스트에 나머지 데이터 추가
        while True:
            sqlrow = cur.fetchone()
            if sqlrow == None:
                break
            self.comboBox.addItem(str(sqlrow[1]))

        self.comboBox.currentIndexChanged.connect(self.combo_change)

        ####지급여부 콤보박스2 리스트 설정
        sql = "SELECT DISTINCT state, IF (state = '', '', state) AS result \
               FROM v_now WHERE NOT state IN ('{}','') ORDER BY state DESC; ".format(selected_data[2])
        cur.execute(sql)

        self.comboBox_2.addItem(selected_data[2])  ###메인창에서 선택한 데이터부터 표출

        ###콤보박스2 리스트에 나머지 데이터 추가
        while True:
            sqlrow = cur.fetchone()
            if sqlrow == None:
                break
            self.comboBox_2.addItem(str(sqlrow[1]))

        a = self.comboBox_2.currentText()  ######지급여부에 따라 나머지 텍스트 세팅

        if a == "지급":
            self.textBrowser_2.setText("{}일자".format(a))
            self.textBrowser_3.setText("{}내용".format(a))
            self.textBrowser_4.setText("인수자")
        elif a == "반납":
            self.textBrowser_2.setText("{}일자".format(a))
            self.textBrowser_3.setText("{}내용".format(a))
            self.textBrowser_4.setText("반납자")
        else:
            self.textBrowser_2.setText("일자")
            self.textBrowser_3.setText("내용")
            self.textBrowser_4.setText("인수자")

        self.comboBox_2.currentIndexChanged.connect(self.combo2_change)  ###콤보박스 선택 시 함수

        global send_data, sub_data
        send_data = selected_data[1]  ####일련번호 이력등록 버튼에 전달
        selected_data = ['', '', '', '', '', '', '', '', '', '', '']  ###사용한 값 초기화, 메인창에서 선택한 행 리셋
        sub_data = ['', '', '', '', '', '', '', '', '', '', '']  ### 수정창에서 선택한 행 리셋
        print("메인창 선택값 초기화를 완료,{}".format(sub_data))

        # self.tableWidget.resizeColumnToContents(0)  #0번째 열 너비 조정
        # self.tableWidget.resizeColumnToContents(4)  #4번째 열 너비 조정
        # self.tableWidget.resizeColumnToContents(6)  #6번째 열 너비 조정
        # self.tableWidget.resizeColumnToContents(9)  #9번째 열 너비 조정
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setFixedWidth(40)  ##열 헤더 너비 고정

    def cellclicked_event(self, row, col):
        global sub_data
        sub_data = ['', '', '', '', '', '', '', '', '', '', '']
        print("발생:", sub_data)

    def headerclicked_event(self, logicalIndex):
        global sub_data
        sub_data = ['', '', '', '', '', '', '', '', '', '', '']
        print("발생:", sub_data)

    def header_click(self, logicalIndex):  ###사용자 행 헤더 클릭시
        global sub_row, sub_data
        sub_row = logicalIndex + 1
        print(str(sub_row) + '번째 행')

        data1 = self.tableWidget.item(logicalIndex, 0).text()
        data2 = self.tableWidget.item(logicalIndex, 1).text()
        data3 = self.tableWidget.item(logicalIndex, 2).text()
        data4 = self.tableWidget.item(logicalIndex, 3).text()
        data5 = self.tableWidget.item(logicalIndex, 4).text()
        data6 = self.tableWidget.item(logicalIndex, 5).text()
        data7 = self.tableWidget.item(logicalIndex, 6).text()
        data8 = self.tableWidget.item(logicalIndex, 7).text()
        data9 = self.tableWidget.item(logicalIndex, 8).text()
        data10 = self.tableWidget.item(logicalIndex, 9).text()
        data11 = self.tableWidget.item(logicalIndex, 10).text()  # history 인덱스 값

        sub_data = [data1, data2, data3, data4, data5, data6, data7, data8, data9, data10, data11]
        print("선택된 값 ->", sub_data)

        ####텍스트에딧에 값 띄우기
        self.textEdit_3.setText(sub_data[3])  ### 기록 일자
        two = sub_data[2]
        if two == "지급":
            self.textEdit_4.setText(sub_data[4])  ###지급내용 표출
            self.textEdit_5.setText(sub_data[5])  ###인수자 표출
        elif two == "반납":
            self.textEdit_4.setText(sub_data[6])  ###반납내용 표출
            self.textEdit_5.setText(sub_data[7])  ###반납자 표출
        else:  # nore or 공백
            self.textEdit_4.setText(sub_data[4])  ###지급내용 표출
            self.textEdit_5.setText(sub_data[5])  ###인수자 표출
        self.textEdit_6.setText(sub_data[8])  ###확인자
        self.textEdit_7.setText(sub_data[9])  ###비고

        ####모델명 콤보박스 리스트 설정
        conn = pymysql.connect(host='127.0.0.1', user='headset', password='headset', port=3306,  # sql테이블 읽어오기
                               db='headset_db', charset='utf8')
        cur = conn.cursor()

        sql = "SELECT DISTINCT model_name, IF (model_name = '', '', model_name) AS result \
               FROM headset WHERE NOT model_name = '{}' ORDER BY model_name DESC ;".format(sub_data[0])
        cur.execute(sql)
        self.comboBox.clear()
        self.comboBox.addItem(sub_data[0])  ###수정창에서 선택한 데이터를 콤보박스 첫행에 추가

        ###콤보박스 리스트에 나머지 데이터 추가
        while True:
            sqlrow = cur.fetchone()
            if sqlrow == None:
                break
            self.comboBox.addItem(str(sqlrow[1]))

        self.comboBox.currentIndexChanged.connect(self.combo_change)  ###콤보박스 선택 시 함수

        ####지급여부 콤보박스2 리스트 설정
        sql = "SELECT DISTINCT state, IF (state = '', '', state) AS result \
               FROM v_now WHERE NOT state IN ('{}','') ORDER BY state DESC; ".format(sub_data[2])
        cur.execute(sql)

        self.comboBox_2.clear()
        self.comboBox_2.addItem(sub_data[2])  ###첫행에 선택한 데이터부터 첫번째 표출

        ###콤보박스2 리스트에 나머지 데이터 추가
        while True:
            sqlrow = cur.fetchone()
            if sqlrow == None:
                break
            self.comboBox_2.addItem(str(sqlrow[1]))

        a = self.comboBox_2.currentText()  ######지급여부에 따라 나머지 텍스트 세팅

        if a == "지급":
            self.textBrowser_2.setText("{}일자".format(a))
            self.textBrowser_3.setText("{}내용".format(a))
            self.textBrowser_4.setText("인수자")
        elif a == "반납":
            self.textBrowser_2.setText("{}일자".format(a))
            self.textBrowser_3.setText("{}내용".format(a))
            self.textBrowser_4.setText("반납자")
        else:
            self.textBrowser_2.setText("일자")
            self.textBrowser_3.setText("내용")
            self.textBrowser_4.setText("인수자")

        self.comboBox_2.currentIndexChanged.connect(self.combo2_change)  ###콤보박스 선택 시 함수

        return sub_row, sub_data

    def combo_change(self):  ###모델명

        combo = self.comboBox.currentText()
        return combo

    def combo2_change(self):  ###### 지급or반납 선택할 때마다 브라우저 텍스트 세팅
        a = self.comboBox_2.currentText()

        if a == "지급":
            self.textBrowser_2.setText("{}일자".format(a))
            self.textBrowser_3.setText("{}내용".format(a))
            self.textBrowser_4.setText("인수자")
        elif a == "반납":
            self.textBrowser_2.setText("{}일자".format(a))
            self.textBrowser_3.setText("{}내용".format(a))
            self.textBrowser_4.setText("반납자")
        else:
            self.textBrowser_2.setText("일자")
            self.textBrowser_3.setText("내용")
            self.textBrowser_4.setText("인수자")

        return a

        ######수정 버튼 클릭

    def update(self):
        print("수정할게요")
        global sub_data
        standard = sub_data[1].strip()  ##일련번호 값
        if standard:  ###공백이 아닐경우

            # 사용자 입력값 받기 위한 변수, history 없뎃
            global value, h_value
            value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
            h_value = [1, 2]

            value[0] = self.combo2_change()  ###상태 콤보박스 데이터 state
            value[1] = self.textEdit_3.toPlainText()  ###state_date

            if value[0] == '지급':
                value[2] = self.textEdit_4.toPlainText()  ###give_memo
                value[3] = ''  ###return_memo
                value[4] = self.textEdit_5.toPlainText()  ###recieve_person
                value[5] = ''  ###return_person
            elif value[0] == '반납':
                value[2] = ''  ###give_memo
                value[3] = self.textEdit_4.toPlainText()  ###return_memo
                value[4] = ''  ###recieve_person
                value[5] = self.textEdit_5.toPlainText()  ###return_person
            else:  ###none or 공백
                value[0] == ''
                value[2] = self.textEdit_4.toPlainText()  ###give_memo
                value[3] = ''  ###return_memo
                value[4] = self.textEdit_5.toPlainText()  ###recieve_person
                value[5] = ''  ###return_person

            value[6] = self.textEdit_6.toPlainText()  ###check_person
            value[7] = self.textEdit_7.toPlainText()  ###bigo
            value[8] = sub_data[10]  ###이력 기록 고유 인덱스 값

            h_value[0] = self.combo_change()  ###모델명
            h_value[1] = sub_data[1]  ###일련번호

            print("{0[0]},{0[1]},{0[2]},{0[3]},{0[4]},{0[5]},{0[6]},{0[7]},{0[8]}".format(value))

            try:
                print(datetime.datetime.strptime(value[1], "%Y-%m-%d"))

                answer = self.Question_event_update()  ### yes or no

                if answer:

                    conn = pymysql.connect(host='127.0.0.1', user='headset', password='headset', port=3306,
                                           # sql테이블 읽어오기
                                           db='headset_db', charset='utf8')
                    cur = conn.cursor()
                    if sub_data[10].strip():  ## 히스토리 인덱스 공백,null아닐 경우
                        sql = "UPDATE history SET state = '{0[0]}', state_date = '{0[1]}', give_memo = '{0[2]}', return_memo='{0[3]}', recieve_person = '{0[4]}', return_person = '{0[5]}', check_person = '{0[6]}', bigo = '{0[7]}' WHERE num = {0[8]};".format(
                            value)
                    if not sub_data[10].strip():  ## 히스토리 데이터x, 인덱스 공백,null인 경우
                        print('인덱스값 없음----->"{}"'.format(value[8]))
                        sql = "INSERT INTO history VALUES (NULL,'{1[1]}','{0[0]}','{0[1]}','{0[2]}','{0[3]}','{0[4]}','{0[5]}','{0[6]}','{0[7]}');".format(
                            value, h_value)
                    try:
                        cur.execute(sql)

                        print(sql)
                        sql = "UPDATE headset SET model_name = '{0[0]}' WHERE serial_num = '{0[1]}';".format(h_value)
                        cur.execute(sql)
                        print(sql)
                        ##########수정 후 다시 표출
                        sql = "SELECT * FROM v_now WHERE serial_num = '{}' ORDER BY state_date DESC".format(sub_data[1])
                        ####테이블 행열 지정
                        cur.execute(sql)
                        allrows = cur.fetchall()
                        self.tableWidget.setRowCount(len(allrows))  # 테이블 행 갯수 지정
                        self.tableWidget.setColumnCount(11)  # 테이블 열 갯수 지정
                        self.tableWidget.setHorizontalHeaderLabels(
                            ['모델명', '일련번호', '상태', '일자', '지급내용', '인수자', '반납내용', '반납자', '확인자', '비고'])  # 헤드이름
                        self.tableWidget.setStyleSheet("border-style:solid;"
                                                       "border-width: 1px;"
                                                       "border-color: #9DCFFF;"
                                                       "border-radius: 3px;")

                        ####테이블 데이터 표출
                        cur.execute(sql)
                        row = 0
                        while True:
                            sqlrow = cur.fetchone()
                            if sqlrow == None:
                                break
                            for col in range(0, 11):  # 0~10열 출력
                                self.tableWidget.setItem(row, col, QTableWidgetItem(str(sqlrow[col])))
                                if str(sqlrow[col]) == "None":  # 일자 null값 공백으로 표출
                                    self.tableWidget.setItem(row, col, QTableWidgetItem(""))
                            row += 1
                        self.tableWidget.setColumnHidden(10, True)  ####마지막 기록 순번 열 숨김

                        conn.commit()  #######DB 적용하려면 이거 필수
                        QMessageBox.about(self, '알림', '헤드셋 이력 정보가 수정되었습니다.')
                    except pymysql.err.DataError:
                        QMessageBox.warning(self, '경고', '허용 글자 수를 초과했습니다')

                if not answer: pass

            except ValueError:
                QMessageBox.warning(self, '경고', '날짜 형식은 YYYY-MM-DD로 입력해주세요.')

            except pymysql.err.OperationalError:
                QMessageBox.warning(self, '경고', '날짜 형식은 YYYY-MM-DD로 입력해주세요.')

        elif not standard:  ####선택값 공백인 경우
            QMessageBox.warning(self, '경고', '수정할 데이터를 선택하세요.')

        sub_data = ['', '', '', '', '', '', '', '', '', '', '']  ### 수정창에서 선택한 행 리셋
        print("수정창에서 선택한 값 초기화를 완료하였다,{}".format(sub_data))

        self.tableWidget.resizeColumnToContents(4)  # 4번째 열 너비 조정
        self.tableWidget.resizeColumnToContents(6)  # 6번째 열 너비 조정
        self.tableWidget.resizeColumnToContents(9)  # 9번째 열 너비 조정

    ######이력 등록 버튼 클릭
    def insert(self):

        print("값은", send_data)
        ####사용자 입력값 받아오기
        global value, h_value
        value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        h_value = [1, 2]

        value[0] = self.combo2_change()  ###상태 콤보박스 현재 데이터

        value[1] = self.textEdit_3.toPlainText()  ###state_date

        if value[0] == '지급':
            value[2] = self.textEdit_4.toPlainText()  ###give_memo
            value[3] = ''  ###return_memo
            value[4] = self.textEdit_5.toPlainText()  ###recieve_person
            value[5] = ''  ###return_person

        elif value[0] == '반납':
            value[2] = ''  ###give_memo
            value[3] = self.textEdit_4.toPlainText()  ###return_memo
            value[4] = ''  ###recieve_person
            value[5] = self.textEdit_5.toPlainText()  ###return_person

        else:  ###none or 공백
            value[0] == ''
            value[2] = self.textEdit_4.toPlainText()  ###give_memo
            value[3] = ''  ###return_memo
            value[4] = self.textEdit_5.toPlainText()  ###recieve_person
            value[5] = ''  ###return_person

        value[6] = self.textEdit_6.toPlainText()  ###check_person
        value[7] = self.textEdit_7.toPlainText()  ###bigo

        h_value[0] = self.combo_change()  ###모델명 콤보박스 현재 데이터
        h_value[1] = send_data  ###일련번호

        print("{0[0]},{0[1]},{0[2]},{0[3]},{0[4]},{0[5]},{0[6]},{0[7]}".format(value))

        try:
            print(datetime.datetime.strptime(value[1], "%Y-%m-%d"))

            answer = self.Question_event_insert()
            if answer:
                conn = pymysql.connect(host='127.0.0.1', user='headset', password='headset', port=3306,
                                       # sql테이블 읽어오기
                                       db='headset_db', charset='utf8')
                cur = conn.cursor()

                sql = "INSERT INTO history VALUES (NULL,'{1[1]}','{0[0]}','{0[1]}','{0[2]}','{0[3]}','{0[4]}','{0[5]}','{0[6]}','{0[7]}');".format(
                    value, h_value)
                cur.execute(sql)
                print(sql)

                ################등록 후 다시 표출

                sql = "SELECT * FROM v_now WHERE serial_num = '{}' ORDER BY state_date DESC".format(send_data)

                ####테이블 행열 지정
                cur.execute(sql)
                allrows = cur.fetchall()
                self.tableWidget.setRowCount(len(allrows))  # 테이블 행 갯수 지정
                self.tableWidget.setColumnCount(11)  # 테이블 열 갯수 지정
                self.tableWidget.setHorizontalHeaderLabels(
                    ['모델명', '일련번호', '상태', '일자', '지급내용', '인수자', '반납내용', '반납자', '확인자', '비고'])  # 헤드이름
                self.tableWidget.setStyleSheet("border-style:solid;"
                                               "border-width: 1px;"
                                               "border-color: #9DCFFF;"
                                               "border-radius: 3px;")

                ###테이블 데이터 표출
                cur.execute(sql)
                row = 0
                while True:
                    sqlrow = cur.fetchone()
                    if sqlrow == None:
                        break
                    for col in range(0, 11):  # 0~10열 출력
                        self.tableWidget.setItem(row, col, QTableWidgetItem(str(sqlrow[col])))
                        if str(sqlrow[col]) == "None":  # 일자 null값 공백으로 표출
                            self.tableWidget.setItem(row, col, QTableWidgetItem(""))
                    row += 1

                self.tableWidget.setColumnHidden(10, True)  ####마지막 기록 순번 열 숨김

                conn.commit()  #######DB 적용하려면 이거 필수
                QMessageBox.about(self, '알림', '일련번호 : {} 헤드셋의 이력이 추가되었습니다.'.format(send_data))
                if not answer: pass
        except ValueError:
            QMessageBox.warning(self, '경고', '날짜 형식은 YYYY-MM-DD로 입력해주세요.')
        except pymysql.err.OperationalError:
            QMessageBox.warning(self, '경고', '날짜 형식은 YYYY-MM-DD로 입력해주세요.')

        self.tableWidget.resizeColumnToContents(4)  # 4번째 열 너비 조정
        self.tableWidget.resizeColumnToContents(6)  # 6번째 열 너비 조정
        self.tableWidget.resizeColumnToContents(9)  # 9번째 열 너비 조정

    #######이력 삭제 버튼 클릭
    def remove(self):
        global sub_data

        standard = sub_data[1].strip()
        if standard:  ###공백이 아닐경우
            if sub_data[10].strip():  ###히스토리 인덱스 공백이 아닐경우
                print("값은", send_data)
                conn = pymysql.connect(host='127.0.0.1', user='headset', password='headset', port=3306,
                                       # sql테이블 읽어오기
                                       db='headset_db', charset='utf8')
                cur = conn.cursor()
                sql = "DELETE FROM history WHERE num = '{}';".format(sub_data[10])  ###header_click함수 실행 시 생성
                answer = self.Question_event_remove()
                if answer:
                    cur.execute(sql)
                    print(sql)
                    ####삭제 후 다시 표출
                    sql = "SELECT * FROM v_now WHERE serial_num = '{}' ORDER BY state_date DESC".format(
                        send_data)  ###메인창에서 선택한 행의 일련번호
                    ####테이블 행열 지정
                    cur.execute(sql)
                    allrows = cur.fetchall()
                    self.tableWidget.setRowCount(len(allrows))  # 테이블 행 갯수 지정
                    self.tableWidget.setColumnCount(11)  # 테이블 열 갯수 지정
                    self.tableWidget.setHorizontalHeaderLabels(
                        ['모델명', '일련번호', '상태', '일자', '지급내용', '인수자', '반납내용', '반납자', '확인자', '비고'])  # 헤드이
                    self.tableWidget.setStyleSheet("border-style:solid;"
                                                   "border-width: 1px;"
                                                   "border-color: #9DCFFF;"
                                                   "border-radius: 3px;")

                    ###테이블 데이터 표출
                    cur.execute(sql)
                    row = 0
                    while True:
                        sqlrow = cur.fetchone()
                        if sqlrow == None:
                            break
                        for col in range(0, 11):  # 0~10열 출력
                            self.tableWidget.setItem(row, col, QTableWidgetItem(str(sqlrow[col])))
                            if str(sqlrow[col]) == "None":  # 일자 null값 공백으로 표출
                                self.tableWidget.setItem(row, col, QTableWidgetItem(""))
                        row += 1
                    self.tableWidget.setColumnHidden(10, True)  ####마지막 기록 순번 열 숨김
                    conn.commit()  #######DB 적용하려면 이거 필수
                    QMessageBox.about(self, '알림', '일련번호 : {} 헤드셋의 이력이 삭제되었습니다.'.format(send_data))

                if not answer: pass
            elif not sub_data[10].strip():
                QMessageBox.warning(self, '경고', '삭제할 이력이 없습니다.')
        elif not standard:  ####선택값 공백인 경우
            QMessageBox.warning(self, '경고', '삭제할 이력을 선택하세요.')

        sub_data = ['', '', '', '', '', '', '', '', '', '', '']  ### 수정창에서 선택한 행 리셋
        print("수정창에서 선택한 값 초기화를 완료하였다,{}".format(sub_data))
        self.tableWidget.resizeColumnToContents(4)  # 4번째 열 너비 조정
        self.tableWidget.resizeColumnToContents(6)  # 6번째 열 너비 조정
        self.tableWidget.resizeColumnToContents(9)  # 9번째 열 너비 조정

    def Question_event_insert(self):

        if value[0] == '지급':
            ment = "'모델명: {1[0]}, 지급여부: {0[0]}, \n지급일자: {0[1]}, \n지급내용: {0[2]}, \n인수자: {0[4]}, 확인자: {0[6]}, \n비고: {0[7]}' \n로 데이터를 추가하시겠습니까?".format(
                value, h_value)
        if value[0] == '반납':
            ment = "'모델명: {1[0]}, 지급여부: {0[0]}, \n반납일자: {0[1]}, \n반납내용: {0[3]}, \n반납자: {0[5]}, 확인자: {0[6]}, \n비고: {0[7]}' \n로 데이터를 추가하시겠습니까?".format(
                value, h_value)
        else:
            ment = "'모델명: {1[0]}, 지급여부: {0[0]}, \n지급일자: {0[1]}, \n지급내용: {0[2]}, \n인수자: {0[4]}, 확인자: {0[6]}, \n비고: {0[7]}' \n로 데이터를 추가하시겠습니까?".format(
                value, h_value)

        buttonReply = QMessageBox.question(self, '알림', ment, QMessageBox.Yes | QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            return True
        elif buttonReply == QMessageBox.No:
            return False

    def Question_event_update(self):

        if value[0] == '지급':
            ment = "{2}번 행을 '모델명: {1[0]}, 지급여부: {0[0]}, \n지급일자: {0[1]}, \n지급내용: {0[2]}, \n인수자: {0[4]}, 확인자: {0[6]}, \n비고: {0[7]}' \n로 수정하시겠습니까?".format(
                value, h_value, sub_row)
        if value[0] == '반납':
            ment = "{2}번 행을 '모델명: {1[0]}, 지급여부: {0[0]}, \n반납일자: {0[1]}, \n반납내용: {0[3]}, \n반납자: {0[5]}, 확인자: {0[6]}, \n비고: {0[7]}' \n로 수정하시겠습니까?".format(
                value, h_value, sub_row)
        else:
            ment = "{2}번 행을 '모델명: {1[0]}, 지급여부: {0[0]}, \n지급일자: {0[1]}, \n지급내용: {0[2]}, \n인수자: {0[5]}, 확인자: {0[6]}, \n비고: {0[7]}' \n로 수정하시겠습니까?".format(
                value, h_value, sub_row)

        buttonReply = QMessageBox.question(self, '알림', ment, QMessageBox.Yes | QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            return True
        elif buttonReply == QMessageBox.No:
            return False

    def Question_event_remove(self):

        ment = "일련번호 : {} 헤드셋의 {}번 행 이력을 삭제하시겠습니까?".format(send_data, sub_row)
        buttonReply = QMessageBox.question(self, '알림', ment, QMessageBox.Yes | QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            return True
        elif buttonReply == QMessageBox.No:
            return False

    def retranslateUi(self, UpdateUi):
        _translate = QtCore.QCoreApplication.translate
        UpdateUi.setWindowTitle(_translate("UpdateUi", "수정"))
        self.label_4.setText(_translate("UpdateUi", "확인자   "))
        self.label_5.setText(_translate("UpdateUi", "비고"))
        self.label_2.setText(_translate("UpdateUi", "수정"))
        self.label_6.setText(_translate("UpdateUi", "모델명"))
        self.label_7.setText(_translate("UpdateUi", "지급여부"))
        self.pushButton_2.setText(_translate("UpdateUi", "수정"))
        self.pushButton_3.setText(_translate("UpdateUi", "이력 등록"))
        self.pushButton_4.setText(_translate("UpdateUi", "이력 삭제"))
