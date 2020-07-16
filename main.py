import tkinter as tk
import sqlite3
import xlsxwriter
import os



def save():

	r_add = r1.get() + r2.get() + r3.get()
	s_add = s1.get() + s2.get() + s3.get()
	mobx = mob1.get()
	moby = mob2.get()
	if mobx == '':
		mobx = int('0')
	else:
		mobx = int(mobx)
	if moby == '':
		moby = int('0')
	else:
		moby = int(moby)
	lst = [Name.get(),r_add,r_city.get(),s_add,s_city.get(),mobx,moby]
	if var1.get()==1:
		c.execute('INSERT INTO IHB(I_NAME , I_R_ADD , I_R_CITY , I_S_ADD , I_S_CITY , I_MOBA , I_MOBB) VALUES(?,?,?,?,?,?,?);',lst)
	if var2.get()==1:
		c.execute('INSERT INTO GOV_CON(GC_NAME , GC_R_ADD , GC_R_CITY , GC_S_ADD , GC_S_CITY , GC_MOBA , GC_MOBB) VALUES(?,?,?,?,?,?,?);',lst)
	if var3.get()==1:
		c.execute('INSERT INTO BUILDER(B_NAME , B_R_ADD , B_R_CITY , B_S_ADD , B_S_CITY , B_MOBA , B_MOBB) VALUES(?,?,?,?,?,?,?);',lst)
	if var4.get()==1:
		c.execute('INSERT INTO CONTRACTOR(C_NAME , C_R_ADD , C_R_CITY , C_S_ADD , C_S_CITY , C_MOBA , C_MOBB) VALUES(?,?,?,?,?,?,?);',lst)
	if var5.get()==1:
		c.execute('INSERT INTO ENGINEER(E_NAME , E_R_ADD , E_R_CITY , E_S_ADD , E_S_CITY , E_MOBA , E_MOBB) VALUES(?,?,?,?,?,?,?);',lst)
	if var6.get()==1:
		c.execute('INSERT INTO KADIYA(K_NAME , K_R_ADD , K_R_CITY , K_S_ADD , K_S_CITY , K_MOBA , K_MOBB) VALUES(?,?,?,?,?,?,?);',lst)
	conn.commit()
	Entry2_6.delete(0,'end')
	Entry2_5.delete(0,'end')
	Entry2_4.delete(0,'end')
	Entry2_3.delete(0,'end')
	Entry2_2.delete(0,'end')
	Entry2.delete(0,'end')
	Entry1_9.delete(0,'end')
	Entry1_7.delete(0,'end')
	Entry1_61.delete(0,'end')
	Entry1_6.delete(0,'end')
	Entry1_5.delete(0,'end')
	Entry1.delete(0,'end')
	#for row in c.execute('SELECT * FROM GOV_CON;'):
	#	print(row)


