from flask import *
from database import *
import uuid
from datetime import datetime,date
from dateutil.relativedelta import relativedelta


admin=Blueprint('admin',__name__)

@admin.route('/admin_home')
def admin_home():
	return render_template('admin_home.html')

@admin.route('/adminmanagestaff',methods=['get','post'])
def adminmanagestaff():
	data={}
	today=date.today()
	data['today']=today
	if "add" in request.form:
		fna=request.form['fn']
		lna=request.form['ln']
		pla=request.form['pl']
		d=request.form['d']
		pho=request.form['ph']
		em=request.form['em']
		hn=request.form['hn']
		dis=request.form['dis']
		c=request.form['c']
		pin=request.form['pin']
		pwd=request.form['p']
		q="select * from login where username='%s'"%(em)
		res=select(q)
		if res:
			flash("username is already exist")
		else:

			ql="insert into login values('%s','%s','staff')"%(em,pwd)
			rl=insert(ql)
			qs="insert into staff values(null,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','active')"%(em,fna,lna,pla,d,pho,em,hn,dis,c,pin)
			insert(qs)
			flash("added successfully")
		return redirect(url_for('admin.adminmanagestaff'))
	if "action" in request.args:
		action=request.args['action']
		sid=request.args['sid']
	else:
		action=None
	if "update" in request.form:
		fna=request.form['fn']
		lna=request.form['ln']
		pla=request.form['pl']
		d=request.form['d']
		pho=request.form['ph']
		em=request.form['em']
		hn=request.form['hn']
		dis=request.form['dis']
		c=request.form['c']
		pin=request.form['pin']
		q="select * from login inner join staff using(username) where staff_id='%s'"%(sid)
		print(q)
		res=select(q)
		preuname=res[0]['username']
		q="update staff set username='%s', firstname='%s',lastname='%s',place='%s',dob='%s',phone='%s',email='%s',house='%s',district='%s',city='%s',pincode='%s' where staff_id='%s'"%(em,fna,lna,pla,d,pho,em,hn,dis,c,pin,sid)
		r=update(q)
		q="update login set username='%s'  where username='%s'"%(em,preuname)
		r=update(q)
		flash("update successfully")

		return redirect(url_for('admin.adminmanagestaff'))
	if action=="update":
		q="select * from  staff where staff_id='%s'"%(sid)
		r=select(q)
		data['updatestaff']=r
	if action=="active":
		q="update staff set ststatus='inactive' where staff_id='%s'"%(sid)
		update(q)
		flash("inactive successfully")
		return redirect(url_for('admin.adminmanagestaff'))
	if action=="inactive":
		q="update staff set ststatus='active' where staff_id='%s'"%(sid)
		update(q)
		flash("active successfully")
		return redirect(url_for('admin.adminmanagestaff'))
	q="select * from staff "
	r=select(q)
	data['staff']=r
	return render_template('adminmanagestaff.html',data=data)

@admin.route('/adminmanagepurchasedetails',methods=['get','post'])
def adminmanagepurchasedetails():
	data={}
	today=date.today()
	data['today']=today
	
	q="select * from book  "
	r=select(q)
	data['book']=r
	q="select * from staff  "
	r=select(q)
	data['staff']=r
	q="select * from  publisher  where pstatus='active' "
	r=select(q)
	data['pub']=r
	q="SELECT * FROM `purchase_master` INNER  JOIN`purchase_child` USING(`pmaster_id`)INNER JOIN `book` USING(`book_id`)INNER JOIN `publisher` USING(`publisher_id`) "
	r=select(q)
	data['view']=r

	if "add" in request.form:
		sid=request.form['staffid']
		bid=request.form['bid']
		pid=request.form['pid']
		amt=request.form['amt']
		data['amt']=amt
		q=request.form['q']
		data['q']=q
		d=request.form['d']
		t=request.form['t']
		qs="insert into purchase_master values(null,'%s','%s','%s','%s')"%(pid,sid,d,t)
		id=insert(qs)
		qp="insert into purchase_child values(null,'%s','%s','%s','%s')"%(id,bid,amt,q)
		insert(qp)
		q="update book set qty='%s' where book_id='%s'"%(q,bid)
		update(q)
		q="update book set status='active' where book_id='%s'"%(bid)
		update(q)
		flash("Purchased successfully")
		return redirect(url_for('admin.adminmanagepurchasedetails'))
	
	
	return render_template('adminmanagepurchasedetails.html',data=data)






