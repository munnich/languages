import vapoursynth as vs
core = vs.core


def load_and_detect_edges(fname: str):
    img = core.imwri.Read(fname)
    # luma
    gray = core.resize.Bicubic(img, format=vs.GRAYS, matrix_s="709")
    # sobel
    edges = core.std.Sobel(gray)
    # write to file
    edges = core.imwri.Write(edges, "PNG", "edges%d.png")
    return edges


def load_and_detect_edges_custom(fname: str):
    img = core.imwri.Read(fname)
    # luma
    gray = core.resize.Bicubic(img, format=vs.GRAYS, matrix_s="709")
    # basic kernel:
    #  0 -1  0
    #  0  0  0
    #  0  1  0
    #
    #  0  0  0
    # -1  0  1
    #  0  0  0
    edges_y = core.std.Convolution(gray, [0, -1, 0,
                                                   0, 0, 0,
                                                   0, 1, 0])
    edges_x = core.std.Convolution(gray, [0, 0, 0,
                                                   -1, 0, 1,
                                                    0, 0, 0])
    # combine                                           (x + y) / 2 in reverse polish
    edges = core.std.Expr([edges_x, edges_y], "x y + 2 /")
    # write to file
    edges = core.imwri.Write(edges, "PNG", "edges%d.png")
    return edges


load_and_detect_edges("my_file.png").set_output()
