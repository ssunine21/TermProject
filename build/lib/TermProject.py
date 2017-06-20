from tkinter import *
from tkinter import ttk


m_TK = Tk()
m_TK.geometry("700x400")
DataList = []

def InitTab():
    global frame1
    global frame2
    notebook = ttk.Notebook(m_TK)
    frame1 = ttk.Frame(notebook, height=370, width=690)
    frame2 = ttk.Frame(notebook)
    notebook.add(frame1, text="국가기술자격 시험일정", )
    notebook.add(frame2, text="종목상세정보")
    notebook.grid(row=0, column=0)

def InitRadio():
    global rVar
    rVar = IntVar()
    r1 = ttk.Radiobutton(frame1, text="기술사", variable=rVar, value=1)
    r2 = ttk.Radiobutton(frame1, text="기능장", variable=rVar, value=2)
    r3 = ttk.Radiobutton(frame1, text="기사, 산업기사", variable=rVar, value=3)
    r4 = ttk.Radiobutton(frame1, text="기능사", variable=rVar, value=4)
    r1.place(x=25, y=50)
    r2.place(x=25, y=80)
    r3.place(x=25, y=110)
    r4.place(x=25, y=140)

    #TopText
    TopText1 = Label(frame1, text="※ 아래 해당항목을 클릭하시면\n    "
                                 "     자세한 내용을 보실 수 있습니다.")
    TopText1.place(x=0, y=10)
    TopText2 = Label(frame2, text="※ 아래 해당항목을 클릭하시면\n    "
                                 "     자세한 내용을 보실 수 있습니다.")
    TopText2.place(x=0, y=10)

def InitSearch1():
    Search1 = Button(frame1, text="Enter", command=Search1Action)
    Search1.place(x=150, y=53, width=70, height=110)

def Search1Action():
    RenderText1.configure(state='normal')
    addressBox.configure(state='normal')
    RenderText1.delete(0.0, END)
    if rVar.get() == 1:
        Library1()
    elif rVar.get() == 2:
        Library2()
    elif rVar.get() == 3:
        Library3()
    elif rVar.get() == 4:
        Library4()

def Library1():
    import http.client
    from xml.dom.minidom import parse, parseString
    conn = http.client.HTTPConnection("openapi.q-net.or.kr")
    conn.request("GET", "/api/service/rest/InquiryTestInformationNTQSVC/getPEList?serviceKey=9LcIiucOT0tvSUSIbEKcxVWQ%2FVyM9FrhsCh6AylGkIj%2FR9sim%2B1cuz%2FIAXE%2BmrQwad9HgJBs%2B4sV2Pw8Y%2BMBrw%3D%3D")
    req = conn.getresponse()

    global DataList
    DataList.clear()

    if req.status == 200:
        BooksDoc = req.read().decode('utf-8')
        if BooksDoc == None:
            print("에러")
        else:
            parseData = parseString(BooksDoc)
            response = parseData.childNodes
            body = response[0].childNodes

            for search1 in body:
                if search1.nodeName == "body":
                    items = body[1].childNodes
                    for search2 in items:
                        if search2.nodeName == "items":
                            item = items[0].childNodes

                            for search3 in item:
                                if search3.nodeName == "item":
                                    subitems = search3.childNodes

                                    DataList.append((subitems[0].firstChild.nodeValue, subitems[1].firstChild.nodeValue, subitems[2].firstChild.nodeValue,
                                                     subitems[3].firstChild.nodeValue, subitems[4].firstChild.nodeValue, subitems[5].firstChild.nodeValue,
                                                     subitems[6].firstChild.nodeValue, subitems[7].firstChild.nodeValue, subitems[8].firstChild.nodeValue,
                                                     subitems[9].firstChild.nodeValue, subitems[10].firstChild.nodeValue, subitems[11].firstChild.nodeValue))

            for i in range(len(DataList)):
                RenderText1.insert(INSERT, "[◈")
                RenderText1.insert(INSERT, DataList[i][0])
                RenderText1.insert(INSERT, "]\n\n")
                RenderText1.insert(INSERT, "- 필기시험 원서접수 : ")
                RenderText1.insert(INSERT, DataList[i][4])
                RenderText1.insert(INSERT, " ~ ")
                RenderText1.insert(INSERT, DataList[i][3])
                RenderText1.insert(INSERT, "\n\n")
                RenderText1.insert(INSERT, "- 필기시험 : ")
                RenderText1.insert(INSERT, DataList[i][1])
                RenderText1.insert(INSERT, "\n\n")
                RenderText1.insert(INSERT, "- 필기시험 합격예정자 발표 : ")
                RenderText1.insert(INSERT, DataList[i][2])
                RenderText1.insert(INSERT, "\n\n")
                RenderText1.insert(INSERT, "- 서류제출, 합격자결정 : ")
                RenderText1.insert(INSERT, DataList[i][6])
                RenderText1.insert(INSERT, " ~ ")
                RenderText1.insert(INSERT, DataList[i][5])
                RenderText1.insert(INSERT, "\n\n")
                RenderText1.insert(INSERT, "- 면접시험 원서접수 : ")
                RenderText1.insert(INSERT, DataList[i][11])
                RenderText1.insert(INSERT, " ~ ")
                RenderText1.insert(INSERT, DataList[i][10])
                RenderText1.insert(INSERT, "\n\n")
                RenderText1.insert(INSERT, "- 면접시험 : ")
                RenderText1.insert(INSERT, DataList[i][8])
                RenderText1.insert(INSERT, " ~ ")
                RenderText1.insert(INSERT, DataList[i][7])
                RenderText1.insert(INSERT, "\n\n")
                RenderText1.insert(INSERT, "- 합격자 발표 : ")
                RenderText1.insert(INSERT, DataList[i][9])
                RenderText1.insert(INSERT, "\n\n\n\n")