@admin.route('/adminmanagepublisher',methods=['get','post'])
def adminmanagepublisher():
	data={}
	
	if "add" in request.form:
		p=request.form['p']
		pho=request.form['ph']
		em=request.form['em']
		dis=request.form['dis']
		c=request.form['c']
		pin=request.form['pin']
		

	
		qs="insert into publisher values(null,'%s','%s','%s','%s','%s','%s','active')"%(em,p,pho,c,dis,pin)
		insert(qs)
		flash("added successfully")
		return redirect(url_for('admin.adminmanagepublisher'))
	if "action" in request.args:
		action=request.args['action']
		pid=request.args['pid']
	else:
		action=None
	if "update" in request.form:
		p=request.form['p']
		pho=request.form['ph']
		em=request.form['em']
		dis=request.form['dis']
		c=request.form['c']
		pin=request.form['pin']
		
		q="update publisher set email='%s',publisher='%s',phone='%s',city='%s',district='%s',pincode='%s' where publisher_id='%s'"%(em,p,pho,c,dis,pin,pid)
		r=update(q)
		flash("update successfully")
		return redirect(url_for('admin.adminmanagepublisher'))
	if action=="update":
		q="select * from  publisher where publisher_id='%s'"%(pid)
		r=select(q)
		data['updatepublisher']=r
	if action=="active":
		q="update publisher set pstatus='inactive' where publisher_id='%s'"%(pid)
		update(q)
		flash("inactive successfully")
		return redirect(url_for('admin.adminmanagepublisher'))
	if action=="inactive":
		q="update publisher set pstatus='active' where publisher_id='%s'"%(pid)
		update(q)
		flash("active successfully")
		return redirect(url_for('admin.adminmanagepublisher'))
	q="select * from publisher "
	r=select(q)
	data['publisher']=r
	return render_template('adminmanagepublisher.html',data=data)



@admin.route('/adminmanagelanguage',methods=['get','post'])
def adminmanagelanguage():
	data={}
	
	if "add" in request.form:
		l=request.form['l']
		

	
		qs="insert into language values(null,'%s','active')"%(l)
		insert(qs)
		flash("added successfully")
		return redirect(url_for('admin.adminmanagelanguage'))
	if "action" in request.args:
		action=request.args['action']
		lid=request.args['lid']
	else:
		action=None
	if "update" in request.form:
		l=request.form['l']
		
		
		q="update language set language='%s' where language_id='%s'"%(l,lid)
		r=update(q)
		flash("update successfully")
		return redirect(url_for('admin.adminmanagelanguage'))
	if action=="update":
		q="select * from  language where language_id='%s'"%(lid)
		r=select(q)
		data['updatelan']=r
	if action=="active":
		q="update language set lstatus='inactive' where language_id='%s'"%(lid)
		update(q)
		flash("inactive successfully")
		return redirect(url_for('admin.adminmanagelanguage'))
	if action=="inactive":
		q="update language set lstatus='active' where language_id='%s'"%(lid)
		update(q)
		flash("active successfully")
		return redirect(url_for('admin.adminmanagelanguage'))
	q="select * from language "
	r=select(q)
	data['lan']=r
	return render_template('adminmanagelanguage.html',data=data)




