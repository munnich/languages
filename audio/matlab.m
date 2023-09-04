%% load and plot audio in matlab
% matlab will load all packages you have installed automatically

% matlab requires functions to be in a separate file: https://www.mathworks.com/help/matlab/ref/function.html
function [] = read_and_plot_file(fname)
    if ~isa(fname,"string")
        error("fname is not a string")
    end

    [data, rate] = audioread(fname);
    % splice first second
    first_second = data(1:rate);
    % abs of dft of first second
    abs_fft = abs(fft(first_second));
    % plot
    plot(abs_fft);
    % save to file
    saveas("plot.pdf");
end

%% IN A SEPARATE FILE
read_and_plot_file("my_file.wav");