def Library2():
    import http.client
    from xml.dom.minidom import parse, parseString
    conn = http.client.HTTPConnection("openapi.q-net.or.kr")
    conn.request("GET", "/api/service/rest/InquiryTestInformationNTQSVC/getMCList?serviceKey=9LcIiucOT0tvSUSIbEKcxVWQ%2FVyM9FrhsCh6AylGkIj%2FR9sim%2B1cuz%2FIAXE%2BmrQwad9HgJBs%2B4sV2Pw8Y%2BMBrw%3D%3D")
    req = conn.getresponse()

    global DataList
    DataList.clear()

    if req.status == 200:
        BooksDoc = req.read().decode('utf-8')
        if BooksDoc == None:
            print("에러")
        else:
            parseData = parseString(BooksDoc)
            response = parseData.childNodes
            body = response[0].childNodes

            for search1 in body:
                if search1.nodeName == "body":
                    items = body[1].childNodes
                    for search2 in items:
                        if search2.nodeName == "items":
                            item = items[0].childNodes

                            for search3 in item:
                                if search3.nodeName == "item":
                                    subitems = search3.childNodes

                                    DataList.append((subitems[0].firstChild.nodeValue, subitems[1].firstChild.nodeValue, subitems[2].firstChild.nodeValue,
                                                     subitems[3].firstChild.nodeValue, subitems[4].firstChild.nodeValue, subitems[5].firstChild.nodeValue,
                                                     subitems[6].firstChild.nodeValue, subitems[7].firstChild.nodeValue, subitems[8].firstChild.nodeValue,
                                                     subitems[9].firstChild.nodeValue, subitems[10].firstChild.nodeValue, subitems[11].firstChild.nodeValue))

            for i in range(len(DataList)):
                RenderText1.insert(INSERT, "[◈")
                RenderText1.insert(INSERT, DataList[i][0])
                RenderText1.insert(INSERT, "]\n\n")
                RenderText1.insert(INSERT, "- 필기시험 원서접수 : ")
                RenderText1.insert(INSERT, DataList[i][4])
                RenderText1.insert(INSERT, " ~ ")
                RenderText1.insert(INSERT, DataList[i][3])
                RenderText1.insert(INSERT, "\n\n")
                RenderText1.insert(INSERT, "- 필기시험 : ")
                RenderText1.insert(INSERT, DataList[i][1])
                RenderText1.insert(INSERT, "\n\n")
                RenderText1.insert(INSERT, "- 필기시험 합격예정자 발표 : ")
                RenderText1.insert(INSERT, DataList[i][2])
                RenderText1.insert(INSERT, "\n\n")
                RenderText1.insert(INSERT, "- 서류제출, 합격자결정 : ")
                RenderText1.insert(INSERT, DataList[i][6])
                RenderText1.insert(INSERT, " ~ ")
                RenderText1.insert(INSERT, DataList[i][5])
                RenderText1.insert(INSERT, "\n\n")
                RenderText1.insert(INSERT, "- 실기시험 원서접수 : ")
                RenderText1.insert(INSERT, DataList[i][11])
                RenderText1.insert(INSERT, " ~ ")
                RenderText1.insert(INSERT, DataList[i][10])
                RenderText1.insert(INSERT, "\n\n")
                RenderText1.insert(INSERT, "- 실기시험 : ")
                RenderText1.insert(INSERT, DataList[i][8])
                RenderText1.insert(INSERT, " ~ ")
                RenderText1.insert(INSERT, DataList[i][7])
                RenderText1.insert(INSERT, "\n\n")
                RenderText1.insert(INSERT, "- 합격자 발표 : ")
                RenderText1.insert(INSERT, DataList[i][9])
                RenderText1.insert(INSERT, "\n\n\n\n")