@admin.route('/adminmanagefinecategory',methods=['get','post'])
def adminmanagefinecategory():
	data={}
	
	if "add" in request.form:
		f=request.form['fc']
		fa=request.form['fa']
		m=request.form['m']
		

	
		qs="insert into fine_category values(null,'%s','%s','%s','active')"%(f,fa,m)
		insert(qs)
		flash("added successfully")
		return redirect(url_for('admin.adminmanagefinecategory'))
	if "action" in request.args:
		action=request.args['action']
		cid=request.args['cid']
	else:
		action=None
	if "update" in request.form:
		fa=request.form['fa']
		q="update fine_category set fine_amount='%s' where fcategory_id='%s'"%(fa,cid)
		r=update(q)
		flash("update successfully")
		return redirect(url_for('admin.adminmanagefinecategory'))
	if action=="update":
		q="select * from  fine_category where fcategory_id='%s'"%(cid)
		r=select(q)
		data['updatecat']=r
	if action=="active":
		q="update fine_category set fcstatus='inactive' where fcategory_id='%s'"%(cid)
		update(q)
		flash("inactive successfully")
		return redirect(url_for('admin.adminmanagefinecategory'))
	if action=="inactive":
		q="update fine_category set fcstatus='active' where fcategory_id='%s'"%(cid)
		update(q)
		flash("active successfully")
		return redirect(url_for('admin.adminmanagefinecategory'))
	q="select * from fine_category "
	r=select(q)
	data['cat']=r
	return render_template('adminmanagefinecategory.html',data=data)





@admin.route('/adminmanagegenre',methods=['get','post'])
def adminmanagegenre():
	data={}
	
	if "add" in request.form:
		g=request.form['g']
		

	
		qs="insert into genre values(null,'%s','active')"%(g)
		insert(qs)
		flash("added successfully")
		return redirect(url_for('admin.adminmanagegenre'))
	if "action" in request.args:
		action=request.args['action']
		gid=request.args['gid']
	else:
		action=None
	if "update" in request.form:
		g=request.form['g']
		
		
		q="update genre set genre_name='%s' where genre_id='%s'"%(g,gid)
		r=update(q)
		flash("update successfully")
		return redirect(url_for('admin.adminmanagegenre'))
	if action=="update":
		q="select * from  genre where genre_id='%s'"%(gid)
		r=select(q)
		data['updategen']=r
	if action=="active":
		q="update genre set gstatus='inactive' where genre_id='%s'"%(gid)
		update(q)
		flash("inactive successfully")
		return redirect(url_for('admin.adminmanagegenre'))
	if action=="inactive":
		q="update genre set gstatus='active' where genre_id='%s'"%(gid)
		update(q)
		flash("active successfully")
		return redirect(url_for('admin.adminmanagegenre'))
	q="select * from genre "
	r=select(q)
	data['gen']=r
	return render_template('adminmanagegenre.html',data=data)



@admin.route('/adminviewfine',methods=['get','post'])
def adminviewfine():
	data={}
	rid=request.args['rid']
	q="SELECT * FROM fine INNER JOIN fine_category USING (fcategory_id)INNER JOIN rent_master USING (rmaster_id) where rmaster_id='%s'  "%(rid)
	r=select(q)
	data['book']=r
	
	return render_template('adminviewfine.html',data=data)


@admin.route('/adminviewdetails',methods=['get','post'])
def adminviewdetails():
	data={}
	rid=request.args['rid']

	q="SELECT * FROM book INNER JOIN LANGUAGE USING (language_id) INNER JOIN genre USING(genre_id) INNER JOIN `rent_child` USING(`book_id`) where rmaster_id='%s' and lstatus='active'and gstatus='active'"%(rid)
	r=select(q)
	data['book']=r
	
	return render_template('adminviewdetails.html',data=data)

@admin.route('/adminviewcustomerdetails',methods=['get','post'])
def adminviewcustomerdetails():
	data={}
	q="SELECT * FROM  customer"
	r=select(q)
	data['view']=r
	
	return render_template('adminviewcustomerdetails.html',data=data)



