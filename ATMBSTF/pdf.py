import requests 
file_url = "https://libri.xyz/luna-nera-le-citta-perdute-tiziana-triana-pdf"

r = requests.get(file_url, stream = True) 

with open("LunaNera.pdf","wb") as pdf: 
	for chunk in r.iter_content(chunk_size=1024): 

		# writing one chunk at a time to pdf file 
		if chunk: 
			pdf.write(chunk) 
