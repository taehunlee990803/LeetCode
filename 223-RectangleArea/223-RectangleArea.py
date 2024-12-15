        # (bx1, by1)
        # (bx2, by2)
        area1 = (ax2 - ax1) * (ay2 - ay1)
        area2 = (bx2 - bx1) * (by2 - by1)

        overlap_x1 = max(ax1, bx1)  # Bottom-left x
        overlap_y1 = max(ay1, by1)  # Bottom-left y
        overlap_x2 = min(ax2, bx2)  # Top-right x
        overlap_y2 = min(ay2, by2)  # Top-right y

        overlap_width = max(0, overlap_x2 - overlap_x1)  # Width of the overlap
        overlap_height = max(0, overlap_y2 - overlap_y1)  # Height of the overlap

        overlap_area = overlap_width*overlap_height

        total_area = area1 + area2 - overlap_area
                


        return total_area

