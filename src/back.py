import pickle



def dump(file_path, hide_name):
    with open(file_path, "rb") as e:
    	data = e.read()
    	

    with open(hide_name, 'wb') as f:
    	pickle.dump(data, f)



def load(hidden_file_name, unhide_name):
	with open(hidden_file_name, 'rb') as f:
		data = pickle.load(f)

	with open(unhide_name,"wb") as e:
		e.write(data)
