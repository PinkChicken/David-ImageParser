from PIL import Image
import argparse

"""
1: Image to text
2: Text to Image
"""


DEFAULT_FILE = "Examples/SampleInputImage.jpg"
DEFAULT_OUT = 'Examples/SampleOutputText.txt'


argument_parser = argparse.ArgumentParser()
argument_parser.add_argument('-i', help='Input File', default=DEFAULT_FILE)
argument_parser.add_argument('-o', help='Output File', default=DEFAULT_OUT)
argument_parser.add_argument('-d', help="Debug switch {True: Text To Image | False: Image To Text} uses "
                                        "Examples/SampleInputImage.png", default="False")

def main():
    DEBUGSWITCH = argument_parser.parse_args().d
    input_file = argument_parser.parse_args().i
    output_file = argument_parser.parse_args().o
    if DEBUGSWITCH == "True":
        input_file = "Examples/SampleOutPutText.txt"
        output_file = "Examples/SampleOutputImage.jpg"
    print(" ===================================== ")
    print("|             Converting              |")
    convert(input_file, str(output_file))


def extractPixelData(input_file, output_file):
    print("|           Image To Text             |")
    print("|        This may take a while        |")
    print(" ===================================== ")
    img = Image.open(input_file)
    img_data = img.load()

    width, height = img.size
    with open(output_file, 'w') as out:
        # out.write(str(width))
        # out.write("||")
        # out.write(str(height))
        # out.write("|")
        for y in range(height):
            # out.write("|")
            for x in range(width):
                pixel_val = str(img_data[x, y])

                out.write(pixel_val)
                out.write("|")
            out.write("|")

    print("\n\n")
    print("Done! File output is: " + output_file + "!")



def injectPixelData(input_file, output_file):
    print("|            Text To Image            |")
    print("|        This may take a while        |")
    print(" ===================================== ")
    with open(input_file) as inp:
        inp = inp.read()
        inp = inp.split("||")
        temp_inp = []
        for i in range(len(inp)):
            temp_inp.append(inp[i].split("|"))
        inp = temp_inp[:-1]
        for i in range(len(inp)):
            for o in range(len(inp[0])):
                inp[i][o] = inp[i][o].split(", ")
                inp[i][o][0] = inp[i][o][0][1:]
                inp[i][o][2] = inp[i][o][2][:-1]

        del temp_inp
        width, height = len(inp), len(inp[0])
        size = (width, height)
        img = Image.new("RGB", size, 0)
        out = img.load()
        for y in range(height):
            for x in range(width):
                pixel = []
                for i in range(3):
                    pixel.append(int(inp[x][y][i]))
                out[x, y] = tuple(pixel)
        img = img.transpose(Image.FLIP_LEFT_RIGHT)
        img = img.rotate(90, expand=True)
        img.save(output_file)

        print("Done!! Output file is " + output_file + "!")



def convert(input_file, output_file):
    if input_file[-3:] != "txt":
        extractPixelData(input_file, output_file)
    else:
        injectPixelData(input_file, output_file)


if __name__ == "__main__":
    main()