def Library3():
    import http.client
    from xml.dom.minidom import parse, parseString
    conn = http.client.HTTPConnection("openapi.q-net.or.kr")
    conn.request("GET", "/api/service/rest/InquiryTestInformationNTQSVC/getEList?serviceKey=9LcIiucOT0tvSUSIbEKcxVWQ%2FVyM9FrhsCh6AylGkIj%2FR9sim%2B1cuz%2FIAXE%2BmrQwad9HgJBs%2B4sV2Pw8Y%2BMBrw%3D%3D")
    req = conn.getresponse()

    global DataList
    DataList.clear()

    if req.status == 200:
        BooksDoc = req.read().decode('utf-8')
        if BooksDoc == None:
            print("에러")
        else:
            parseData = parseString(BooksDoc)
            response = parseData.childNodes
            body = response[0].childNodes

            for search1 in body:
                if search1.nodeName == "body":
                    items = body[1].childNodes
                    for search2 in items:
                        if search2.nodeName == "items":
                            item = items[0].childNodes

                            for search3 in item:
                                if search3.nodeName == "item":
                                    subitems = search3.childNodes

                                    DataList.append((subitems[0].firstChild.nodeValue, subitems[1].firstChild.nodeValue, subitems[2].firstChild.nodeValue,
                                                     subitems[3].firstChild.nodeValue, subitems[4].firstChild.nodeValue, subitems[5].firstChild.nodeValue,
                                                     subitems[6].firstChild.nodeValue, subitems[7].firstChild.nodeValue, subitems[8].firstChild.nodeValue,
                                                     subitems[9].firstChild.nodeValue, subitems[10].firstChild.nodeValue, subitems[11].firstChild.nodeValue))

            for i in range(len(DataList)):
                RenderText1.insert(INSERT, "[◈")
                RenderText1.insert(INSERT, DataList[i][0])
                RenderText1.insert(INSERT, "]\n\n")
                RenderText1.insert(INSERT, "- 필기시험 원서접수 : ")
                RenderText1.insert(INSERT, DataList[i][4])
                RenderText1.insert(INSERT, " ~ ")
                RenderText1.insert(INSERT, DataList[i][3])
                RenderText1.insert(INSERT, "\n\n")
                RenderText1.insert(INSERT, "- 필기시험 : ")
                RenderText1.insert(INSERT, DataList[i][1])
                RenderText1.insert(INSERT, "\n\n")
                RenderText1.insert(INSERT, "- 필기시험 합격예정자 발표 : ")
                RenderText1.insert(INSERT, DataList[i][2])
                RenderText1.insert(INSERT, "\n\n")
                RenderText1.insert(INSERT, "- 서류제출, 합격자결정 : ")
                RenderText1.insert(INSERT, DataList[i][6])
                RenderText1.insert(INSERT, " ~ ")
                RenderText1.insert(INSERT, DataList[i][5])
                RenderText1.insert(INSERT, "\n\n")
                RenderText1.insert(INSERT, "- 실기시험 원서접수 : ")
                RenderText1.insert(INSERT, DataList[i][11])
                RenderText1.insert(INSERT, " ~ ")
                RenderText1.insert(INSERT, DataList[i][10])
                RenderText1.insert(INSERT, "\n\n")
                RenderText1.insert(INSERT, "- 실기시험 : ")
                RenderText1.insert(INSERT, DataList[i][8])
                RenderText1.insert(INSERT, " ~ ")
                RenderText1.insert(INSERT, DataList[i][7])
                RenderText1.insert(INSERT, "\n\n")
                RenderText1.insert(INSERT, "- 합격자 발표 : ")
                RenderText1.insert(INSERT, DataList[i][9])
                RenderText1.insert(INSERT, "\n\n\n\n")

def Library4():
    import http.client
    from xml.dom.minidom import parse, parseString
    conn = http.client.HTTPConnection("openapi.q-net.or.kr")
    conn.request("GET", "/api/service/rest/InquiryTestInformationNTQSVC/getCList?serviceKey=9LcIiucOT0tvSUSIbEKcxVWQ%2FVyM9FrhsCh6AylGkIj%2FR9sim%2B1cuz%2FIAXE%2BmrQwad9HgJBs%2B4sV2Pw8Y%2BMBrw%3D%3D")
    req = conn.getresponse()

    global DataList
    DataList.clear()

    if req.status == 200:
        BooksDoc = req.read().decode('utf-8')
        if BooksDoc == None:
            print("에러")
        else:
            parseData = parseString(BooksDoc)
            response = parseData.childNodes
            body = response[0].childNodes

            for search1 in body:
                if search1.nodeName == "body":
                    items = body[1].childNodes
                    for search2 in items:
                        if search2.nodeName == "items":
                            item = items[0].childNodes

                            for search3 in item:
                                if search3.nodeName == "item":
                                    subitems = search3.childNodes
                                    if subitems[1].firstChild.nodeValue == "XXXXXXXX":
                                        continue
                                    elif subitems[2].firstChild.nodeValue == "XXXXXXXX":
                                        continue
                                    elif subitems[3].firstChild.nodeValue == "XXXXXXXX":
                                        continue
                                    elif subitems[1].firstChild.nodeValue == "20170611":
                                        continue
                                    else:
                                        DataList.append((subitems[0].firstChild.nodeValue, subitems[1].firstChild.nodeValue, subitems[2].firstChild.nodeValue,
                                                         subitems[3].firstChild.nodeValue, subitems[4].firstChild.nodeValue, subitems[5].firstChild.nodeValue,
                                                         subitems[6].firstChild.nodeValue, subitems[7].firstChild.nodeValue, subitems[8].firstChild.nodeValue,
                                                         subitems[9].firstChild.nodeValue))

            for i in range(len(DataList)):
                RenderText1.insert(INSERT, "[◈")
                RenderText1.insert(INSERT, DataList[i][0])
                RenderText1.insert(INSERT, "]\n\n")
                RenderText1.insert(INSERT, "- 필기시험 원서접수 : ")
                RenderText1.insert(INSERT, DataList[i][4])
                RenderText1.insert(INSERT, " ~ ")
                RenderText1.insert(INSERT, DataList[i][3])
                RenderText1.insert(INSERT, "\n\n")
                RenderText1.insert(INSERT, "- 필기시험 : ")
                RenderText1.insert(INSERT, DataList[i][1])
                RenderText1.insert(INSERT, "\n\n")
                RenderText1.insert(INSERT, "- 필기시험 합격예정자 발표 : ")

                if DataList[i][1] == DataList[i][2]:
                    RenderText1.insert(INSERT, "시행당일")
                else:
                    RenderText1.insert(INSERT, DataList[i][2])

                RenderText1.insert(INSERT, "\n\n- 실기시험 원서접수 : ")
                RenderText1.insert(INSERT, DataList[i][9])
                RenderText1.insert(INSERT, " ~ ")
                RenderText1.insert(INSERT, DataList[i][8])
                RenderText1.insert(INSERT, "\n\n")
                RenderText1.insert(INSERT, "- 실기시험 : ")
                RenderText1.insert(INSERT, DataList[i][6])
                RenderText1.insert(INSERT, " ~ ")
                RenderText1.insert(INSERT, DataList[i][5])
                RenderText1.insert(INSERT, "\n\n")
                RenderText1.insert(INSERT, "- 합격자 발표 : ")
                RenderText1.insert(INSERT, DataList[i][7])
                RenderText1.insert(INSERT, "\n\n\n\n")

