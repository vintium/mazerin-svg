from xml.etree import ElementTree
from xml.etree.ElementTree import Element, SubElement







def create_svg(view_window: int, outer_padding: int) -> Element:
    viewbox_size = view_window + 2*outer_padding
    return Element("svg", {
        "viewBox" : f"0 0 {viewbox_size} {viewbox_size}",
        "width" : "500",
        "height" : "500",
        "xmlns" : "http://www.w3.org/2000/svg",
    })

def add_grid(svg: Element, grid_size: int, view_window: int, outer_padding: int) -> None:
    cell_size = view_window/grid_size
    points: list[(int, int)] = [(x*cell_size, y*cell_size) for y in range(0, grid_size) for x in range (0, grid_size)]
    for x, y in points:
        SubElement(svg, "rect", {
            "x": f"{x+outer_padding}",
            "y": f"{y+outer_padding}", 
            "width" : f"{cell_size}", 
            "height" : f"{cell_size}", 
           "fill": "none", 
           "stroke" : "black",
           }
       )


def add_hints(svg: Element, hints: list[(int, int, int)], grid_size: int, view_window: int, outer_padding: int, font: str, font_size: float) -> None:
    cell_size = view_window/grid_size
    x_offset = cell_size * 0.3
    y_offset = cell_size * 0.8
    for (x, y, hint) in hints:
        e = SubElement(svg, "text", {
            "x": f"{x*cell_size+outer_padding+x_offset}", 
            "y": f"{y*cell_size+outer_padding+y_offset}", 
            "font-family": font,
            "font-size" : str(cell_size * font_size)
            }
        )
        e.text = f"{hint}"



GRID_SIZE = 5
VIEW_WINDOW = 100
OUTER_PADDING = 5

hints: list[(int, int, int)] = [(0, 0, 3), (0, 2, 3), (2, 0, 5)]
svg = create_svg(VIEW_WINDOW, OUTER_PADDING)
add_grid(svg, GRID_SIZE, VIEW_WINDOW, OUTER_PADDING)
add_hints(svg, hints, GRID_SIZE, VIEW_WINDOW, OUTER_PADDING, "Noto Sans", 0.8)

ElementTree.dump(svg)
