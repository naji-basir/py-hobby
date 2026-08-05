from qr_generator.generator import generate_qr

def main()->None:
    text = input('Enter the text or URL: ').strip()

    if not text:
        print("❌ Input cannot be empty.")
        return 
    generate_qr(text)

if __name__ == "__main__":
    main()