@admin.route('/adminviewbook',methods=['get','post'])
def adminviewbook():
	data={}
	q="SELECT * FROM book INNER JOIN LANGUAGE USING (language_id) INNER JOIN genre USING(genre_id)where lstatus='active' and gstatus='active' "
	r=select(q)
	data['view']=r
	q="select * from language where lstatus='active' "
	r=select(q)
	data['lan']=r
	q="select * from  genre where gstatus='active' "
	r=select(q)
	data['gen']=r
	
	return render_template('adminviewbook.html',data=data)


@admin.route('/adminmanagesbook',methods=['get','post'])
def adminmanagesbook():
	data={}
	q="SELECT * FROM book INNER JOIN LANGUAGE USING (language_id) INNER JOIN genre USING(genre_id)where lstatus='active' and gstatus='active' "
	r=select(q)
	data['book']=r
	q="select * from language where lstatus='active' "
	r=select(q)
	data['lan']=r
	q="select * from  genre where gstatus='active' "
	r=select(q)
	data['gen']=r
	if "add" in request.form:
		lid=request.form['lid']
		gid=request.form['gid']
		bn=request.form['bn']
		a=request.form['a']
		d=request.form['d']
		i=request.files['i']
		path="static/images/"+str(uuid.uuid4())+i.filename
		i.save(path)
		

	
		qs="insert into book values(null,'%s','%s','%s','%s','%s','%s','0','innactive')"%(lid,gid,bn,a,path,d)
		insert(qs)
		flash("added successfully")
		return redirect(url_for('admin.adminmanagesbook'))
	if "action" in request.args:
		action=request.args['action']
		bid=request.args['bid']
	else:
		action=None
	if "update" in request.form:
		lid=request.form['lid']
		gid=request.form['gid']
		bn=request.form['bn']
		a=request.form['a']
		d=request.form['d']
		i=request.files['i']
		path="static/images"+str(uuid.uuid4())+i.filename
		i.save(path)
				
		q="update book set language_id='%s',genre_id='%s',bname='%s',author='%s',image='%s',description='%s' where book_id='%s'"%(lid,gid,bn,a,path,d,bid)
		r=update(q)
		flash("update successfully")
		return redirect(url_for('admin.adminmanagesbook'))
	if action=="update":
		q="select * from  book where book_id='%s'"%(bid)
		r=select(q)
		data['updatebook']=r
	if action=="active":
		q="update book set status='inactive' where book_id='%s'"%(bid)
		update(q)
		flash("inactive successfully")

		return redirect(url_for('admin.adminmanagesbook'))
	if action=="inactive":
		q="update book set status='active' where book_id='%s'"%(bid)
		update(q)
		flash("active successfully")

		return redirect(url_for('admin.adminmanagesbook'))
	
	return render_template('adminmanagesbook.html',data=data)

# @admin.route('/adminviewbookrentrequest',methods=['get','post'])
# def adminviewbookrentrequest():
# 	data={}
# 	q="SELECT * FROM rent_master INNER JOIN customer USING (customer_id)INNER JOIN rent_child USING (rmaster_id)  "
# 	r=select(q)
# 	data['book']=r
# 	if "action" in request.args:
# 		action=request.args['action']
# 		rid=request.args['rid']
# 		bookid=request.args['bookid']
# 	else:
# 		action=None
	
# 	if action=="accept":
# 		q="update  rent_master set status='accept' where rmaster_id='%s' "%(rid)
# 		r=update(q)
# 		q="update book set qty=qty-1 where book_id='%s'"%(bookid)
# 		update(q)
# 		flash(" accepted successfully")
# 		return redirect(url_for('admin.adminviewbookrentrequest'))
	
# 	if action=="confirm":
# 		q="update  rent_master set status='confirm' where rmaster_id='%s' "%(rid)
# 		r=update(q)
# 		flash(" returned successfully")
# 		return redirect(url_for('admin.adminviewbookrentrequest'))