def search():
	#frame_s = tk.Toplevel(screen1)
	#frame_s.title('Search Results')
	global cust

	lst = ['0','1','2','3','4','5','6','7','8','9']

	cust = cid.get()
	if cust[0] in lst:
		cust = int(cust)
		workbook = xlsxwriter.Workbook('Personal Details.xlsx')
		worksheet = workbook.add_worksheet()
		workbook1 = xlsxwriter.Workbook('Link Details.xlsx')
		worksheet1 = workbook1.add_worksheet()
		row = 0
		col = 0
		row2 = 0
		col2 = 0
		worksheet.write(row , col , 'CUSTOMER')
		worksheet.write(row , col+1 , 'ID')
		worksheet.write(row , col+2 , 'Name')
		worksheet.write(row , col+3 , 'RESIDENTIAL ADDRESS')
		worksheet.write(row , col+4 , 'RESIDENTIAL CITY')
		worksheet.write(row , col+5 , 'SITE ADDRESS')
		worksheet.write(row , col+6 , 'SITE CITY')
		worksheet.write(row , col+7 , 'MOBILE-1')
		worksheet.write(row , col+8 , 'MOBILE-2')
		worksheet1.write(row2 , col2 , 'CUSTOMER')
		worksheet1.write(row2 , col2+1 , 'CUSTOMER ID')
		worksheet1.write(row2 , col2+2 , 'CUSTOMER Name')
		worksheet1.write(row2 , col2+3 , 'CONTRACTOR ID')
		worksheet1.write(row2 , col2+4 , 'CONTRACTOR NAME')
		worksheet1.write(row2 , col2+5 , 'ENGINEER ID')
		worksheet1.write(row2 , col2+6 , 'ENGINEER NAME')
		worksheet1.write(row2 , col2+7 , 'KADIYA ID')
		worksheet1.write(row2 , col2+8 , 'KADIYA NAME')
		row = row+1
		row2 = row2 + 1
		if var1.get()==1:
			if cust==0:
				rows = c.execute('SELECT * FROM IHB').fetchall()
			else:
				rows = c.execute('SELECT * FROM IHB WHERE IHB.I_ID = ?',(cust,)).fetchall()

			for row1 in rows:
				worksheet.write(row , col , 'IHB')
				worksheet.write(row , col+1 , row1[0])
				worksheet.write(row , col+2 , row1[1])
				worksheet.write(row , col+3 , row1[2])
				worksheet.write(row , col+4 , row1[3])
				worksheet.write(row , col+5 , row1[4])
				worksheet.write(row , col+6 , row1[5])
				worksheet.write(row , col+7 , row1[6])
				worksheet.write(row , col+8 , row1[7])
				row = row + 1
				try:
					con1 = c.execute('SELECT CONTRACTOR.C_ID,CONTRACTOR.C_NAME FROM CONTRACTOR,LINK WHERE CONTRACTOR.C_ID=LINK.C_IDA AND LINK.I_ID = ?',(row1[0],)).fetchone()
					if con1 == None:
						con1 = ['NULL' , 'NULL']
					con2 = c.execute('SELECT CONTRACTOR.C_ID,CONTRACTOR.C_NAME FROM CONTRACTOR,LINK WHERE CONTRACTOR.C_ID=LINK.C_IDB AND LINK.I_ID = ?',(row1[0],)).fetchone()
					if con2 == None:
						con2 = ['NULL' , 'NULL']
					eng1 = c.execute('SELECT ENGINEER.E_ID,ENGINEER.E_NAME FROM ENGINEER,LINK WHERE ENGINEER.E_ID=LINK.E_IDA AND LINK.I_ID = ?',(row1[0],)).fetchone()
					if eng1 == None:
						eng1 = ['NULL' , 'NULL']
					eng2 = c.execute('SELECT ENGINEER.E_ID,ENGINEER.E_NAME FROM ENGINEER,LINK WHERE ENGINEER.E_ID=LINK.E_IDB AND LINK.I_ID = ?',(row1[0],)).fetchone()
					if eng2 == None:
						eng2 = ['NULL' , 'NULL']
					kad1 = c.execute('SELECT KADIYA.K_ID,KADIYA.K_NAME FROM KADIYA,LINK WHERE KADIYA.K_ID=LINK.K_IDA AND LINK.I_ID = ?',(row1[0],)).fetchone()
					if kad1 == None:
						kad1 = ['NULL' , 'NULL']
					kad2 = c.execute('SELECT KADIYA.K_ID,KADIYA.K_NAME FROM KADIYA,LINK WHERE KADIYA.K_ID=LINK.K_IDB AND LINK.I_ID = ?',(row1[0],)).fetchone()
					if kad2 == None:
						kad2 = ['NULL' , 'NULL']
					kad3 = c.execute('SELECT KADIYA.K_ID,KADIYA.K_NAME FROM KADIYA,LINK WHERE KADIYA.K_ID=LINK.K_IDC AND LINK.I_ID = ?',(row1[0],)).fetchone()
					if kad3 == None:
						kad3 = ['NULL' , 'NULL']
					kad4 = c.execute('SELECT KADIYA.K_ID,KADIYA.K_NAME FROM KADIYA,LINK WHERE KADIYA.K_ID=LINK.K_IDD AND LINK.I_ID = ?',(row1[0],)).fetchone()
					if kad4 == None:
						kad4 = ['NULL' , 'NULL']
					kad5 = c.execute('SELECT KADIYA.K_ID,KADIYA.K_NAME FROM KADIYA,LINK WHERE KADIYA.K_ID=LINK.K_IDE AND LINK.I_ID = ?',(row1[0],)).fetchone()
					if kad5 == None:
						kad5 = ['NULL' , 'NULL']
					worksheet1.write(row2 , col2 , 'IHB')
					worksheet1.write(row2 , col2+1 , row1[0])
					worksheet1.write(row2 , col2+2 , row1[1])
					worksheet1.write(row2 , col2+3 , con1[0])
					worksheet1.write(row2 , col2+4 , con1[1])
					worksheet1.write(row2+1, col2+3 , con2[0])
					worksheet1.write(row2+1 , col2+4 , con2[1])
					worksheet1.write(row2 , col2+5 , eng1[0])
					worksheet1.write(row2 , col2+6 , eng1[1])
					worksheet1.write(row2+1, col2+5 , eng2[0])
					worksheet1.write(row2+1 , col2+6 , eng2[1])
					worksheet1.write(row2 , col2+7 , kad1[0])
					worksheet1.write(row2 , col2+8 , kad1[1])
					worksheet1.write(row2+1 , col2+7 , kad2[0])
					worksheet1.write(row2+1 , col2+8 , kad2[1])
					worksheet1.write(row2+2 , col2+7 , kad3[0])
					worksheet1.write(row2+2 , col2+8 , kad3[1])
					worksheet1.write(row2+3 , col2+7 , kad4[0])
					worksheet1.write(row2+3 , col2+8 , kad4[1])
					worksheet1.write(row2+4 , col2+7 , kad5[0])
					worksheet1.write(row2+4 , col2+8 , kad5[1])
					row2 = row2 + 5
				except:
					continue
			#workbook.close()
		if var2.get()==1:
			if cust==0:
				rows = c.execute('SELECT * FROM GOV_CON').fetchall()
			else:
				rows = c.execute('SELECT * FROM GOV_CON WHERE GC_ID = ?',(cust,)).fetchall()
			for row1 in rows:
				worksheet.write(row , col , 'GOVT_CON')
				worksheet.write(row , col+1 , row1[0])
				worksheet.write(row , col+2 , row1[1])
				worksheet.write(row , col+3 , row1[2])
				worksheet.write(row , col+4 , row1[3])
				worksheet.write(row , col+5 , row1[4])
				worksheet.write(row , col+6 , row1[5])
				worksheet.write(row , col+7 , row1[6])
				worksheet.write(row , col+8 , row1[7])
				row = row+1
				try:
					con1 = c.execute('SELECT CONTRACTOR.C_ID,CONTRACTOR.C_NAME FROM CONTRACTOR,LINK WHERE CONTRACTOR.C_ID=LINK.C_IDA AND LINK.I_ID = ?',(row1[0],)).fetchone()
					if con1 == None:
						con1 = ['NULL' , 'NULL']
					con2 = c.execute('SELECT CONTRACTOR.C_ID,CONTRACTOR.C_NAME FROM CONTRACTOR,LINK WHERE CONTRACTOR.C_ID=LINK.C_IDB AND LINK.I_ID = ?',(row1[0],)).fetchone()
					if con2 == None:
						con2 = ['NULL' , 'NULL']
					eng1 = c.execute('SELECT ENGINEER.E_ID,ENGINEER.E_NAME FROM ENGINEER,LINK WHERE ENGINEER.E_ID=LINK.E_IDA AND LINK.I_ID = ?',(row1[0],)).fetchone()
					if eng1 == None:
						eng1 = ['NULL' , 'NULL']
					eng2 = c.execute('SELECT ENGINEER.E_ID,ENGINEER.E_NAME FROM ENGINEER,LINK WHERE ENGINEER.E_ID=LINK.E_IDB AND LINK.I_ID = ?',(row1[0],)).fetchone()
					if eng2 == None:
						eng2 = ['NULL' , 'NULL']
					kad1 = c.execute('SELECT KADIYA.K_ID,KADIYA.K_NAME FROM KADIYA,LINK WHERE KADIYA.K_ID=LINK.K_IDA AND LINK.I_ID = ?',(row1[0],)).fetchone()
					if kad1 == None:
						kad1 = ['NULL' , 'NULL']
					kad2 = c.execute('SELECT KADIYA.K_ID,KADIYA.K_NAME FROM KADIYA,LINK WHERE KADIYA.K_ID=LINK.K_IDB AND LINK.I_ID = ?',(row1[0],)).fetchone()
					if kad2 == None:
						kad2 = ['NULL' , 'NULL']
					kad3 = c.execute('SELECT KADIYA.K_ID,KADIYA.K_NAME FROM KADIYA,LINK WHERE KADIYA.K_ID=LINK.K_IDC AND LINK.I_ID = ?',(row1[0],)).fetchone()
					if kad3 == None:
						kad3 = ['NULL' , 'NULL']
					kad4 = c.execute('SELECT KADIYA.K_ID,KADIYA.K_NAME FROM KADIYA,LINK WHERE KADIYA.K_ID=LINK.K_IDD AND LINK.I_ID = ?',(row1[0],)).fetchone()
					if kad4 == None:
						kad4 = ['NULL' , 'NULL']
					kad5 = c.execute('SELECT KADIYA.K_ID,KADIYA.K_NAME FROM KADIYA,LINK WHERE KADIYA.K_ID=LINK.K_IDE AND LINK.I_ID = ?',(row1[0],)).fetchone()
					if kad5 == None:
						kad5 = ['NULL' , 'NULL']
					worksheet1.write(row2 , col2 , 'GOV_CON')
					worksheet1.write(row2 , col2+1 , row1[0])
					worksheet1.write(row2 , col2+2 , row1[1])
					worksheet1.write(row2 , col2+3 , con1[0])
					worksheet1.write(row2 , col2+4 , con1[1])
					worksheet1.write(row2+1, col2+3 , con2[0])
					worksheet1.write(row2+1 , col2+4 , con2[1])
					worksheet1.write(row2 , col2+5 , eng1[0])
					worksheet1.write(row2 , col2+6 , eng1[1])
					worksheet1.write(row2+1, col2+5 , eng2[0])
					worksheet1.write(row2+1 , col2+6 , eng2[1])
					worksheet1.write(row2 , col2+7 , kad1[0])
					worksheet1.write(row2 , col2+8 , kad1[1])
					worksheet1.write(row2+1 , col2+7 , kad2[0])
					worksheet1.write(row2+1 , col2+8 , kad2[1])
					worksheet1.write(row2+2 , col2+7 , kad3[0])
					worksheet1.write(row2+2 , col2+8 , kad3[1])
					worksheet1.write(row2+3 , col2+7 , kad4[0])
					worksheet1.write(row2+3 , col2+8 , kad4[1])
					worksheet1.write(row2+4 , col2+7 , kad5[0])
					worksheet1.write(row2+4 , col2+8 , kad5[1])
					row2 = row2 + 5
				except:
					continue
			#workbook.close()
		if var3.get()==1:
			if cust==0:
				rows = c.execute('SELECT * FROM BUILDER').fetchall()
			else:
				rows = c.execute('SELECT * FROM BUILDER WHERE B_ID = ?',(cust,)).fetchall()
			for row1 in rows:
				worksheet.write(row , col , 'BUILDER')
				worksheet.write(row , col+1 , row1[0])
				worksheet.write(row , col+2 , row1[1])
				worksheet.write(row , col+3 , row1[2])
				worksheet.write(row , col+4 , row1[3])
				worksheet.write(row , col+5 , row1[4])
				worksheet.write(row , col+6 , row1[5])
				worksheet.write(row , col+7 , row1[6])
				worksheet.write(row , col+8 , row1[7])
				row = row+1
				try:
					con1 = c.execute('SELECT CONTRACTOR.C_ID,CONTRACTOR.C_NAME FROM CONTRACTOR,LINK WHERE CONTRACTOR.C_ID=LINK.C_IDA AND LINK.I_ID = ?',(row1[0],)).fetchone()
					if con1 == None:
						con1 = ['NULL' , 'NULL']
					con2 = c.execute('SELECT CONTRACTOR.C_ID,CONTRACTOR.C_NAME FROM CONTRACTOR,LINK WHERE CONTRACTOR.C_ID=LINK.C_IDB AND LINK.I_ID = ?',(row1[0],)).fetchone()
					if con2 == None:
						con2 = ['NULL' , 'NULL']
					eng1 = c.execute('SELECT ENGINEER.E_ID,ENGINEER.E_NAME FROM ENGINEER,LINK WHERE ENGINEER.E_ID=LINK.E_IDA AND LINK.I_ID = ?',(row1[0],)).fetchone()
					if eng1 == None:
						eng1 = ['NULL' , 'NULL']
					eng2 = c.execute('SELECT ENGINEER.E_ID,ENGINEER.E_NAME FROM ENGINEER,LINK WHERE ENGINEER.E_ID=LINK.E_IDB AND LINK.I_ID = ?',(row1[0],)).fetchone()
					if eng2 == None:
						eng2 = ['NULL' , 'NULL']
					kad1 = c.execute('SELECT KADIYA.K_ID,KADIYA.K_NAME FROM KADIYA,LINK WHERE KADIYA.K_ID=LINK.K_IDA AND LINK.I_ID = ?',(row1[0],)).fetchone()
					if kad1 == None:
						kad1 = ['NULL' , 'NULL']
					kad2 = c.execute('SELECT KADIYA.K_ID,KADIYA.K_NAME FROM KADIYA,LINK WHERE KADIYA.K_ID=LINK.K_IDB AND LINK.I_ID = ?',(row1[0],)).fetchone()
					if kad2 == None:
						kad2 = ['NULL' , 'NULL']
					kad3 = c.execute('SELECT KADIYA.K_ID,KADIYA.K_NAME FROM KADIYA,LINK WHERE KADIYA.K_ID=LINK.K_IDC AND LINK.I_ID = ?',(row1[0],)).fetchone()
					if kad3 == None:
						kad3 = ['NULL' , 'NULL']
					kad4 = c.execute('SELECT KADIYA.K_ID,KADIYA.K_NAME FROM KADIYA,LINK WHERE KADIYA.K_ID=LINK.K_IDD AND LINK.I_ID = ?',(row1[0],)).fetchone()
					if kad4 == None:
						kad4 = ['NULL' , 'NULL']
					kad5 = c.execute('SELECT KADIYA.K_ID,KADIYA.K_NAME FROM KADIYA,LINK WHERE KADIYA.K_ID=LINK.K_IDE AND LINK.I_ID = ?',(row1[0],)).fetchone()
					if kad5 == None:
						kad5 = ['NULL' , 'NULL']
					worksheet1.write(row2 , col2 , 'BUILDER')
					worksheet1.write(row2 , col2+1 , row1[0])
					worksheet1.write(row2 , col2+2 , row1[1])
					worksheet1.write(row2 , col2+3 , con1[0])
					worksheet1.write(row2 , col2+4 , con1[1])
					worksheet1.write(row2+1, col2+3 , con2[0])
					worksheet1.write(row2+1 , col2+4 , con2[1])
					worksheet1.write(row2 , col2+5 , eng1[0])
					worksheet1.write(row2 , col2+6 , eng1[1])
					worksheet1.write(row2+1, col2+5 , eng2[0])
					worksheet1.write(row2+1 , col2+6 , eng2[1])
					worksheet1.write(row2 , col2+7 , kad1[0])
					worksheet1.write(row2 , col2+8 , kad1[1])
					worksheet1.write(row2+1 , col2+7 , kad2[0])
					worksheet1.write(row2+1 , col2+8 , kad2[1])
					worksheet1.write(row2+2 , col2+7 , kad3[0])
					worksheet1.write(row2+2 , col2+8 , kad3[1])
					worksheet1.write(row2+3 , col2+7 , kad4[0])
					worksheet1.write(row2+3 , col2+8 , kad4[1])
					worksheet1.write(row2+4 , col2+7 , kad5[0])
					worksheet1.write(row2+4 , col2+8 , kad5[1])
					row2 = row2 + 5
				except:
					continue
			#workbook.close()
		if var4.get()==1:
			if cust==0:
				rows = c.execute('SELECT * FROM CONTRACTOR').fetchall()
			else:
				rows = c.execute('SELECT * FROM CONTRACTOR WHERE C_ID = ?',(cust,)).fetchall()
			for row1 in rows:
				worksheet.write(row , col , 'CONTRACTOR')
				worksheet.write(row , col+1 , row1[0])
				worksheet.write(row , col+2 , row1[1])
				worksheet.write(row , col+3 , row1[2])
				worksheet.write(row , col+4 , row1[3])
				worksheet.write(row , col+5 , row1[4])
				worksheet.write(row , col+6 , row1[5])
				worksheet.write(row , col+7 , row1[6])
				worksheet.write(row , col+8 , row1[7])
				row = row+1
			#workbook.close()
		if var5.get()==1:
			if cust==0:
				rows = c.execute('SELECT * FROM ENGINEER').fetchall()
			else:
				rows = c.execute('SELECT * FROM ENGINEER WHERE E_ID = ?',(cust,)).fetchall()
			for row1 in rows:
				worksheet.write(row , col , 'ENGINEER')
				worksheet.write(row , col+1 , row1[0])
				worksheet.write(row , col+2 , row1[1])
				worksheet.write(row , col+3 , row1[2])
				worksheet.write(row , col+4 , row1[3])
				worksheet.write(row , col+5 , row1[4])
				worksheet.write(row , col+6 , row1[5])
				worksheet.write(row , col+7 , row1[6])
				worksheet.write(row , col+8 , row1[7])
				row = row+1
			#workbook.close()
		if var6.get()==1:
			if cust==0:
				rows = c.execute('SELECT * FROM KADIYA').fetchall()
			else:
				rows = c.execute('SELECT * FROM KADIYA WHERE K_ID = ?',(cust,)).fetchall()
			for row1 in rows:
				worksheet.write(row , col , 'KADIYA')
				worksheet.write(row , col+1 , row1[0])
				worksheet.write(row , col+2 , row1[1])
				worksheet.write(row , col+3 , row1[2])
				worksheet.write(row , col+4 , row1[3])
				worksheet.write(row , col+5 , row1[4])
				worksheet.write(row , col+6 , row1[5])
				worksheet.write(row , col+7 , row1[6])
				worksheet.write(row , col+8 , row1[7])
				row = row+1
			#workbook.close()
		
		#cid.delete(0,'end')

	else:
		cust = '%'+cust+'%'
		workbook = xlsxwriter.Workbook('Personal Details.xlsx')
		worksheet = workbook.add_worksheet()
		workbook1 = xlsxwriter.Workbook('Link Details.xlsx')
		worksheet1 = workbook1.add_worksheet()
		row = 0
		col = 0
		row2 = 0
		col2 = 0
		worksheet.write(row , col , 'CUSTOMER')
		worksheet.write(row , col+1 , 'ID')
		worksheet.write(row , col+2 , 'Name')
		worksheet.write(row , col+3 , 'RESIDENTIAL ADDRESS')
		worksheet.write(row , col+4 , 'RESIDENTIAL CITY')
		worksheet.write(row , col+5 , 'SITE ADDRESS')
		worksheet.write(row , col+6 , 'SITE CITY')
		worksheet.write(row , col+7 , 'MOBILE-1')
		worksheet.write(row , col+8 , 'MOBILE-2')
		worksheet1.write(row2 , col2 , 'CUSTOMER')
		worksheet1.write(row2 , col2+1 , 'CUSTOMER ID')
		worksheet1.write(row2 , col2+2 , 'CUSTOMER Name')
		worksheet1.write(row2 , col2+3 , 'CONTRACTOR ID')
		worksheet1.write(row2 , col2+4 , 'CONTRACTOR NAME')
		worksheet1.write(row2 , col2+5 , 'ENGINEER ID')
		worksheet1.write(row2 , col2+6 , 'ENGINEER NAME')
		worksheet1.write(row2 , col2+7 , 'KADIYA ID')
		worksheet1.write(row2 , col2+8 , 'KADIYA NAME')
		row = row+1
		row2 = row2 + 1
		if var1.get()==1:
			rows = c.execute('SELECT * FROM IHB WHERE I_NAME like(?)',(cust,)).fetchall()
			for row1 in rows:
				worksheet.write(row , col , 'IHB')
				worksheet.write(row , col+1 , row1[0])
				worksheet.write(row , col+2 , row1[1])
				worksheet.write(row , col+3 , row1[2])
				worksheet.write(row , col+4 , row1[3])
				worksheet.write(row , col+5 , row1[4])
				worksheet.write(row , col+6 , row1[5])
				worksheet.write(row , col+7 , row1[6])
				worksheet.write(row , col+8 , row1[7])
				row = row+1
				try:
					con1 = c.execute('SELECT CONTRACTOR.C_ID,CONTRACTOR.C_NAME FROM CONTRACTOR,LINK WHERE CONTRACTOR.C_ID=LINK.C_IDA AND LINK.I_ID = ?',(row1[0],)).fetchone()
					if con1 == None:
						con1 = ['NULL' , 'NULL']
					con2 = c.execute('SELECT CONTRACTOR.C_ID,CONTRACTOR.C_NAME FROM CONTRACTOR,LINK WHERE CONTRACTOR.C_ID=LINK.C_IDB AND LINK.I_ID = ?',(row1[0],)).fetchone()
					if con2 == None:
						con2 = ['NULL' , 'NULL']
					eng1 = c.execute('SELECT ENGINEER.E_ID,ENGINEER.E_NAME FROM ENGINEER,LINK WHERE ENGINEER.E_ID=LINK.E_IDA AND LINK.I_ID = ?',(row1[0],)).fetchone()
					if eng1 == None:
						eng1 = ['NULL' , 'NULL']
					eng2 = c.execute('SELECT ENGINEER.E_ID,ENGINEER.E_NAME FROM ENGINEER,LINK WHERE ENGINEER.E_ID=LINK.E_IDB AND LINK.I_ID = ?',(row1[0],)).fetchone()
					if eng2 == None:
						eng2 = ['NULL' , 'NULL']
					kad1 = c.execute('SELECT KADIYA.K_ID,KADIYA.K_NAME FROM KADIYA,LINK WHERE KADIYA.K_ID=LINK.K_IDA AND LINK.I_ID = ?',(row1[0],)).fetchone()
					if kad1 == None:
						kad1 = ['NULL' , 'NULL']
					kad2 = c.execute('SELECT KADIYA.K_ID,KADIYA.K_NAME FROM KADIYA,LINK WHERE KADIYA.K_ID=LINK.K_IDB AND LINK.I_ID = ?',(row1[0],)).fetchone()
					if kad2 == None:
						kad2 = ['NULL' , 'NULL']
					kad3 = c.execute('SELECT KADIYA.K_ID,KADIYA.K_NAME FROM KADIYA,LINK WHERE KADIYA.K_ID=LINK.K_IDC AND LINK.I_ID = ?',(row1[0],)).fetchone()
					if kad3 == None:
						kad3 = ['NULL' , 'NULL']
					kad4 = c.execute('SELECT KADIYA.K_ID,KADIYA.K_NAME FROM KADIYA,LINK WHERE KADIYA.K_ID=LINK.K_IDD AND LINK.I_ID = ?',(row1[0],)).fetchone()
					if kad4 == None:
						kad4 = ['NULL' , 'NULL']
					kad5 = c.execute('SELECT KADIYA.K_ID,KADIYA.K_NAME FROM KADIYA,LINK WHERE KADIYA.K_ID=LINK.K_IDE AND LINK.I_ID = ?',(row1[0],)).fetchone()
					if kad5 == None:
						kad5 = ['NULL' , 'NULL']
					worksheet1.write(row2 , col2 , 'IHB')
					worksheet1.write(row2 , col2+1 , row1[0])
					worksheet1.write(row2 , col2+2 , row1[1])
					worksheet1.write(row2 , col2+3 , con1[0])
					worksheet1.write(row2 , col2+4 , con1[1])
					worksheet1.write(row2+1, col2+3 , con2[0])
					worksheet1.write(row2+1 , col2+4 , con2[1])
					worksheet1.write(row2 , col2+5 , eng1[0])
					worksheet1.write(row2 , col2+6 , eng1[1])
					worksheet1.write(row2+1, col2+5 , eng2[0])
					worksheet1.write(row2+1 , col2+6 , eng2[1])
					worksheet1.write(row2 , col2+7 , kad1[0])
					worksheet1.write(row2 , col2+8 , kad1[1])
					worksheet1.write(row2+1 , col2+7 , kad2[0])
					worksheet1.write(row2+1 , col2+8 , kad2[1])
					worksheet1.write(row2+2 , col2+7 , kad3[0])
					worksheet1.write(row2+2 , col2+8 , kad3[1])
					worksheet1.write(row2+3 , col2+7 , kad4[0])
					worksheet1.write(row2+3 , col2+8 , kad4[1])
					worksheet1.write(row2+4 , col2+7 , kad5[0])
					worksheet1.write(row2+4 , col2+8 , kad5[1])
					row2 = row2 + 5
				except:
					continue
			#workbook.close()
		if var2.get()==1:
			rows = c.execute('SELECT * FROM GOV_CON WHERE GC_NAME like(?)',(cust,)).fetchall()
			for row1 in rows:
				worksheet.write(row , col , 'GOVT_CON')
				worksheet.write(row , col+1 , row1[0])
				worksheet.write(row , col+2 , row1[1])
				worksheet.write(row , col+3 , row1[2])
				worksheet.write(row , col+4 , row1[3])
				worksheet.write(row , col+5 , row1[4])
				worksheet.write(row , col+6 , row1[5])
				worksheet.write(row , col+7 , row1[6])
				worksheet.write(row , col+8 , row1[7])
				row = row+1
				try:
					con1 = c.execute('SELECT CONTRACTOR.C_ID,CONTRACTOR.C_NAME FROM CONTRACTOR,LINK WHERE CONTRACTOR.C_ID=LINK.C_IDA AND LINK.I_ID = ?',(row1[0],)).fetchone()
					if con1 == None:
						con1 = ['NULL' , 'NULL']
					con2 = c.execute('SELECT CONTRACTOR.C_ID,CONTRACTOR.C_NAME FROM CONTRACTOR,LINK WHERE CONTRACTOR.C_ID=LINK.C_IDB AND LINK.I_ID = ?',(row1[0],)).fetchone()
					if con2 == None:
						con2 = ['NULL' , 'NULL']
					eng1 = c.execute('SELECT ENGINEER.E_ID,ENGINEER.E_NAME FROM ENGINEER,LINK WHERE ENGINEER.E_ID=LINK.E_IDA AND LINK.I_ID = ?',(row1[0],)).fetchone()
					if eng1 == None:
						eng1 = ['NULL' , 'NULL']
					eng2 = c.execute('SELECT ENGINEER.E_ID,ENGINEER.E_NAME FROM ENGINEER,LINK WHERE ENGINEER.E_ID=LINK.E_IDB AND LINK.I_ID = ?',(row1[0],)).fetchone()
					if eng2 == None:
						eng2 = ['NULL' , 'NULL']
					kad1 = c.execute('SELECT KADIYA.K_ID,KADIYA.K_NAME FROM KADIYA,LINK WHERE KADIYA.K_ID=LINK.K_IDA AND LINK.I_ID = ?',(row1[0],)).fetchone()
					if kad1 == None:
						kad1 = ['NULL' , 'NULL']
					kad2 = c.execute('SELECT KADIYA.K_ID,KADIYA.K_NAME FROM KADIYA,LINK WHERE KADIYA.K_ID=LINK.K_IDB AND LINK.I_ID = ?',(row1[0],)).fetchone()
					if kad2 == None:
						kad2 = ['NULL' , 'NULL']
					kad3 = c.execute('SELECT KADIYA.K_ID,KADIYA.K_NAME FROM KADIYA,LINK WHERE KADIYA.K_ID=LINK.K_IDC AND LINK.I_ID = ?',(row1[0],)).fetchone()
					if kad3 == None:
						kad3 = ['NULL' , 'NULL']
					kad4 = c.execute('SELECT KADIYA.K_ID,KADIYA.K_NAME FROM KADIYA,LINK WHERE KADIYA.K_ID=LINK.K_IDD AND LINK.I_ID = ?',(row1[0],)).fetchone()
					if kad4 == None:
						kad4 = ['NULL' , 'NULL']
					kad5 = c.execute('SELECT KADIYA.K_ID,KADIYA.K_NAME FROM KADIYA,LINK WHERE KADIYA.K_ID=LINK.K_IDE AND LINK.I_ID = ?',(row1[0],)).fetchone()
					if kad5 == None:
						kad5 = ['NULL' , 'NULL']
					worksheet1.write(row2 , col2 , 'GOV_CON')
					worksheet1.write(row2 , col2+1 , row1[0])
					worksheet1.write(row2 , col2+2 , row1[1])
					worksheet1.write(row2 , col2+3 , con1[0])
					worksheet1.write(row2 , col2+4 , con1[1])
					worksheet1.write(row2+1, col2+3 , con2[0])
					worksheet1.write(row2+1 , col2+4 , con2[1])
					worksheet1.write(row2 , col2+5 , eng1[0])
					worksheet1.write(row2 , col2+6 , eng1[1])
					worksheet1.write(row2+1, col2+5 , eng2[0])
					worksheet1.write(row2+1 , col2+6 , eng2[1])
					worksheet1.write(row2 , col2+7 , kad1[0])
					worksheet1.write(row2 , col2+8 , kad1[1])
					worksheet1.write(row2+1 , col2+7 , kad2[0])
					worksheet1.write(row2+1 , col2+8 , kad2[1])
					worksheet1.write(row2+2 , col2+7 , kad3[0])
					worksheet1.write(row2+2 , col2+8 , kad3[1])
					worksheet1.write(row2+3 , col2+7 , kad4[0])
					worksheet1.write(row2+3 , col2+8 , kad4[1])
					worksheet1.write(row2+4 , col2+7 , kad5[0])
					worksheet1.write(row2+4 , col2+8 , kad5[1])
					row2 = row2 + 5
				except:
					continue
			#workbook.close()
		if var3.get()==1:
			rows = c.execute('SELECT * FROM BUILDER WHERE B_NAME like(?)',(cust,)).fetchall()
			for row1 in rows:
				worksheet.write(row , col , 'BUILDER')
				worksheet.write(row , col+1 , row1[0])
				worksheet.write(row , col+2 , row1[1])
				worksheet.write(row , col+3 , row1[2])
				worksheet.write(row , col+4 , row1[3])
				worksheet.write(row , col+5 , row1[4])
				worksheet.write(row , col+6 , row1[5])
				worksheet.write(row , col+7 , row1[6])
				worksheet.write(row , col+8 , row1[7])
				row = row+1
				try:
					con1 = c.execute('SELECT CONTRACTOR.C_ID,CONTRACTOR.C_NAME FROM CONTRACTOR,LINK WHERE CONTRACTOR.C_ID=LINK.C_IDA AND LINK.I_ID = ?',(row1[0],)).fetchone()
					if con1 == None:
						con1 = ['NULL' , 'NULL']
					con2 = c.execute('SELECT CONTRACTOR.C_ID,CONTRACTOR.C_NAME FROM CONTRACTOR,LINK WHERE CONTRACTOR.C_ID=LINK.C_IDB AND LINK.I_ID = ?',(row1[0],)).fetchone()
					if con2 == None:
						con2 = ['NULL' , 'NULL']
					eng1 = c.execute('SELECT ENGINEER.E_ID,ENGINEER.E_NAME FROM ENGINEER,LINK WHERE ENGINEER.E_ID=LINK.E_IDA AND LINK.I_ID = ?',(row1[0],)).fetchone()
					if eng1 == None:
						eng1 = ['NULL' , 'NULL']
					eng2 = c.execute('SELECT ENGINEER.E_ID,ENGINEER.E_NAME FROM ENGINEER,LINK WHERE ENGINEER.E_ID=LINK.E_IDB AND LINK.I_ID = ?',(row1[0],)).fetchone()
					if eng2 == None:
						eng2 = ['NULL' , 'NULL']
					kad1 = c.execute('SELECT KADIYA.K_ID,KADIYA.K_NAME FROM KADIYA,LINK WHERE KADIYA.K_ID=LINK.K_IDA AND LINK.I_ID = ?',(row1[0],)).fetchone()
					if kad1 == None:
						kad1 = ['NULL' , 'NULL']
					kad2 = c.execute('SELECT KADIYA.K_ID,KADIYA.K_NAME FROM KADIYA,LINK WHERE KADIYA.K_ID=LINK.K_IDB AND LINK.I_ID = ?',(row1[0],)).fetchone()
					if kad2 == None:
						kad2 = ['NULL' , 'NULL']
					kad3 = c.execute('SELECT KADIYA.K_ID,KADIYA.K_NAME FROM KADIYA,LINK WHERE KADIYA.K_ID=LINK.K_IDC AND LINK.I_ID = ?',(row1[0],)).fetchone()
					if kad3 == None:
						kad3 = ['NULL' , 'NULL']
					kad4 = c.execute('SELECT KADIYA.K_ID,KADIYA.K_NAME FROM KADIYA,LINK WHERE KADIYA.K_ID=LINK.K_IDD AND LINK.I_ID = ?',(row1[0],)).fetchone()
					if kad4 == None:
						kad4 = ['NULL' , 'NULL']
					kad5 = c.execute('SELECT KADIYA.K_ID,KADIYA.K_NAME FROM KADIYA,LINK WHERE KADIYA.K_ID=LINK.K_IDE AND LINK.I_ID = ?',(row1[0],)).fetchone()
					if kad5 == None:
						kad5 = ['NULL' , 'NULL']
					worksheet1.write(row2 , col2 , 'BUILDER')
					worksheet1.write(row2 , col2+1 , row1[0])
					worksheet1.write(row2 , col2+2 , row1[1])
					worksheet1.write(row2 , col2+3 , con1[0])
					worksheet1.write(row2 , col2+4 , con1[1])
					worksheet1.write(row2+1, col2+3 , con2[0])
					worksheet1.write(row2+1 , col2+4 , con2[1])
					worksheet1.write(row2 , col2+5 , eng1[0])
					worksheet1.write(row2 , col2+6 , eng1[1])
					worksheet1.write(row2+1, col2+5 , eng2[0])
					worksheet1.write(row2+1 , col2+6 , eng2[1])
					worksheet1.write(row2 , col2+7 , kad1[0])
					worksheet1.write(row2 , col2+8 , kad1[1])
					worksheet1.write(row2+1 , col2+7 , kad2[0])
					worksheet1.write(row2+1 , col2+8 , kad2[1])
					worksheet1.write(row2+2 , col2+7 , kad3[0])
					worksheet1.write(row2+2 , col2+8 , kad3[1])
					worksheet1.write(row2+3 , col2+7 , kad4[0])
					worksheet1.write(row2+3 , col2+8 , kad4[1])
					worksheet1.write(row2+4 , col2+7 , kad5[0])
					worksheet1.write(row2+4 , col2+8 , kad5[1])
					row2 = row2 + 5
				except:
					continue
			#workbook.close()
		if var4.get()==1:
			rows = c.execute('SELECT * FROM CONTRACTOR WHERE C_NAME like(?)',(cust,)).fetchall()
			for row1 in rows:
				worksheet.write(row , col , 'CONTRACTOR')
				worksheet.write(row , col+1 , row1[0])
				worksheet.write(row , col+2 , row1[1])
				worksheet.write(row , col+3 , row1[2])
				worksheet.write(row , col+4 , row1[3])
				worksheet.write(row , col+5 , row1[4])
				worksheet.write(row , col+6 , row1[5])
				worksheet.write(row , col+7 , row1[6])
				worksheet.write(row , col+8 , row1[7])
				row = row+1
			#workbook.close()
		if var5.get()==1:
			rows = c.execute('SELECT * FROM ENGINEER WHERE E_NAME like(?)',(cust,)).fetchall()
			for row1 in rows:
				worksheet.write(row , col , 'ENGINEER')
				worksheet.write(row , col+1 , row1[0])
				worksheet.write(row , col+2 , row1[1])
				worksheet.write(row , col+3 , row1[2])
				worksheet.write(row , col+4 , row1[3])
				worksheet.write(row , col+5 , row1[4])
				worksheet.write(row , col+6 , row1[5])
				worksheet.write(row , col+7 , row1[6])
				worksheet.write(row , col+8 , row1[7])
				row = row+1
			#workbook.close()
		if var6.get()==1:
			rows = c.execute('SELECT * FROM KADIYA WHERE K_NAME like(?)',(cust,)).fetchall()
			for row1 in rows:
				worksheet.write(row , col , 'KADIYA')
				worksheet.write(row , col+1 , row1[0])
				worksheet.write(row , col+2 , row1[1])
				worksheet.write(row , col+3 , row1[2])
				worksheet.write(row , col+4 , row1[3])
				worksheet.write(row , col+5 , row1[4])
				worksheet.write(row , col+6 , row1[5])
				worksheet.write(row , col+7 , row1[6])
				worksheet.write(row , col+8 , row1[7])
				row = row+1
	workbook.close()
	workbook1.close()
		#cid.delete(0,'end')


