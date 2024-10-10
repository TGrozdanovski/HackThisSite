import xml.etree.ElementTree as ET
from PIL import Image, ImageDraw

def get_color(color_name):
    colors = {
        'red': (255, 0, 0),
        'green': (0, 255, 0),
        'blue': (0, 0, 255),
        'yellow': (255, 255, 0),
        'black': (0, 0, 0),
        'white': (255, 255, 255)
    }
    return colors.get(color_name, (255, 255, 255))

def main():
    w, h = 1920, 1080
    image = Image.new('RGB', (w, h), (33, 33, 33))
    draw = ImageDraw.Draw(image)

    try:
        tree = ET.parse('plotMe.xml')
        root = tree.getroot()

        for line in root.findall('Line'):
            x_start = line.find('XStart')
            y_start = line.find('YStart')
            x_end = line.find('XEnd')
            y_end = line.find('YEnd')
            color = line.find('Color')

            if x_start is not None and y_start is not None and x_end is not None and y_end is not None and color is not None:
                draw.line(
                    [
                        (float(x_start.text), h - float(y_start.text)),
                        (float(x_end.text), h - float(y_end.text))
                    ],
                    fill=get_color(color.text),
                    width=1
                )

        for arc in root.findall('Arc'):
            x_center = arc.find('XCenter')
            y_center = arc.find('YCenter')
            radius = arc.find('Radius')
            start_angle = arc.find('ArcStart')
            arc_extend = arc.find('ArcExtend')
            color = arc.find('Color')

            if x_center is not None and y_center is not None and radius is not None and start_angle is not None and arc_extend is not None and color is not None:
                bbox = [
                    float(x_center.text) - float(radius.text),
                    float(y_center.text) - float(radius.text),
                    float(x_center.text) + float(radius.text),
                    float(y_center.text) + float(radius.text)
                ]
                draw.arc(
                    bbox,
                    start=float(start_angle.text),
                    end=float(start_angle.text) + float(arc_extend.text),
                    fill=get_color(color.text),
                    width=1
                )

        image.show()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