# 	if action=="reject":
# 		q="delete from rent_master where rmaster_id='%s' "%(rid)
# 		r=delete(q)
# 		flash(" rejected successfully")
# 		return redirect(url_for('admin.adminviewbookrentrequest'))

# 	if action=="picked":
# 		q="update  rent_master set status='picked' where rmaster_id='%s' "%(rid)
# 		r=update(q)
# 		flash(" picked successfully")
# 		return redirect(url_for('admin.adminviewbookrentrequest'))

# 	if action=="dpicked":
# 		q="update  rent_master set status='not picked' where rmaster_id='%s' "%(rid)
# 		r=update(q)
# 		flash(" Book Renting Cancelled")
# 		return redirect(url_for('admin.adminviewbookrentrequest'))


# 	if "r_id" in request.args:
# 		r_id= request.args['r_id']
# 		date_after_month = datetime.today()+ relativedelta(months=1)
# 		fromdate=datetime.today().strftime('%d/%m/%Y')
# 		enddate=date_after_month.strftime('%m/%d/%Y')
# 		q="update  rent_master set rdate='%s' where rmaster_id='%s' "%(enddate,r_id)
# 		r=update(q)
# 		flash(" return date added successfully")
# 		return redirect(url_for('admin.adminviewbookrentrequest'))


# 	return render_template('adminviewbookrentrequest.html',data=data)

@admin.route('/adminviewbookrentrequest',methods=['get','post'])
def adminviewbookrentrequest():
	data={}
	q="SELECT * FROM rent_master INNER JOIN customer USING (customer_id)INNER JOIN rent_child USING (rmaster_id)  "
	r=select(q)
	data['book']=r
	if "action" in request.args:
		action=request.args['action']
		rid=request.args['rid']

		bookid=request.args['bookid']
	else:
		action=None
	
	if action=="accept":
		q="update  rent_master set status='accept' where rmaster_id='%s' "%(rid)
		r=update(q)
		q="update book set qty=qty-1 where book_id='%s'"%(bookid)
		update(q)
		flash(" accepted successfully")
		return redirect(url_for('admin.adminviewbookrentrequest'))
	
	if action=="confirm":
		q="update  rent_master set status='confirm' where rmaster_id='%s' "%(rid)
		r=update(q)
		flash(" returned successfully")
		return redirect(url_for('admin.adminviewbookrentrequest'))



	if action=="reject":
		q="update  rent_master set status='reject' where rmaster_id='%s' "%(rid)
		r=update(q)
		flash(" rejected successfully")
		return redirect(url_for('admin.adminviewbookrentrequest'))
		
	if action=="picked":
		q="update  rent_master set status='picked' where rmaster_id='%s' "%(rid)
		r=update(q)
		flash(" picked successfully")
		return redirect(url_for('admin.adminviewbookrentrequest'))
	if action=="dpicked":
		q="update  rent_master set status='not picked' where rmaster_id='%s' "%(rid)
		r=update(q)
		flash(" Book Renting Cancelled")
		return redirect(url_for('admin.adminviewbookrentrequest'))


	if "r_id" in request.args:
		r_id= request.args['r_id']
		date_after_month = datetime.today()+ relativedelta(months=1)
		fromdate=datetime.today().strftime('%d/%m/%Y')
		enddate=date_after_month.strftime('%m/%d/%Y')
		q="update  rent_master set rdate='%s' where rmaster_id='%s' "%(enddate,r_id)
		r=update(q)
		flash(" return date added successfully")
		return redirect(url_for('admin.adminviewbookrentrequest'))


	return render_template('adminviewbookrentrequest.html',data=data)