def InitRenderText1():
    global RenderText1
    RenderText1=Text(frame1, width=52, height=27, relief='ridge', borderwidth=1)
    RenderText1.place(x=315, y=10)
    RenderText1.configure(state='normal')




#Frame2

def InitOrder():
    global Order
    Order = IntVar()
    ascending = ttk.Radiobutton(frame2, text="오름차순", variable=Order, value=1, command=OrderAction)
    desending = ttk.Radiobutton(frame2, text="내림차순", variable=Order, value=2, command=OrderAction)
    ascending.place(x=145, y=170)
    desending.place(x=145, y=190)

def OrderAction():
    if Order.get() == 1:
        SearchListBox.delete(0, END)
        SearchListBox.insert(1, "건설기계운전")
        SearchListBox.insert(2, "건설배관")
        SearchListBox.insert(3, "건축")
        SearchListBox.insert(4, "경비.청소")
        SearchListBox.insert(5, "경영")
        SearchListBox.insert(6, "금속.재료")
        SearchListBox.insert(7, "금형.공작기계")
        SearchListBox.insert(8, "기계장비설비.설치")
        SearchListBox.insert(9, "기계제작")
        SearchListBox.insert(10, "농업")
        SearchListBox.insert(11, "단조.주조")
        SearchListBox.insert(12, "도시.교통")
        SearchListBox.insert(13, "도장.도금")
        SearchListBox.insert(14, "디자인")
        SearchListBox.insert(15, "목재.가구.공예")
        SearchListBox.insert(16, "방송")
        SearchListBox.insert(17, "방송.무선")
        SearchListBox.insert(18, "보건.의료")
        SearchListBox.insert(19, "비파괴검사")
        SearchListBox.insert(20, "사무")
        SearchListBox.insert(21, "사회복지.종교")
        SearchListBox.insert(22, "생산관리")
        SearchListBox.insert(23, "섬유")
        SearchListBox.insert(24, "숙박.여행.오락.스포츠")
        SearchListBox.insert(25, "식품")
        SearchListBox.insert(26, "안전관리")
        SearchListBox.insert(27, "어업")
        SearchListBox.insert(28, "에너지.기상")
        SearchListBox.insert(29, "영업.판매")
        SearchListBox.insert(30, "용접")
        SearchListBox.insert(31, "운전.운송")
        SearchListBox.insert(32, "위험물")
        SearchListBox.insert(33, "의복")
        SearchListBox.insert(34, "이용.미용")
        SearchListBox.insert(35, "인쇄.사진")
        SearchListBox.insert(36, "임업")
        SearchListBox.insert(37, "자동차")
        SearchListBox.insert(38, "전기")
        SearchListBox.insert(39, "전자")
        SearchListBox.insert(40, "정보기술")
        SearchListBox.insert(41, "제과.제빵")
        SearchListBox.insert(42, "조경")
        SearchListBox.insert(43, "조리")
        SearchListBox.insert(44, "조선")
        SearchListBox.insert(45, "채광")
        SearchListBox.insert(46, "철도")
        SearchListBox.insert(47, "축산")
        SearchListBox.insert(48, "토목")
        SearchListBox.insert(49, "통신")
        SearchListBox.insert(50, "판금.제관.새시")
        SearchListBox.insert(51, "항공")
        SearchListBox.insert(52, "화공")
        SearchListBox.insert(53, "환경")

    if Order.get() == 2:
        SearchListBox.delete(0, END)
        SearchListBox.insert(1, "환경")
        SearchListBox.insert(2, "화공")
        SearchListBox.insert(3, "항공")
        SearchListBox.insert(4, "판금.제관.새시")
        SearchListBox.insert(5, "통신")
        SearchListBox.insert(6, "토목")
        SearchListBox.insert(7, "축산")
        SearchListBox.insert(8, "철도")
        SearchListBox.insert(9, "채광")
        SearchListBox.insert(10, "조선")
        SearchListBox.insert(11, "조리")
        SearchListBox.insert(12, "조경")
        SearchListBox.insert(13, "제과.제빵")
        SearchListBox.insert(14, "정보기술")
        SearchListBox.insert(15, "전자")
        SearchListBox.insert(16, "전기")
        SearchListBox.insert(17, "자동차")
        SearchListBox.insert(18, "임업")
        SearchListBox.insert(19, "인쇄.사진")
        SearchListBox.insert(20, "이용.미용")
        SearchListBox.insert(21, "의복")
        SearchListBox.insert(22, "위험물")
        SearchListBox.insert(23, "운전.운송")
        SearchListBox.insert(24, "용접")
        SearchListBox.insert(25, "영업.판매")
        SearchListBox.insert(26, "에너지.기상")
        SearchListBox.insert(27, "어업")
        SearchListBox.insert(28, "안전관리")
        SearchListBox.insert(29, "식품")
        SearchListBox.insert(30, "숙박.여행.오락.스포츠")
        SearchListBox.insert(31, "섬유")
        SearchListBox.insert(32, "생산관리")
        SearchListBox.insert(33, "사회복지.종교")
        SearchListBox.insert(34, "사무")
        SearchListBox.insert(35, "비파괴검사")
        SearchListBox.insert(36, "보건.의료")
        SearchListBox.insert(37, "방송.무선")
        SearchListBox.insert(38, "방송")
        SearchListBox.insert(39, "목재.가구.공예")
        SearchListBox.insert(40, "디자인")
        SearchListBox.insert(41, "도장.도금")
        SearchListBox.insert(42, "도시.교통")
        SearchListBox.insert(43, "단조.주조")
        SearchListBox.insert(44, "농업")
        SearchListBox.insert(45, "기계제작")
        SearchListBox.insert(46, "기계장비설비.설치")
        SearchListBox.insert(47, "금형.공작기계")
        SearchListBox.insert(48, "금속.재료")
        SearchListBox.insert(49, "경영")
        SearchListBox.insert(50, "경비.청소")
        SearchListBox.insert(51, "건축")
        SearchListBox.insert(52, "건설배관")
        SearchListBox.insert(53, "건설기계운전")

