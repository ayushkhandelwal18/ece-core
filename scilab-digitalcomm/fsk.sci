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


f1 = 30;      
f0 = 10;      

c1 = sin(2*%pi*f1*t);
c0 = sin(2*%pi*f0*t);

fsk = msg .* c1 + (1-msg) .* c0;

figure();
subplot(4,1,1);
plot(t,msg);
title("Message Signal");
xgrid();

subplot(4,1,2);
plot(t,c1);
title("Carrier for 1 (high freq)");
xgrid();

subplot(4,1,3);
plot(t,c0);
title("Carrier for 0 (low freq)");
xgrid();

subplot(4,1,4);
plot(t,fsk);
title("FSK Modulated Signal");
xgrid();
