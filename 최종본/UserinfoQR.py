import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, NumericProperty, StringProperty

import qrcode
import os


#-*-coding: utf-8-*-                                                                #한글입력 받으려면 utf-8-


info = []               #QR코드로 띄울 정보들 저장할 행렬

#사용자 정보 초기화
surname = ''
years = ''
symp = ''

kivy.require('1.11.1')


#ContentArea로 선언된 박스레이아웃 불러오기

class ContentArea(BoxLayout):
    
    #입력창에서 정보 받아오기
    name_text_input = ObjectProperty()
    ego = NumericProperty(0)
    surname = StringProperty('')
    
    age_text_input = ObjectProperty()
    ego = NumericProperty(0)
    years = StringProperty('')
    
    symptom_text_input = ObjectProperty()
    ego = NumericProperty(0)
    symp = StringProperty('')

    #Save버튼을 누르면 실행할 함수 (변수 txt파일저장, QR코드 생성)
    def submit_surname(self):
        
        self.surname = self.name_text_input.text
        print("Assign surname: {}".format(self.surname))
        self.save()
        
        
        self.years = self.age_text_input.text
        print("Assign age: {}".format(self.years))
        self.save()
        
        
        self.symp = self.symptom_text_input.text
        print("Assign symptom: {}".format(self.symp))
        self.save()
        
        
        na = '이름 : ' + str(self.surname)
        ye = '나이 : ' + str(self.years)
        sy = '특이사항 : ' + str(self.symp)
        
        info.append(na)
        info.append(ye)
        info.append(sy)
        
        print(info)

        QR = qrcode.make(info)
        QR.save("C:/Users/kimbumjoon/Desktop/Python/programming/제개설/jgs/최종본/사용자정보_QR.png")
        
    
    
    def save(self):
        
        os.system('cls')
        
        with open("C:/Users/kimbumjoon/Desktop/Python/programming/제개설/jgs/최종본/surname.txt", "w") as fobj:
            writeuser = str(self.surname)+str(self.years)+str(self.symp)
            # print('writeuser:',writeuser)
            
            fobj.write(writeuser)
            
            
    pass

class Upper_bar(BoxLayout):
    pass



#test.kv와 함께 실행될 메인 App부분
class UserInfoQRApp(App):
    pass


#TestApp부분 실행
if __name__ == '__main__':
    UserInfoQRApp().run()