def InitListBox():
    global SearchListBox
    ListBoxScrollbar = Scrollbar(frame2)
    ListBoxScrollbar.pack()
    ListBoxScrollbar.place(x=136, y=45)

    SearchListBox = Listbox(frame2, width=18, height=15, yscrollcommand = ListBoxScrollbar.set)
    SearchListBox.insert(1, "건설기계운전")
    SearchListBox.insert(2, "건설배관")
    SearchListBox.insert(3, "건축")
    SearchListBox.insert(4, "경비.청소")
    SearchListBox.insert(5, "경영")
    SearchListBox.insert(6, "금속.재료")
    SearchListBox.insert(7, "금형.공작기계")
    SearchListBox.insert(8, "기계장비설비.설치")
    SearchListBox.insert(9, "기계제작")
    SearchListBox.insert(10, "농업")
    SearchListBox.insert(11, "단조.주조")
    SearchListBox.insert(12, "도시.교통")
    SearchListBox.insert(13, "도장.도금")
    SearchListBox.insert(14, "디자인")
    SearchListBox.insert(15, "목재.가구.공예")
    SearchListBox.insert(16, "방송")
    SearchListBox.insert(17, "방송.무선")
    SearchListBox.insert(18, "보건.의료")
    SearchListBox.insert(19, "비파괴검사")
    SearchListBox.insert(20, "사무")
    SearchListBox.insert(21, "사회복지.종교")
    SearchListBox.insert(22, "생산관리")
    SearchListBox.insert(23, "섬유")
    SearchListBox.insert(24, "숙박.여행.오락.스포츠")
    SearchListBox.insert(25, "식품")
    SearchListBox.insert(26, "안전관리")
    SearchListBox.insert(27, "어업")
    SearchListBox.insert(28, "에너지.기상")
    SearchListBox.insert(29, "영업.판매")
    SearchListBox.insert(30, "용접")
    SearchListBox.insert(31, "운전.운송")
    SearchListBox.insert(32, "위험물")
    SearchListBox.insert(33, "의복")
    SearchListBox.insert(34, "이용.미용")
    SearchListBox.insert(35, "인쇄.사진")
    SearchListBox.insert(36, "임업")
    SearchListBox.insert(37, "자동차")
    SearchListBox.insert(38, "전기")
    SearchListBox.insert(39, "전자")
    SearchListBox.insert(40, "정보기술")
    SearchListBox.insert(41, "제과.제빵")
    SearchListBox.insert(42, "조경")
    SearchListBox.insert(43, "조리")
    SearchListBox.insert(44, "조선")
    SearchListBox.insert(45, "채광")
    SearchListBox.insert(46, "철도")
    SearchListBox.insert(47, "축산")
    SearchListBox.insert(48, "토목")
    SearchListBox.insert(49, "통신")
    SearchListBox.insert(50, "판금.제관.새시")
    SearchListBox.insert(51, "항공")
    SearchListBox.insert(52, "화공")
    SearchListBox.insert(53, "환경")
    SearchListBox.pack()
    SearchListBox.place(x=5, y=50)

    ListBoxScrollbar.config(command=SearchListBox.yview)

def InitTopText():
    MainText2 = Label(frame2, text = "시행종목명")
    MainText2.pack()
    MainText2.place(x=365, y=10)