def changes():
	boolean = [0 , 0 , 0 , 0 , 0 , 0 , 0]
	r_add = r1.get() + r2.get() + r3.get()
	if r_add != '':
		boolean[1] = 1
	s_add = s1.get() + s2.get() + s3.get()
	if s_add != '':
		boolean[3] = 1
	mobx = mob1.get()
	if mobx != '':
		boolean[5] = 1
		mobx = int(mobx)
	moby = mob2.get()
	if moby != '':
		boolean[6] = 1
		moby = int(moby)
	ename = Name.get()
	if ename != '':
		boolean[0] = 1
	er_city = r_city.get()
	if er_city != '':
		boolean[2] = 1
	es_city = s_city.get()
	if es_city != '':
		boolean[4] = 1
	cust = int(cid.get())
	if var1.get() == 1:
		if boolean[0] == 1:
			c.execute('UPDATE IHB SET I_NAME = ? WHERE I_ID = ?',(ename,cust))
		if boolean[1] == 1:
			c.execute('UPDATE IHB SET I_R_ADD = ? WHERE I_ID = ?',(r_add,cust))
		if boolean[2] == 1:
			c.execute('UPDATE IHB SET I_R_CITY = ? WHERE I_ID = ?',(er_city,cust))
		if boolean[3] == 1:
			c.execute('UPDATE IHB SET I_S_ADD = ? WHERE I_ID = ?',(s_add,cust))
		if boolean[4] == 1:
			c.execute('UPDATE IHB SET I_S_CITY = ? WHERE I_ID = ?',(es_city,cust))
		if boolean[5] == 1:
			c.execute('UPDATE IHB SET I_MOBA = ? WHERE I_ID = ?',(mobx,cust))
		if boolean[6] == 1:
			c.execute('UPDATE IHB SET I_MOBB = ? WHERE I_ID = ?',(moby,cust))

	if var2.get() == 1:
		if boolean[0] == 1:
			c.execute('UPDATE GOV_CON SET GC_NAME = ? WHERE GC_ID = ?',(ename,cust))
		if boolean[1] == 1:
			c.execute('UPDATE GOV_CON SET GC_R_ADD = ? WHERE GC_ID = ?',(r_add,cust))
		if boolean[2] == 1:
			c.execute('UPDATE GOV_CON SET GC_R_CITY = ? WHERE GC_ID = ?',(er_city,cust))
		if boolean[3] == 1:
			c.execute('UPDATE GOV_CON SET GC_S_ADD = ? WHERE GC_ID = ?',(s_add,cust))
		if boolean[4] == 1:
			c.execute('UPDATE GOV_CON SET GC_S_CITY = ? WHERE GC_ID = ?',(es_city,cust))
		if boolean[5] == 1:
			c.execute('UPDATE GOV_CON SET GC_MOBA = ? WHERE GC_ID = ?',(mobx,cust))
		if boolean[6] == 1:
			c.execute('UPDATE GOV_CON SET GC_MOBB = ? WHERE GC_ID = ?',(moby,cust))

	if var3.get() == 1:
		if boolean[0] == 1:
			c.execute('UPDATE BUILDER SET B_NAME = ? WHERE B_ID = ?',(ename,cust))
		if boolean[1] == 1:
			c.execute('UPDATE BUILDER SET B_R_ADD = ? WHERE B_ID = ?',(r_add,cust))
		if boolean[2] == 1:
			c.execute('UPDATE BUILDER SET B_R_CITY = ? WHERE B_ID = ?',(er_city,cust))
		if boolean[3] == 1:
			c.execute('UPDATE BUILDER SET B_S_ADD = ? WHERE B_ID = ?',(s_add,cust))
		if boolean[4] == 1:
			c.execute('UPDATE BUILDER SET B_S_CITY = ? WHERE B_ID = ?',(es_city,cust))
		if boolean[5] == 1:
			c.execute('UPDATE BUILDER SET B_MOBA = ? WHERE B_ID = ?',(mobx,cust))
		if boolean[6] == 1:
			c.execute('UPDATE BUILDER SET B_MOBB = ? WHERE B_ID = ?',(moby,cust))

	if var4.get() == 1:
		if boolean[0] == 1:
			c.execute('UPDATE CONTRACTOR SET C_NAME = ? WHERE C_ID = ?',(ename,cust))
		if boolean[1] == 1:
			c.execute('UPDATE CONTRACTOR SET C_R_ADD = ? WHERE C_ID = ?',(r_add,cust))
		if boolean[2] == 1:
			c.execute('UPDATE CONTRACTOR SET C_R_CITY = ? WHERE C_ID = ?',(er_city,cust))
		if boolean[3] == 1:
			c.execute('UPDATE CONTRACTOR SET C_S_ADD = ? WHERE C_ID = ?',(s_add,cust))
		if boolean[4] == 1:
			c.execute('UPDATE CONTRACTOR SET C_S_CITY = ? WHERE C_ID = ?',(es_city,cust))
		if boolean[5] == 1:
			c.execute('UPDATE CONTRACTOR SET C_MOBA = ? WHERE C_ID = ?',(mobx,cust))
		if boolean[6] == 1:
			c.execute('UPDATE CONTRACTOR SET C_MOBB = ? WHERE C_ID = ?',(moby,cust))

	if var5.get() == 1:
		if boolean[0] == 1:
			c.execute('UPDATE ENGINEER SET E_NAME = ? WHERE E_ID = ?',(ename,cust))
		if boolean[1] == 1:
			c.execute('UPDATE ENGINEER SET E_R_ADD = ? WHERE E_ID = ?',(r_add,cust))
		if boolean[2] == 1:
			c.execute('UPDATE ENGINEER SET E_R_CITY = ? WHERE E_ID = ?',(er_city,cust))
		if boolean[3] == 1:
			c.execute('UPDATE ENGINEER SET E_S_ADD = ? WHERE E_ID = ?',(s_add,cust))
		if boolean[4] == 1:
			c.execute('UPDATE ENGINEER SET E_S_CITY = ? WHERE E_ID = ?',(es_city,cust))
		if boolean[5] == 1:
			c.execute('UPDATE ENGINEER SET E_MOBA = ? WHERE E_ID = ?',(mobx,cust))
		if boolean[6] == 1:
			c.execute('UPDATE ENGINEER SET E_MOBB = ? WHERE E_ID = ?',(moby,cust))

	if var6.get() == 1:
		if boolean[0] == 1:
			c.execute('UPDATE KADIYA SET K_NAME = ? WHERE K_ID = ?',(ename,cust))
		if boolean[1] == 1:
			c.execute('UPDATE KADIYA SET K_R_ADD = ? WHERE K_ID = ?',(r_add,cust))
		if boolean[2] == 1:
			c.execute('UPDATE KADIYA SET K_R_CITY = ? WHERE K_ID = ?',(er_city,cust))
		if boolean[3] == 1:
			c.execute('UPDATE KADIYA SET K_S_ADD = ? WHERE K_ID = ?',(s_add,cust))
		if boolean[4] == 1:
			c.execute('UPDATE KADIYA SET K_S_CITY = ? WHERE K_ID = ?',(es_city,cust))
		if boolean[5] == 1:
			c.execute('UPDATE KADIYA SET K_MOBA = ? WHERE K_ID = ?',(mobx,cust))
		if boolean[6] == 1:
			c.execute('UPDATE KADIYA SET K_MOBB = ? WHERE K_ID = ?',(moby,cust))
	conn.commit()