@admin.route('/adminmanageplan',methods=['get','post'])
def adminmanageplan():
	data={}
	
	if "add" in request.form:
		f=request.form['fc']
		fa=request.form['fa']
	
	
		qs="insert into plan values(null,'%s','%s','active')"%(f,fa)
		insert(qs)
		flash("added successfully")
		return redirect(url_for('admin.adminmanageplan'))
	if "action" in request.args:
		action=request.args['action']
		cid=request.args['cid']
	else:
		action=None
	if "update" in request.form:
		f=request.form['fc']
		fa=request.form['fa']
		
		q="update plan set plan='%s',amount='%s' where plan_id='%s'"%(f,fa,cid)
		r=update(q)
		flash("update successfully")
		return redirect(url_for('admin.adminmanageplan'))
	if action=="update":
		q="select * from  plan where plan_id='%s'"%(cid)
		r=select(q)
		data['updatecat']=r
	if action=="active":
		q="update plan set pl_status='inactive' where plan_id='%s'"%(cid)
		update(q)
		flash("inactive successfully")
		return redirect(url_for('admin.adminmanageplan'))
	if action=="inactive":
		q="update plan set pl_status='active' where plan_id='%s'"%(cid)
		update(q)
		flash("active successfully")
		return redirect(url_for('admin.adminmanagefinecategory'))
	q="select * from plan "
	r=select(q)
	data['cat']=r
	return render_template('adminmanageplan.html',data=data)


@admin.route('/adminprintstaff')
def adminprintstaff():
	data={}
	today=date.today()
	print(today)
	data['today']=today
	now=datetime.now()
	current_time=now.strftime("%H:%M:%S")
	print(current_time)
	data['current_time']=current_time	

	q="select * from  staff"

	data['view']=select(q)
	return render_template('adminprintstaff.html',data=data)


@admin.route('/adminprintpublisher',methods=['get','post'])
def adminprintpublisher():
	data={}
	today=date.today()
	print(today)
	data['today']=today
	now=datetime.now()
	current_time=now.strftime("%H:%M:%S")
	print(current_time)
	data['current_time']=current_time	
	q="SELECT * FROM  publisher"
	r=select(q)
	data['view']=r
	
	return render_template('adminprintpublisher.html',data=data)

# @admin.route('/adminprintlanguage',methods=['get','post'])
# def adminprintlanguage():
# 	data={}
# 	today=date.today()
# 	print(today)
# 	data['today']=today
# 	now=datetime.now()
# 	current_time=now.strftime("%H:%M:%S")
# 	print(current_time)
# 	data['current_time']=current_time	
# 	q="SELECT * FROM  language"
# 	r=select(q)
# 	data['view']=r
	
# 	return render_template('adminprintlanguage.html',data=data)

@admin.route('/adminviewpurchasedetails',methods=['get','post'])
def adminviewpurchasedetails():
	data={}
	today=date.today()
	data['today']=today
	now=datetime.now()
	current_time=now.strftime("%H:%M:%S")
	print(current_time)
	data['current_time']=current_time	

	q="SELECT * FROM `purchase_master` INNER  JOIN`purchase_child` USING(`pmaster_id`)INNER JOIN `book` USING(`book_id`)INNER JOIN `publisher` USING(`publisher_id`) "
	session['q']=q
	r=select(q)

	data['view']=r
	if "search" in request.form:
		sname=request.form['sname']
		fname=request.form['fname']
		q="SELECT * FROM `purchase_master` INNER  JOIN`purchase_child` USING(`pmaster_id`)INNER JOIN `book` USING(`book_id`)INNER JOIN `publisher` USING(`publisher_id`) where pur_date between '%s' and '%s'"%(sname,fname) 
		# q="select *  FROM book INNER JOIN LANGUAGE USING (language_id) INNER JOIN genre USING(genre_id) where bname like '%s'"%(book)
		print(q)
		session['q']=q
		r=select(q)
		if r:
			data['search']=r
			print(data['search'])
		else:
			flash("NO MATCHED RESULTS FOUND")

	return render_template('adminviewpurchasedetails.html',data=data)


