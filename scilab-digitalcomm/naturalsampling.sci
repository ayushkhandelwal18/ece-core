clc;
clear;
close;

f=5;
fs=1000;
t=0:1/fs:1;
msg=sin(2*%pi*f*t);
subplot(3,1,1);
plot(t,msg);
title("Message Signal m(t)");
xlabel("Time (s)"); ylabel("Amplitude");
xgrid();

fp = 50;
Ts = 1/fp;
pulse = zeros(1,length(t));

for k = 1:fp
    pulse((t >= (k-1)*Ts) & (t < (k-1)*Ts + Ts/4)) = 1; // wider block
end
subplot(3,1,2);
plot(t,pulse);
title("Pulse Train");
xlabel("Time (s)"); ylabel("Amplitude");
xgrid();

naturalsampled = msg.*pulse;
subplot(3,1,3);
plot(t,naturalsampled);
title("Natural Sampled Signal");
xlabel("Time (s)"); ylabel("Amplitude");
xgrid();
