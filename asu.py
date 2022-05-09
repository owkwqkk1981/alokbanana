import os, sys, time, re, json, requests, bs4, random, calendar, datetime,subprocess, logging
from concurrent.futures import ThreadPoolExecutor as khamdihiXD
from datetime import datetime
from bs4 import BeautifulSoup as parser
#MLAKU
def jalan(kontol):
	for wibu in kontol + "\n":
		sys.stdout.write(wibu)
		sys.stdout.flush()
		time.sleep(0.03)
def folder():
	try:os.mkdir('okeh')
	except:pass
	try:os.mkdir('cepeh')
	except:pass

class menu:

	def __init__(self):
		self.uid = []
	def main(self):
		os.system('clear')
		try:
			toke = open('token.x','r').read()
		except IOError:
			print(' [%s+%s] Kamu belum login'%(M,N));login().__login__()
		try:
			r = requests.get('https://graph.facebook.com/me?access_token=%s'%(toke)).json()['name']
		except KeyError:
			print(' [%s!%s] Login gagal ...'%(M,N));os.system('rm -rf token.x');time.sleep(2);login().__login__()
		except requests.exceptions.ConnectionError:
			exit(' [%s!%s] cek koneksi'%(M,N))
		try:
			akss = open('license.txt','r').read()
		except IOError:
			akss = '-'
		banner()
		IP = requests.get('https://api.ipify.org').text
		jalan(' %s[ %sselamat Datang Om %s%s ]'%(N,H,r,N))
		print(' %s[%s•%s] Alamat IP kamu saat ini : %s'%(N,O,N,IP))
		print(' %s[%s•%s] Kamu masuk pada         : %s'%(N,O,N,waktu))
		print(' %s'%(N))
		print(' %s[%s0%s] crack dari daftar teman'%(N,O,N))
		print(' %s[%s1%s] crack dari akun publik'%(N,O,N))
		print(' %s[%s2%s] crack dari akun massal'%(N,O,N))
		print(' %s[%s3%s] crack dari postingan'%(N,O,N))
		print(' %s[%s4%s] crack dari likes post'%(N,O,N))
		print(' %s[%s5%s] crack dari followers'%(N,O,N))
		print(' %s[%s6%s] cek opsi akun chekpoint'%(N,O,N))
		print(' %s[%s7%s] cek hasil crack ok,cp'%(N,O,N))
		print(' %s[%s8%s] seting User-Agent'%(N,O,N))
		print(' %s[%s9%s] crack email'%(N,O,N))
		print(' %s[%sG%s] Get data² facebook'%(N,O,N))
		print(' %s[%sK%s] Lapor bug script'%(N,O,N))
		print(' %s[%sA%s] Keluar, hapus token'%(N,O,N))
		self.pilih()