@admin.route('/adminprintpurchase',methods=['get','post'])
def adminprintpurchase():
	data={}
	today=date.today()
	data['today']=today
	now=datetime.now()
	current_time=now.strftime("%H:%M:%S")
	print(current_time)
	data['current_time']=current_time
	q=session['q']
	data['pur']=select(q)
	return render_template('adminprintpurchase.html',data=data)

@admin.route('/adminviewrentdetails',methods=['get','post'])
def adminviewrentdetails():
	data={}
	today=date.today()
	data['today']=today
	now=datetime.now()
	current_time=now.strftime("%H:%M:%S")
	print(current_time)
	data['current_time']=current_time	

	q="SELECT * FROM `rent_master` INNER  JOIN`rent_child` USING(`rmaster_id`)INNER JOIN `book` USING(`book_id`)INNER JOIN customer USING(customer_id) "
	session['q']=q
	r=select(q)

	data['view']=r
	if "search" in request.form:
		sname=request.form['sname']
		fname=request.form['fname']
		q="SELECT * FROM `rent_master` INNER  JOIN`rent_child` USING(`rmaster_id`)INNER JOIN `book` USING(`book_id`)INNER JOIN customer USING(customer_id) where date between '%s' and '%s'"%(sname,fname) 
		# q="select *  FROM book INNER JOIN LANGUAGE USING (language_id) INNER JOIN genre USING(genre_id) where bname like '%s'"%(book)
		print(q)
		session['q']=q
		r=select(q)
		if r:
			data['search']=r
			print(data['search'])
		else:
			flash("NO MATCHED RESULTS FOUND")

	return render_template('adminviewrentdetails.html',data=data)

@admin.route('/adminprintrent',methods=['get','post'])
def adminprintrent():
	data={}
	today=date.today()
	data['today']=today
	now=datetime.now()
	current_time=now.strftime("%H:%M:%S")
	print(current_time)
	data['current_time']=current_time
	q=session['q']
	data['pur']=select(q)
	return render_template('adminprintrent.html',data=data)

@admin.route('/adminviewpayment',methods=['get','post'])
def adminviewpayment():
	data={}
	q="SELECT * FROM `payment` INNER JOIN `rent_master` USING(`rmaster_id`)INNER JOIN `rent_child` USING(`rmaster_id`) INNER JOIN BOOK USING(BOOK_ID)INNER JOIN customer USING(customer_id)"
	r=select(q)
	data['book']=r
	return render_template('adminviewpayment.html',data=data)

@admin.route('/adminviewsub',methods=['get','post'])
def adminviewsub():
	data={}

	q="SELECT * FROM `subscription` INNER JOIN plan USING(plan_id) INNER JOIN customer USING(customer_id)"
	r=select(q)
	data['book']=r
	
	return render_template('adminviewsub.html',data=data)

@admin.route('/adminviewrentrequestdetails',methods=['get','post'])
def adminviewrentrequestdetails():
	data={}
	rid=request.args['rid']

	q="SELECT * FROM book INNER JOIN LANGUAGE USING (language_id) INNER JOIN genre USING(genre_id) INNER JOIN `rent_child` USING(`book_id`) where rmaster_id='%s'"%(rid)
	r=select(q)
	data['book']=r
	
	return render_template('adminviewrentrequestdetails.html',data=data)

@admin.route('/adminprintbook',methods=['get','post'])
def adminprintbook():
	data={}
	today=date.today()
	print(today)
	data['today']=today
	now=datetime.now()
	current_time=now.strftime("%H:%M:%S")
	print(current_time)
	data['current_time']=current_time	
	q="SELECT * FROM book INNER JOIN LANGUAGE USING (language_id) INNER JOIN genre USING(genre_id)"
	r=select(q)
	data['view']=r
	
	return render_template('adminprintbook.html',data=data)