def InitSearchText():
    global InputLabel
    InputLabel = Entry(frame2, width = 26, relief = 'ridge', bg='lightgray')
    InputLabel.place(x=435, y=10)

def InitSearch2():
    Search2 = Button(frame2, text="Enter", command=Search2Action)
    Search2.place(x=150, y=53, width=70, height=110)

    Search3 = Button(frame2, text="Search", command=Library5)
    Search3.pack()
    Search3.place(x=630, y=6)

def Search2Action():
    SearchListBoxIndex = str(SearchListBox.get(ACTIVE))

    RenderText2.configure(state='normal')
    RenderText2.delete(0.0, END)
    addressBox2.configure(state='normal')
    import http.client
    from xml.dom.minidom import parse, parseString
    conn = http.client.HTTPConnection("openapi.q-net.or.kr")
    conn.request("GET",
                 "/api/service/rest/InquiryListNationalQualifcationSVC/getList?serviceKey=9LcIiucOT0tvSUSIbEKcxVWQ%2FVyM9FrhsCh6AylGkIj%2FR9sim%2B1cuz%2FIAXE%2BmrQwad9HgJBs%2B4sV2Pw8Y%2BMBrw%3D%3D")
    req = conn.getresponse()

    global DataList
    DataList.clear()

    if req.status == 200:
        BooksDoc = req.read().decode('utf-8')
        if BooksDoc == None:
            print("에러")
        else:
            parseData = parseString(BooksDoc)
            response = parseData.childNodes
            body = response[0].childNodes

            for search1 in body:
                if search1.nodeName == "body":
                    items = body[1].childNodes
                    for search2 in items:
                        if search2.nodeName == "items":
                            item = items[0].childNodes

                            for search3 in item:
                                if search3.nodeName == "item":
                                    subitems = search3.childNodes

                                    if subitems[3].firstChild.nodeValue == SearchListBoxIndex:
                                        pass
                                    else:
                                        continue

                                    DataList.append((subitems[1].firstChild.nodeValue, subitems[7].firstChild.nodeValue,
                                                     subitems[3].firstChild.nodeValue))

            for i in range(len(DataList)):
                RenderText2.insert(INSERT, "· ")
                RenderText2.insert(INSERT, DataList[i][0])
                RenderText2.insert(INSERT, "")
                RenderText2.insert(INSERT, "\n\n")

            import spam
            linecnt = spam.linecnt(RenderText2.get(0.0, END))

            RenderText2.insert(INSERT, "                               [총 ")
            RenderText2.insert(INSERT, linecnt-1)
            RenderText2.insert(INSERT, "개]\n\n\n- 자격증별 상세내용은 검색을 활용하세요 -")

def Library5():
    import http.client
    from xml.dom.minidom import parse, parseString
    conn = http.client.HTTPConnection("openapi.q-net.or.kr")
    conn.request("GET", "/api/service/rest/InquiryListNationalQualifcationSVC/getList?serviceKey=9LcIiucOT0tvSUSIbEKcxVWQ%2FVyM9FrhsCh6AylGkIj%2FR9sim%2B1cuz%2FIAXE%2BmrQwad9HgJBs%2B4sV2Pw8Y%2BMBrw%3D%3D")
    req = conn.getresponse()

    global DataList
    global jmCd

    DataList.clear()

    if req.status == 200:
        BooksDoc = req.read().decode('utf-8')
        if BooksDoc == None:
            print("에러")
        else:
            parseData = parseString(BooksDoc)
            response = parseData.childNodes
            body = response[0].childNodes

            for search1 in body:
                if search1.nodeName == "body":
                    items = body[1].childNodes
                    for search2 in items:
                        if search2.nodeName == "items":
                            item = items[0].childNodes

                            for search3 in item:
                                if search3.nodeName == "item":
                                    subitems = search3.childNodes

                                    if subitems[1].firstChild.nodeValue == InputLabel.get():
                                        jmCd = str(subitems[0].firstChild.nodeValue)
                                        Library5Action()
                                    else:
                                        continue

