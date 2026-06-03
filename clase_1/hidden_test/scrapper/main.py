from pathlib import Path
from datetime import datetime

from fetcher import (
    get_detail_html,
    get_html,
    download_pdf,
)

from parsers.parser import parse_fondos
from parsers.parser_detalle import (parse_fondo_detalle)
from storage import (save_csv,save_detail_csv)

BASE_DIR = Path(__file__).resolve().parent

SNAPSHOTS_DIR = BASE_DIR / "snapshots"
LIST_DIR = SNAPSHOTS_DIR / "list"
DETAIL_DIR = SNAPSHOTS_DIR / "detail"
PDF_DIR = SNAPSHOTS_DIR / "pdf"

PDF_DIR.mkdir(parents=True,exist_ok=True)
LIST_DIR.mkdir(parents=True,exist_ok=True)
DETAIL_DIR.mkdir(parents=True,exist_ok=True)

def main():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # listado principal
    html = get_html()
    fondos = parse_fondos(html)
    print(f"Fondos encontrados: {len(fondos)}")
    
    # guardar html listado
    list_html_file = (LIST_DIR / f"fondos_{timestamp}.html")
    with open(list_html_file, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"HTML listado generado: {list_html_file}")
    
    # guardar csv listado
    csv_file = (LIST_DIR / f"fondos_{timestamp}.csv")
    save_csv(fondos, csv_file)
    print(f"CSV listado generado: {csv_file}")
    
    # detalles
    detalles = []
    
    # solo primeros 3 por ahora
    for fondo in fondos[:3]:
        print(f"\nProcesando detalle: {fondo.nombre}")
        try:
            detail_html = get_detail_html(fondo.url_detalle)
            
            # guardar html detalle
            detail_file = (DETAIL_DIR / f"detalle_{fondo.id}_{timestamp}.html")
            with open(detail_file, "w", encoding="utf-8") as f:
                f.write(detail_html)
            print(f"HTML detalle generado: {detail_file}")
            
            # parsear detalle
            detalle, tenencias = parse_fondo_detalle(detail_html, fondo.id)
            
            pdf_urls = [
                detalle.factsheet_url,
                detalle.reglamento_url,
                detalle.calificaciones_url,
            ]
            
            for index, pdf_url in enumerate(pdf_urls, start=1):

              if not pdf_url:
                  continue
                
              try:
              
                  pdf_file = (
                      PDF_DIR /
                      f"{fondo.id}_{index}_{timestamp}.pdf"
                  )
          
                  download_pdf(
                      pdf_url,
                      pdf_file
                  )
          
                  print(
                      f"PDF descargado: "
                      f"{pdf_file}"
                  )
          
              except Exception as e:
              
                  print(
                      f"Error descargando PDF "
                      f"{pdf_url}: {e}"
                  )
                  
            detalles.append(detalle)
            
            print(detalle)
            print(tenencias)
            
        except Exception as e:
            print(f"Error procesando {fondo.nombre}: {e}")
    
    # guardar csv detalle
    if detalles:
        detail_csv_file = (DETAIL_DIR / f"detalles_{timestamp}.csv")
        save_detail_csv(detalles, detail_csv_file)
        print(f"\nCSV detalle generado: {detail_csv_file}")

if __name__ == "__main__":
    main()