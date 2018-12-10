from subprocess import call, list2cmdline
import base64
import time


def lambda_handler(event, context):
	opt = event['opt']
	html_base64 = event['html_base64']
	
	command_array = ['./wkhtmltopdf']

	for key in opt:
		command_array.append(key)
		command_array.append(opt[key])

	if(html_base64['header']):
		header_filename = '/tmp/header.html'
		header_html = base64.b64decode(html_base64['header'])
		f = open(header_filename, 'w+')
		f.write(header_html)
		f.close()
		command_array.append('--header-html')
		command_array.append(header_filename)
	
	body_filename = '/tmp/body.html'
	body_html = base64.b64decode(html_base64['body'])
	f = open(body_filename, 'w+')
	f.write(body_html)
	f.close()
	command_array.append(body_filename)

	filename = '/tmp/document_generated.pdf'
	command_array.append(filename)

	call(command_array)
	time.sleep(1)

	return open(filename, 'rb').read().encode('base64').replace('\n', '')  


#if __name__ == "__main__":
#	event = {
#        'opt': {
#			'--encoding': 'UTF8',
#			'--margin-top': '15mm',
#			'--header-spacing': '5',
#			'--margin-bottom': '10mm',
#			'--footer-center': '[page]/[toPage]'
#		},
#		'html_base64': {
#				'body': 'PCFET0NUWVBFIGh0bWw+CjxodG1sIGxhbmc9InB0LWJyIj4KPGhlYWQ+Cgk8bGluayByZWw9InN0eWxlc2hlZXQiIGhyZWY9Imh0dHBzOi8vdW5wa2cuY29tL2xlYWZsZXRAMS4zLjQvZGlzdC9sZWFmbGV0LmNzcyIgaW50ZWdyaXR5PSJzaGE1MTItcHVCcGRSMDc5OE9adlRUYlA0QThJeC9sK0E0ZEhERDBER3FZVzZSUSs5anhrUkZjbGF4eFFiL1NKQVdaZldBa3V5ZVFVeXRPNys3TjRRS3JEaCtkckE9PSIgY3Jvc3NvcmlnaW49IiIvPgoJPHNjcmlwdCBzcmM9Imh0dHBzOi8vdW5wa2cuY29tL2xlYWZsZXRAMS4zLjQvZGlzdC9sZWFmbGV0LmpzIiBpbnRlZ3JpdHk9InNoYTUxMi1uTU1tUnlUVm9MWXFqUDlocmJlZDlTK0Z6alpIVzVnWTFUV0NIQTVja3dYWkJhZG50Q05zOGtFcUFXZHJiOU83cnhiQ2FBNGxLVElXakRYWnhmbE9jQT09IiBjcm9zc29yaWdpbj0iIj48L3NjcmlwdD4KCjwvaGVhZD4KPGJvZHk+Cgk8ZGl2IGNsYXNzPSJoZWFkZXItZmFybS1uYW1lIj4KCQk8c3R5bGU+CgkJCS5oZWFkZXItZmFybS1uYW1lIHsKCQkJCXRleHQtYWxpZ246IGNlbnRlcjsKCQkJfQoJCQkuaGVhZGVyLWZhcm0tbmFtZSBoMSB7CgkJCQltYXJnaW4tYm90dG9tOiAwcHg7CgkJCX0KCQk8L3N0eWxlPgoJCTxoMT4yIElybcOjb3MgLSBQaXJhdGluaTwvaDE+CgkJPHNwYW4+RmFtw61saWEgRnJlbmhhbjwvc3Bhbj4KCTwvZGl2PgoKCTwhLS0gRklNIERPIEhFQURFUiAtLT4KCgk8ZGl2IGNsYXNzPSJjb250ZW50LWZhcm0tb3RoZXItZGF0ZXMiPgoJCTxzdHlsZT4KCQkJLmNvbnRlbnQtZmFybS1vdGhlci1kYXRlcyB7CgkJCQltYXJnaW4tdG9wOiAyMHB4OwoJCQl9CgkJCS5jb250ZW50LWZhcm0tb3RoZXItZGF0ZXMgI21hcGEtZnVsbC1mYXJtewoJCQkJd2lkdGg6IDkwMHB4OwoJCQkJaGVpZ2h0OiA1MDBweDsKCQkJfQoJCTwvc3R5bGU+CgkJPGRpdiBpZD0ibWFwYS1mdWxsLWZhcm0iPjwvZGl2PgoJCTxzY3JpcHQ+CgoJCQl2YXIgbWFwID0gTC5tYXAoJ21hcGEtZnVsbC1mYXJtJywgewoJCQkJem9vbUNvbnRyb2w6IGZhbHNlLAoJCQkJYXR0cmlidXRpb25Db250cm9sOiBmYWxzZQoJCQl9KS5zZXRWaWV3KFs1MS41MDUsIC0wLjA5XSwgMTMpOwoKCQkJTC50aWxlTGF5ZXIoJ2h0dHBzOi8vc2VydmVyLmFyY2dpc29ubGluZS5jb20vQXJjR0lTL3Jlc3Qvc2VydmljZXMvV29ybGRfSW1hZ2VyeS9NYXBTZXJ2ZXIvdGlsZS97en0ve3l9L3t4fScpLmFkZFRvKG1hcCk7CgoJCTwvc2NyaXB0PgoJPC9kaXY+Cgo8L2JvZHk+CjwvaHRtbD4=',
#				'header': 'PCFET0NUWVBFIGh0bWw+CjxodG1sIGxhbmc9InB0LWJyIj4KPGhlYWQ+CjxoZWFkPgoJPG1ldGEgY2hhcnNldD0iVVRGLTgiPgoJPHN0eWxlPgoJCWRpdnsKCQkJd2lkdGg6IDEwMCU7CgkJCXRleHQtYWxpZ246IHJpZ2h0OwoJCQlmb250LXNpemU6IDIwcHg7CgkJCWZvbnQtc3R5bGU6IGl0YWxpYzsKCQl9Cgk8L3N0eWxlPgo8L2hlYWQ+Cjxib2R5PgoJPGRpdj5EYXRhIGRvIHJlbGF0w7NyaW86IDIwMTgtMTItMTA8L2Rpdj4KPC9ib2R5Pgo8L2h0bWw+'
#		}
#	}
#	context = []
#	print lambda_handler(event, context)

