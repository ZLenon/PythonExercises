import pprint

path = "./automatize_tarefas_maçantes/read_write_arquives/pagina260/data.py"

cats = [{"name": "Zophie", "desc": "chubby"}, {"name": "Pooka", "desc": "fluffy"}]

pprint.pformat(cats)
# "[{'desc': 'chubby', 'name': 'Zophie'}, {'desc': 'fluffy', 'name': 'Pooka'}]"

fileObj = open(path, "w")
fileObj.write("cats = " + pprint.pformat(cats) + "\n")

fileObj.close()
