from bottle import route, run, template, request, static_file
import json


ID = "xtable1"


@route('/js/<filename>')
def send_static(filename):
	return static_file(filename, root="js")


@route('/css/<filename>')
def send_static(filename):
	return static_file(filename, root="css")


@route("/table")
def index():
	with open("./" + ID + ".json", "r", encoding='utf-8') as infile:
		data = json.load(infile)
	table = "<table id='" + ID + "'>\n"
	for a, b in sorted(data.items()):
		if a == "caption":
			table += "\t<caption><input type='text' value='{}'></caption>\n".format(b)
		if a == "headers":
			table += "\t<tr>\n"
			for _, c in sorted(b.items()):
				table += "\t\t<th><input type='text' value='{}'></th>\n".format(c)
			table += "\t</tr>\n"
		if a == "rows":
			for _, c in sorted(b.items()):
				table += "\t<tr>\n"
				for _, d in sorted(c.items()):
					table += "\t\t<td><input type='text' value='{}'></td>\n".format(d)
				table += "\t</tr>\n"

	table += "</table>"
	return template("index.html", table=table)


@route("/table", method="POST")
def do_table_post():
	with open(ID + ".json", "w", encoding='utf-8') as outfile:
		json.dump(request.json, outfile, indent="\t", ensure_ascii=False)


run(host="localhost", port=80, server="tornado")
