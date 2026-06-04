Tenes:

snapshots/
├── fondos_20260602_194500.csv
├── fondos_20260602_194500.html

Por qué esto importa mucho

Porque en scraping:

  los datos cambian,
  pero el debugging depende del HTML histórico.

Eso te permite:

  reproducir bugs,
  testear parsers offline,
  comparar cambios de DOM,
  mejorar selectores sin pegarle al sitio,
  desarrollar sin Selenium abierto.

runnealo asi : (desde clase_1 sino ajustalo)
  python  .\hidden_test\scrapper\main.py