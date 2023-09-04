# load and plot audio in julia

# import packages
using WAV, FFTW, Plots

function read_and_plot_file(fname::String)
    # read audio file
    data, rate, = wavread(fname)
    # slice first second
    first_second = data[1:rate]
    # abs of dft of first second (@. is https://docs.julialang.org/en/v1/manual/mathematical-operations/#man-dot-operators)
    abs_fft = @. abs(fft(first_second))
    # plot
    plot(abs_fft)
    # save to file
    savefig("plot.pdf")
    return
end

read_and_plot_file("my_file.wav")
