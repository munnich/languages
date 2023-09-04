# image edge detection in julia

# load packages
using Images

function load_and_detect_edges(fname::String)
    img = load(fname)
    # sobel kernel for image filtering
    edges = imfilter(img, Kernel.sobel())
    save("edges.png", edges)
end

function load_and_detect_edges_custom(fname::String)
    img = load(fname)
    # convert to Y'CbCr
    img = YCbCr.(img)
    # convert to standard matrix of 8-bit floats
    img_matrix = channelview(img)
    # extract Y'
    luma = img_matrix[1, :, :]
    # prepare output image
    edges = zeros(size(luma)...)

    # basic kernel:
    #  0 -1  0
    #  0  0  0
    #  0  1  0
    #
    #  0  0  0
    # -1  0  1
    #  0  0  0
    
    # loop through image
    for h in 1:size(luma, 1)
        for w in 1:size(luma, 2)
            hm1 = max(1, h - 1)
            hp1 = min(size(luma, 1), h + 1)
            wm1 = max(1, w - 1)
            wp1 = min(size(luma, 2), w + 1)
            edges[h, w] = (-luma[hm1, w] + luma[hp1, w] - luma[h, wm1] + luma[h, wp1]) / 2
        end
    end

    save("edges.png", colorview(Gray, edges))
end


load_and_detect_edges("my_file.png")
