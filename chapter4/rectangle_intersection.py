import collections

Rect = collections.namedtuple('Rect', ('x', 'y', 'width', 'height'))


def is_intersect(rect1: Rect, rect2: Rect) -> bool:
    return (rect1.x <= rect2.x + rect2.width and rect1.x + rect1.width >= rect2.x and
            rect1.y <= rect2.y + rect2.height and rect2.y + rect2.height >= rect2.y
            )


def create_rectangle(x1, x2, y1, y2):
    return Rect(x1, y1, x2 - x1, y2 - y1)


def compute_common_rectangle(ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> Rect:
    rect1 = create_rectangle(ax1, ax2, ay1, ay2)
    rect2 = create_rectangle(bx1, bx2, by1, by2)
    if not is_intersect(rect1, rect2): return Rect(0, 0, -1, -1)
    return Rect(
        max(rect1.x, rect2.x),
        max(rect2.y, rect2.y),
        min(rect1.x + rect1.width, rect2.x + rect2.width) - max(rect1.x, rect2.x),
        min(rect1.y + rect1.height, rect2.y + rect2.height) - max(rect1.y, rect2.y)
    )
