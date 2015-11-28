# Gen_bib
Genera un archivo con la bibliografía a partir de un archivo con urls.

El script recibe un archivo con urls y las etiquetas con las que serán citadas en el archivo .tex:

*Ejemplo archivo entrada:* 

cron;http://linux.die.net/man/8/cron<br />
ls;http://man7.org/linux/man-pages/man1/ls.1.html

*Archivo generado:*

@misc{cron,<br />
	author = {},<br />
	title = {cron(8): daemon to execute scheduled commands - Linux man page},<br />
	year = {(Accedido el 28/11/2015)}, <br />
	howpublished ="\url{http://linux.die.net/man/8/cron}"<br />
} <br />

@misc{ls,<br />
	author = {},<br />
	title = {ls(1) - Linux manual page},<br />
	year = {(Accedido el 28/11/2015)}, <br />
	howpublished ="\url{http://man7.org/linux/man-pages/man1/ls.1.html}"<br />
} <br />
