from PIL import Image
import argparse
DEFAULT_FILE = "TestImage.png"
DEFAULT_OUT = 'TestImageText.txt'
# DEFAULT_FILE = 'TestImageText.txt'
# DEFAULT_OUT = "TestImage.png"
argument_parser = argparse.ArgumentParser()
argument_parser.add_argument('-i', help='Input File', default=DEFAULT_FILE)
argument_parser.add_argument('-o', help='Output File', default=DEFAULT_OUT)


def main():
    input_file = argument_parser.parse_args().i
    output_file = argument_parser.parse_args().o
    print(" ===================================== ")
    print("|             Converting              |")
    print(" ===================================== ")
    convert(input_file, str(output_file))


def extractPixelData(input_file, output_file):
    img = Image.open(input_file)
    img_data = img.load()

    width, height = img.size
    with open(output_file, 'w') as out:
        for y in range(height):
            out.write("\n")
            for x in range(width):
                pixel_val = str(img_data[x, y])

                out.write(pixel_val)

    print("\n\n")
    print("Done! File output is: " + output_file + "!")


def injectPixelData(input_file, output_file):
    pass


def convert(input_file, output_file):
    if input_file[-3:] != "txt":
        extractPixelData(input_file, output_file)
    else:
        injectPixelData(input_file, output_file)


if __name__ == "__main__":
    main()
