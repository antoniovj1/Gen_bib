________
# Gen_bib
________
Genera un archivo con la bibliografía para **LaTex** a partir de un archivo con URLs.

El script recibe un archivo con URLs y las etiquetas con las que serán citadas en el archivo .tex:

**Ejemplo archivo entrada:** 
```
cron;http://linux.die.net/man/8/cron
ls;http://man7.org/linux/man-pages/man1/ls.1.html
```
**Archivo generado:**
```
@misc{cron,
	author = {},
	title = {cron(8): daemon to execute scheduled commands - Linux man page},
	year = {(Accedido el 28/11/2015)}, 
	howpublished ="\url{http://linux.die.net/man/8/cron}"
} 

@misc{ls,
	author = {},
	title = {ls(1) - Linux manual page},
	year = {(Accedido el 28/11/2015)}, 
	howpublished ="\url{http://man7.org/linux/man-pages/man1/ls.1.html}"
} 
```
