from google_images_download import google_images_download 

def download(key):
	palavrasChave = key
	resposta = google_images_download.googleimagesdownload() 
	padrao = {"keywords": palavrasChave, 
			"format": "jpg", 
			"limit":4, 
			"print_urls":False, 
			"size": "medium",
			"language": "Portuguese",
			"aspect_ratio": "square"
			} 
	try: 
		resposta.download(padrao)
		
	except FileNotFoundError: 
		padrao = {"keywords": palavrasChave, 
					"format": "jpg", 
					"limit":4, 
					"print_urls":False,
					"language": "Portuguese", 
					"size": "medium"} 
					
		# Providing padrao for the searched query 
		try: 
			# Downloading the photos based 
			# on the given padrao 
			resposta.download(padrao) 
			
		except: 
			pass
