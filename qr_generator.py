import argparse
import qrcode
import sys

def generate_qr(url, output_file):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output_file)
    print(f"Código QR generado y guardado como {output_file}")

def main():
    parser = argparse.ArgumentParser(description="Genera un código QR a partir de un enlace")
    parser.add_argument("url", help="El enlace para convertir en código QR")
    parser.add_argument("-o", "--output", default="qr_code.png", help="Nombre del archivo de salida (por defecto: qr_code.png)")

    args = parser.parse_args()

    generate_qr(args.url, args.output)

if __name__ == "__main__":
    main()