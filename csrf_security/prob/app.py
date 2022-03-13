from flask import Flask, render_template, request, redirect, session, url_for
from flask_sqlalchemy import SQLAlchemy
from user_model import User

app = Flask(__name__)

app.secret_key="123123123"

# database 설정파일
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@localhost:3306/testdb"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

@app.route('/')
def home():
	#로그인 세션정보('userid')가 있을 경우
	if not session.get('userid'):  
		return render_template('home.html')
	
	#로그인 세션정보가 없을 경우
	else:		
		userid = session.get('userid') 
		return render_template('home.html', userid=userid)

@app.route('/register', methods=['GET','POST'])
def register():
	if request.method =='GET':
		return render_template("register.html")
	else:
		userid = request.form.get('userid')
		username = request.form.get('username')
		password = request.form.get('password')
		re_password = request.form.get('re_password')

		if not (userid and username and password and re_password):
			return "모두 입력해주세요"
		elif password != re_password:
			return "비밀번호를 확인해주세요"
		else:
			user = User()
			user.password = password
			user.userid = userid
			user.username = username
			db.session.add(user)
			db.session.commit()
			return "회원가입 완료"
		return redirect('/')

# login 페이지 접속(GET)처리와, "action=/login" 처리(POST)모두 정의
@app.route('/login', methods=['GET', 'POST'])	
def login():
	if request.method=='GET':
		return render_template('login.html')
	else:
		userid = request.form['userid']
		password = request.form['password']
		try:
			data = User.query.filter_by(userid=userid, password=password).first()	# ID/PW 조회Query 실행
			if data is not None:	# 쿼리 데이터가 존재하면
				session['userid'] = userid	# userid를 session에 저장한다.
				return redirect('/')
			else:
				return 'Don\'t Login'	# 쿼리 데이터가 없으면 출력
		except:
			return "Don\'t login"	# 예외 상황 발생 시 출력

@app.route('/logout', methods=['GET'])
def logout():
	session.pop('userid', None)
	return redirect('/')