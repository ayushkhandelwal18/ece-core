clc;
clear;
close;

bits = [1 0 1 1 0 1 0 0];
n = length(bits);

A = 1;
fs = 1000;
Rb = 2;
Tb = 1/Rb;
samplesPerBit = fs * Tb;
fc = 20;

// -------- Message waveform generation --------
msg = [];
for i = 1:n
    msg = [msg bits(i)*ones(1, samplesPerBit)];
end

t_msg = 0:1/fs:(length(msg)-1)/fs;

// -------- Carrier for whole duration --------
carrier = sin(2*%pi*fc*t_msg);

// -------- QPSK Modulation (phase mapping) --------
t_sym = 0:1/fs:(2*Tb - 1/fs);      // time for each 2-bit symbol
QPSK = [];

for i = 1:2:n-1
    first = bits(i);
    second = bits(i+1);

    if first==0 & second==0 then
        phase = 45 * %pi/180;
    elseif first==0 & second==1 then
        phase = 135 * %pi/180;
    elseif first==1 & second==1 then
        phase = 225 * %pi/180;
    else
        phase = 315 * %pi/180;
    end

    QPSK_BIT = A * sin(2*%pi*fc*t_sym + phase);
    QPSK = [QPSK QPSK_BIT];
end

t_final = 0:1/fs:(length(QPSK)-1)/fs;

// -------- PLOTTING --------
figure();

subplot(3,1,1);
plot(t_msg, msg, 'LineWidth',2);
title("Message Signal (Custom Bits)");
xlabel("Time (s)");
ylabel("Amplitude");
xgrid();

subplot(3,1,2);
plot(t_msg, carrier, 'LineWidth',1.5);
title("Carrier Signal");
xlabel("Time (s)");
ylabel("Amplitude");
xgrid();

subplot(3,1,3);
plot(t_final, QPSK, 'LineWidth',1.5);
title("QPSK Modulated Signal (Phase Shifted)");
xlabel("Time (s)");
ylabel("Amplitude");
xgrid();
