test:swr2-recorder.py
	./swr2-recorder.py test-swr2.mp3 60
	echo "/home/david/Dokumente/programming/github/swr2/swr2-recorder.py /home/david/Musik/swr2/next-minute.mp3 60" | at now + 1 minutes ##-t 07141010.00
	echo "/home/david/Dokumente/programming/github/swr2/swr2-recorder.py /home/david/Musik/swr2/now.mp3 60" | at now

install-cgi: swr2-recorder-cgi.py
	cp -pr swr2-recorder-cgi.py /usr/share/apache2/httpd

install:swr2-recorder.py
	sudo cp swr2-recorder.py /usr/bin/
