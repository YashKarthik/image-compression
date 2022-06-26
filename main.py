from PIL import Image

def compress(file, quality=50):
    picture = Image.open(file)
    picture.save("compressed_"+file,
                 optimize=True,
                 quality=quality)
    return

def main():
    file = input("Enter path to file:")
    quality = int(input("Size of desired file (as percentage of original file):"))
    print("Compressing...")
    compress(file, quality)
    print("DONE")

if __name__ == "__main__":
    main()
