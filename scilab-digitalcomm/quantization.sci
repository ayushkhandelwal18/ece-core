clc;
clear;
close;

fs = 10000;
t = 0:1/fs:0.1;
f_signal = 50;
Am = 5;
x = Am * sin(2 * %pi * f_signal * t);

N = 4;
no_levels = 2^N;

Amin = min(x);
Amax = max(x);

stepSize = (Amax - Amin) / no_levels;

quant_type = "mid-tread";

if quant_type == "mid-tread" then
    x_quantized = round((x - Amin) / stepSize) * stepSize + Amin;

elseif quant_type == "mid-rise" then
    x_quantized = floor((x - Amin) / stepSize + 0.5) * stepSize + Amin;
end

figure();

subplot(2,1,1);
plot(t, x);
title("Original Signal");
xlabel("Time (s)"); ylabel("Amplitude");
xgrid();

subplot(2,1,2);
plot(t, x_quantized);
title("Quantized Signal");
xlabel("Time (s)"); ylabel("Amplitude");
xgrid();
