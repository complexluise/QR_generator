import argparse
import qrcode
import os
import sys

def generate_qr(url, output_file):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output_file)
    print(f"Código QR generado y guardado como {output_file}")

def process_file(file_path):
    if not os.path.exists(file_path):
        print(f"El archivo {file_path} no existe.")
        return

    # Crear la carpeta qr_codes en la misma ubicación que el archivo de texto
    base_dir = os.path.dirname(file_path)
    qr_dir = os.path.join(base_dir, "qr_codes")
    os.makedirs(qr_dir, exist_ok=True)

    with open(file_path, 'r') as file:
        for line_number, url in enumerate(file, 1):
            url = url.strip()
            if url:
                output_file = os.path.join(qr_dir, f"qr_code_{line_number}.png")
                generate_qr(url, output_file)

def main():
    parser = argparse.ArgumentParser(description="Genera códigos QR a partir de un enlace o un archivo de texto con enlaces")
    parser.add_argument("input", help="URL o ruta del archivo de texto con URLs")
    parser.add_argument("-o", "--output", help="Nombre del archivo de salida (solo para URL individual)")

    args = parser.parse_args()

    if os.path.isfile(args.input):
        process_file(args.input)
    else:
        if args.output:
            generate_qr(args.input, args.output)
        else:
            generate_qr(args.input, "qr_code.png")

if __name__ == "__main__":
    main()