def Insert():
	global screen1
	global var1
	global var2
	global var3
	global var4
	global var5
	global var6
	global Name
	global r_add
	global r1
	global r2
	global r3
	global s_add
	global s1
	global s2
	global s3
	global r_city
	global s_city
	global mob1
	global mob2
	global cid

	screen1 = tk.Toplevel(main_screen)
	screen1.title('ADD CUSTOMERS')

	var1 = tk.IntVar()
	var2 = tk.IntVar()
	var3 = tk.IntVar()
	var4 = tk.IntVar()
	var5 = tk.IntVar()
	var6 = tk.IntVar()
	Name = tk.StringVar()
	r_add = tk.StringVar()
	r1 = tk.StringVar()
	r2 = tk.StringVar()
	r3 = tk.StringVar()
	s_add = tk.StringVar()
	s1 = tk.StringVar()
	s2 = tk.StringVar()
	s3 = tk.StringVar()
	r_city = tk.StringVar()
	s_city = tk.StringVar()
	mob1 = tk.StringVar()
	mob2 = tk.StringVar()
	cid = tk.StringVar()

	_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
	_fgcolor = '#000000'  # X11 color: 'black'
	_compcolor = '#d9d9d9' # X11 color: 'gray85'
	_ana1color = '#d9d9d9' # X11 color: 'gray85'
	_ana2color = '#ececec' # Closest X11 color: 'gray92'
	font11 = "-family {Arial Black} -size 40 -weight bold -slant "  \
			"roman -underline 0 -overstrike 0"
	font9 = "-family {Segoe UI} -size 16 -weight bold -slant roman"  \
			" -underline 0 -overstrike 0"

	Frame1 = tk.Frame(screen1)
	Frame1.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=0.999)
	Frame1.configure(relief='groove')
	Frame1.configure(borderwidth="2")
	Frame1.configure(relief="groove")
	Frame1.configure(background="#d9d9d9")
	Frame1.configure(highlightbackground="#d9d9d9")
	Frame1.configure(highlightcolor="black")

	Checkbutton1 = tk.Checkbutton(Frame1)
	Checkbutton1.place(relx=0.037, rely=0.134, relheight=0.034 , relwidth=0.034)
	Checkbutton1.configure(activebackground="#ececec")
	Checkbutton1.configure(activeforeground="#000000")
	Checkbutton1.configure(background="#d9d9d9")
	Checkbutton1.configure(disabledforeground="#a3a3a3")
	Checkbutton1.configure(foreground="#000000")
	Checkbutton1.configure(highlightbackground="#d9d9d9")
	Checkbutton1.configure(highlightcolor="black")
	Checkbutton1.configure(justify='left')
	Checkbutton1.configure(text='''IHB''')
	Checkbutton1.configure(variable = var1)
	
	Checkbutton2 = tk.Checkbutton(Frame1)
	Checkbutton2.place(relx=0.088, rely=0.134, relheight=0.034 , relwidth=0.113)
	Checkbutton2.configure(activebackground="#ececec")
	Checkbutton2.configure(activeforeground="#000000")
	Checkbutton2.configure(background="#d9d9d9")
	Checkbutton2.configure(disabledforeground="#a3a3a3")
	Checkbutton2.configure(foreground="#000000")
	Checkbutton2.configure(highlightbackground="#d9d9d9")
	Checkbutton2.configure(highlightcolor="black")
	Checkbutton2.configure(justify='left')
	Checkbutton2.configure(text='''Government Contractor''')
	Checkbutton2.configure(variable = var2)
	
	Checkbutton3 = tk.Checkbutton(Frame1)
	Checkbutton3.place(relx=0.22, rely=0.134, relheight=0.034 , relwidth=0.048)
	Checkbutton3.configure(activebackground="#ececec")
	Checkbutton3.configure(activeforeground="#000000")
	Checkbutton3.configure(background="#d9d9d9")
	Checkbutton3.configure(disabledforeground="#a3a3a3")
	Checkbutton3.configure(foreground="#000000")
	Checkbutton3.configure(highlightbackground="#d9d9d9")
	Checkbutton3.configure(highlightcolor="black")
	Checkbutton3.configure(justify='left')
	Checkbutton3.configure(text='''Builder''')
	Checkbutton3.configure(variable = var3)
	
	Checkbutton4 = tk.Checkbutton(Frame1)
	Checkbutton4.place(relx=0.278, rely=0.134, relheight=0.034 , relwidth=0.062)
	Checkbutton4.configure(activebackground="#ececec")
	Checkbutton4.configure(activeforeground="#000000")
	Checkbutton4.configure(background="#d9d9d9")
	Checkbutton4.configure(disabledforeground="#a3a3a3")
	Checkbutton4.configure(foreground="#000000")
	Checkbutton4.configure(highlightbackground="#d9d9d9")
	Checkbutton4.configure(highlightcolor="black")
	Checkbutton4.configure(justify='left')
	Checkbutton4.configure(text='''Contractor''')
	Checkbutton4.configure(variable = var4)
	
	Checkbutton5 = tk.Checkbutton(Frame1)
	Checkbutton5.place(relx=0.352, rely=0.134, relheight=0.034 , relwidth=0.054)
	Checkbutton5.configure(activebackground="#ececec")
	Checkbutton5.configure(activeforeground="#000000")
	Checkbutton5.configure(background="#d9d9d9")
	Checkbutton5.configure(disabledforeground="#a3a3a3")
	Checkbutton5.configure(foreground="#000000")
	Checkbutton5.configure(highlightbackground="#d9d9d9")
	Checkbutton5.configure(highlightcolor="black")
	Checkbutton5.configure(justify='left')
	Checkbutton5.configure(text='''Engineer''')
	Checkbutton5.configure(variable = var5)
	
	Checkbutton6 = tk.Checkbutton(Frame1)
	Checkbutton6.place(relx=0.418, rely=0.134, relheight=0.034 , relwidth=0.046)
	Checkbutton6.configure(activebackground="#ececec")
	Checkbutton6.configure(activeforeground="#000000")
	Checkbutton6.configure(background="#d9d9d9")
	Checkbutton6.configure(disabledforeground="#a3a3a3")
	Checkbutton6.configure(foreground="#000000")
	Checkbutton6.configure(highlightbackground="#d9d9d9")
	Checkbutton6.configure(highlightcolor="black")
	Checkbutton6.configure(justify='left')
	Checkbutton6.configure(text='''Kadiya''')
	Checkbutton6.configure(variable = var6)

	Label1 = tk.Label(Frame1)
	Label1.place(relx=0.022, rely=0.215, height=31, width=114)
	Label1.configure(activebackground="#f9f9f9")
	Label1.configure(activeforeground="black")
	Label1.configure(background="#d9d9d9")
	Label1.configure(disabledforeground="#a3a3a3")
	Label1.configure(font=font9)
	Label1.configure(foreground="#000000")
	Label1.configure(highlightbackground="#d9d9d9")
	Label1.configure(text='''Name :''')

	Label1_1 = tk.Label(  Frame1)
	Label1_1.place(relx=0.029, rely=0.295, height=31, width=124)
	Label1_1.configure(activebackground="#f9f9f9")
	Label1_1.configure(activeforeground="black")
	Label1_1.configure(background="#d9d9d9")
	Label1_1.configure(disabledforeground="#a3a3a3")
	Label1_1.configure(font="-family {Segoe UI} -size 16 -weight bold")
	Label1_1.configure(foreground="#000000")
	Label1_1.configure(highlightbackground="#d9d9d9")
	Label1_1.configure(highlightcolor="black")
	Label1_1.configure(text='''Res. Add. :''')

	global Entry1
	Entry1 = tk.Entry(Frame1 , textvariable = Name)
	Entry1.place(relx=0.22, rely=0.228,height=20, relwidth=0.289)
	Entry1.configure(background="white")
	Entry1.configure(disabledforeground="#a3a3a3")
	Entry1.configure(font="TkFixedFont")
	Entry1.configure(foreground="#000000")
	Entry1.configure(insertbackground="black")
	'''
	Text1 = tk.Text(Frame1 , textvariable = r_add)
	Text1.place(relx=0.22, rely=0.295, relheight=0.126, relwidth=0.289)
	Text1.configure(background="white")
	Text1.configure(font="TkTextFont")
	Text1.configure(foreground="black")
	Text1.configure(highlightbackground="#d9d9d9")
	Text1.configure(highlightcolor="black")
	Text1.configure(insertbackground="black")
	Text1.configure(selectbackground="#c4c4c4")
	Text1.configure(selectforeground="black")
	Text1.configure(wrap="word")
	'''
	Label1_2 = tk.Label(Frame1)
	Label1_2.place(relx=0.029, rely=0.55, height=31, width=124)
	Label1_2.configure(activebackground="#f9f9f9")
	Label1_2.configure(activeforeground="black")
	Label1_2.configure(background="#d9d9d9")
	Label1_2.configure(disabledforeground="#a3a3a3")
	Label1_2.configure(font="-family {Segoe UI} -size 16 -weight bold")
	Label1_2.configure(foreground="#000000")
	Label1_2.configure(highlightbackground="#d9d9d9")
	Label1_2.configure(highlightcolor="black")
	Label1_2.configure(text='''Site Add. :''')
	'''
	Text1_3 = tk.Text(Frame1 , s_add)
	Text1_3.place(relx=0.22, rely=0.55, relheight=0.126, relwidth=0.289)
	Text1_3.configure(background="white")
	Text1_3.configure(font="TkTextFont")
	Text1_3.configure(foreground="black")
	Text1_3.configure(highlightbackground="#d9d9d9")
	Text1_3.configure(highlightcolor="black")
	Text1_3.configure(insertbackground="black")
	Text1_3.configure(selectbackground="#c4c4c4")
	Text1_3.configure(selectforeground="black")
	Text1_3.configure(wrap="word")
	'''
	Label1_4 = tk.Label(Frame1)
	Label1_4.place(relx=0.029, rely=0.456, height=31, width=114)
	Label1_4.configure(activebackground="#f9f9f9")
	Label1_4.configure(activeforeground="black")
	Label1_4.configure(background="#d9d9d9")
	Label1_4.configure(disabledforeground="#a3a3a3")
	Label1_4.configure(font="-family {Segoe UI} -size 16 -weight bold")
	Label1_4.configure(foreground="#000000")
	Label1_4.configure(highlightbackground="#d9d9d9")
	Label1_4.configure(highlightcolor="black")
	Label1_4.configure(text='''Res. City :''')

	global Entry1_5
	Entry1_5 = tk.Entry(Frame1 , textvariable = r_city)
	Entry1_5.place(relx=0.22, rely=0.47,height=20, relwidth=0.289)
	Entry1_5.configure(background="white")
	Entry1_5.configure(disabledforeground="#a3a3a3")
	Entry1_5.configure(font="TkFixedFont")
	Entry1_5.configure(foreground="#000000")
	Entry1_5.configure(highlightbackground="#d9d9d9")
	Entry1_5.configure(highlightcolor="black")
	Entry1_5.configure(insertbackground="black")
	Entry1_5.configure(selectbackground="#c4c4c4")
	Entry1_5.configure(selectforeground="black")

	Label1_5 = tk.Label(Frame1)
	Label1_5.place(relx=0.029, rely=0.711, height=31, width=114)
	Label1_5.configure(activebackground="#f9f9f9")
	Label1_5.configure(activeforeground="black")
	Label1_5.configure(background="#d9d9d9")
	Label1_5.configure(disabledforeground="#a3a3a3")
	Label1_5.configure(font="-family {Segoe UI} -size 16 -weight bold")
	Label1_5.configure(foreground="#000000")
	Label1_5.configure(highlightbackground="#d9d9d9")
	Label1_5.configure(highlightcolor="black")
	Label1_5.configure(text='''Site City :''')

	global Entry1_6
	Entry1_6 = tk.Entry(Frame1 , textvariable = s_city)
	Entry1_6.place(relx=0.22, rely=0.725,height=20, relwidth=0.289)
	Entry1_6.configure(background="white")
	Entry1_6.configure(disabledforeground="#a3a3a3")
	Entry1_6.configure(font="TkFixedFont")
	Entry1_6.configure(foreground="#000000")
	Entry1_6.configure(highlightbackground="#d9d9d9")
	Entry1_6.configure(highlightcolor="black")
	Entry1_6.configure(insertbackground="black")
	Entry1_6.configure(selectbackground="#c4c4c4")
	Entry1_6.configure(selectforeground="black")
	global Entry1_61
	Entry1_61 = tk.Entry(Frame1 , textvariable = mob1)
	Entry1_61.place(relx=0.22, rely=0.805,height=20, relwidth=0.289)
	Entry1_61.configure(background="white")
	Entry1_61.configure(disabledforeground="#a3a3a3")
	Entry1_61.configure(font="TkFixedFont")
	Entry1_61.configure(foreground="#000000")
	Entry1_61.configure(highlightbackground="#d9d9d9")
	Entry1_61.configure(highlightcolor="black")
	Entry1_61.configure(insertbackground="black")
	Entry1_61.configure(selectbackground="#c4c4c4")
	Entry1_61.configure(selectforeground="black")
	
	Label1_6 = tk.Label(  Frame1)
	Label1_6.place(relx=0.029, rely=0.792, height=31, width=114)
	Label1_6.configure(activebackground="#f9f9f9")
	Label1_6.configure(activeforeground="black")
	Label1_6.configure(background="#d9d9d9")
	Label1_6.configure(disabledforeground="#a3a3a3")
	Label1_6.configure(font="-family {Segoe UI} -size 16 -weight bold")
	Label1_6.configure(foreground="#000000")
	Label1_6.configure(highlightbackground="#d9d9d9")
	Label1_6.configure(highlightcolor="black")
	Label1_6.configure(text='''Mobile(1) :''')

	Label1_7 = tk.Label(  Frame1)
	Label1_7.place(relx=0.029, rely=0.872, height=31, width=114)
	Label1_7.configure(activebackground="#f9f9f9")
	Label1_7.configure(activeforeground="black")
	Label1_7.configure(background="#d9d9d9")
	Label1_7.configure(disabledforeground="#a3a3a3")
	Label1_7.configure(font="-family {Segoe UI} -size 16 -weight bold")
	Label1_7.configure(foreground="#000000")
	Label1_7.configure(highlightbackground="#d9d9d9")
	Label1_7.configure(highlightcolor="black")
	Label1_7.configure(text='''Mobile(2) :''')

	global Entry1_7
	Entry1_7 = tk.Entry(Frame1 , textvariable = mob2)
	Entry1_7.place(relx=0.22, rely=0.886,height=20, relwidth=0.289)
	Entry1_7.configure(background="white")
	Entry1_7.configure(disabledforeground="#a3a3a3")
	Entry1_7.configure(font="TkFixedFont")
	Entry1_7.configure(foreground="#000000")
	Entry1_7.configure(highlightbackground="#d9d9d9")
	Entry1_7.configure(highlightcolor="black")
	Entry1_7.configure(insertbackground="black")
	Entry1_7.configure(selectbackground="#c4c4c4")
	Entry1_7.configure(selectforeground="black")

	Label2 = tk.Label(  Frame1)
	Label2.place(relx=0.0, rely=0.0, height=71, width=1364)
	Label2.configure(background="#d9d9d9")
	Label2.configure(disabledforeground="#a3a3a3")
	Label2.configure(font=font11)
	Label2.configure(foreground="#000000")
	Label2.configure(text='''Jay Trading Co.''')

	Label1_8 = tk.Label(  Frame1)
	Label1_8.place(relx=0.63, rely=0.242, height=31, width=74)
	Label1_8.configure(activebackground="#f9f9f9")
	Label1_8.configure(activeforeground="black")
	Label1_8.configure(background="#d9d9d9")
	Label1_8.configure(disabledforeground="#a3a3a3")
	Label1_8.configure(font="-family {Segoe UI} -size 16 -weight bold")
	Label1_8.configure(foreground="#000000")
	Label1_8.configure(highlightbackground="#d9d9d9")
	Label1_8.configure(highlightcolor="black")
	Label1_8.configure(text='''ID :''')

	global Entry1_9
	Entry1_9 = tk.Entry(Frame1 , textvariable = cid)
	Entry1_9.place(relx=0.689, rely=0.255,height=20, relwidth=0.12)
	Entry1_9.configure(background="white")
	Entry1_9.configure(disabledforeground="#a3a3a3")
	Entry1_9.configure(font="TkFixedFont")
	Entry1_9.configure(foreground="#000000")
	Entry1_9.configure(highlightbackground="#d9d9d9")
	Entry1_9.configure(highlightcolor="black")
	Entry1_9.configure(insertbackground="black")
	Entry1_9.configure(selectbackground="#c4c4c4")
	Entry1_9.configure(selectforeground="black")

	Button1 = tk.Button(Frame1 , command = save)
	Button1.place(relx=0.432, rely=0.94, height=24, width=307)
	Button1.configure(activebackground="#ececec")
	Button1.configure(activeforeground="#000000")
	Button1.configure(background="#d9d9d9")
	Button1.configure(disabledforeground="#a3a3a3")
	Button1.configure(foreground="#000000")
	Button1.configure(highlightbackground="#d9d9d9")
	Button1.configure(highlightcolor="black")
	Button1.configure(pady="0")
	Button1.configure(text='''SAVE''')

	Button1_10 = tk.Button(Frame1 , command = search)
	Button1_10.place(relx=0.645, rely=0.376, height=24, width=307)
	Button1_10.configure(activebackground="#ececec")
	Button1_10.configure(activeforeground="#000000")
	Button1_10.configure(background="#d9d9d9")
	Button1_10.configure(disabledforeground="#a3a3a3")
	Button1_10.configure(foreground="#000000")
	Button1_10.configure(highlightbackground="#d9d9d9")
	Button1_10.configure(highlightcolor="black")
	Button1_10.configure(pady="0")
	Button1_10.configure(text='''SEARCH''')

	Button1_11 = tk.Button(Frame1 , command = changes)
	Button1_11.place(relx=0.645, rely=0.443, height=24, width=307)
	Button1_11.configure(activebackground="#ececec")
	Button1_11.configure(activeforeground="#000000")
	Button1_11.configure(background="#d9d9d9")
	Button1_11.configure(disabledforeground="#a3a3a3")
	Button1_11.configure(foreground="#000000")
	Button1_11.configure(highlightbackground="#d9d9d9")
	Button1_11.configure(highlightcolor="black")
	Button1_11.configure(pady="0")
	Button1_11.configure(text='''EDIT''')

	global Entry2
	Entry2 = tk.Entry(Frame1 , textvariable = r1)
	Entry2.place(relx=0.22, rely=0.309,height=20, relwidth=0.289)
	Entry2.configure(background="white")
	Entry2.configure(disabledforeground="#a3a3a3")
	Entry2.configure(font="TkFixedFont")
	Entry2.configure(foreground="#000000")
	Entry2.configure(insertbackground="black")
	global Entry2_2
	Entry2_2 = tk.Entry(Frame1 , textvariable = r2)
	Entry2_2.place(relx=0.22, rely=0.362,height=20, relwidth=0.289)
	Entry2_2.configure(background="white")
	Entry2_2.configure(disabledforeground="#a3a3a3")
	Entry2_2.configure(font="TkFixedFont")
	Entry2_2.configure(foreground="#000000")
	Entry2_2.configure(highlightbackground="#d9d9d9")
	Entry2_2.configure(highlightcolor="black")
	Entry2_2.configure(insertbackground="black")
	Entry2_2.configure(selectbackground="#c4c4c4")
	Entry2_2.configure(selectforeground="black")
	global Entry2_3
	Entry2_3 = tk.Entry(Frame1 , textvariable = r3)
	Entry2_3.place(relx=0.22, rely=0.416,height=20, relwidth=0.289)
	Entry2_3.configure(background="white")
	Entry2_3.configure(disabledforeground="#a3a3a3")
	Entry2_3.configure(font="TkFixedFont")
	Entry2_3.configure(foreground="#000000")
	Entry2_3.configure(highlightbackground="#d9d9d9")
	Entry2_3.configure(highlightcolor="black")
	Entry2_3.configure(insertbackground="black")
	Entry2_3.configure(selectbackground="#c4c4c4")
	Entry2_3.configure(selectforeground="black")
	global Entry2_4
	Entry2_4 = tk.Entry(Frame1 , textvariable = s1)
	Entry2_4.place(relx=0.22, rely=0.564,height=20, relwidth=0.289)
	Entry2_4.configure(background="white")
	Entry2_4.configure(disabledforeground="#a3a3a3")
	Entry2_4.configure(font="TkFixedFont")
	Entry2_4.configure(foreground="#000000")
	Entry2_4.configure(highlightbackground="#d9d9d9")
	Entry2_4.configure(highlightcolor="black")
	Entry2_4.configure(insertbackground="black")
	Entry2_4.configure(selectbackground="#c4c4c4")
	Entry2_4.configure(selectforeground="black")
	global Entry2_5
	Entry2_5 = tk.Entry(Frame1 , textvariable = s2)
	Entry2_5.place(relx=0.22, rely=0.617,height=20, relwidth=0.289)
	Entry2_5.configure(background="white")
	Entry2_5.configure(disabledforeground="#a3a3a3")
	Entry2_5.configure(font="TkFixedFont")
	Entry2_5.configure(foreground="#000000")
	Entry2_5.configure(highlightbackground="#d9d9d9")
	Entry2_5.configure(highlightcolor="black")
	Entry2_5.configure(insertbackground="black")
	Entry2_5.configure(selectbackground="#c4c4c4")
	Entry2_5.configure(selectforeground="black")
	global Entry2_6
	Entry2_6 = tk.Entry(Frame1 , textvariable = s3)
	Entry2_6.place(relx=0.22, rely=0.671,height=20, relwidth=0.289)
	Entry2_6.configure(background="white")
	Entry2_6.configure(disabledforeground="#a3a3a3")
	Entry2_6.configure(font="TkFixedFont")
	Entry2_6.configure(foreground="#000000")
	Entry2_6.configure(highlightbackground="#d9d9d9")
	Entry2_6.configure(highlightcolor="black")
	Entry2_6.configure(insertbackground="black")
	Entry2_6.configure(selectbackground="#c4c4c4")
	Entry2_6.configure(selectforeground="black")



