"use strict"

function post_table()
{
	var object1 = {};
	object1.caption = $("caption > input").val()
	object1.headers = {};
	object1.rows = {};
	$("tr").each(function(index1) {
		if (index1 !== 0)
			object1.rows[index1] = {};
		$(this).find("input").each(function(index2) {
			if (index1 === 0)
				object1.headers[index2] = $(this).val();
			else
				object1.rows[index1][index2] = $(this).val();
		});
	});
	$.ajax({
		type: "POST",
		url: "/table",
		data: JSON.stringify(object1),
		contentType: "application/json; charset=utf-8",
		dataType: "json"
	});
}