def Library5Action():
    RenderText2.configure(state='normal')
    RenderText2.delete(0.0, END)
    addressBox2.configure(state='normal')
    import http.client
    from xml.dom.minidom import parse, parseString
    conn = http.client.HTTPConnection("openapi.q-net.or.kr")
    conn.request("GET", "/api/service/rest/InquiryTestInformationNTQSVC/getJMList?serviceKey=9LcIiucOT0tvSUSIbEKcxVWQ%2FVyM9FrhsCh6AylGkIj%2FR9sim%2B1cuz%2FIAXE%2BmrQwad9HgJBs%2B4sV2Pw8Y%2BMBrw%3D%3D&jmCd="+jmCd)
    req = conn.getresponse()

    DataList.clear()

    if req.status == 200:
        BooksDoc = req.read().decode('utf-8')
        if BooksDoc == None:
            print("에러")
        else:
            parseData = parseString(BooksDoc)
            response = parseData.childNodes
            body = response[0].childNodes

            for search1 in body:
                if search1.nodeName == "body":
                    items = body[1].childNodes
                    for search2 in items:
                        if search2.nodeName == "items":
                            item = items[0].childNodes

                            for search3 in item:
                                if search3.nodeName == "item":
                                    subitems = search3.childNodes
                                    if subitems[5].nodeName == "docSubmitEndDt":
                                        DataList.append((subitems[0].firstChild.nodeValue, subitems[1].firstChild.nodeValue, subitems[2].firstChild.nodeValue,
                                                         subitems[3].firstChild.nodeValue, subitems[4].firstChild.nodeValue, subitems[7].firstChild.nodeValue,
                                                         subitems[8].firstChild.nodeValue, subitems[10].firstChild.nodeValue, subitems[13].firstChild.nodeValue,
                                                         subitems[14].firstChild.nodeValue, subitems[15].firstChild.nodeValue, subitems[16].firstChild.nodeValue,
                                                         subitems[17].firstChild.nodeValue, subitems[18].firstChild.nodeValue))
                                    else:
                                        DataList.append((subitems[0].firstChild.nodeValue, subitems[1].firstChild.nodeValue, subitems[2].firstChild.nodeValue,
                                                         subitems[3].firstChild.nodeValue,subitems[4].firstChild.nodeValue,subitems[5].firstChild.nodeValue,
                                                         subitems[6].firstChild.nodeValue,subitems[8].firstChild.nodeValue,subitems[11].firstChild.nodeValue,
                                                         subitems[12].firstChild.nodeValue,subitems[13].firstChild.nodeValue,subitems[14].firstChild.nodeValue,
                                                         subitems[15].firstChild.nodeValue,subitems[16].firstChild.nodeValue))


            for i in range(len(DataList)):
                if i == 0:
                    RenderText2.insert(INSERT, DataList[i][6])
                    RenderText2.insert(INSERT, " (")
                    RenderText2.insert(INSERT, DataList[i][7])
                    RenderText2.insert(INSERT, ")\n\n")
                    RenderText2.insert(INSERT, " ㄱ.시험일정\n\n")
                RenderText2.insert(INSERT, "       |     구분     | ")
                RenderText2.insert(INSERT, DataList[i][5])
                RenderText2.insert(INSERT, " |\n")
                RenderText2.insert(INSERT, "       | 필기원서접수 | ")
                RenderText2.insert(INSERT, DataList[i][4])
                RenderText2.insert(INSERT, " ~ ")
                RenderText2.insert(INSERT, DataList[i][3])
                RenderText2.insert(INSERT, "  |\n       |   필기시험   | ")
                RenderText2.insert(INSERT, DataList[i][1])
                if DataList[i][1] != DataList[i][0]:
                    RenderText2.insert(INSERT, " ~ ")
                    RenderText2.insert(INSERT, DataList[i][0])
                    RenderText2.insert(INSERT, "  |\n       |필기합격자발표| ")
                else:
                    RenderText2.insert(INSERT, "             |\n       |필기합격자발표| ")
                if DataList[i][2] == DataList[i][1]:
                    RenderText2.insert(INSERT, "시행당일")
                else:
                    RenderText2.insert(INSERT, DataList[i][2])
                RenderText2.insert(INSERT, "             |\n       | 실기원서접수 | ")
                RenderText2.insert(INSERT, DataList[i][13])
                RenderText2.insert(INSERT, " ~ ")
                RenderText2.insert(INSERT, DataList[i][12])
                RenderText2.insert(INSERT, "  |\n       |   실기시험   | ")
                RenderText2.insert(INSERT, DataList[i][9])
                RenderText2.insert(INSERT, " ~ ")
                RenderText2.insert(INSERT, DataList[i][8])
                RenderText2.insert(INSERT, "  |\n\n\n\n")

            Library5Action_continue()

def Library5Action_continue():
    import http.client
    from xml.dom.minidom import parse, parseString
    conn = http.client.HTTPConnection("openapi.q-net.or.kr")
    conn.request("GET", "/api/service/rest/InquiryTestInformationNTQSVC/getFeeList?serviceKey=9LcIiucOT0tvSUSIbEKcxVWQ%2FVyM9FrhsCh6AylGkIj%2FR9sim%2B1cuz%2FIAXE%2BmrQwad9HgJBs%2B4sV2Pw8Y%2BMBrw%3D%3D&jmCd="+jmCd)
    req = conn.getresponse()

    DataList.clear()

    if req.status == 200:
        BooksDoc = req.read().decode('utf-8')
        if BooksDoc == None:
            print("에러")
        else:
            parseData = parseString(BooksDoc)
            response = parseData.childNodes
            body = response[0].childNodes

            for search1 in body:
                if search1.nodeName == "body":
                    items = body[1].childNodes
                    for search2 in items:
                        if search2.nodeName == "items":
                            item = items[0].childNodes

                            for search3 in item:
                                if search3.nodeName == "item":
                                    subitems = search3.childNodes

                                    DataList.append((subitems[0].firstChild.nodeValue, subitems[1].firstChild.nodeValue, subitems[2].firstChild.nodeValue))


            for i in range(len(DataList)):
                RenderText2.insert(INSERT, "\n ㄴ.")
                RenderText2.insert(INSERT, DataList[i][1])
                RenderText2.insert(INSERT, "\n        ")
                RenderText2.insert(INSERT, DataList[i][0])
                RenderText2.insert(INSERT, "\n\n")

            Library5Action_continue2()