def glink():
	if ihb.get():
		LST = [ihb.get(),'NULL','NULL',c1.get(),c2.get(),e1.get(),e2.get(),k1.get(),k2.get(),k3.get(),k4.get(),k5.get()]
		CHECK = c.execute('SELECT I_ID FROM LINK').fetchall()
		if LST[0] in CHECK:
			c.execute('UPDATE LINK SET I_ID=?,GC_ID=?,B_ID=?,C_IDA=?,C_IDB=?,E_IDA=?,E_IDB=?,K_IDA=?,K_IDB=?,K_IDC=?,K_IDD=?,K_IDE=? WHERE I_ID=?',(LST[0],LST[1],LST[2],LST[3],LST[4],LST[5],LST[6],LST[7],LST[8],LST[9],LST[10],LST[11],LST[0]))
		else:
			conn.execute('INSERT INTO LINK VALUES(?,?,?,?,?,?,?,?,?,?,?,?)',LST)
		conn.commit()
	elif gc.get():
		LST = ['NULL',gc.get(),'NULL',c1.get(),c2.get(),e1.get(),e2.get(),k1.get(),k2.get(),k3.get(),k4.get(),k5.get()]
		CHECK = c.execute('SELECT GC_ID FROM LINK').fetchall()
		if LST[1] in CHECK:
			c.execute('UPDATE LINK SET I_ID=?,GC_ID=?,B_ID=?,C_IDA=?,C_IDB=?,E_IDA=?,E_IDB=?,K_IDA=?,K_IDB=?,K_IDC=?,K_IDD=?,K_IDE=? WHERE GC_ID=?',(LST[0],LST[1],LST[2],LST[3],LST[4],LST[5],LST[6],LST[7],LST[8],LST[9],LST[10],LST[11],LST[1]))
		else:
			conn.execute('INSERT INTO LINK VALUES(?,?,?,?,?,?,?,?,?,?,?,?)',LST)
		conn.commit()
	elif b.get():
		LST = ['NULL','NULL',b.get(),c1.get(),c2.get(),e1.get(),e2.get(),k1.get(),k2.get(),k3.get(),k4.get(),k5.get()]
		CHECK = c.execute('SELECT B_ID FROM LINK').fetchall()
		if LST[2] in CHECK:
			c.execute('UPDATE LINK SET I_ID=?,GC_ID=?,B_ID=?,C_IDA=?,C_IDB=?,E_IDA=?,E_IDB=?,K_IDA=?,K_IDB=?,K_IDC=?,K_IDD=?,K_IDE=? WHERE B_ID=?',(LST[0],LST[1],LST[2],LST[3],LST[4],LST[5],LST[6],LST[7],LST[8],LST[9],LST[10],LST[11],LST[1]))
		else:
			conn.execute('INSERT INTO LINK VALUES(?,?,?,?,?,?,?,?,?,?,?,?)',LST)
		conn.commit()

