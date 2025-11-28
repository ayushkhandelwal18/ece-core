clc;
clear;
close;

bits = [1 0 1 1 0 1];  

fs = 1000;             
Rb = 1;               
Tb = 1/Rb;            
samplesPerBit = fs * Tb;

msg = [];             

for i = 1:length(bits)
    msg = [msg bits(i)*ones(1, samplesPerBit)];
end

t = 0:1/fs:(length(msg)-1)/fs;     
fc = 20;
carrier = sin(2*%pi*fc*t);

ask = msg .* carrier;

figure();

subplot(3,1,1);
plot(t,msg);
title("Message Signal");
xlabel("Time (s)"); ylabel("Amplitude");
xgrid();

subplot(3,1,2);
plot(t,carrier);
title("Carrier Signal");
xlabel("Time (s)"); ylabel("Amplitude");
xgrid();

subplot(3,1,3);
plot(t,ask);
title("ASK Modulated Signal");
xlabel("Time (s)"); ylabel("Amplitude");
xgrid();