def Library5Action_continue2():
    import http.client
    from xml.dom.minidom import parse, parseString
    conn = http.client.HTTPConnection("openapi.q-net.or.kr")
    conn.request("GET", "/api/service/rest/InquiryInformationTradeNTQSVC/getList?serviceKey=9LcIiucOT0tvSUSIbEKcxVWQ%2FVyM9FrhsCh6AylGkIj%2FR9sim%2B1cuz%2FIAXE%2BmrQwad9HgJBs%2B4sV2Pw8Y%2BMBrw%3D%3D&jmCd="+jmCd)
    req = conn.getresponse()

    DataList.clear()

    if req.status == 200:
        BooksDoc = req.read().decode('utf-8')
        if BooksDoc == None:
            print("에러")
        else:
            parseData = parseString(BooksDoc)
            response = parseData.childNodes
            body = response[0].childNodes

            for search1 in body:
                if search1.nodeName == "body":
                    items = body[1].childNodes
                    for search2 in items:
                        if search2.nodeName == "items":
                            item = items[0].childNodes

                            for search3 in item:
                                if search3.nodeName == "item":
                                    subitems = search3.childNodes

                                    DataList.append((subitems[0].firstChild.nodeValue, subitems[1].firstChild.nodeValue, subitems[2].firstChild.nodeValue))


            #for i in range(len(DataList)):
            RenderText2.insert(INSERT, "\n\n\n ㄷ.")
            RenderText2.insert(INSERT, DataList[0][1])
            RenderText2.insert(INSERT, "\n\n        ")
            RenderText2.insert(INSERT, DataList[0][0])
            RenderText2.insert(INSERT, "\n\n\n")
            RenderText2.insert(INSERT, "\n\n ㄹ.")
            RenderText2.insert(INSERT, DataList[1][1])
            RenderText2.insert(INSERT, "\n\n        ")
            RenderText2.insert(INSERT, DataList[1][0])
            RenderText2.insert(INSERT, "\n\n\n")
            RenderText2.insert(INSERT, "\n\n ㅁ.")
            RenderText2.insert(INSERT, DataList[2][1])
            RenderText2.insert(INSERT, "\n\n        ")
            RenderText2.insert(INSERT, DataList[2][0])
            RenderText2.insert(INSERT, "\n\n\n")


def InitRenderText2():
    global RenderText2
    RenderText2=Text(frame2, width=52, height=24, relief='ridge', borderwidth=1)
    RenderText2.place(x=315, y=50)
    RenderText2.configure(state='normal')

def InitSendMail():
    global addressBox, addressBox2

    mailText = Label(frame1, text="※ E-mail 보내기")
    mailText.place(x=21, y=230)

    addressBox=Entry(frame1, width = 26, relief = 'ridge')
    addressBox.place(x=23, y=260)
    addressBox.configure(state='disable')

    sendMailButton = Button(frame1, text="메일 전송", command = sendMail)
    sendMailButton.pack()
    sendMailButton.place(x=220, y=255)

    ################################################################

    mailText2 = Label(frame2, text="※ E-mail 보내기")
    mailText2.place(x=15, y=300)

    addressBox2=Entry(frame2, width = 26, relief = 'ridge')
    addressBox2.place(x=17, y=330)
    addressBox2.configure(state='disable')

    sendMailButton2 = Button(frame2, text="메일 전송", command = sendMail2)
    sendMailButton2.pack()
    sendMailButton2.place(x=214, y=325)


def sendMail():
    import mimetypes
    import smtplib
    from email.mime.base import MIMEBase
    from email.mime.text import MIMEText

    host = "smtp.gmail.com"
    port = "587"

    msg = MIMEBase("multipart", "alternative")

    msgtext = RenderText1.get(0.0, END)
    senderAddr = "ssunine21@gmail.com"
    recipientAddr = "xcvbnm757@naver.com"

    msg['Subject'] = "국가기술자격증 상세 안내"
    msg['From'] = senderAddr
    msg['To'] = recipientAddr

    msgPart = MIMEText(msgtext, 'plain')
    msg.attach(msgPart)

    s = smtplib.SMTP(host, port)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login("ssunine21@gmail.com", "a786s156!@#")
    s.sendmail(senderAddr, [recipientAddr], msg.as_string())
    s.close()

def sendMail2():
    import mimetypes
    import smtplib
    from email.mime.base import MIMEBase
    from email.mime.text import MIMEText

    host = "smtp.gmail.com"
    port = "587"

    msg = MIMEBase("multipart", "alternative")

    msgtext = RenderText2.get(0.0, END)
    senderAddr = "ssunine21@gmail.com"
    recipientAddr = "xcvbnm757@naver.com"

    msg['Subject'] = "국가기술자격증 상세 안내"
    msg['From'] = senderAddr
    msg['To'] = recipientAddr

    msgPart = MIMEText(msgtext, 'plain')
    msg.attach(msgPart)

    s = smtplib.SMTP(host, port)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login("ssunine21@gmail.com", "a786s156!@#")
    s.sendmail(senderAddr, [recipientAddr], msg.as_string())
    s.close()



#Frame1
InitTab()
InitRadio()
InitSearch1()
InitRenderText1()
InitSendMail()

#Frame2
InitOrder()
InitListBox()
InitTopText()
InitSearchText()
InitSearch2()
InitRenderText2()

m_TK.mainloop()