def Link():
	global screen2
	global ihb
	global gc
	global b
	global c1
	global c2
	global e1
	global e2
	global k1
	global k2
	global k3
	global k4
	global k5

	_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
	_fgcolor = '#000000'  # X11 color: 'black'
	_compcolor = '#d9d9d9' # X11 color: 'gray85'
	_ana1color = '#d9d9d9' # X11 color: 'gray85'
	_ana2color = '#ececec' # Closest X11 color: 'gray92'
	font11 = "-family {Arial Black} -size 40 -weight bold -slant "  \
			"roman -underline 0 -overstrike 0"
	font9 = "-family {Segoe UI} -size 16 -weight bold -slant roman"  \
			" -underline 0 -overstrike 0"
	
	screen2 = tk.Toplevel(main_screen)
	screen2.title('LINK')

	ihb = tk.StringVar()
	gc = tk.StringVar()
	b = tk.StringVar()
	c1 = tk.StringVar()
	c2 = tk.StringVar()
	e1 = tk.StringVar()
	e2 = tk.StringVar()
	k1 = tk.StringVar()
	k2 = tk.StringVar()
	k3 = tk.StringVar()
	k4 = tk.StringVar()
	k5 = tk.StringVar()

	Frame2 = tk.Frame(screen2)
	Frame2.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=0.999)
	Frame2.configure(relief='groove')
	Frame2.configure(borderwidth="2")
	Frame2.configure(relief="groove")
	Frame2.configure(background="#d9d9d9")

	Label2 = tk.Label(Frame2)
	Label2.place(relx=0.0, rely=0.0, height=71, width=1364)
	Label2.configure(background="#d9d9d9")
	Label2.configure(disabledforeground="#a3a3a3")
	Label2.configure(font=font11)
	Label2.configure(foreground="#000000")
	Label2.configure(text='''Jay Trading Co.''')

	Label2 = tk.Label(Frame2)
	Label2.place(relx=0.015, rely=0.161, height=31, width=174)
	Label2.configure(activebackground="#f9f9f9")
	Label2.configure(activeforeground="black")
	Label2.configure(background="#d9d9d9")
	Label2.configure(disabledforeground="#a3a3a3")
	Label2.configure(foreground="#000000")
	Label2.configure(highlightbackground="#d9d9d9")
	Label2.configure(highlightcolor="black")
	Label2.configure(text='''IHB''')

	Label2_1 = tk.Label(Frame2)
	Label2_1.place(relx=0.015, rely=0.255, height=31, width=174)
	Label2_1.configure(activebackground="#f9f9f9")
	Label2_1.configure(activeforeground="black")
	Label2_1.configure(background="#d9d9d9")
	Label2_1.configure(disabledforeground="#a3a3a3")
	Label2_1.configure(foreground="#000000")
	Label2_1.configure(highlightbackground="#d9d9d9")
	Label2_1.configure(highlightcolor="black")
	Label2_1.configure(text='''Govt. Cont.''')

	Label2_2 = tk.Label(Frame2)
	Label2_2.place(relx=0.015, rely=0.349, height=31, width=174)
	Label2_2.configure(activebackground="#f9f9f9")
	Label2_2.configure(activeforeground="black")
	Label2_2.configure(background="#d9d9d9")
	Label2_2.configure(disabledforeground="#a3a3a3")
	Label2_2.configure(foreground="#000000")
	Label2_2.configure(highlightbackground="#d9d9d9")
	Label2_2.configure(highlightcolor="black")
	Label2_2.configure(text='''Builder''')

	Label2_3 = tk.Label(Frame2)
	Label2_3.place(relx=0.015, rely=0.443, height=31, width=174)
	Label2_3.configure(activebackground="#f9f9f9")
	Label2_3.configure(activeforeground="black")
	Label2_3.configure(background="#d9d9d9")
	Label2_3.configure(disabledforeground="#a3a3a3")
	Label2_3.configure(foreground="#000000")
	Label2_3.configure(highlightbackground="#d9d9d9")
	Label2_3.configure(highlightcolor="black")
	Label2_3.configure(text='''Contractor(1)''')
	
	Label2_4 = tk.Label(Frame2)
	Label2_4.place(relx=0.015, rely=0.537, height=31, width=174)
	Label2_4.configure(activebackground="#f9f9f9")
	Label2_4.configure(activeforeground="black")
	Label2_4.configure(background="#d9d9d9")
	Label2_4.configure(disabledforeground="#a3a3a3")
	Label2_4.configure(foreground="#000000")
	Label2_4.configure(highlightbackground="#d9d9d9")
	Label2_4.configure(highlightcolor="black")
	Label2_4.configure(text='''Contractor(2)''')

	Label2_5 = tk.Label(Frame2)
	Label2_5.place(relx=0.015, rely=0.631, height=31, width=174)
	Label2_5.configure(activebackground="#f9f9f9")
	Label2_5.configure(activeforeground="black")
	Label2_5.configure(background="#d9d9d9")
	Label2_5.configure(disabledforeground="#a3a3a3")
	Label2_5.configure(foreground="#000000")
	Label2_5.configure(highlightbackground="#d9d9d9")
	Label2_5.configure(highlightcolor="black")
	Label2_5.configure(text='''Engineer(1)''')

	Label2_6 = tk.Label(Frame2)
	Label2_6.place(relx=0.015, rely=0.738, height=31, width=174)
	Label2_6.configure(activebackground="#f9f9f9")
	Label2_6.configure(activeforeground="black")
	Label2_6.configure(background="#d9d9d9")
	Label2_6.configure(disabledforeground="#a3a3a3")
	Label2_6.configure(foreground="#000000")
	Label2_6.configure(highlightbackground="#d9d9d9")
	Label2_6.configure(highlightcolor="black")
	Label2_6.configure(text='''Engineer(2)''')

	Entry1 = tk.Entry(Frame2 , textvariable = ihb)
	Entry1.place(relx=0.183, rely=0.161,height=20, relwidth=0.12)
	Entry1.configure(background="white")
	Entry1.configure(disabledforeground="#a3a3a3")
	Entry1.configure(font="TkFixedFont")
	Entry1.configure(foreground="#000000")
	Entry1.configure(highlightbackground="#d9d9d9")
	Entry1.configure(highlightcolor="black")
	Entry1.configure(insertbackground="black")
	Entry1.configure(selectbackground="#c4c4c4")
	Entry1.configure(selectforeground="black")

	Entry1_8 = tk.Entry(Frame2 , textvariable = gc)
	Entry1_8.place(relx=0.183, rely=0.255,height=20, relwidth=0.12)
	Entry1_8.configure(background="white")
	Entry1_8.configure(disabledforeground="#a3a3a3")
	Entry1_8.configure(font="TkFixedFont")
	Entry1_8.configure(foreground="#000000")
	Entry1_8.configure(highlightbackground="#d9d9d9")
	Entry1_8.configure(highlightcolor="black")
	Entry1_8.configure(insertbackground="black")
	Entry1_8.configure(selectbackground="#c4c4c4")
	Entry1_8.configure(selectforeground="black")

	Entry1_9 = tk.Entry(Frame2 , textvariable = b)
	Entry1_9.place(relx=0.183, rely=0.349,height=20, relwidth=0.12)
	Entry1_9.configure(background="white")
	Entry1_9.configure(disabledforeground="#a3a3a3")
	Entry1_9.configure(font="TkFixedFont")
	Entry1_9.configure(foreground="#000000")
	Entry1_9.configure(highlightbackground="#d9d9d9")
	Entry1_9.configure(highlightcolor="black")
	Entry1_9.configure(insertbackground="black")
	Entry1_9.configure(selectbackground="#c4c4c4")
	Entry1_9.configure(selectforeground="black")

	Entry1_10 = tk.Entry(Frame2 , textvariable = c1)
	Entry1_10.place(relx=0.183, rely=0.443,height=20, relwidth=0.12)
	Entry1_10.configure(background="white")
	Entry1_10.configure(disabledforeground="#a3a3a3")
	Entry1_10.configure(font="TkFixedFont")
	Entry1_10.configure(foreground="#000000")
	Entry1_10.configure(highlightbackground="#d9d9d9")
	Entry1_10.configure(highlightcolor="black")
	Entry1_10.configure(insertbackground="black")
	Entry1_10.configure(selectbackground="#c4c4c4")
	Entry1_10.configure(selectforeground="black")

	Entry1_11 = tk.Entry(Frame2 , textvariable = c2)
	Entry1_11.place(relx=0.183, rely=0.537,height=20, relwidth=0.12)
	Entry1_11.configure(background="white")
	Entry1_11.configure(disabledforeground="#a3a3a3")
	Entry1_11.configure(font="TkFixedFont")
	Entry1_11.configure(foreground="#000000")
	Entry1_11.configure(highlightbackground="#d9d9d9")
	Entry1_11.configure(highlightcolor="black")
	Entry1_11.configure(insertbackground="black")
	Entry1_11.configure(selectbackground="#c4c4c4")
	Entry1_11.configure(selectforeground="black")

	Entry1_12 = tk.Entry(Frame2 , textvariable = e1)
	Entry1_12.place(relx=0.183, rely=0.631,height=20, relwidth=0.12)
	Entry1_12.configure(background="white")
	Entry1_12.configure(disabledforeground="#a3a3a3")
	Entry1_12.configure(font="TkFixedFont")
	Entry1_12.configure(foreground="#000000")
	Entry1_12.configure(highlightbackground="#d9d9d9")
	Entry1_12.configure(highlightcolor="black")
	Entry1_12.configure(insertbackground="black")
	Entry1_12.configure(selectbackground="#c4c4c4")
	Entry1_12.configure(selectforeground="black")

	Entry1_13 = tk.Entry(Frame2 , textvariable = e2)
	Entry1_13.place(relx=0.183, rely=0.738,height=20, relwidth=0.12)
	Entry1_13.configure(background="white")
	Entry1_13.configure(disabledforeground="#a3a3a3")
	Entry1_13.configure(font="TkFixedFont")
	Entry1_13.configure(foreground="#000000")
	Entry1_13.configure(highlightbackground="#d9d9d9")
	Entry1_13.configure(highlightcolor="black")
	Entry1_13.configure(insertbackground="black")
	Entry1_13.configure(selectbackground="#c4c4c4")
	Entry1_13.configure(selectforeground="black")

	Entry1_14 = tk.Entry(Frame2 , textvariable = k1)
	Entry1_14.place(relx=0.761, rely=0.201,height=20, relwidth=0.12)
	Entry1_14.configure(background="white")
	Entry1_14.configure(disabledforeground="#a3a3a3")
	Entry1_14.configure(font="TkFixedFont")
	Entry1_14.configure(foreground="#000000")
	Entry1_14.configure(highlightbackground="#d9d9d9")
	Entry1_14.configure(highlightcolor="black")
	Entry1_14.configure(insertbackground="black")
	Entry1_14.configure(selectbackground="#c4c4c4")
	Entry1_14.configure(selectforeground="black")

	Entry1_15 = tk.Entry(Frame2 , textvariable = k2)
	Entry1_15.place(relx=0.761, rely=0.295,height=20, relwidth=0.12)
	Entry1_15.configure(background="white")
	Entry1_15.configure(disabledforeground="#a3a3a3")
	Entry1_15.configure(font="TkFixedFont")
	Entry1_15.configure(foreground="#000000")
	Entry1_15.configure(highlightbackground="#d9d9d9")
	Entry1_15.configure(highlightcolor="black")
	Entry1_15.configure(insertbackground="black")
	Entry1_15.configure(selectbackground="#c4c4c4")
	Entry1_15.configure(selectforeground="black")

	Entry1_16 = tk.Entry(Frame2 , textvariable = k3)
	Entry1_16.place(relx=0.761, rely=0.389,height=20, relwidth=0.12)
	Entry1_16.configure(background="white")
	Entry1_16.configure(disabledforeground="#a3a3a3")
	Entry1_16.configure(font="TkFixedFont")
	Entry1_16.configure(foreground="#000000")
	Entry1_16.configure(highlightbackground="#d9d9d9")
	Entry1_16.configure(highlightcolor="black")
	Entry1_16.configure(insertbackground="black")
	Entry1_16.configure(selectbackground="#c4c4c4")
	Entry1_16.configure(selectforeground="black")

	Entry1_17 = tk.Entry(Frame2 , textvariable = k4)
	Entry1_17.place(relx=0.761, rely=0.483,height=20, relwidth=0.12)
	Entry1_17.configure(background="white")
	Entry1_17.configure(disabledforeground="#a3a3a3")
	Entry1_17.configure(font="TkFixedFont")
	Entry1_17.configure(foreground="#000000")
	Entry1_17.configure(highlightbackground="#d9d9d9")
	Entry1_17.configure(highlightcolor="black")
	Entry1_17.configure(insertbackground="black")
	Entry1_17.configure(selectbackground="#c4c4c4")
	Entry1_17.configure(selectforeground="black")

	Entry1_18 = tk.Entry(Frame2 , textvariable = k5)
	Entry1_18.place(relx=0.761, rely=0.564,height=20, relwidth=0.12)
	Entry1_18.configure(background="white")
	Entry1_18.configure(disabledforeground="#a3a3a3")
	Entry1_18.configure(font="TkFixedFont")
	Entry1_18.configure(foreground="#000000")
	Entry1_18.configure(highlightbackground="#d9d9d9")
	Entry1_18.configure(highlightcolor="black")
	Entry1_18.configure(insertbackground="black")
	Entry1_18.configure(selectbackground="#c4c4c4")
	Entry1_18.configure(selectforeground="black")

	Label2_19 = tk.Label(Frame2)
	Label2_19.place(relx=0.586, rely=0.188, height=31, width=174)
	Label2_19.configure(activebackground="#f9f9f9")
	Label2_19.configure(activeforeground="black")
	Label2_19.configure(background="#d9d9d9")
	Label2_19.configure(disabledforeground="#a3a3a3")
	Label2_19.configure(foreground="#000000")
	Label2_19.configure(highlightbackground="#d9d9d9")
	Label2_19.configure(highlightcolor="black")
	Label2_19.configure(text='''Kadiya(1)''')

	Label2_20 = tk.Label(Frame2)
	Label2_20.place(relx=0.586, rely=0.295, height=31, width=174)
	Label2_20.configure(activebackground="#f9f9f9")
	Label2_20.configure(activeforeground="black")
	Label2_20.configure(background="#d9d9d9")
	Label2_20.configure(disabledforeground="#a3a3a3")
	Label2_20.configure(foreground="#000000")
	Label2_20.configure(highlightbackground="#d9d9d9")
	Label2_20.configure(highlightcolor="black")
	Label2_20.configure(text='''Kadiya(2)''')

	Label2_21 = tk.Label(Frame2)
	Label2_21.place(relx=0.586, rely=0.389, height=31, width=174)
	Label2_21.configure(activebackground="#f9f9f9")
	Label2_21.configure(activeforeground="black")
	Label2_21.configure(background="#d9d9d9")
	Label2_21.configure(disabledforeground="#a3a3a3")
	Label2_21.configure(foreground="#000000")
	Label2_21.configure(highlightbackground="#d9d9d9")
	Label2_21.configure(highlightcolor="black")
	Label2_21.configure(text='''Kadiya(3)''')

	Label2_22 = tk.Label(Frame2)
	Label2_22.place(relx=0.586, rely=0.47, height=31, width=174)
	Label2_22.configure(activebackground="#f9f9f9")
	Label2_22.configure(activeforeground="black")
	Label2_22.configure(background="#d9d9d9")
	Label2_22.configure(disabledforeground="#a3a3a3")
	Label2_22.configure(foreground="#000000")
	Label2_22.configure(highlightbackground="#d9d9d9")
	Label2_22.configure(highlightcolor="black")
	Label2_22.configure(text='''Kadiya(4)''')

	Label2_23 = tk.Label(Frame2)
	Label2_23.place(relx=0.586, rely=0.564, height=31, width=174)
	Label2_23.configure(activebackground="#f9f9f9")
	Label2_23.configure(activeforeground="black")
	Label2_23.configure(background="#d9d9d9")
	Label2_23.configure(disabledforeground="#a3a3a3")
	Label2_23.configure(foreground="#000000")
	Label2_23.configure(highlightbackground="#d9d9d9")
	Label2_23.configure(highlightcolor="black")
	Label2_23.configure(text='''Kadiya(5)''')

	Button1 = tk.Button(Frame2 , command = glink)
	Button1.place(relx=0.359, rely=0.846, height=44, width=347)
	Button1.configure(activebackground="#ececec")
	Button1.configure(activeforeground="#000000")
	Button1.configure(background="#d9d9d9")
	Button1.configure(disabledforeground="#a3a3a3")
	Button1.configure(foreground="#000000")
	Button1.configure(highlightbackground="#d9d9d9")
	Button1.configure(highlightcolor="black")
	Button1.configure(pady="0")
	Button1.configure(text='''LINK''')


