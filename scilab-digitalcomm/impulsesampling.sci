clc;
clear;
close;

f = 5;
fs = 1000;
t = 0:1/fs:1;
msg = sin(2*%pi*f*t);

subplot(3,1,1);
plot(t,msg);
title("Message Signal m(t)");
xlabel("Time (s)"); ylabel("Amplitude");
xgrid();

Ts = 1/50;                 
n = 0:Ts:1;                
imp_train = zeros(1,length(t));

for k = 1:length(n)
    diff = abs(t - n(k));
    [min_val, idx] = min(diff);
    imp_train(idx) = 1;
end

subplot(3,1,2);
plot2d3(t,imp_train);
title("Impulse Train");
xlabel("Time (s)"); ylabel("Amplitude");
xgrid();


imp_sampled = msg .* imp_train;

subplot(3,1,3);
plot2d3(t,imp_sampled);
title("Impulse Sampled Signal");
xlabel("Time (s)"); ylabel("Amplitude");
xgrid();
