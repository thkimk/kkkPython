## pip install ipython
## ipython 실행후, run test01.py

print("hello world");


# 리스트 데이터 생성
from faker import Faker

fake = Faker("ko_KR")
fakeName = [fake.name() for i in range(3)]
fakeMail = [fake.email() for i in range(3)]
fakePhone = [fake.phone_number() for i in range(3)]
print("## kkk: fake: ", type(fake))
print("## kkk: fakeName: ", type(fakeName))

# (1) 딕셔너리 형태로 key값과 리스트 변수를 선택하면서 데이터프레임 만들기
import pandas as pd

name = ['박영철', '심영미', '황주원']
phone = ['042-400-9479', '016-335-6830', '062-642-3039']
mail = ['ygim@hotmail.com','gimsujin@baghan.kr','jiweongu@gimi.com']

df1 = pd.DataFrame({"name":name, "phone":phone, "mail":mail})
print("## kkk: df1: ", type(df1))
print("## kkk: df1: \n", df1)

# (2) 리스트 형태로 데이터프레임 만들기
data2 = [['AMY', 13, 'girl'], 
            ['BEN', 13, 'boy'],
            ['EVA', 14,  'girl'], 
            ['KIM', 14,  'girl'], 
            ['NEO', 14, 'boy']]

df2 = pd.DataFrame(data2, columns=['Name', 'Age', 'Sex'])
print("## kkk: df1: ", type(df2))
print("## kkk: df1: \n", df2)

# (3) 딕셔너리(json) 형태로 데이터프레임 만들기
data3 = {'Name': ['AMY', 'BEN', 'EVE', 'KIM', 'NEO'], 
           'Age': [13, 13, 14, 14, 14], 
           'Sex': [ 'girl',  'boy', 'girl', 'girl', 'boy']}

df3 = pd.DataFrame(data3)
print("## kkk: df1: ", type(df3))
print("## kkk: df1: \n", df3)


# 결국 데이터프레임은 리스트 오프 클래스, 즉 List<Class> 와 유사한 형태임
# 그리고 딕셔너리라는 용어를 많이 사용하는데, 딕셔너리는 json 형태를 띈 구조체를 말함
# 데이터프레임에서 데이터에 접근하는 방법들
# d1 = df1.loc[:, ['Name', 'Type']]
print("## kkk: d1: \n", df1.loc[:, ['name', 'mail']])
print("## kkk: d2: \n", df1.iloc[:, [0, 2]])
print("## kkk: d3: \n", df1.loc[0])     # loc는 인덱스 기준으로 조회
print("## kkk: d4: \n", df1.iloc[0])    # iloc는 행번호 기준으로 조회

for row1 in df1:
    print("## kkk: row1", type(row1))
    print("## kkk: row1", row1)