def app():
	global main_screen

	main_screen = tk.Toplevel(screen)
	main_screen.title("Jay Trading Co.")

	tk.Label(main_screen,text='').pack()
	tk.Label(main_screen,text='').pack()

	insert = tk.Button(main_screen , command = Insert , text = "ADD CUSTOMERS")
	insert.pack()
	tk.Label(main_screen,text='').pack()

	#search = tk.Button(main_screen , command = Search , text = 'SEARCH CUSTOMERS')
	#search.pack()
	#tk.Label(main_screen,text='').pack()

	link = tk.Button(main_screen , command = Link , text = 'LINK CUSTOMERS')
	link.pack()
	tk.Label(main_screen,text='').pack()

	tk.Label(main_screen,text='').pack()
	tk.Label(main_screen,text='').pack()	
	

def check():
	user_ = user.get()
	pass_ = password.get()



	if user_ == 'dhir':
		if pass_ == '258025':
			login_entry.delete(0,'end')
			password_entry.delete(0,'end')
			app()
		else:
			tk.Label(screen,text='Wrong username or password').pack()

	elif user_ == 'rajenyfr':
		if pass_ == '4909':
			password_entry.delete(0,'end')
			login_entry.delete(0,'end')
			app()
		else:
			tk.Label(screen,text='Wrong username or password').pack()
	else:
		tk.Label(screen,text='Wrong username or password').pack()


