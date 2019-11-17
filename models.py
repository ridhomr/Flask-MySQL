# Ridho Marhaban 
import pymysql
import config

db = cursor = None

class biografi:
	def __init__ (self, no=None, nama=None, alamat=None, kota=None, agama=None, no_telp=None):
		self.no = no
		self.nama = nama
		self.alamat = alamat
		self.kota = kota
		self.agama = agama
		self.no_telp = no_telp

	def openDB(self):
		global db, cursor
		db = pymysql.connect(
			config.DB_HOST,
			config.DB_USER,
			config.DB_PASSWORD,
			config.DB_NAME)
		cursor = db.cursor()

	def closeDB(self):
		global db, cursor
		db.close()

	def selectDB(self):
		self.openDB()
		cursor.execute("SELECT * FROM biografi")
		container = []
		for no,nama,alamat,kota,agama,no_telp in cursor.fetchall():
			container.append((no,nama,alamat,kota,agama,no_telp))
		self.closeDB()
		return container

	def insertDB(self, data):
		self.openDB()
		cursor.execute("INSERT INTO biografi (nama,alamat,kota,agama,no_telp) VALUES('%s','%s','%s','%s','%s')" % data)
		db.commit()
		self.closeDB()

	def getDBbyNo(self, no):
		self.openDB()
		cursor.execute("SELECT * FROM biografi WHERE no='%s'" % no)
		data = cursor.fetchone()
		return data

	def updateDB(self, data):
		self.openDB()
		cursor.execute("UPDATE biografi SET nama='%s', alamat='%s', kota='%s', agama='%s', no_telp='%s' WHERE no=%s" % data)
		db.commit()
		self.closeDB()

	def deleteDB(self, no):
		self.openDB()
		cursor.execute("DELETE FROM biografi WHERE no='%s'" % no)
		db.commit()
		self.closeDB()
		