def login():
	global user
	global password
	global screen
	global login_entry
	global password_entry

	screen = tk.Tk()
	screen.title("Jay Trading Co.")

	user = tk.StringVar()
	password = tk.StringVar()

	tk.Label(screen,text='').pack()

	Header = tk.Label(screen,text='     --LOGIN--     ')
	Header.pack()

	tk.Label(screen,text='').pack()

	login_label = tk.Label(screen,text='Enter Username : ')
	login_label.pack()

	login_entry = tk.Entry(screen , textvariable = user)
	login_entry.pack()

	tk.Label(screen,text='').pack()

	password_label = tk.Label(screen , text='Enter Password : ')
	password_label.pack()

	password_entry = tk.Entry(screen , textvariable = password , show='*')
	password_entry.pack()

	tk.Label(screen,text='').pack()

	submit = tk.Button(screen , command = check , text = 'SUBMIT')
	submit.pack()

	tk.Label(screen,text='').pack()
	tk.Label(screen,text='').pack()

	screen.mainloop()

if __name__ == '__main__':
	global conn
	global c
	conn = sqlite3.connect('CUSTOMERS.db')
	c = conn.cursor()
	conn.execute('''CREATE TABLE IF NOT EXISTS IHB(
	I_ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	I_NAME TEXT NOT NULL,
	I_R_ADD TEXT,
	I_R_CITY TEXT,
	I_S_ADD TEXT,
	I_S_CITY TEXT,
	I_MOBA INT,
	I_MOBB INT) ''')

	conn.execute('''CREATE TABLE IF NOT EXISTS GOV_CON(
	GC_ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	GC_NAME TEXT NOT NULL,
	GC_R_ADD TEXT,
	GC_R_CITY TEXT,
	GC_S_ADD TEXT,
	GC_S_CITY TEXT,
	GC_MOBA INT,
	GC_MOBB INT) ''')

	conn.execute('''CREATE TABLE IF NOT EXISTS BUILDER(
	B_ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	B_NAME TEXT NOT NULL,
	B_R_ADD TEXT,
	B_R_CITY TEXT,
	B_S_ADD TEXT,
	B_S_CITY TEXT,
	B_MOBA INT,
	B_MOBB INT) ''')

	conn.execute('''CREATE TABLE IF NOT EXISTS CONTRACTOR(
	C_ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	C_NAME TEXT NOT NULL,
	C_R_ADD TEXT,
	C_R_CITY TEXT,
	C_S_ADD TEXT,
	C_S_CITY TEXT,
	C_MOBA INT,
	C_MOBB INT) ''')

	conn.execute('''CREATE TABLE IF NOT EXISTS ENGINEER(
	E_ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	E_NAME TEXT NOT NULL,
	E_R_ADD TEXT,
	E_R_CITY TEXT,
	E_S_ADD TEXT,
	E_S_CITY TEXT,
	E_MOBA INT,
	E_MOBB INT) ''')

	conn.execute('''CREATE TABLE IF NOT EXISTS KADIYA(
	K_ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	K_NAME TEXT NOT NULL,
	K_R_ADD TEXT,
	K_R_CITY TEXT,
	K_S_ADD TEXT,
	K_S_CITY TEXT,
	K_MOBA INT,
	K_MOBB INT) ''')

	#conn.execute('DROP TABLE LINK')

	conn.execute('''CREATE TABLE IF NOT EXISTS LINK(
	I_ID INT ,
	GC_ID INT ,
	B_ID INT,
	C_IDA INT DEFAULT NULL,
	C_IDB INT DEFAULT NULL,
	E_IDA INT DEFAULT NULL,
	E_IDB INT DEFAULT NULL,
	K_IDA INT DEFAULT NULL,
	K_IDB INT DEFAULT NULL,
	K_IDC INT DEFAULT NULL,
	K_IDD INT DEFAULT NULL,
	K_IDE INT DEFAULT NULL,
	FOREIGN KEY(B_ID) REFERENCES BUILDER(B_ID),
	FOREIGN KEY(GC_ID) REFERENCES GOV_CON(GC_ID),
	FOREIGN KEY(I_ID) REFERENCES IHB(I_ID),
	FOREIGN KEY(C_IDA) REFERENCES CONTRACTOR(C_ID),
	FOREIGN KEY(C_IDB) REFERENCES CONTRACTOR(C_ID),
	FOREIGN KEY(E_IDA) REFERENCES ENGINEER(E_ID),
	FOREIGN KEY(E_IDB) REFERENCES ENGINEER(E_ID),
	FOREIGN KEY(K_IDA) REFERENCES KADIYA(K_ID),
	FOREIGN KEY(K_IDB) REFERENCES KADIYA(K_ID),
	FOREIGN KEY(K_IDC) REFERENCES KADIYA(K_ID),
	FOREIGN KEY(K_IDD) REFERENCES KADIYA(K_ID),
	FOREIGN KEY(K_IDE) REFERENCES KADIYA(K_ID))
	''')

	conn.commit()
	login()